#!/usr/bin/env python3
"""
Import MIT OpenCourseWare course downloads into a corpus, for the public demo.

OCW publishes each course as a zip (the "Download course" button). Every file
in it carries its own license; only CC BY-NC-SA files are imported, so nothing
third-party ends up in a public app. Each document records where it came from,
and credits.json holds the attribution the demo shows for each course.

    python brain/ocw_import.py demo/ocw/*.zip --out demo
"""

import argparse
import html
import json
import os
import re
import sys
import tempfile
import zipfile

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from common import slugify, write_doc  # noqa: E402
from convert import PLURAL, Unsupported, convert_pdf, html_to_md  # noqa: E402

LICENSE = "https://creativecommons.org/licenses/by-nc-sa/4.0/"
TYPE_MAP = {
    "Lecture Notes": "slides", "Problem Sets": "assignment", "Problem Set Solutions": "assignment",
    "Exams": "assignment", "Exam Solutions": "assignment", "Problem-solving Notes": "reading",
    "Readings": "reading", "Case Studies": "case", "Supplemental Exam Materials": "assignment",
}
PAGE_TYPES = {"syllabus": "syllabus", "assignments": "assignment", "readings": "reading",
              "calendar": "page", "projects": "assignment"}
SKIP_PAGES = {"download", "instructor-insights"}


def humanize(filename):
    stem = re.sub(r"^[0-9a-f]{32}_", "", os.path.splitext(os.path.basename(filename))[0])
    stem = re.sub(r"^MIT\d+_\w+?_", "", stem)
    return re.sub(r"[_-]+", " ", stem).strip().capitalize()


def clean(text):
    text = html.unescape(re.sub(r"<[^>]+>", " ", text or ""))
    text = re.sub(r"\((?:PDF|XLS|DOC)[^)]*\)?\)?", "", text, flags=re.I)
    text = re.sub(r"^This resource contains (?:the )?information regarding\s*", "", text, flags=re.I)
    while re.search(r"\(\s*\)", text):
        text = re.sub(r"\(\s*\)", "", text)
    while text.count(")") > text.count("("):
        text = text[::-1].replace(")", "", 1)[::-1]
    text = re.sub(r"(?<=\w)\?(?=s\b)", "\u2019", text)          # "Intel?s" -> "Intel's"
    return re.sub(r"\s+", " ", text).strip(" -:|.")


GENERIC = re.compile(r"^(pdf|xls|doc|zip|download|link|here|slides?|handout|lecture notes file|file)?$", re.I)


PLAIN_HEADERS = {"assignments", "exams", "topics", "lecture notes", "files", "readings", "lec #", "ses #"}


def short(text, limit=72):
    text = re.split(r"\s*(?:Objectives?|Readings?):", text)[0].strip()
    if len(text) <= limit:
        return text
    cut = text[:limit].rsplit(" ", 1)[0]
    return cut.rstrip(",;:-") + "…"


def page_titles(zf):
    """OCW course pages list files in tables: | L3 | Consumer demand | (PDF) | Solutions (PDF) |.
    Title each file by its row's topic plus its column header or link text."""
    titles = {}
    link_re = re.compile(r'<a\b[^>]*href="[^"]*/resources/([^/"#]+)[^"]*"[^>]*>(.*?)</a>', re.S | re.I)
    for name in zf.namelist():
        if not re.match(r"pages/.+/data\.json$", name):
            continue
        content = json.loads(zf.read(name)).get("content") or ""
        for table in re.findall(r"<table\b.*?</table>", content, re.S | re.I):
            headers = [clean(h) for h in re.findall(r"<th\b.*?</th>", table, re.S | re.I)]
            for row in re.findall(r"<tr\b.*?</tr>", table, re.S | re.I):
                cells = re.findall(r"<td\b.*?</td>", row, re.S | re.I)
                topic = ""
                for c in cells:
                    first = re.split(r"<br\s*/?>|<li\b|</p>|<ul\b|<ol\b", c, maxsplit=1, flags=re.I)[0]
                    plain = clean(link_re.sub(" ", first)) or clean(link_re.sub(" ", c))
                    if plain and re.search(r"[A-Za-z]{3}", plain) and not re.fullmatch(r"(?:[A-Z]{1,3}\s*)?#?\d+[A-Z]?|[\d/.\- ]+", plain):
                        topic = short(plain)
                        break
                for i, c in enumerate(cells):
                    for ref, text in link_re.findall(c):
                        anchor = clean(text)
                        header = headers[i] if i < len(headers) else ""
                        header = header.capitalize() if header.isupper() else header
                        if not GENERIC.match(anchor):
                            title = anchor if not topic or topic.lower() in anchor.lower() else (
                                f"{anchor} ({topic})" if len(anchor) < 40 else anchor)
                        elif header and topic and header.lower().rstrip("s") not in topic.lower() \
                                and header.lower() not in PLAIN_HEADERS:
                            title = f"{topic} — {header[0].upper() + header[1:]}"
                        else:
                            title = topic or header
                        if title and ref not in titles:
                            titles[ref] = short(title, 110)
        for ref, text in link_re.findall(content):
            anchor = clean(text)
            if ref not in titles and not GENERIC.match(anchor) and len(anchor) > 6:
                titles[ref] = short(anchor, 110)
    return titles


