# Setup

From zero to a working **brain.fabio.cool**. Steps 1–2 are urgent (Canvas
access ends); steps 3–6 can wait for a free afternoon. About 1–2 hours total.

Commands are for **PowerShell** on Windows. On a Mac, use Terminal and type
`python3` wherever it says `python`.

---

## Step 0 — Tools and the repo

You need Python 3.10+ (you have it from the Canvas digest), [Node.js LTS](https://nodejs.org)
and [Git](https://git-scm.com/downloads). Then:

```
cd $HOME
git clone https://github.com/fabiomn97/sloan-brain.git
cd sloan-brain
python -m pip install -r requirements.txt
```

---

## Step 1 — Harvest Canvas (do this now)

The harvester reuses the Canvas token from your digest bot. Either point it at
that config file:

```
python brain\canvas_harvest.py --config $HOME\canvas-digest\config.json --list
```

(that's where the digest's own setup put it), or copy
`config.example.json` to `config.json` here and paste the token into it.

`--list` shows every course Canvas can see, current and past. If one is missing,
open it once in Canvas and try again. Then harvest everything:

```
python brain\canvas_harvest.py --config $HOME\canvas-digest\config.json
```

It saves into `raw\` and takes a few minutes per course. It's safe to stop and
re-run; files it already has are skipped.

**Then open `raw\failed.csv`** in Excel. It lists what it couldn't get, and why:

| status | meaning | what to do |
|---|---|---|
| `failed` | locked, hidden or restricted by the instructor | Open the link, download it, and save it in `inbox\canvas\<course>\` |
| `manual` | an external link (HBS case, article, video, tool) | If it's a reading you want kept, save it as PDF into `inbox\canvas\<course>\` |
| `skipped` | video/audio, or larger than `max_file_mb` | Usually nothing |

Anything you'd rather send me instead, send it, and I'll put it in the inbox.

---

## Step 2 — Convert and commit

```
python brain\convert.py
```

This turns everything in `raw\` and `inbox\` into Markdown in `corpus\`. Files it
can't read land in `raw\convert-failed.csv`. Usually these are scanned PDFs: open
them in Acrobat or Preview, export with text recognition (OCR), and drop the new
file in the inbox.

```
git add corpus
git commit -m "Harvest Fall 2026"
git push
```

**Back up `raw\` and `inbox\`** (the original PDFs and decks) to Google Drive or
an external disk. They are not in git, and Canvas won't have them forever.

At this point the brain already works without a website: open Claude Code in
this folder and ask. `CLAUDE.md` tells it how to answer from `corpus\`.

---

## Step 3 — Cloudflare account and the fabio.cool DNS

1. Sign up at [dash.cloudflare.com](https://dash.cloudflare.com/sign-up) with your
   personal email (not MIT). Choose the **Free** plan whenever asked.
2. **Add a domain** → `fabio.cool` → Free plan. Cloudflare copies your existing
   DNS records.
3. Check the imported records against what GitHub Pages needs (four `A` records
   for `fabio.cool` pointing at `185.199.108–111.153`, and the `www` CNAME to
   `fabiomn97.github.io`). Set those records to **DNS only** (grey cloud) so
   GitHub keeps issuing the certificate for fabio.cool.
4. Cloudflare shows two nameservers. At your domain registrar (wherever you bought
   fabio.cool), replace the nameservers with those two. It takes from minutes to
   a few hours; Cloudflare emails you when it's active. fabio.cool keeps working
   throughout.

---

## Step 4 — Create the database and deploy

```
cd app
npm install
npx wrangler login
npx wrangler d1 create sloan-brain
```

`wrangler login` opens a browser to approve. `d1 create` prints a
`database_id`: paste it into `app\wrangler.toml`, replacing
`REPLACE_WITH_ID_FROM_wrangler_d1_create`. Then:

```
cd ..
python brain\sync.py --remote
cd app
npx wrangler deploy
```

`sync.py` uploads the corpus (the first time takes a few minutes).
`wrangler deploy` publishes the app at **brain.fabio.cool** and creates the DNS
record itself.

Opening it now shows *"Locked: Cloudflare Access is not configured"*. That's on
purpose: the app refuses to serve anything until the login is set up.

---

## Step 5 — Lock it with a one-time email code

1. In the Cloudflare dashboard open **Zero Trust**. The first time, pick a team
   name (e.g. `fabio`) and the **Free** plan. It may ask for a card; the free
   plan isn't charged.
2. **Access → Applications → Add an application → Self-hosted.**
   - Application domain: `brain.fabio.cool`
   - Session duration: 1 month (so you rarely log in)
3. Add a policy: **Allow**, rule **Emails**, value: your personal email.
4. Login method: **One-time PIN** (it's on by default).
5. Save. On the application's overview, copy the **Application Audience (AUD) Tag**.
   Your team domain is `<team-name>.cloudflareaccess.com`.
6. Paste both into `app\wrangler.toml`:
   ```
   ACCESS_TEAM_DOMAIN = "fabio.cloudflareaccess.com"
   ACCESS_AUD = "the long AUD tag"
   ```
7. `npx wrangler deploy` again.

Open brain.fabio.cool: it asks for your email, sends a code, and you're in.
Both locks have to pass: Cloudflare checks you at the edge, and the app checks
Cloudflare's signed token on every request, so a mistake in one doesn't expose
the content.

Commit `app\wrangler.toml` and push.

---

## Step 6 — Automatic updates on push

From now on, pushing `corpus\` should update the site by itself.

1. Cloudflare dashboard → **My Profile → API Tokens → Create Token** → template
   **Edit Cloudflare Workers**. Add two permissions: **Account · D1 · Edit**, and
   **Zone · DNS · Edit** for fabio.cool. Create, then copy the token.
2. Your **Account ID** is on the right side of any domain's Overview page.
3. GitHub → `sloan-brain` → **Settings → Secrets and variables → Actions → New
   repository secret**: add `CLOUDFLARE_API_TOKEN` and `CLOUDFLARE_ACCOUNT_ID`.

Every push to `main` now runs the tests, syncs the corpus, and redeploys
(**Actions** tab to watch). **Run workflow → rebuild** reloads the whole
database if it ever gets out of step.

---

## Running it locally

```
cd app
copy .dev.vars.example .dev.vars
cd ..
python brain\sync.py --local
cd app
npm run dev
```

Open http://localhost:8787. `.dev.vars` skips the login and uses a canned
answer (`MOCK_AI=true`), so nothing is billed and no account is needed.

---

## If something breaks

| Symptom | Fix |
|---|---|
| Harvester: `Canvas rejected the access token` | The token expired. Make a new one in Canvas (Account → Settings → New access token) and update the config. |
| A course is missing from `--list` | Open it once in Canvas, or it may already be closed: ask the instructor or the Registrar for the files. |
| "Today's free answers are used up" | Daily free AI limit reached. Search and *Ask Claude* still work; answers come back at 00:00 UTC. |
| Answers miss something you know is there | Try **Search** mode with the exact term. If it isn't found, check `corpus/` for the file; it may not have converted (`raw\convert-failed.csv`). |
| A Workers AI model is retired | Change `ANSWER_MODEL` / `EXPAND_MODEL` in `app\wrangler.toml` to a current model from Cloudflare's model catalog and redeploy. |
| Deploy fails in GitHub Actions | Open the failed run in the **Actions** tab. Usually an expired API token (step 6). |
