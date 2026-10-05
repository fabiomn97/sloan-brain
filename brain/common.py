"""Shared helpers: paths, slugs, and the front-matter format every corpus file uses."""

import hashlib
import json
import os
import re
import unicodedata

CODE_ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
# SLOAN_BRAIN_ROOT lets the tests run the pipeline in a scratch folder.
ROOT = os.environ.get("SLOAN_BRAIN_ROOT") or CODE_ROOT
RAW_DIR = os.path.join(ROOT, "raw")            # originals, local only (gitignored)
CORPUS_DIR = os.path.join(ROOT, "corpus")      # Markdown, committed to the private repo
INBOX_DIR = os.path.join(ROOT, "inbox")        # anything you add by hand
BUILD_DIR = os.path.join(ROOT, "build")        # index output (gitignored)
MANIFEST = os.path.join(RAW_DIR, "manifest.jsonl")
FAILED_CSV = os.path.join(RAW_DIR, "failed.csv")

# Order matters: front matter is written in this order so diffs stay readable.
FIELDS = ["title", "course", "course_name", "term", "type", "module", "date",
          "source", "url", "original", "locator_kind", "notes"]

TYPES = {
    "slides", "reading", "case", "syllabus", "assignment", "page", "announcement",
    "discussion", "transcript", "newsletter", "note", "document", "spreadsheet",
}


def slugify(text, limit=80):
    text = unicodedata.normalize("NFKD", text or "").encode("ascii", "ignore").decode()
    text = re.sub(r"[^A-Za-z0-9.]+", "-", text).strip("-.").lower()
    return (text[:limit].rstrip("-.") or "untitled")


def sha1(*parts):
    h = hashlib.sha1()
    for p in parts:
        h.update(str(p).encode("utf-8"))
        h.update(b"\0")
    return h.hexdigest()


def file_sha1(path):
    h = hashlib.sha1()
    with open(path, "rb") as f:
        for block in iter(lambda: f.read(1 << 20), b""):
            h.update(block)
    return h.hexdigest()


def write_doc(path, meta, body):
    """Write a corpus Markdown file. Values are JSON-quoted, which is valid YAML."""
    os.makedirs(os.path.dirname(path), exist_ok=True)
    lines = ["---"]
    for key in FIELDS:
        value = meta.get(key)
        if value not in (None, ""):
            lines.append(f"{key}: {json.dumps(str(value), ensure_ascii=False)}")
    lines.append("---")
    text = "\n".join(lines) + "\n\n" + body.strip() + "\n"
    with open(path, "w", encoding="utf-8", newline="\n") as f:
        f.write(text)


def read_doc(path):
    """Return (meta, body). Tolerates hand-written files with no front matter."""
    with open(path, encoding="utf-8") as f:
        text = f.read()
    meta = {}
    if text.startswith("---\n"):
        end = text.find("\n---", 4)
        if end != -1:
            for line in text[4:end].splitlines():
                if ":" not in line:
                    continue
                key, _, value = line.partition(":")
                value = value.strip()
                if value.startswith('"'):
                    try:
                        value = json.loads(value)
                    except json.JSONDecodeError:
                        value = value.strip('"')
                meta[key.strip()] = value
            text = text[end + 4:]
    return meta, text.strip()


def load_manifest():
    entries = {}
    if os.path.exists(MANIFEST):
        with open(MANIFEST, encoding="utf-8") as f:
            for line in f:
                line = line.strip()
                if line:
                    item = json.loads(line)
                    entries[item["key"]] = item
    return entries


def save_manifest(entries):
    os.makedirs(RAW_DIR, exist_ok=True)
    tmp = MANIFEST + ".tmp"
    with open(tmp, "w", encoding="utf-8") as f:
        for key in sorted(entries):
            f.write(json.dumps(entries[key], ensure_ascii=False) + "\n")
    os.replace(tmp, MANIFEST)