def resource_title(meta, titles, folder):
    desc = clean(meta.get("description"))
    if folder in titles:
        return titles[folder]
    if desc and len(desc) <= 110 and not GENERIC.match(desc):
        return desc
    return humanize(meta.get("file") or meta.get("title") or "") or desc[:110]


def import_zip(path, out):
    zf = zipfile.ZipFile(path)
    site = json.loads(zf.read("data.json"))
    code = site.get("primary_course_number") or "?"
    term = f"{site.get('term', '')} {site.get('year', '')}".strip()
    base_url = f"https://ocw.mit.edu/{site['site_url_path']}/"
    raw = site.get("instructors") or []
    instructors = ([i.get("title", "") for i in raw if isinstance(i, dict)] if isinstance(raw, list)
                   else re.findall(r"'title': '([^']+)'", raw))
    credit = {
        "course": code, "title": site.get("course_title", ""), "term": term,
        "instructors": instructors, "url": base_url, "license": LICENSE,
    }
    common = {"course": code, "course_name": site.get("course_title", ""), "term": term,
              "source": "MIT OpenCourseWare"}
    written = skipped = 0
    seen_titles = set()

    def emit(meta, body):
        nonlocal written
        title = meta["title"] = re.sub(r"\s*\(+\s*\)+$", "", meta["title"]).strip()
        n = 2
        while (meta["type"], title) in seen_titles:
            title = f"{meta['title']} ({n})"
            n += 1
        seen_titles.add((meta["type"], title))
        meta["title"] = title
        plural = PLURAL.get(meta["type"], meta["type"])
        dest = os.path.join(out, "corpus", slugify(code), plural, slugify(title) + ".md")
        write_doc(dest, {**common, **meta}, body)
        written += 1

    # Course pages: syllabus, assignments, readings lists, case preparation, ...
    for name in sorted(zf.namelist()):
        m = re.match(r"pages/(.+)/data\.json$", name)
        if not m or m.group(1).split("/")[0] in SKIP_PAGES:
            continue
        page = json.loads(zf.read(name))
        body, _ = html_to_md(page.get("content") or "")
        if len(body.split()) < 40:
            continue
        key = m.group(1).split("/")[0]
        emit({"title": f"{code} {page.get('title') or humanize(key)}",
              "type": PAGE_TYPES.get(key, "page"), "url": base_url + "pages/" + m.group(1) + "/",
              "locator_kind": "section"}, body)

    # Files: only PDFs that OCW itself licenses CC BY-NC-SA.
    titles = page_titles(zf)
    with tempfile.TemporaryDirectory() as tmp:
        for name in sorted(zf.namelist()):
            if not re.match(r"resources/[^/]+/data\.json$", name):
                continue
            meta = json.loads(zf.read(name))
            if (meta.get("license") or "").rstrip("/") != LICENSE.rstrip("/") or meta.get("file_type") != "application/pdf":
                skipped += 1
                continue
            fname = os.path.basename(meta["file"])
            member = "static_resources/" + fname
            if member not in zf.namelist():
                skipped += 1
                continue
            local = zf.extract(member, tmp)
            try:
                body, info = convert_pdf(local)
            except Unsupported:
                skipped += 1
                continue
            kinds = meta.get("learning_resource_types") or []
            typ = TYPE_MAP.get(kinds[0], "reading") if kinds else "reading"
            if typ == "slides" and not info.get("slides"):
                typ = "reading"            # lecture notes that are prose, not decks
            emit({"title": resource_title(meta, titles, name.split("/")[1]), "type": typ,
                  "module": meta.get("parent_title", ""),
                  "url": "https://ocw.mit.edu" + meta["file"], "locator_kind": "page"}, body)
    print(f"{code} {term}: {written} documents, {skipped} files skipped")
    return credit


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("zips", nargs="+")
    ap.add_argument("--out", default="demo")
    args = ap.parse_args()
    path = os.path.join(args.out, "credits.json")
    credits = json.load(open(path, encoding="utf-8")) if os.path.exists(path) else {}
    for z in args.zips:
        c = import_zip(z, args.out)
        credits[c["course"]] = c
    with open(path, "w", encoding="utf-8") as f:
        json.dump(credits, f, indent=2, ensure_ascii=False)
    print(f"Wrote {os.path.join(args.out, 'credits.json')}")


if __name__ == "__main__":
    main()
