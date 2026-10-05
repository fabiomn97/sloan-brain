// Sloan Brain: search and answer over everything I learned at MIT Sloan.
//
//   GET  /api/stats           library overview (courses, counts)
//   GET  /api/search?q=       ranked passages, no AI (free, unlimited)
//   POST /api/ask             streamed answer with numbered citations (SSE)
//   GET  /api/doc/:id         one document, for the reader
//
// Everything else is the static app in public/. Every request, assets included,
// must carry a valid Cloudflare Access token: the site is private.

const ANSWER_MODEL = "@cf/meta/llama-3.3-70b-instruct-fp8-fast";
const EXPAND_MODEL = "@cf/meta/llama-3.1-8b-instruct-fast";
const MAX_SOURCES = 8;
const PER_DOC = 2;
const CONTEXT_WORDS = 3200;

const STOP = new Set(["a an and are as at be but by can could did do does for from had has have how i if in " +
  "into is it its me my of on or our should so than that the their them then there these they this to " +
  "was we were what when where which who why will with would you your about tell explain learned learn " +
  "sloan mit class course remember any some get make good best way need want know think use "+
  "instead also just like really thing things"].join("").split(" "));

export default {
  async fetch(request, env, ctx) {
    const auth = await authorize(request, env);
    if (!auth.ok) return new Response(auth.message, { status: 403, headers: { "content-type": "text/plain" } });

    const url = new URL(request.url);
    try {
      if (url.pathname === "/api/stats") return json(await stats(env));
      if (url.pathname === "/api/search") return json(await searchRoute(url, env));
      if (url.pathname === "/api/ask" && request.method === "POST") return await ask(request, env, ctx);
      if (url.pathname.startsWith("/api/doc/")) return await docRoute(url, env);
      if (url.pathname.startsWith("/api/")) return json({ error: "Not found" }, 404);
    } catch (err) {
      return json({ error: String(err && err.message || err) }, 500);
    }
    const res = await env.ASSETS.fetch(request);
    const headers = new Headers(res.headers);
    headers.set("x-robots-tag", "noindex, nofollow");
    headers.set("referrer-policy", "no-referrer");
    return new Response(res.body, { status: res.status, headers });
  },
};

// ---------------------------------------------------------------------------
// Access: verify the Cloudflare Access JWT (defense in depth behind the edge).
// ---------------------------------------------------------------------------

let jwks = { at: 0, keys: [] };

async function authorize(request, env) {
  if (env.ALLOW_UNAUTHENTICATED === "true") return { ok: true };
  if (!env.ACCESS_TEAM_DOMAIN || !env.ACCESS_AUD) {
    return { ok: false, message: "Locked: Cloudflare Access is not configured (see SETUP.md, step 5)." };
  }
  const cookie = (request.headers.get("cookie") || "").match(/(?:^|;\s*)CF_Authorization=([^;]+)/);
  const token = request.headers.get("cf-access-jwt-assertion") || (cookie && cookie[1]);
  if (!token) return { ok: false, message: "Locked: sign in through Cloudflare Access." };
  try {
    const [h, p, s] = token.split(".");
    const header = JSON.parse(b64text(h));
    const payload = JSON.parse(b64text(p));
    const now = Date.now() / 1000;
    const aud = Array.isArray(payload.aud) ? payload.aud : [payload.aud];
    if (!aud.includes(env.ACCESS_AUD)) throw new Error("audience");
    if (payload.iss !== `https://${env.ACCESS_TEAM_DOMAIN}`) throw new Error("issuer");
    if (!(payload.exp > now)) throw new Error("expired");
    const key = await accessKey(env.ACCESS_TEAM_DOMAIN, header.kid);
    const ok = await crypto.subtle.verify("RSASSA-PKCS1-v1_5", key, b64bytes(s),
      new TextEncoder().encode(`${h}.${p}`));
    return ok ? { ok: true, email: payload.email } : { ok: false, message: "Locked: bad signature." };
  } catch (e) {
    return { ok: false, message: `Locked: invalid Access token (${e.message}).` };
  }
}

