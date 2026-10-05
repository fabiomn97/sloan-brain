#!/usr/bin/env python3
"""
Canvas harvester: save everything you can still reach on Canvas, for good.

For every course you are or were enrolled in, it saves:

  files         slides, readings, cases, spreadsheets: from the Files tab, from
                Modules, and from links inside pages, assignments and the syllabus
  syllabus      the syllabus page
  pages         every wiki page, including the front page
  assignments   the instructions (not your submissions)
  announcements every announcement
  discussions   the prompts only (other students' replies are theirs, not yours)

Everything lands in raw/ (local only, never committed). raw/manifest.jsonl
records what each file is; raw/failed.csv lists anything it could not get, and
why, so you can download those by hand and drop them into inbox/canvas/.

Safe to re-run: unchanged files are skipped, so a second run takes seconds.
Run it at the end of every semester, before Canvas access to old courses lapses.

Standard library only.

    python brain/canvas_harvest.py --list        show the courses it can see
    python brain/canvas_harvest.py               harvest every course
    python brain/canvas_harvest.py --course 15.010 --course 15.060
"""

import argparse
import csv
import html
import json
import os
import re
import ssl
import sys
import time
import urllib.error
import urllib.parse
import urllib.request
from datetime import datetime, timezone

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from common import (FAILED_CSV, RAW_DIR, ROOT, load_manifest, save_manifest,  # noqa: E402
                    slugify)

TIMEOUT = 60
USER_AGENT = "sloan-brain-harvester/1.0"
DEFAULT_CONFIG = os.path.join(ROOT, "config.json")
DEFAULTS = {"max_file_mb": 150, "ignore_course_ids": [], "include_discussions": True}
MEDIA = ("video/", "audio/")
COURSE_CODE = re.compile(r"\b(\d{1,2}\.[0-9A-Z]{2,4}[A-Z]?)\b")
FILE_LINK = re.compile(r"/(?:api/v1/)?(?:courses/(\d+)/)?files/(\d+)")
TOOL_LINK = re.compile(r'<a\b[^>]*href="([^"]*/external_tools/retrieve\?[^"]*)"[^>]*>(.*?)</a>', re.S | re.I)


# --------------------------------------------------------------------------
# Canvas API
# --------------------------------------------------------------------------


class CanvasError(Exception):
    pass


class Canvas:
    def __init__(self, host, token):
        self.host = host
        origin = host if host.startswith("http://") else f"https://{host}"   # http only for tests
        self.base = f"{origin}/api/v1"
        self.token = token
        self.ctx = ssl.create_default_context()

    def _open(self, url, auth=True):
        headers = {"User-Agent": USER_AGENT}
        if auth:
            headers["Authorization"] = f"Bearer {self.token}"
            headers["Accept"] = "application/json"
        req = urllib.request.Request(url, headers=headers)
        return urllib.request.urlopen(req, timeout=TIMEOUT, context=self.ctx)

    def _request(self, url):
        """GET with retries for rate limiting and transient server errors."""
        for attempt in range(5):
            try:
                with self._open(url) as resp:
                    return json.loads(resp.read().decode("utf-8")), resp.headers.get("Link", "")
            except urllib.error.HTTPError as e:
                body = e.read().decode("utf-8", "ignore")
                if e.code == 401 and "access token" in body.lower():
                    raise CanvasError("Canvas rejected the access token (401). Generate a "
                                      "new one in Canvas > Account > Settings and update "
                                      "config.json.")
                throttled = e.code == 403 and "rate limit" in body.lower()
                if (throttled or e.code >= 500) and attempt < 4:
                    time.sleep(2 ** attempt * 2)
                    continue
                raise
            except urllib.error.URLError as e:
                if attempt < 4:
                    time.sleep(2 ** attempt * 2)
                    continue
                raise CanvasError(f"Couldn't reach Canvas: {e.reason}")
        raise CanvasError(f"Gave up on {url}")

    @staticmethod
    def _next_link(header):
        for part in header.split(","):
            bits = part.split(";")
            if len(bits) > 1 and 'rel="next"' in bits[1].replace(" ", ""):
                return bits[0].strip().strip("<>")
        return None

    def get_one(self, path, params=None):
        query = urllib.parse.urlencode(params or [], doseq=True)
        data, _ = self._request(f"{self.base}{path}" + (f"?{query}" if query else ""))
        return data

    def get_all(self, path, params=None):
        params = list(params or []) + [("per_page", 100)]
        url = f"{self.base}{path}?{urllib.parse.urlencode(params, doseq=True)}"
        results, pages = [], 0
        while url and pages < 200:
            data, link = self._request(url)
            results.extend(data if isinstance(data, list) else [data])
            url = self._next_link(link)
            pages += 1
        return results

    def download(self, url, dest):
        """Stream a file to disk. Pre-signed URLs need no token; fall back to one."""
        tmp = dest + ".part"
        os.makedirs(os.path.dirname(dest), exist_ok=True)
        last = None
        for auth in (False, True):
            try:
                with self._open(url, auth=auth) as resp, open(tmp, "wb") as out:
                    while True:
                        block = resp.read(1 << 20)
                        if not block:
                            break
                        out.write(block)
                os.replace(tmp, dest)
                return
            except (urllib.error.HTTPError, urllib.error.URLError, TimeoutError) as e:
                last = e
        if os.path.exists(tmp):
            os.remove(tmp)
        raise last


