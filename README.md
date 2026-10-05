# Sloan Brain

A private memory of everything I learned at MIT Sloan: every slide, reading,
case, syllabus and assignment from Canvas, plus coffee chats, newsletters and
notes. When I face a situation years from now, I ask, and it answers from my own
materials, citing the course and the exact slide or page.

Lives at **brain.fabio.cool**, behind a login that emails a one-time code to my
personal address. No MIT account needed, so it keeps working after graduation.
Costs **$0 a month**.

## How it works

```
 Canvas ──► brain/canvas_harvest.py ──► raw/          originals, local only
 inbox/ (chats, newsletters, notes) ─┐
                                     ▼
              brain/convert.py ──► corpus/*.md        Markdown + front matter, in git
                                     │
                git push ──► GitHub Actions ──► brain/sync.py ──► Cloudflare D1 (full-text index)
                                     │
                                     └──► wrangler deploy ──► Worker at brain.fabio.cool
                                                              (Cloudflare Access login)
```

**Asking a question:** a small model expands it into search terms (synonyms,
framework names), full-text search finds the best passages, and Llama 3.3 70B
writes a short answer citing them as [1], [2]. Click a citation to see the
passage, click a source to read the whole document with the passage highlighted.
**Ask Claude** copies the question and sources into claude.ai when I want a
deeper answer.

## What it costs, and the limits

Everything runs on Cloudflare's free plan.

| Piece | Free allowance | What that means |
|---|---|---|
| Answers (Workers AI) | 10,000 neurons/day | About **30 answered questions a day**. Search and *Ask Claude* keep working after that, and it resets at 00:00 UTC. |
| Search database (D1) | 500 MB per database, 5M rows read/day | Enough for the text of a whole MBA. `sync.py --stats` shows the real size. |
| App (Workers) | 100,000 requests/day | Far more than one person uses. |
| Login (Access) | 50 users | Only me. |
| GitHub Actions (private repo) | 2,000 min/month | About 2 minutes per push. |

The corpus in git is the source of truth. The database can always be rebuilt
from it (`python brain/sync.py --remote --rebuild`), so nothing is lost if
Cloudflare changes.

## Repository

```
brain/canvas_harvest.py   download everything from Canvas (standard library only)
brain/convert.py          PDF, PPTX, DOCX, XLSX, HTML, EML, VTT -> Markdown
brain/sync.py             chunk corpus/ and upload changes to D1
brain/common.py           paths and the front-matter format
app/                      the Worker (src/worker.js), the web app (public/), the schema
corpus/                   the brain itself: one Markdown file per document
inbox/                    drop folder for anything Canvas didn't have
tests/                    end-to-end test with a fake Canvas
```

## Commands

| Command | What it does |
|---|---|
| `python brain/canvas_harvest.py --list` | Show every course Canvas can see |
| `python brain/canvas_harvest.py` | Download everything new or changed |
| `python brain/convert.py` | Turn `raw/` and `inbox/` into `corpus/` |
| `python brain/sync.py --stats` | Count what would be indexed |
| `python brain/sync.py --remote` | Push changes to the live app (CI does this on push) |
| `cd app && npm run dev` | Run the app locally at http://localhost:8787 |
| `python tests/test_pipeline.py` | Run the end-to-end test |

Setup, from zero to a working site: **[SETUP.md](SETUP.md)**.

## The semester routine

1. `python brain/canvas_harvest.py` after finals, before Canvas closes old courses.
2. Download what's in `raw/failed.csv` by hand into `inbox/canvas/<course>/`.
3. Drop the semester's chats and newsletters into `inbox/`.
4. `python brain/convert.py`, then commit and push `corpus/`. The site updates itself.
5. Back up `raw/` and `inbox/` to a personal drive. They hold the original files.
