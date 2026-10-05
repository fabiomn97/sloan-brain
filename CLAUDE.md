# Sloan Brain — instructions for Claude Code

This repo is Fabio's private memory of the MIT Sloan MBA (Class of 2028).
`corpus/` holds one Markdown file per document: Canvas slides, readings, cases,
syllabi, assignments, announcements, plus transcripts, newsletters and notes.

## Answering questions from the corpus

When asked what Sloan taught about something:

1. Search `corpus/` (grep for the concept, its synonyms, and framework names).
   Front matter gives `course`, `term`, `type`, `module`; `## Slide N` and
   `## Page N` headings give the location.
2. Open with the takeaway Fabio can act on, then the supporting ideas.
3. Cite every claim: course, document title, slide or page, e.g.
   *(15.010, Session 4 — Pricing and Elasticity, slide 3)*.
4. Keep what the materials say separate from general knowledge. If the corpus
   doesn't cover it, say so, then offer general knowledge under its own heading.
5. Never invent sources, numbers, quotes or frameworks.

## Adding material

- Meeting notes from Granola, emails from Gmail, or files Fabio sends: save them
  in `inbox/transcripts/`, `inbox/newsletters/` or `inbox/notes/` as
  `YYYY-MM-DD Title.md` (or the original format), then run `python brain/convert.py`.
- Course files the harvester missed go in `inbox/canvas/<course number>/`.
- After converting: `git add corpus && git commit && git push`. The GitHub Action
  syncs the search database and redeploys brain.fabio.cool.

## Rules

- The repo is private and must stay private: it contains copyrighted course
  materials and private conversations. Never publish `corpus/` anywhere.
- Never commit `config.json` (Canvas token), `raw/`, or `inbox/` contents.
- Run `python tests/test_pipeline.py` after changing anything in `brain/`.
- The app (`app/`) has no build step: plain JS/CSS in `app/public/`, one Worker in
  `app/src/worker.js`. Preview with `cd app && npm run dev` (see SETUP.md).
