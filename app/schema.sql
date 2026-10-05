-- Sloan Brain search database (Cloudflare D1 = SQLite).
-- The corpus/ folder in git is the source of truth; this database is always
-- rebuildable from it with `python brain/sync.py --remote --rebuild`.

CREATE TABLE IF NOT EXISTS docs (
  id           TEXT PRIMARY KEY,      -- stable hash of the corpus path
  path         TEXT NOT NULL,         -- corpus/15-010/slides/session-4.md
  title        TEXT NOT NULL,
  course       TEXT,                  -- 15.010
  course_name  TEXT,
  term         TEXT,                  -- Fall 2026
  type         TEXT,                  -- slides, reading, case, transcript, ...
  module       TEXT,                  -- Canvas module, e.g. "Week 3: Pricing"
  date         TEXT,
  source       TEXT,                  -- canvas, upload, ...
  url          TEXT,
  locator_kind TEXT,                  -- page, slide, sheet, section
  hash         TEXT NOT NULL,         -- content hash, for incremental sync
  words        INTEGER,
  n_chunks     INTEGER
);
CREATE INDEX IF NOT EXISTS docs_course ON docs(course);
CREATE INDEX IF NOT EXISTS docs_type ON docs(type);

CREATE TABLE IF NOT EXISTS chunks (
  rowid    INTEGER PRIMARY KEY,
  doc_id   TEXT NOT NULL,
  seq      INTEGER NOT NULL,
  locator  TEXT,                      -- "slide 7", "pp. 3–4"
  heading  TEXT,
  title    TEXT,                      -- doc title + course, searchable
  text     TEXT NOT NULL
);
CREATE INDEX IF NOT EXISTS chunks_doc ON chunks(doc_id, seq);

-- Full-text index over chunks. Porter stemming: "pricing" matches "price".
CREATE VIRTUAL TABLE IF NOT EXISTS chunks_fts USING fts5(
  title, heading, text,
  content='chunks', content_rowid='rowid',
  tokenize='porter unicode61 remove_diacritics 2'
);

CREATE TRIGGER IF NOT EXISTS chunks_ai AFTER INSERT ON chunks BEGIN
  INSERT INTO chunks_fts(rowid, title, heading, text)
  VALUES (new.rowid, new.title, new.heading, new.text);
END;
CREATE TRIGGER IF NOT EXISTS chunks_ad AFTER DELETE ON chunks BEGIN
  INSERT INTO chunks_fts(chunks_fts, rowid, title, heading, text)
  VALUES ('delete', old.rowid, old.title, old.heading, old.text);
END;