async function accessKey(team, kid) {
  if (Date.now() - jwks.at > 3600_000 || !jwks.keys.some(k => k.kid === kid)) {
    const res = await fetch(`https://${team}/cdn-cgi/access/certs`);
    const body = await res.json();
    jwks = { at: Date.now(), keys: await Promise.all(body.keys.map(async jwk => ({
      kid: jwk.kid,
      key: await crypto.subtle.importKey("jwk", jwk, { name: "RSASSA-PKCS1-v1_5", hash: "SHA-256" }, false, ["verify"]),
    }))) };
  }
  const found = jwks.keys.find(k => k.kid === kid);
  if (!found) throw new Error("unknown key");
  return found.key;
}

function b64bytes(s) {
  const bin = atob(s.replace(/-/g, "+").replace(/_/g, "/").padEnd(Math.ceil(s.length / 4) * 4, "="));
  return Uint8Array.from(bin, c => c.charCodeAt(0));
}
function b64text(s) { return new TextDecoder().decode(b64bytes(s)); }

// ---------------------------------------------------------------------------
// Search
// ---------------------------------------------------------------------------

function terms(text) {
  const words = (text.toLowerCase().match(/[\p{L}\p{N}][\p{L}\p{N}'.&-]*/gu) || [])
    .map(w => w.replace(/^[.'-]+|[.'-]+$/g, ""))
    .filter(w => w && (w.length > 1 || /\d/.test(w)) && !STOP.has(w));
  return [...new Set(words)];
}

function ftsQuery(keywords, phrases = []) {
  const quote = t => `"${t.replace(/"/g, '""')}"`;
  const parts = [...phrases.filter(p => p.split(/\s+/).length > 1).map(quote), ...keywords.map(quote)];
  return [...new Set(parts)].slice(0, 32).join(" OR ");
}

const HIT_SQL = `
  SELECT c.rowid AS rid, c.doc_id, c.seq, c.locator, c.heading, c.text,
         d.title, d.course, d.course_name, d.term, d.type, d.module, d.date, d.url,
         bm25(chunks_fts, 4.0, 2.0, 1.0) AS score,
         snippet(chunks_fts, 2, '', '', ' … ', 32) AS snip
  FROM chunks_fts
  JOIN chunks c ON c.rowid = chunks_fts.rowid
  JOIN docs d ON d.id = c.doc_id
  WHERE chunks_fts MATCH ?1 AND (?2 = '' OR d.course = ?2) AND (?3 = '' OR d.type = ?3)
  ORDER BY score LIMIT ?4`;

async function search(env, match, course = "", type = "", limit = 40) {
  if (!match) return [];
  const { results } = await env.DB.prepare(HIT_SQL).bind(match, course, type, limit).all();
  return results;
}

// Keep the best passages, at most perDoc per document, and drop the long tail
// whose relevance is a small fraction of the best hit (bm25 scores are negative).
function diversify(hits, max, perDoc, floor = 0.18) {
  const best = hits.length ? -hits[0].score : 0;
  const seen = new Map(), out = [];
  for (const h of hits) {
    if (best > 0 && -h.score < best * floor) break;
    const n = seen.get(h.doc_id) || 0;
    if (n >= perDoc) continue;
    seen.set(h.doc_id, n + 1);
    out.push(h);
    if (out.length >= max) break;
  }
  return out;
}

function publicHit(h, i) {
  return {
    n: i + 1, doc_id: h.doc_id, seq: h.seq, locator: h.locator, heading: h.heading,
    title: h.title, course: h.course, course_name: h.course_name, term: h.term,
    type: h.type, module: h.module, date: h.date, url: h.url, snippet: cleanSnippet(h.snip), text: h.text,
  };
}

function cleanSnippet(s) {
  return String(s || "")
    .replace(/\[(?:Slide|Page|Sheet) [^\]]*\]/g, " ")      // passage labels
    .replace(/\|\s*-{3,}\s*(?=\|)/g, "")                    // table rules
    .replace(/(^|\n)\s*(?:[-*•]|#{1,6})\s+/g, "$1")          // bullets and headings
    .replace(/\*\*/g, "")
    .replace(/\s+/g, " ")
    .trim();
}

async function searchRoute(url, env) {
  const q = (url.searchParams.get("q") || "").slice(0, 500);
  const course = url.searchParams.get("course") || "";
  const type = url.searchParams.get("type") || "";
  const hits = await search(env, ftsQuery(terms(q)), course, type, 60);
  return { query: q, results: diversify(hits, 25, 3).map(publicHit) };
}

// ---------------------------------------------------------------------------
// Ask: expand the question, retrieve, stream a cited answer.
// ---------------------------------------------------------------------------

async function expand(env, question) {
  if (env.MOCK_AI) return { keywords: [], phrases: [] };
  try {
    const res = await env.AI.run(env.EXPAND_MODEL || EXPAND_MODEL, {
      messages: [
        { role: "system", content:
          "You turn a question into search terms for an archive of MBA course materials " +
          "(slides, readings, cases, syllabi, meeting notes). Reply with JSON only: " +
          '{"keywords": [...], "phrases": [...]}. keywords: 6-12 single words that would appear in ' +
          "the materials, including synonyms and the technical term for the idea. phrases: 2-5 " +
          "multi-word terms, framework or model names (e.g. \"price elasticity\", \"BATNA\", \"net present value\")." },
        { role: "user", content: question },
      ],
      max_tokens: 160, temperature: 0,
    });
    const text = typeof res.response === "string" ? res.response : JSON.stringify(res.response || "");
    const parsed = JSON.parse(text.slice(text.indexOf("{"), text.lastIndexOf("}") + 1));
    return {
      keywords: (parsed.keywords || []).map(String).flatMap(terms).slice(0, 14),
      phrases: (parsed.phrases || []).map(p => String(p).toLowerCase().replace(/[^\p{L}\p{N}\s'&-]/gu, " ").trim()).filter(Boolean).slice(0, 6),
    };
  } catch {
    return { keywords: [], phrases: [] };
  }
}

function sourceBlock(h, i) {
  const label = [h.course, h.course_name].filter(Boolean).join(" ");
  const where = [h.locator, h.module, h.term].filter(Boolean).join(" · ");
  return `[${i + 1}] ${label ? label + " — " : ""}${h.title} (${h.type}${where ? "; " + where : ""})\n${h.text}`;
}

function systemPrompt(env) {
  const owner = env.OWNER_NAME || "Fabio";
  return `You are ${owner}'s Sloan Brain: the memory of what ${owner} learned in the MIT Sloan MBA, built from ${owner}'s own course slides, readings, cases, syllabi, notes and conversations. ${owner} asks you when facing a real situation and wants to know what Sloan taught that applies.

Rules:
1. Open with the takeaway ${owner} can act on, in one or two sentences.
2. Then the supporting ideas as short bullets or paragraphs. Cite every claim drawn from a source with its number in square brackets, like [2] or [1][4]. Name the course and the framework or author when the source gives them ("In 15.010, ...").
3. Use only the numbered sources for anything you attribute to Sloan. Never invent sources, numbers, quotes, professors or frameworks.
4. If the sources don't answer the question, say so in one sentence ("Your Sloan materials don't cover this directly."). You may then add general knowledge under a final heading "**Beyond your materials**", with no citations.
5. Under 250 words unless asked for more. Markdown: short paragraphs, bullets, bold sparingly. No preamble, no closing summary.`;
}

async function ask(request, env, ctx) {
  const body = await request.json().catch(() => ({}));
  const question = String(body.q || "").trim().slice(0, 1000);
  const course = String(body.course || ""), type = String(body.type || "");
  const history = Array.isArray(body.history) ? body.history.slice(-2) : [];
  if (!question) return json({ error: "Empty question" }, 400);

  // Short follow-ups ("and for services?") borrow the previous question's words.
  const prev = history.length ? String(history[history.length - 1].q || "") : "";
  const base = terms(question).length < 3 && prev ? `${prev} ${question}` : question;
  const ex = await expand(env, base);
  const keywords = [...new Set([...terms(base), ...ex.keywords])];
  let hits = await search(env, ftsQuery(keywords, ex.phrases), course, type, 60);
  hits = diversify(hits, MAX_SOURCES, PER_DOC);

  let words = 0;
  hits = hits.filter(h => (words += h.text.split(/\s+/).length) <= CONTEXT_WORDS || h === hits[0]);
  const sources = hits.map(publicHit);

  const { readable, writable } = new TransformStream();
  const writer = writable.getWriter();
  const enc = new TextEncoder();
  const send = (event, data) => writer.write(enc.encode(`event: ${event}\ndata: ${JSON.stringify(data)}\n\n`));

  ctx.waitUntil((async () => {
    try {
      await send("sources", { sources, keywords: [...ex.phrases, ...keywords].slice(0, 16) });
      if (!hits.length) {
        await send("empty", {});
        return;
      }
      const messages = [{ role: "system", content: systemPrompt(env) }];
      for (const turn of history) {
        if (turn.q && turn.a) {
          messages.push({ role: "user", content: String(turn.q).slice(0, 1000) });
          messages.push({ role: "assistant", content: String(turn.a).slice(0, 2000) });
        }
      }
      messages.push({ role: "user", content:
        `Question: ${question}\n\nSources:\n\n${hits.map(sourceBlock).join("\n\n---\n\n")}` });

      if (env.MOCK_AI === "true") return await mockAnswer(writer, enc, hits);
      if (env.MOCK_AI === "quota") throw new Error("4006: you have used up your daily free allocation of 10,000 neurons");
      const stream = await env.AI.run(env.ANSWER_MODEL || ANSWER_MODEL,
        { messages, stream: true, max_tokens: 900, temperature: 0.2 });
      // Relay the model's SSE bytes untouched; the browser parses them.
      const reader = stream.getReader();
      for (;;) {
        const { done, value } = await reader.read();
        if (done) break;
        await writer.write(value);
      }
    } catch (err) {
      const msg = String(err && err.message || err);
      const quota = /4006|daily free allocation|neurons|exceeded|quota/i.test(msg);
      await send("error", { code: quota ? "quota" : "ai", message: msg });
    } finally {
      await send("done", {}).catch(() => {});
      await writer.close().catch(() => {});
    }
  })());

  return new Response(readable, {
    headers: { "content-type": "text/event-stream; charset=utf-8", "cache-control": "no-store" },
  });
}

// Local development only (MOCK_AI=true in .dev.vars): a canned answer that
// exercises streaming, citations and the "Beyond" box without Workers AI.
async function mockAnswer(writer, enc, hits) {
  const n = Math.min(hits.length, 3);
  const cite = i => `[${Math.min(i, n)}]`;
  const text = `**Raise prices when your customers are not very price-sensitive; cut only when demand is elastic and you have the cost position to win a price war.** ${cite(1)}\n\n` +
    `- **Check elasticity first.** If demand is inelastic, a price increase raises revenue; if it is elastic, a cut does. Estimate it with small experiments, not intuition. ${cite(1)}\n` +
    `- **Price to value, not to cost.** Start from the customer's next best alternative and charge for the differentiation you add on top. Marginal cost only sets the floor. ${cite(1)}\n` +
    `- **Segment before you discount.** Versions and menus let price-sensitive buyers self-select, so you avoid cutting price for everyone. ${cite(2)}${cite(1)}\n\n` +
    `**Beyond your materials**\n\nThis is a mock answer for local development; the live app writes it with Workers AI.`;
  for (const piece of text.match(/[\s\S]{1,10}/g)) {
    await writer.write(enc.encode(`data: ${JSON.stringify({ response: piece })}\n\n`));
    await new Promise(r => setTimeout(r, 8));
  }
  await writer.write(enc.encode("data: [DONE]\n\n"));
}

// ---------------------------------------------------------------------------
// Library and reader
// ---------------------------------------------------------------------------

async function stats(env) {
  const [totals, courses, types] = await env.DB.batch([
    env.DB.prepare("SELECT COUNT(*) AS docs, COALESCE(SUM(n_chunks),0) AS chunks, COALESCE(SUM(words),0) AS words FROM docs"),
    env.DB.prepare(`SELECT course, MAX(course_name) AS course_name, MAX(term) AS term, COUNT(*) AS n
                    FROM docs WHERE course <> '' GROUP BY course ORDER BY MAX(term) DESC, course`),
    env.DB.prepare("SELECT type, COUNT(*) AS n FROM docs GROUP BY type ORDER BY n DESC"),
  ]);
  return { ...totals.results[0], courses: courses.results, types: types.results,
           owner: env.OWNER_NAME || "Fabio" };
}

async function docRoute(url, env) {
  const id = url.pathname.split("/").pop();
  const doc = await env.DB.prepare("SELECT * FROM docs WHERE id = ?").bind(id).first();
  if (!doc) return json({ error: "Not found" }, 404);
  const { results } = await env.DB.prepare(
    "SELECT seq, locator, heading, text FROM chunks WHERE doc_id = ? ORDER BY seq").bind(id).all();
  return json({ ...doc, chunks: results });
}

function json(data, status = 200) {
  return new Response(JSON.stringify(data), {
    status, headers: { "content-type": "application/json; charset=utf-8", "cache-control": "no-store" },
  });
}
