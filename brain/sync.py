#!/usr/bin/env python3
"""
Index corpus/ and push it into the app's search database (Cloudflare D1).

Each Markdown file is cut into passages of about 300 words that never cross a
slide or page boundary carelessly, so every search hit can say "slide 7" or
"pp. 3–4". Only new or changed files are uploaded; deleted files are removed.

    python brain/sync.py --stats            what would be indexed, no upload
    python brain/sync.py --local            into the local dev database
    python brain/sync.py --remote           into the live app (needs wrangler login
                                            or CLOUDFLARE_API_TOKEN)
    python brain/sync.py --remote --rebuild drop everything and reload

Runs automatically in GitHub Actions on every push that changes corpus/.
"""

import argparse
import json
import os
import re
import shutil
import subprocess
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from common import BUILD_DIR, CODE_ROOT, CORPUS_DIR, ROOT, read_doc, sha1  # noqa: E402

APP_DIR = os.path.join(CODE_ROOT, "app")
DB_NAME = "DB"          # the binding name; works for the main app and for --env demo
ENV_ARGS = []
TARGET_WORDS = 300       # a passage: long enough for context, short enough to cite
MAX_WORDS = 450
SQL_FILE_BYTES = 8_000_000

MARKER = re.compile(r"^## (Page|Slide|Sheet) (\S+)(?:\s+[—-]\s+(.*))?\s*$")
SUBHEAD = re.compile(r"^#{2,6} (.+)$")
DOC_FIELDS = ["id", "path", "title", "course", "course_name", "term", "type", "module",
              "date", "source", "url", "locator_kind", "hash", "words", "n_chunks"]


# --------------------------------------------------------------------------
# Chunking
# --------------------------------------------------------------------------


def sections(body):
    """Split a document into (kind, number, heading, text) at page/slide markers."""
    out, cur = [], {"kind": None, "num": None, "heading": "", "lines": []}
    for line in body.splitlines():
        m = MARKER.match(line)
        if m:
            out.append(cur)
            cur = {"kind": m.group(1).lower(), "num": m.group(2),
                   "heading": (m.group(3) or "").strip(), "lines": []}
            continue
        sub = SUBHEAD.match(line)
        if sub and not cur["lines"] and not cur["heading"]:
            cur["heading"] = sub.group(1).strip()
        cur["lines"].append(line)
    out.append(cur)
    return [dict(s, text="\n".join(s["lines"]).strip()) for s in out
            if "\n".join(s["lines"]).strip()]


def split_long(text, limit=MAX_WORDS):
    """Split an over-long section at paragraph, then sentence, boundaries."""
    pieces, buf = [], []
    units = []
    for para in re.split(r"\n\s*\n", text):
        if len(para.split()) > limit:
            units += re.split(r"(?<=[.!?])\s+", para)
        else:
            units.append(para)
    for unit in units:
        words = unit.split()
        while len(words) > limit:                      # a single monster sentence
            pieces.append(" ".join(words[:limit]))
            words = words[limit:]
        unit = " ".join(words) if len(unit.split()) > limit else unit
        if buf and len(" ".join(buf).split()) + len(unit.split()) > TARGET_WORDS:
            pieces.append("\n\n".join(buf))
            buf = []
        buf.append(unit)
    if buf:
        pieces.append("\n\n".join(buf))
    return [p for p in pieces if p.strip()]


def locator(kind, nums, slides=False):
    if not kind or not nums:
        return ""
    if kind == "page" and slides:          # a deck exported to PDF: pages are slides
        kind = "slide"
    if kind == "sheet":
        return "sheet " + ", ".join(dict.fromkeys(nums))
    label = {"page": ("p.", "pp."), "slide": ("slide", "slides")}[kind]
    first, last = nums[0], nums[-1]
    return f"{label[0]} {first}" if first == last else f"{label[1]} {first}–{last}"


JUNK = re.compile(r"_x[0-9A-Fa-f]{4}_|[\x00-\x08\x0b\x0c\x0e-\x1f]")
MAX_CHUNK_CHARS = 6000          # well under D1's 100 KB statement limit


def sanitize(text):
    """Strip encoded binary and absurdly long tokens that leak in from some files."""
    text = JUNK.sub("", text)
    return re.sub(r"\S{120,}", "", text)


