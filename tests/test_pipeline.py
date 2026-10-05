#!/usr/bin/env python3
"""End-to-end test: fake Canvas -> harvest -> convert -> index.

Runs entirely offline in a scratch folder:

    python tests/test_pipeline.py            run the checks
    python tests/test_pipeline.py --keep DIR keep the scratch folder (for local previews)
"""

import csv
import json
import os
import shutil
import subprocess
import sys
import tempfile
import threading
import urllib.parse
from http.server import BaseHTTPRequestHandler, ThreadingHTTPServer

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(HERE)
sys.path.insert(0, HERE)
import fixtures  # noqa: E402


def canvas_data(files):
    T = "2026-09-20T12:00:00Z"

    def f(fid, key, folder, ctype, **kw):
        path = files.get(key)
        d = {"id": fid, "display_name": os.path.basename(path) if path else kw.pop("name"),
             "content-type": ctype, "size": os.path.getsize(path) if path else kw.pop("size", 10),
             "folder_id": folder, "updated_at": T, "created_at": "2026-09-18T12:00:00Z",
             "url": f"/files/{fid}/download?verifier=abc", "locked_for_user": False}
        d.update(kw)
        return d

    return {
        "courses": {
            "active": [
                {"id": 101, "name": "15.010 Economic Analysis for Business Decisions",
                 "course_code": "15.010-F26", "term": {"name": "Fall 2026"}},
                {"id": 102, "name": "Organizational Processes", "course_code": "15.311",
                 "term": {"name": "Fall 2026"}},
            ],
            "completed": [
                {"id": 103, "name": "15.761 Introduction to Operations Management",
                 "course_code": "15.761", "term": {"name": "Fall 2026"}},
            ],
        },
        "syllabus": {101: "<h2>Course overview</h2><p>Economics for managers: demand, pricing, "
                          "competition, and strategy. Grading: 40% problem sets, 60% exams.</p>"},
        "files": {
            101: [f(1001, "pricing_pptx", 11, "application/vnd.openxmlformats-officedocument.presentationml.presentation"),
                  f(1002, "pd_note_pdf", 12, "application/pdf"),
                  f(1003, None, 11, "video/mp4", name="Session 4 recording.mp4", size=900_000_000)],
            102: None,                                    # Files tab hidden: 403
            103: [f(3001, "littles_docx", 31, "application/vnd.openxmlformats-officedocument.wordprocessingml.document"),
                  f(3002, "newsvendor_xlsx", 31, "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet")],
        },
        "single_files": {
            2001: f(2001, "feedback_pdf", 21, "application/pdf"),
            2002: f(2002, None, 21, "application/pdf", name="Peer review rubric.pdf",
                    locked_for_user=True, url=None, lock_explanation="This file is locked until <b>Oct 30</b>."),
        },
        "folders": {101: [{"id": 11, "full_name": "course files/Lecture Slides"},
                          {"id": 12, "full_name": "course files/Readings"}],
                    102: [], 103: [{"id": 31, "full_name": "course files/Session 3"}]},
        "modules": {
            101: [{"id": 1, "name": "Week 4: Pricing", "items": [
                {"type": "File", "content_id": 1001, "title": "Slides"},
                {"type": "Page", "page_url": "session-4-prep", "title": "Prep"},
                {"type": "ExternalUrl", "title": "HBS case: Pricing a subscription",
                 "external_url": "https://hbsp.harvard.edu/product/123"}]}],
            102: [{"id": 2, "name": "Session 7: Feedback", "items": [
                {"type": "File", "content_id": 2001, "title": "Slides"},
                {"type": "File", "content_id": 2002, "title": "Rubric"},
                {"type": "Assignment", "content_id": 501, "title": "Team charter"}]}],
            103: [],
        },
        "pages": {101: [{"url": "session-4-prep", "title": "Session 4 prep",
                         "html_url": "/courses/101/pages/session-4-prep", "updated_at": T,
                         "body": "<p>Before class, read the <a href='/courses/101/files/1002'>note on "
                                 "price discrimination</a> and think about how an airline sets fares.</p>"}],
                  102: [], 103: []},
        "assignments": {101: [], 103: [],
                        102: [{"id": 501, "name": "Team charter", "due_at": "2026-09-25T04:00:00Z",
                               "points_possible": 10, "html_url": "/courses/102/assignments/501",
                               "updated_at": T, "description":
                               "<p>Agree with your Core Team on <strong>how you will give feedback</strong>, "
                               "how you will make decisions, and what happens when someone misses a deadline.</p>"}]},
        "announcements": {101: [{"id": 9001, "title": "Problem set 2 posted", "posted_at": T,
                                 "author": {"display_name": "Teaching team"},
                                 "message": "<p>Problem set 2 on elasticity is now on Canvas.</p>",
                                 "html_url": "/courses/101/discussion_topics/9001"}],
                          102: [], 103: []},
    }