# --------------------------------------------------------------------------
# Harvest
# --------------------------------------------------------------------------


def http_reason(e):
    if isinstance(e, urllib.error.HTTPError):
        return {401: "not authorized (the instructor restricted it)",
                403: "forbidden (locked, hidden, or restricted)",
                404: "not found (deleted or moved)"}.get(e.code, f"HTTP {e.code}")
    return str(getattr(e, "reason", e))


def course_label(course):
    text = f"{course.get('course_code', '')} {course.get('name', '')}"
    match = COURSE_CODE.search(text)
    return match.group(1) if match else (course.get("course_code") or str(course["id"])).strip()


def html_page(title, meta_lines, body):
    """Save Canvas HTML with a small header the converter knows how to read."""
    head = "".join(f'<meta name="{k}" content="{html.escape(str(v))}">\n'
                   for k, v in meta_lines.items() if v)
    return (f"<!doctype html>\n<html><head><meta charset=\"utf-8\">\n"
            f"<title>{html.escape(title)}</title>\n{head}</head>\n"
            f"<body>\n<h1>{html.escape(title)}</h1>\n{body or ''}\n</body></html>\n")


class Harvester:
    def __init__(self, api, cfg, manifest):
        self.api = api
        self.cfg = cfg
        self.manifest = manifest
        self.failures = []
        self.stats = {"saved": 0, "unchanged": 0, "failed": 0, "skipped": 0}

    # -- bookkeeping -------------------------------------------------------

    def fail(self, course, kind, title, url, reason, status="failed", todo=""):
        self.failures.append({
            "status": status, "course": course["label"], "term": course["term"],
            "kind": kind, "title": title, "canvas_url": url, "reason": reason,
            "what_to_do": todo or "Open the link, download it, and put it in "
                                  f"inbox/canvas/{slugify(course['label'])}/",
        })
        self.stats["skipped" if status == "skipped" else "failed"] += 1

    def record(self, course, key, kind, title, path, **extra):
        entry = {
            "key": key, "kind": kind, "title": title,
            "course_id": course["id"], "course": course["label"],
            "course_name": course["name"], "term": course["term"],
            "path": os.path.relpath(path, RAW_DIR).replace(os.sep, "/"),
            "harvested_at": datetime.now(timezone.utc).isoformat(timespec="seconds"),
        }
        entry.update({k: v for k, v in extra.items() if v not in (None, "")})
        self.manifest[key] = entry
        self.stats["saved"] += 1

    def course_dir(self, course):
        return os.path.join(RAW_DIR, slugify(course["term"] or "no-term"),
                            slugify(course["label"]))

    def save_html(self, course, key, kind, title, sub, name, body, **extra):
        path = os.path.join(self.course_dir(course), sub, slugify(name) + ".html")
        meta = {"course": course["label"], "course_name": course["name"],
                "term": course["term"], "kind": kind, "module": extra.get("module"),
                "date": extra.get("date"), "url": extra.get("url")}
        os.makedirs(os.path.dirname(path), exist_ok=True)
        with open(path, "w", encoding="utf-8") as f:
            f.write(html_page(title, meta, body))
        self.record(course, key, kind, title, path, **extra)
        return body or ""

    # -- courses -----------------------------------------------------------

    def courses(self):
        seen = {}
        for params in ([("enrollment_state", "active")],
                       [("enrollment_state", "completed")],
                       [("include[]", "concluded")]):
            try:
                rows = self.api.get_all("/courses", params + [("include[]", "term")])
            except urllib.error.HTTPError:
                continue
            for c in rows:
                if c.get("id") and c.get("name") and c["id"] not in seen:
                    seen[c["id"]] = c
        out = []
        for c in seen.values():
            if c["id"] in self.cfg["ignore_course_ids"] or c.get("access_restricted_by_date"):
                continue
            label = course_label(c)
            name = re.sub(r"^\s*" + re.escape(label) + r"[\w-]*\s*[-:–|]?\s*", "", c.get("name") or "").strip()
            out.append({"id": c["id"], "label": label,
                        "name": name or (c.get("name") or "").strip(),
                        "term": ((c.get("term") or {}).get("name") or "").strip(),
                        "url": f"{self.api.base[:-7]}/courses/{c['id']}"})
        return sorted(out, key=lambda c: (c["term"], c["label"]))

    # -- one course ----------------------------------------------------------

    def harvest(self, course):
        cid = course["id"]
        print(f"\n{course['label']}  {course['name']}  [{course['term'] or 'no term'}]")
        bodies = []                                   # HTML to scan for file links
        modules, file_ids = self.modules(course)

        try:
            info = self.api.get_one(f"/courses/{cid}", [("include[]", "syllabus_body")])
            if (info.get("syllabus_body") or "").strip():
                bodies.append(self.save_html(
                    course, f"syllabus:{cid}", "syllabus", f"{course['label']} syllabus",
                    "", "syllabus", info["syllabus_body"], url=f"{course['url']}/assignments/syllabus"))
        except urllib.error.HTTPError as e:
            self.fail(course, "syllabus", "Syllabus", f"{course['url']}/assignments/syllabus", http_reason(e))

        bodies += self.pages(course, modules)
        bodies += self.assignments(course, modules)
        bodies += self.announcements(course)
        if self.cfg["include_discussions"]:
            bodies += self.discussions(course, modules)

        tools = {}
        for body in bodies:
            for link_course, fid in FILE_LINK.findall(body or ""):
                if not link_course or int(link_course) == cid:
                    file_ids.setdefault(int(fid), "")
            # Cases and articles sold through Harvard Business Publishing (and other
            # LTI tools) open inside Canvas but can't be fetched through the API.
            for href, text in TOOL_LINK.findall(body or ""):
                title = re.sub(r"\s+", " ", re.sub(r"<[^>]+>", "", html.unescape(text))).strip()
                tools.setdefault(html.unescape(href), title or "Linked reading")
        for href, title in tools.items():
            vendor = "Harvard Business Publishing" if "hbsp" in urllib.parse.unquote(href) else "an external tool"
            self.fail(course, "linked reading", title, href, f"sold through {vendor}; not downloadable via API",
                      status="manual", todo="Open it from Canvas (your coursepack), download the PDF, and "
                                            f"save it in inbox/canvas/{slugify(course['label'])}/")
        self.files(course, modules, file_ids)

    def modules(self, course):
        """Map Canvas content to its module name ('Week 3: Pricing'), for context."""
        names, file_ids = {}, {}
        try:
            mods = self.api.get_all(f"/courses/{course['id']}/modules", [("include[]", "items")])
        except urllib.error.HTTPError:
            return names, file_ids
        for m in mods:
            items = m.get("items")
            if items is None:
                try:
                    items = self.api.get_all(f"/courses/{course['id']}/modules/{m['id']}/items")
                except urllib.error.HTTPError:
                    items = []
            for it in items:
                kind, mname = it.get("type"), (m.get("name") or "").strip()
                if kind == "File" and it.get("content_id"):
                    file_ids[it["content_id"]] = mname
                    names[("file", it["content_id"])] = mname
                elif kind == "Page" and it.get("page_url"):
                    names[("page", it["page_url"])] = mname
                elif kind in ("Assignment", "Discussion", "Quiz") and it.get("content_id"):
                    names[(kind.lower(), it["content_id"])] = mname
                elif kind in ("ExternalUrl", "ExternalTool"):
                    url = it.get("external_url") or it.get("html_url") or ""
                    self.external(course, it.get("title") or url, url, mname)
        return names, file_ids

    def external(self, course, title, url, module):
        """Module links to outside sites. Direct PDF links are fetched; the rest listed."""
        if re.search(r"\.pdf(\?|$)", url, re.I):
            name = slugify(os.path.splitext(os.path.basename(urllib.parse.urlparse(url).path))[0])
            dest = os.path.join(self.course_dir(course), "files", "_external", name + ".pdf")
            try:
                if not os.path.exists(dest):
                    self.api.download(url, dest)
                self.record(course, f"external:{url}", "file", title, dest, module=module,
                            url=url, content_type="application/pdf")
                return
            except Exception as e:  # noqa: BLE001 -- any failure is reported, not fatal
                reason = http_reason(e)
        else:
            reason = "external site (case vendor, video, tool, or article)"
        self.fail(course, "external link", title, url, reason, status="manual",
                  todo="If it's a reading you want kept, save it as PDF and put it in "
                       f"inbox/canvas/{slugify(course['label'])}/")

    def pages(self, course, modules):
        out = []
        try:
            pages = self.api.get_all(f"/courses/{course['id']}/pages")
        except urllib.error.HTTPError as e:
            if e.code not in (401, 403, 404):
                self.fail(course, "pages", "Pages list", f"{course['url']}/pages", http_reason(e))
            return out
        for p in pages:
            slug = p.get("url")
            try:
                full = self.api.get_one(f"/courses/{course['id']}/pages/{urllib.parse.quote(slug)}")
            except urllib.error.HTTPError as e:
                self.fail(course, "page", p.get("title") or slug, p.get("html_url", ""), http_reason(e))
                continue
            out.append(self.save_html(
                course, f"page:{course['id']}:{slug}", "page", full.get("title") or slug,
                "pages", slug, full.get("body"), module=modules.get(("page", slug)),
                url=full.get("html_url"), date=(full.get("updated_at") or "")[:10],
                updated_at=full.get("updated_at")))
        return out

    def assignments(self, course, modules):
        out = []
        try:
            rows = self.api.get_all(f"/courses/{course['id']}/assignments")
        except urllib.error.HTTPError:
            return out
        for a in rows:
            due = a.get("due_at") or ""
            facts = []
            if due:
                facts.append(f"<p><strong>Due:</strong> {html.escape(due[:10])}</p>")
            if a.get("points_possible"):
                facts.append(f"<p><strong>Points:</strong> {a['points_possible']}</p>")
            body = "".join(facts) + (a.get("description") or "")
            out.append(self.save_html(
                course, f"assignment:{a['id']}", "assignment", a.get("name") or "Assignment",
                "assignments", f"{a.get('name', '')}-{a['id']}", body,
                module=modules.get(("assignment", a["id"])), url=a.get("html_url"),
                date=due[:10], updated_at=a.get("updated_at")))
        return out

    def announcements(self, course):
        out = []
        try:
            rows = self.api.get_all(f"/courses/{course['id']}/discussion_topics",
                                    [("only_announcements", "true")])
        except urllib.error.HTTPError:
            return out
        for a in rows:
            date = (a.get("posted_at") or a.get("created_at") or "")[:10]
            author = (a.get("author") or {}).get("display_name") or a.get("user_name") or ""
            body = (f"<p><em>Posted {html.escape(date)} by {html.escape(author)}</em></p>"
                    if author else "") + (a.get("message") or "")
            out.append(self.save_html(
                course, f"announcement:{a['id']}", "announcement", a.get("title") or "Announcement",
                "announcements", f"{date}-{a.get('title', '')}", body,
                url=a.get("html_url"), date=date, updated_at=a.get("updated_at") or date))
        return out

    def discussions(self, course, modules):
        out = []
        try:
            rows = self.api.get_all(f"/courses/{course['id']}/discussion_topics")
        except urllib.error.HTTPError:
            return out
        for d in rows:
            if d.get("is_announcement"):
                continue
            date = (d.get("posted_at") or d.get("created_at") or "")[:10]
            out.append(self.save_html(
                course, f"discussion:{d['id']}", "discussion", d.get("title") or "Discussion",
                "discussions", f"{d.get('title', '')}-{d['id']}", d.get("message"),
                module=modules.get(("discussion", d["id"])), url=d.get("html_url"),
                date=date, updated_at=d.get("updated_at") or date))
        return out

    def files(self, course, modules, file_ids):
        cid = course["id"]
        folders = {}
        try:
            for f in self.api.get_all(f"/courses/{cid}/folders"):
                folders[f["id"]] = re.sub(r"^course files/?", "", f.get("full_name") or "")
        except urllib.error.HTTPError:
            pass

        listed = {}
        try:
            for f in self.api.get_all(f"/courses/{cid}/files"):
                listed[f["id"]] = f
        except urllib.error.HTTPError as e:
            # Common: the instructor hid the Files tab. Modules and links still work.
            print(f"  Files tab not accessible ({http_reason(e)}); using modules and links")

        for fid in file_ids:
            if fid in listed:
                continue
            try:
                listed[fid] = self.api.get_one(f"/courses/{cid}/files/{fid}")
            except urllib.error.HTTPError as e:
                try:
                    listed[fid] = self.api.get_one(f"/files/{fid}")
                except urllib.error.HTTPError:
                    self.fail(course, "file", f"file {fid}", f"{course['url']}/files/{fid}",
                              http_reason(e))

        print(f"  {len(listed)} files")
        used_paths = set()
        for fid, f in sorted(listed.items()):
            self.one_file(course, f, folders, modules, used_paths)

    def one_file(self, course, f, folders, modules, used_paths):
        fid, name = f["id"], f.get("display_name") or f.get("filename") or str(f["id"])
        key = f"file:{fid}"
        page_url = f"{course['url']}/files/{fid}"
        ctype = f.get("content-type") or f.get("content_type") or ""
        size_mb = (f.get("size") or 0) / 1e6
        if ctype.startswith(MEDIA):
            self.fail(course, "file", name, page_url, "video/audio, not text", status="skipped",
                      todo="Download by hand only if you want the recording itself")
            return
        if size_mb > self.cfg["max_file_mb"]:
            self.fail(course, "file", name, page_url, f"{size_mb:.0f} MB, over max_file_mb",
                      status="skipped", todo="Raise max_file_mb in config.json, or download by hand")
            return
        if f.get("locked_for_user") or not f.get("url"):
            reason = f.get("lock_explanation") or "locked or not downloadable"
            self.fail(course, "file", name, page_url, re.sub(r"<[^>]+>", "", reason))
            return

        folder = folders.get(f.get("folder_id"), "")
        base, ext = os.path.splitext(name)
        rel = os.path.join(*(slugify(p) for p in folder.split("/") if p), "") if folder else ""
        dest = os.path.join(self.course_dir(course), "files", rel, slugify(base) + ext.lower())
        if dest in used_paths:
            dest = os.path.join(os.path.dirname(dest), f"{slugify(base)}-{fid}{ext.lower()}")
        used_paths.add(dest)

        old = self.manifest.get(key)
        if (old and old.get("updated_at") == f.get("updated_at")
                and os.path.exists(os.path.join(RAW_DIR, old["path"]))):
            self.stats["unchanged"] += 1
            return
        try:
            self.api.download(f["url"], dest)
        except Exception as e:  # noqa: BLE001 -- report and keep going
            self.fail(course, "file", name, page_url, http_reason(e))
            return
        self.record(course, key, "file", name, dest, module=modules.get(("file", fid)),
                    folder=folder, url=page_url, content_type=ctype, size=f.get("size"),
                    updated_at=f.get("updated_at"), date=(f.get("created_at") or "")[:10])