def chunk(body, slides=False):
    """Pack sections into passages of ~TARGET_WORDS, keeping locators exact."""
    chunks, group = [], []

    def flush():
        if group:
            chunks.append({
                "locator": locator(group[0]["kind"], [g["num"] for g in group if g["num"]], slides),
                "heading": next((g["heading"] for g in group if g["heading"]), ""),
                "text": "\n\n".join(
                    (f"[{('Slide' if slides and g['kind'] == 'page' else g['kind'].title())} {g['num']}" + (f" — {g['heading']}" if g["heading"] else "")
                     + "]\n" if g["kind"] and len(group) > 1 else "") + g["text"]
                    for g in group),
            })
            group.clear()

    for sec in sections(sanitize(body)):
        words = len(sec["text"].split())
        if words > MAX_WORDS:
            flush()
            for piece in split_long(sec["text"]):
                group.append(dict(sec, text=piece))
                flush()
            continue
        size = sum(len(g["text"].split()) for g in group)
        if group and (size + words > TARGET_WORDS or group[0]["kind"] != sec["kind"]):
            flush()
        group.append(sec)
    flush()
    for c in chunks:
        if len(c["text"]) > MAX_CHUNK_CHARS:
            c["text"] = c["text"][:MAX_CHUNK_CHARS].rsplit(" ", 1)[0] + " …"
    return [c for c in chunks if c["text"].strip()]


SEASON_ORDER = {"IAP": 1, "Spring": 2, "Summer": 3, "Fall": 4}


def parse_term(term):
    """Canvas term name -> "Fall 2026"-style label, or "" if it names no semester.

    "Fall Term (AY 2026-2027)" -> "Fall 2026"; "Spring Term (AY 2026-2027)" -> "Spring 2027".
    """
    term = term or ""
    m = re.search(r"(Fall|Spring|Summer|IAP|January)\b.*?AY\s*(\d{4})\s*[-–/]\s*(\d{2,4})", term, re.I)
    if m:
        season = "IAP" if m.group(1).lower() in ("iap", "january") else m.group(1).title()
        first = int(m.group(2))
        return f"{season} {first if season == 'Fall' else first + 1}"
    m = re.search(r"(Fall|Spring|Summer|IAP)\s+(\d{4})", term, re.I)
    if m:
        season = "IAP" if m.group(1).lower() == "iap" else m.group(1).title()
        return f"{season} {m.group(2)}"
    return ""


def term_key(label):
    season, _, year = label.partition(" ")
    return (int(year) if year.isdigit() else 0, SEASON_ORDER.get(season, 0))


def term_from_date(date):
    """MIT calendar: Jan is IAP, Feb-May Spring, Jun-Jul Summer, Aug-Dec Fall."""
    m = re.match(r"(\d{4})-(\d{2})", date or "")
    if not m:
        return ""
    year, month = int(m.group(1)), int(m.group(2))
    season = "IAP" if month == 1 else "Spring" if month <= 5 else "Summer" if month <= 7 else "Fall"
    return f"{season} {year}"


