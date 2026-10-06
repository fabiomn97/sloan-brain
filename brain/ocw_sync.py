#!/usr/bin/env python3
"""
Keep the OpenCourseWare shelf in step with the courses in corpus/.

For every course number in your private corpus (15.010, 15.761, ...), look for
an MIT OpenCourseWare edition. If one exists and isn't imported yet, download
it and import its CC BY-NC-SA files into demo/. That content then appears in
both the public demo and, as its own shelf, in the private brain.

Runs in the deploy workflow on every push, so adding a course is enough.

    python brain/ocw_sync.py            import any missing editions
    python brain/ocw_sync.py --dry-run  only show what would be imported
"""

import argparse
import json
import os
import re
import sys
import urllib.request

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from common import CODE_ROOT, read_doc  # noqa: E402
import ocw_import  # noqa: E402

OCW = "https://ocw.mit.edu"
DEMO = os.path.join(CODE_ROOT, "demo")
SEASONS = {"january": 1, "iap": 1, "spring": 2, "summer": 3, "fall": 4}
UA = {"User-Agent": "sloan-brain-ocw-sync/1.0"}


def fetch(url, binary=False, timeout=120):
    with urllib.request.urlopen(urllib.request.Request(url, headers=UA), timeout=timeout) as r:
        data = r.read()
    return data if binary else data.decode("utf-8", "replace")


def private_course_codes():
    codes = set()
    corpus = os.path.join(CODE_ROOT, "corpus")
    for dirpath, _, files in os.walk(corpus):
        md = next((f for f in files if f.endswith(".md") and f.lower() != "readme.md"), None)
        if md:
            code = read_doc(os.path.join(dirpath, md))[0].get("course", "")
            if re.fullmatch(r"\d{1,2}\.[0-9A-Z]{2,5}", code or "", re.I):
                codes.add(code.upper())
    return sorted(codes)


def latest_edition(code, slugs):
    """Most recent OCW edition for a course number, e.g. 15.761 -> 15-761-...-spring-2013."""
    prefix = code.lower().replace(".", "-") + "-"
    best = None
    for slug in slugs:
        if not slug.startswith(prefix):
            continue
        m = re.search(r"-(january-iap|january|iap|spring|summer|fall)-(\d{4})$", slug)
        key = (int(m.group(2)), SEASONS.get(m.group(1).split("-")[-1], 0)) if m else (0, 0)
        if best is None or key > best[0]:
            best = (key, slug)
    return best[1] if best else None


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--dry-run", action="store_true")
    args = ap.parse_args()

    codes = private_course_codes()
    credits_path = os.path.join(DEMO, "credits.json")
    have = set(json.load(open(credits_path, encoding="utf-8"))) if os.path.exists(credits_path) else set()
    missing = [c for c in codes if c not in have]
    print(f"Private courses: {', '.join(codes) or 'none'}")
    if not missing:
        print("Every course with an OpenCourseWare edition is already imported.")
        return

    sitemap = fetch(f"{OCW}/sitemap.xml")
    slugs = sorted(set(re.findall(r"/courses/([a-z0-9-]+)/sitemap\.xml", sitemap)))
    todo = {c: latest_edition(c, slugs) for c in missing}
    for code, slug in todo.items():
        print(f"  {code}: {slug or 'no OpenCourseWare edition'}")
    todo = {c: s for c, s in todo.items() if s}
    if args.dry_run or not todo:
        return

    os.makedirs(os.path.join(DEMO, "ocw"), exist_ok=True)
    credits = json.load(open(credits_path, encoding="utf-8")) if os.path.exists(credits_path) else {}
    for code, slug in todo.items():
        page = fetch(f"{OCW}/courses/{slug}/download/")
        m = re.search(rf"https://ocw\.mit\.edu/courses/{re.escape(slug)}/[^\"']+\.zip", page)
        if not m:
            print(f"  {code}: no download zip found, skipped")
            continue
        dest = os.path.join(DEMO, "ocw", slug + ".zip")
        with open(dest, "wb") as f:
            f.write(fetch(m.group(0), binary=True, timeout=600))
        credit = ocw_import.import_zip(dest, DEMO)
        credits[credit["course"]] = credit
    with open(credits_path, "w", encoding="utf-8") as f:
        json.dump(credits, f, indent=2, ensure_ascii=False)


if __name__ == "__main__":
    main()