def make_handler(data, files):
    class H(BaseHTTPRequestHandler):
        def log_message(self, *a):
            pass

        def send(self, obj, code=200, link=None):
            body = json.dumps(obj).encode()
            self.send_response(code)
            self.send_header("Content-Type", "application/json")
            if link:
                self.send_header("Link", link)
            self.end_headers()
            self.wfile.write(body)

        def do_GET(self):
            u = urllib.parse.urlparse(self.path)
            qs = urllib.parse.parse_qs(u.query)
            parts = u.path.strip("/").split("/")
            origin = f"http://{self.headers['Host']}"
            if parts[0] == "files" and parts[-1] == "download":
                fid = int(parts[1])
                meta = next((x for v in list(data["files"].values()) + [list(data["single_files"].values())]
                             if v for x in v if x["id"] == fid), None)
                key = {1001: "pricing_pptx", 1002: "pd_note_pdf", 2001: "feedback_pdf",
                       3001: "littles_docx", 3002: "newsvendor_xlsx"}.get(fid)
                if not meta or not key:
                    return self.send({"error": "nope"}, 404)
                if "Authorization" in self.headers:          # presigned URLs reject tokens
                    return self.send({"error": "only one auth mechanism"}, 400)
                with open(files[key], "rb") as fh:
                    blob = fh.read()
                self.send_response(200)
                self.send_header("Content-Type", "application/octet-stream")
                self.end_headers()
                self.wfile.write(blob)
                return
            if self.headers.get("Authorization") != "Bearer test-token":
                return self.send({"errors": [{"message": "Invalid access token."}]}, 401)
            p = parts[2:]                                      # after api/v1

            def absolutize(objs):
                out = []
                for o in objs:
                    o = dict(o)
                    for k in ("url", "html_url"):
                        if o.get(k) and o[k].startswith("/"):
                            o[k] = origin + o[k]
                    out.append(o)
                return out

            if p == ["courses"]:
                st = qs.get("enrollment_state", [None])[0]
                if st:
                    return self.send(data["courses"].get(st, []))
                return self.send(data["courses"]["active"] + data["courses"]["completed"])
            cid = int(p[1])
            if len(p) == 2:
                return self.send({"id": cid, "syllabus_body": data["syllabus"].get(cid, "")})
            what = p[2]
            if what == "files" and len(p) == 3:
                listed = data["files"][cid]
                if listed is None:
                    return self.send({"status": "unauthorized"}, 403)
                page = int(qs.get("page", ["1"])[0])
                chunk = listed[(page - 1) * 2: page * 2]
                link = None
                if page * 2 < len(listed):
                    link = f'<{origin}/api/v1/courses/{cid}/files?page={page + 1}&per_page=100>; rel="next"'
                return self.send(absolutize(chunk), link=link)
            if what == "files":
                fid = int(p[3])
                meta = data["single_files"].get(fid) or next(
                    (x for x in (data["files"].get(cid) or []) if x["id"] == fid), None)
                return self.send(absolutize([meta])[0]) if meta else self.send({}, 404)
            if what == "folders":
                return self.send(data["folders"][cid])
            if what == "modules":
                return self.send(data["modules"][cid])
            if what == "pages":
                if len(p) == 3:
                    return self.send(absolutize([{k: v for k, v in pg.items() if k != "body"}
                                                 for pg in data["pages"][cid]]))
                pg = next(x for x in data["pages"][cid] if x["url"] == p[3])
                return self.send(absolutize([pg])[0])
            if what == "assignments":
                return self.send(absolutize(data["assignments"][cid]))
            if what == "discussion_topics":
                if qs.get("only_announcements"):
                    return self.send(absolutize(data["announcements"][cid]))
                return self.send([dict(a, is_announcement=True) for a in absolutize(data["announcements"][cid])])
            return self.send({}, 404)
    return H


def run(cmd, env):
    res = subprocess.run([sys.executable] + cmd, cwd=ROOT, env=env, capture_output=True, text=True)
    if res.returncode != 0:
        print(res.stdout, res.stderr)
        raise SystemExit(f"FAILED: {' '.join(cmd)}")
    return res.stdout