def write_failures(failures):
    os.makedirs(RAW_DIR, exist_ok=True)
    cols = ["status", "course", "term", "kind", "title", "reason", "what_to_do", "canvas_url"]
    with open(FAILED_CSV, "w", encoding="utf-8-sig", newline="") as f:
        w = csv.DictWriter(f, fieldnames=cols, extrasaction="ignore")
        w.writeheader()
        order = {"failed": 0, "manual": 1, "skipped": 2}
        for row in sorted(failures, key=lambda r: (order.get(r["status"], 3), r["term"], r["course"])):
            w.writerow(row)


def load_config(path):
    if not os.path.exists(path):
        sys.exit(f"No config found at {path}. Copy config.example.json to config.json "
                 "and paste your Canvas token, or point --config at your digest's config.json.")
    with open(path, encoding="utf-8") as f:
        cfg = dict(DEFAULTS, **json.load(f))
    if not cfg.get("canvas_token") or "PASTE" in cfg["canvas_token"]:
        sys.exit("config.json has no canvas_token.")
    host = (cfg.get("canvas_host") or "canvas.mit.edu").strip("/")
    local = host.startswith(("http://localhost", "http://127.0.0.1"))
    cfg["canvas_host"] = host if local else host.replace("https://", "").replace("http://", "")
    return cfg


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--config", default=DEFAULT_CONFIG, help="path to config.json")
    ap.add_argument("--list", action="store_true", help="list courses and exit")
    ap.add_argument("--course", action="append", default=[],
                    help="only this course code or Canvas id (repeatable)")
    args = ap.parse_args()

    cfg = load_config(args.config)
    api = Canvas(cfg["canvas_host"], cfg["canvas_token"])
    manifest = load_manifest()
    h = Harvester(api, cfg, manifest)
    try:
        courses = h.courses()
    except CanvasError as e:
        sys.exit(str(e))

    if args.list:
        for c in courses:
            print(f"{c['id']:>8}  {c['label']:<10} {c['term']:<18} {c['name']}")
        print(f"\n{len(courses)} courses")
        return
    if args.course:
        wanted = {w.lower() for w in args.course}
        courses = [c for c in courses if c["label"].lower() in wanted or str(c["id"]) in wanted]

    try:
        for course in courses:
            try:
                h.harvest(course)
            except urllib.error.HTTPError as e:
                h.fail(course, "course", course["name"], course["url"], http_reason(e))
            save_manifest(manifest)   # checkpoint after every course
    except CanvasError as e:
        print(f"\nStopped: {e}")
    except KeyboardInterrupt:
        print("\nInterrupted. Progress so far is saved; re-run to continue.")
    finally:
        save_manifest(manifest)
        write_failures(h.failures)

    s = h.stats
    print(f"\nDone. {s['saved']} saved, {s['unchanged']} unchanged, "
          f"{s['failed']} failed, {s['skipped']} skipped (video or too large).")
    if h.failures:
        print(f"See {os.path.relpath(FAILED_CSV, ROOT)} for what needs a manual download.")
    print("Next: python brain/convert.py")


if __name__ == "__main__":
    main()