def assign_semesters(docs):
    """Give every document a clean semester label, decided per course.

    Canvas names most terms ("Fall Term (AY 2026-2027)"); orientation sites and
    workshops say "Default term", so those fall back to their documents' dates.
    """
    groups = {}
    for d in docs:
        groups.setdefault(d["course"] or ("@" + d["path"]), []).append(d)
    named_terms = sorted({parse_term(d["term"]) for d in docs if parse_term(d["term"])}, key=term_key)
    for members in groups.values():
        named = [parse_term(d["term"]) for d in members if parse_term(d["term"])]
        if named:
            label = max(set(named), key=named.count)
        else:
            # Pre-term material (summer pre-work, orientation) belongs to the next real
            # semester; undated material to the first one.
            dates = sorted(d["date"] for d in members if d["date"])
            guess = term_from_date(dates[len(dates) // 2]) if dates else ""
            later = [t for t in named_terms if not guess or term_key(t) >= term_key(guess)]
            label = later[0] if later else guess
        for d in members:
            d["course_name"] = re.sub(r":\s*[A-Z]{1,2}\d?$", "", d["course_name"] or "").strip()  # drop ": E2" sections
            d["term"] = label
            d["hash"] = sha1(d["hash"], label, d["course_name"])[:20]   # relabeling re-uploads the doc


def collect(corpus_dir=CORPUS_DIR, rel_root=ROOT):
    """Read a corpus folder. Canvas often posts one file in two places; identical
    copies are indexed once, so an answer never cites the same passage twice."""
    docs, seen_bodies = [], set()
    paths = []
    for dirpath, _, files in os.walk(corpus_dir):
        for name in files:
            if name.endswith(".md") and name.lower() != "readme.md":
                paths.append(os.path.join(dirpath, name))
    # Plain names before "-a1b2c3" collision copies, so the clean name is kept.
    paths.sort(key=lambda p: (bool(re.search(r"-[0-9a-f]{6}\.md$", p)), p))
    for path in paths:
        name = os.path.basename(path)
        rel = os.path.relpath(path, rel_root).replace(os.sep, "/")
        with open(path, "rb") as f:
            digest = sha1(f.read().decode("utf-8", "replace"))
        meta, body = read_doc(path)
        body_key = sha1(body)
        if body_key in seen_bodies:
            continue
        seen_bodies.add(body_key)
        parts = chunk(body, slides=meta.get("type") == "slides")
        if not parts:
            continue
        title = meta.get("title") or os.path.splitext(name)[0]
        label = " · ".join(x for x in (meta.get("course"), meta.get("course_name"), title) if x)
        doc = {
            "id": sha1(rel)[:16], "path": rel, "title": title,
            "course": meta.get("course", ""), "course_name": meta.get("course_name", ""),
            "term": meta.get("term", ""), "type": meta.get("type", "document"),
            "module": meta.get("module", ""), "date": meta.get("date", ""),
            "source": meta.get("source", ""), "url": meta.get("url", ""),
            "locator_kind": meta.get("locator_kind", "section"), "hash": digest[:20],
            "words": len(body.split()), "n_chunks": len(parts),
        }
        doc["chunks"] = [dict(p, title=label, seq=i) for i, p in enumerate(parts)]
        docs.append(doc)
    assign_semesters(docs)
    return docs


# --------------------------------------------------------------------------
# SQL and upload
# --------------------------------------------------------------------------


def q(value):
    if value is None:
        return "NULL"
    if isinstance(value, int):
        return str(value)
    return "'" + str(value).replace("\x00", "").replace("'", "''") + "'"


def doc_sql(doc):
    yield f"DELETE FROM chunks WHERE doc_id = {q(doc['id'])};"
    yield f"DELETE FROM docs WHERE id = {q(doc['id'])};"
    yield ("INSERT INTO docs (" + ", ".join(DOC_FIELDS) + ") VALUES ("
           + ", ".join(q(doc[f]) for f in DOC_FIELDS) + ");")
    rows = []
    for c in doc["chunks"]:
        row = f"({q(doc['id'])}, {c['seq']}, {q(c['locator'])}, {q(c['heading'])}, {q(c['title'])}, {q(c['text'])})"
        if rows and sum(len(r) for r in rows) + len(row) > 60_000:   # D1: 100 KB per statement
            yield "INSERT INTO chunks (doc_id, seq, locator, heading, title, text) VALUES " + ", ".join(rows) + ";"
            rows = []
        rows.append(row)
    if rows:
        yield "INSERT INTO chunks (doc_id, seq, locator, heading, title, text) VALUES " + ", ".join(rows) + ";"


def wrangler(args):
    exe = shutil.which("npx") or shutil.which("npx.cmd")
    if not exe:
        sys.exit("npx not found. Install Node.js (nodejs.org), then run `npm install` in app/.")
    cmd = [exe, "wrangler", "d1", "execute", DB_NAME] + ENV_ARGS + args
    res = subprocess.run(cmd, cwd=APP_DIR, capture_output=True, text=True, encoding="utf-8")
    if res.returncode != 0:
        sys.exit(f"wrangler failed: {' '.join(args[:3])}\n{res.stdout[-2000:]}\n{res.stderr[-2000:]}")
    return res.stdout


def remote_hashes(where):
    out = wrangler([where, "--json", "--command", "SELECT id, hash FROM docs"])
    start = out.find("[")
    data = json.loads(out[start:]) if start != -1 else []
    rows = data[0].get("results", []) if data else []
    return {r["id"]: r["hash"] for r in rows}


def write_sql_files(statements):
    out_dir = os.path.join(BUILD_DIR, "sql")
    shutil.rmtree(out_dir, ignore_errors=True)
    os.makedirs(out_dir)
    files, buf, size = [], [], 0
    for stmt in statements:
        buf.append(stmt)
        size += len(stmt.encode("utf-8"))
        if size > SQL_FILE_BYTES:
            files.append(buf)
            buf, size = [], 0
    if buf:
        files.append(buf)
    paths = []
    for i, stmts in enumerate(files, 1):
        p = os.path.join(out_dir, f"sync-{i:03d}.sql")
        with open(p, "w", encoding="utf-8") as f:
            f.write("\n".join(stmts) + "\n")
        paths.append(p)
    return paths


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    where = ap.add_mutually_exclusive_group(required=True)
    where.add_argument("--local", action="store_true")
    where.add_argument("--remote", action="store_true")
    where.add_argument("--stats", action="store_true")
    ap.add_argument("--rebuild", action="store_true", help="drop and reload everything")
    ap.add_argument("--env", help="wrangler environment, e.g. demo (use with SLOAN_BRAIN_ROOT=demo)")
    ap.add_argument("--also", action="append", default=[],
                    help="extra corpus folder to index as its own shelf, e.g. demo/corpus")
    ap.add_argument("--shelf", default="MIT OpenCourseWare", help="shelf name for --also folders")
    ap.add_argument("--shelf-prefix", default="OCW ", help="prefix that keeps --also course codes apart")
    args = ap.parse_args()
    if args.env:
        ENV_ARGS.extend(["--env", args.env])

    docs = collect()
    credit_files = [os.path.join(ROOT, "credits.json")]
    for extra in args.also:
        # Another corpus shown as its own shelf (the private brain's OpenCourseWare courses).
        # Labeled after the semester pass so it can't shift your own courses' semesters.
        extra = os.path.abspath(extra)
        for d in collect(extra, CODE_ROOT):
            d["course_name"] = " · ".join(x for x in (d["course_name"], d["term"]) if x)
            d["course"] = f"{args.shelf_prefix}{d['course']}" if d["course"] else ""
            d["term"] = args.shelf
            d["hash"] = sha1(d["hash"], args.shelf, d["course"])[:20]
            docs.append(d)
        credit_files.append(os.path.join(os.path.dirname(extra), "credits.json"))
    n_chunks = sum(d["n_chunks"] for d in docs)
    words = sum(d["words"] for d in docs)
    print(f"{len(docs)} documents, {n_chunks} passages, {words:,} words")
    os.makedirs(BUILD_DIR, exist_ok=True)
    with open(os.path.join(BUILD_DIR, "index.jsonl"), "w", encoding="utf-8") as f:
        for d in docs:
            f.write(json.dumps(d, ensure_ascii=False) + "\n")
    if args.stats:
        by_course = {}
        for d in docs:
            by_course[d["course"] or "(no course)"] = by_course.get(d["course"] or "(no course)", 0) + 1
        for course, n in sorted(by_course.items()):
            print(f"  {course:<14} {n} docs")
        return

    flag = "--local" if args.local else "--remote"
    schema = os.path.join(APP_DIR, "schema.sql")
    if args.rebuild:
        print("Dropping existing tables")
        wrangler([flag, "--yes", "--command",
                  "DROP TABLE IF EXISTS chunks_fts; DROP TABLE IF EXISTS chunks; DROP TABLE IF EXISTS docs;"])
    wrangler([flag, "--yes", "--file", schema])

    credits = {}
    for path in credit_files:            # OpenCourseWare attribution shown in the reader
        if os.path.exists(path):
            with open(path, encoding="utf-8") as f:
                credits.update(json.load(f))
    if credits:
        wrangler([flag, "--yes", "--command",
                  f"INSERT OR REPLACE INTO meta (key, value) VALUES ('credits', {q(json.dumps(credits, ensure_ascii=False))});"])

    existing = {} if args.rebuild else remote_hashes(flag)
    local = {d["id"]: d for d in docs}
    changed = [d for d in docs if existing.get(d["id"]) != d["hash"]]
    removed = [i for i in existing if i not in local]
    print(f"{len(changed)} new or changed, {len(removed)} removed, "
          f"{len(docs) - len(changed)} unchanged")
    if not changed and not removed:
        print("Nothing to upload.")
        return

    def statements():
        for doc_id in removed:
            yield f"DELETE FROM chunks WHERE doc_id = {q(doc_id)};"
            yield f"DELETE FROM docs WHERE id = {q(doc_id)};"
        for d in changed:
            yield from doc_sql(d)

    paths = write_sql_files(statements())
    for i, p in enumerate(paths, 1):
        print(f"Uploading part {i}/{len(paths)}")
        wrangler([flag, "--yes", "--file", p])
    print("Done.")


if __name__ == "__main__":
    main()