def main():
    keep = sys.argv[sys.argv.index("--keep") + 1] if "--keep" in sys.argv else None
    tmp = keep or tempfile.mkdtemp(prefix="sloan-brain-test-")
    if keep:
        shutil.rmtree(tmp, ignore_errors=True)
        os.makedirs(tmp)
    files = fixtures.build(os.path.join(tmp, "_fixtures"))
    data = canvas_data(files)
    server = ThreadingHTTPServer(("127.0.0.1", 0), make_handler(data, files))
    threading.Thread(target=server.serve_forever, daemon=True).start()
    host = f"http://127.0.0.1:{server.server_address[1]}"

    cfg = os.path.join(tmp, "config.json")
    with open(cfg, "w") as f:
        json.dump({"canvas_host": host, "canvas_token": "test-token"}, f)
    env = dict(os.environ, SLOAN_BRAIN_ROOT=tmp)
    checks = []

    def check(name, cond):
        checks.append((name, bool(cond)))

    out = run(["brain/canvas_harvest.py", "--config", cfg, "--list"], env)
    check("lists active and completed courses", "15.010" in out and "15.761" in out and "3 courses" in out)

    out = run(["brain/canvas_harvest.py", "--config", cfg], env)
    manifest = [json.loads(line) for line in open(os.path.join(tmp, "raw", "manifest.jsonl"))]
    keys = {m["key"] for m in manifest}
    check("downloads listed files across pages", {"file:1001", "file:1002", "file:3001", "file:3002"} <= keys)
    check("falls back to modules when Files tab is hidden", "file:2001" in keys)
    check("saves syllabus, pages, assignments, announcements",
          {"syllabus:101", "page:101:session-4-prep", "assignment:501", "announcement:9001"} <= keys)
    check("records module context", any(m.get("module") == "Week 4: Pricing" for m in manifest))
    failed = list(csv.DictReader(open(os.path.join(tmp, "raw", "failed.csv"), encoding="utf-8-sig")))
    reasons = {r["title"]: r for r in failed}
    check("reports locked file", reasons.get("Peer review rubric.pdf", {}).get("status") == "failed")
    check("lists external case link for manual download",
          reasons.get("HBS case: Pricing a subscription", {}).get("status") == "manual")
    check("skips video", reasons.get("Session 4 recording.mp4", {}).get("status") == "skipped")

    out = run(["brain/canvas_harvest.py", "--config", cfg], env)
    check("second run skips unchanged files", "5 unchanged" in out)

    inbox = os.path.join(tmp, "inbox")
    for sub in ("transcripts", "newsletters", "canvas/15.761"):
        os.makedirs(os.path.join(inbox, sub), exist_ok=True)
    with open(os.path.join(inbox, "transcripts", "2026-10-02 Coffee chat with a fintech PM.txt"), "w") as f:
        f.write(fixtures.TRANSCRIPT)
    with open(os.path.join(inbox, "newsletters", "sloan-weekly.eml"), "w") as f:
        f.write(fixtures.NEWSLETTER)
    shutil.copy(files["scanned_pdf"], os.path.join(inbox, "canvas", "15.761", "Scanned handout.pdf"))

    out = run(["brain/convert.py"], env)
    corpus = os.path.join(tmp, "corpus")
    produced = {os.path.relpath(os.path.join(d, n), corpus) for d, _, ns in os.walk(corpus) for n in ns}
    check("pptx becomes slides", "15.010/slides/session-4-pricing-and-elasticity.md" in produced)
    check("landscape PDF classified as slides", "15.311/slides/session-7-feedback-slides.md" in produced)
    check("portrait PDF classified as reading", "15.010/readings/note-on-price-discrimination.md" in produced)
    check("docx and xlsx convert", "15.761/documents/littles-law-class-notes.md" in produced
          and "15.761/spreadsheets/newsvendor-model.md" in produced)
    check("transcript dated from filename",
          "_transcripts/2026-10-02-coffee-chat-with-a-fintech-pm.md" in produced)
    check("newsletter titled from email subject", any(p.startswith("_newsletters/2026-09-28-sloan-weekly") for p in produced))
    slides = open(os.path.join(corpus, "15.010/slides/session-4-pricing-and-elasticity.md")).read()
    check("slide markers and speaker notes kept", "## Slide 3 — The markup rule" in slides and "Speaker notes" in slides)
    reading = open(os.path.join(corpus, "15.010/readings/note-on-price-discrimination.md")).read()
    check("repeated PDF footer removed", "Not for distribution" not in reading)
    check("front matter has course and module", 'course: "15.010"' in slides and 'module: "Week 4: Pricing"' in slides)
    sheet = open(os.path.join(corpus, "15.761/spreadsheets/newsvendor-model.md")).read()
    check("hidden add-in sheets skipped", "rsklib" not in sheet and "_x0001_" not in sheet)
    conv_failed = open(os.path.join(tmp, "raw", "convert-failed.csv"), encoding="utf-8-sig").read()
    check("scanned PDF reported for OCR", "needs OCR" in conv_failed)

    out = run(["brain/convert.py"], env)
    check("second convert is incremental", "Converted 0" in out)

    out = run(["brain/sync.py", "--stats"], env)
    index = [json.loads(line) for line in open(os.path.join(tmp, "build", "index.jsonl"))]
    locators = {c["locator"] for d in index for c in d["chunks"]}
    check("passages carry slide and page locators",
          any(loc.startswith("slide") for loc in locators) and any(loc.startswith(("p.", "pp.")) for loc in locators))

    server.shutdown()
    width = max(len(n) for n, _ in checks)
    for name, ok in checks:
        print(f"  {'PASS' if ok else 'FAIL'}  {name.ljust(width)}")
    passed = sum(ok for _, ok in checks)
    print(f"\n{passed}/{len(checks)} checks passed" + (f" (scratch kept in {tmp})" if keep else ""))
    if not keep:
        shutil.rmtree(tmp, ignore_errors=True)
    sys.exit(0 if passed == len(checks) else 1)


if __name__ == "__main__":
    main()
