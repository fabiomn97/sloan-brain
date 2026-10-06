// Sloan Brain front end. No framework, no build step.
(() => {
  "use strict";

  const $ = (sel, el = document) => el.querySelector(sel);
  const TYPE_ONE = {
    slides: "slides", reading: "reading", case: "case", syllabus: "syllabus", assignment: "assignment",
    page: "page", announcement: "announcement", discussion: "discussion", transcript: "conversation",
    newsletter: "newsletter", note: "note", document: "document", spreadsheet: "spreadsheet",
  };
  const OUTSIDE = {   // material that belongs to no course, filterable as "@type"
    transcript: ["Conversations", "Coffee chats and meetings"],
    newsletter: ["Newsletters", "Sloan newsletters"],
    note: ["Notes", "Your own notes"],
  };
  const SEASONS = { IAP: 1, Spring: 2, Summer: 3, Fall: 4 };

  const state = { mode: "ask", turns: [], stats: null, busy: false, docs: new Map(),
                  selected: new Set(), options: [] };
  const el = {
    q: $("#q"), form: $("#composer"), send: $("#send"),
    pickerBtn: $("#picker-btn"), pickerPop: $("#picker-pop"), pickerBody: $("#picker-body"),
    pickerLabel: $("#picker-label"), pickerCount: $("#picker-count"),
    thread: $("#thread"), tiles: $("#tiles"), library: $("#library"), libTotal: $("#lib-total"),
    navStat: $("#nav-stat"), newBtn: $("#new-btn"), reader: $("#reader"), toast: $("#toast"),
  };

  // ------------------------------------------------------------------ utils

  const esc = s => String(s ?? "").replace(/[&<>"']/g, c => ({ "&": "&amp;", "<": "&lt;", ">": "&gt;", '"': "&quot;", "'": "&#39;" }[c]));
  const plural = (n, one, many = one + "s") => `${n.toLocaleString()} ${n === 1 ? one : many}`;
  const marks = s => esc(s).replace(//g, "<mark>").replace(//g, "</mark>");

  function toast(msg) {
    el.toast.textContent = msg;
    el.toast.classList.add("show");
    clearTimeout(toast.t);
    toast.t = setTimeout(() => el.toast.classList.remove("show"), 3200);
  }

  async function copy(text) {
    try { await navigator.clipboard.writeText(text); return true; }
    catch {
      const ta = document.createElement("textarea");
      ta.value = text; ta.style.position = "fixed"; ta.style.opacity = "0";
      document.body.appendChild(ta); ta.select();
      const ok = document.execCommand("copy"); ta.remove(); return ok;
    }
  }

  // ------------------------------------------------------------------ markdown

  function inline(s, cites) {
    let h = esc(s).replace(//g, "<mark>").replace(//g, "</mark>");
    h = h.replace(/`([^`]+)`/g, "<code>$1</code>");
    h = h.replace(/\*\*([^*]+?)\*\*/g, "<strong>$1</strong>");
    h = h.replace(/(^|[\s(])\*([^*\s][^*]*?)\*(?=[\s).,;:!?]|$)/g, "$1<em>$2</em>");
    h = h.replace(/(https?:\/\/[^\s<)]+[^\s<).,;:!?])/g, '<a href="$1" target="_blank" rel="noopener noreferrer">$1</a>');
    if (cites) {
      h = h.replace(/\[(\d{1,2}(?:\s*[,;–-]\s*\d{1,2})*)\]/g, (m, list) => {
        const nums = [];
        for (const part of list.split(/\s*[,;]\s*/)) {
          const r = part.split(/\s*[–-]\s*/).map(Number);
          if (r.length === 2 && r[1] >= r[0] && r[1] - r[0] < 10) for (let i = r[0]; i <= r[1]; i++) nums.push(i);
          else nums.push(r[0]);
        }
        if (!nums.every(n => n >= 1 && n <= cites)) return m;
        return nums.map(n => `<button type="button" class="cite" data-n="${n}" aria-label="Source ${n}">${n}</button>`).join("");
      });
    }
    return h;
  }

  function md(src, cites = 0) {
    const lines = String(src).replace(/\r/g, "").split("\n");
    const out = [];
    let para = [], list = null, table = null;
    const flushPara = () => { if (para.length) { out.push(`<p>${inline(para.join(" "), cites)}</p>`); para = []; } };
    const flushList = () => { if (list) { out.push(`<${list.tag}>${list.items.map(i => `<li>${inline(i, cites)}</li>`).join("")}</${list.tag}>`); list = null; } };
    const flushTable = () => {
      if (table) {
        const [head, ...rows] = table;
        out.push(`<table><thead><tr>${head.map(c => `<th>${inline(c, cites)}</th>`).join("")}</tr></thead><tbody>` +
          rows.map(r => `<tr>${r.map(c => `<td>${inline(c, cites)}</td>`).join("")}</tr>`).join("") + "</tbody></table>");
        table = null;
      }
    };
    const flush = () => { flushPara(); flushList(); flushTable(); };

    for (const raw of lines) {
      const line = raw.trimEnd();
      let m;
      if (!line.trim()) { flush(); continue; }
      if ((m = line.match(/^\s*\[((?:Slide|Page|Sheet) [^\]]+)\]\s*$/))) { flush(); out.push(`<p class="passage-loc">${esc(m[1])}</p>`); continue; }
      if ((m = line.match(/^#{1,6}\s+(.*)$/))) { flush(); out.push(`<h4>${inline(m[1], cites)}</h4>`); continue; }
      if (/^\s*([-*_])\1{2,}\s*$/.test(line)) { flush(); out.push("<hr>"); continue; }
      if (/^\s*\|.*\|\s*$/.test(line)) {
        flushPara(); flushList();
        if (/^\s*\|(\s*:?-{2,}:?\s*\|)+\s*$/.test(line)) continue;
        (table ||= []).push(line.trim().replace(/^\||\|$/g, "").split("|").map(c => c.trim()));
        continue;
      }
      if ((m = line.match(/^\s*(?:[-*•]|(\d+)[.)])\s+(.*)$/))) {
        flushPara(); flushTable();
        const tag = m[1] ? "ol" : "ul";
        if (!list || list.tag !== tag) { flushList(); list = { tag, items: [] }; }
        list.items.push(m[2]);
        continue;
      }
      if (list && /^\s{2,}\S/.test(raw)) { list.items[list.items.length - 1] += " " + line.trim(); continue; }
      flushList(); flushTable();
      para.push(line.trim());
    }
    flush();
    return out.join("");
  }

  // The model puts general knowledge under "Beyond your materials"; set it apart.
  function renderAnswer(text, cites) {
    const m = text.match(/\n?\s*(?:#{1,6}\s*)?\*{0,2}Beyond your materials:?\*{0,2}:?\s*\n?/i);
    if (!m) return `<div class="md">${md(text, cites)}</div>`;
    const before = text.slice(0, m.index), after = text.slice(m.index + m[0].length);
    return `<div class="md">${md(before, cites)}</div>` +
      `<div class="beyond"><p class="beyond-label">Beyond your materials · general knowledge, not from Sloan</p><div class="md">${md(after, 0)}</div></div>`;
  }

  // ------------------------------------------------------------------ library

  // Semester labels look like "Fall 2026"; newest first, unlabeled last.
  function semKey(label) {
    const [season, year] = String(label || "").split(" ");
    return (Number(year) || 0) * 10 + (SEASONS[season] || 0);
  }

  // Every filterable thing, grouped by semester: courses, plus non-course material.
  function buildOptions(s) {
    // Course numbers ("15.010") are the label; non-credit sites (workshops, orientation) have none.
    const isCode = c => /^\d{1,2}\.[0-9A-Z]{2,5}$/i.test(c);
    // OpenCourseWare editions in the private brain are keyed "OCW 15.010".
    const opts = s.courses.map(c => {
      const ocw = c.course.startsWith("OCW "), num = ocw ? c.course.slice(4) : c.course;
      let name = c.course_name || num, sub;
      const cut = ocw ? name.lastIndexOf(" · ") : -1;          // "Financial Accounting · Fall 2003"
      if (cut > 0) { sub = name.slice(cut + 3); name = name.slice(0, cut); }
      return { key: c.course, code: isCode(num) ? num : "Non-credit", name, sub,
        term: c.term || "", n: c.n, short: ocw ? `${num} (OCW)` : isCode(num) ? num : name };
    });
    for (const t of s.types) {
      if (OUTSIDE[t.type]) opts.push({ key: "@" + t.type, code: OUTSIDE[t.type][0], name: OUTSIDE[t.type][1], term: t.term || "", n: t.n, outside: true, short: OUTSIDE[t.type][0] });
    }
    // The demo's OpenCourseWare courses come from different years: one group, terms on the tiles.
    const groups = new Map();
    for (const o of opts) {
      if (s.demo && o.term) o.sub = o.term;
      const g = s.demo ? "Sloan core courses · MIT OpenCourseWare" : (o.term || "Other");
      if (!groups.has(g)) groups.set(g, []);
      groups.get(g).push(o);
    }
    const rank = o => o.outside ? 2 : o.code === "Non-credit" ? 1 : 0;
    return [...groups.entries()]
      .sort((a, b) => semKey(b[0]) - semKey(a[0]))
      .map(([term, items]) => ({ term, items: items.sort((a, b) => (rank(a) - rank(b)) || a.short.localeCompare(b.short, undefined, { numeric: true })) }));
  }

  async function loadStats() {
    try {
      const res = await fetch("/api/stats");
      if (!res.ok) throw new Error(await res.text());
      const s = state.stats = await res.json();
      if (s.demo) applyDemo();
      el.navStat.textContent = `${plural(s.docs, "doc")} · ${plural(s.courses.length, "course")}`;
      el.navStat.hidden = false;
      state.options = buildOptions(s);

      el.pickerBody.innerHTML = state.options.map(g => `
        <div class="sem-group" data-term="${esc(g.term)}">
          <div class="sem"><span class="sem-name">${esc(g.term)}</span>
            <button type="button" class="link" data-sem="${esc(g.term)}">Select all</button></div>
          ${g.items.map(o => `
          <label class="opt">
            <input type="checkbox" value="${esc(o.key)}">
            <span class="opt-code">${esc(o.code)}</span>
            <span class="opt-name">${esc(o.sub ? `${o.name} · ${o.sub}` : o.name)}</span>
          </label>`).join("")}
        </div>`).join("") || `<p class="picker-count" style="padding:8px">Nothing indexed yet.</p>`;

      el.tiles.innerHTML = state.options.map(g => `
        <p class="lib-sem">${esc(g.term)}</p>
        <div class="tiles-grid">${g.items.map(o => `
          <button type="button" class="tile" data-key="${esc(o.key)}" aria-pressed="false">
            <span class="tile-top"><span class="tile-code">${esc(o.code)}</span><span class="tile-n">${plural(o.n, "doc")}</span></span>
            <span class="tile-name">${esc(o.name)}</span>
            ${o.outside ? `<span class="tile-term">Outside the classroom</span>` : o.sub ? `<span class="tile-term">${esc(o.sub)}</span>` : ""}
          </button>`).join("")}</div>`).join("")
        || `<p class="notice notice--plain">Nothing is indexed yet. Run <code>python brain/sync.py --remote</code> after converting your materials.</p>`;
      el.libTotal.textContent = `${plural(s.docs, "document")} · ${plural(s.chunks, "passage")} · ${Math.round(s.words / 1000).toLocaleString()}k words`;
      el.library.hidden = false;
      syncFilterUI();
    } catch (err) {
      el.library.hidden = false;
      el.tiles.innerHTML = `<p class="notice">Couldn’t load the library: ${esc(err.message || err)}</p>`;
    }
  }

  // ------------------------------------------------------------------ public demo

  const DEMO_SUGGESTIONS = [
    "How do two-part tariffs help a firm capture more value?",
    "What is the winner's curse, and how do I avoid it when bidding?",
    "How should I read a company's statement of cash flows?",
    "Why do cartels break down, and when can collusion last?",
  ];

  function applyDemo() {
    document.body.classList.add("is-demo");
    document.title = "Sloan Brain · Public demo";
    $("#demo-bar").hidden = false;
    $("#foot").hidden = false;
    $(".brand-ver").textContent = "Demo";
    $(".kicker").lastChild.textContent = "The Sloan core, open edition";
    $(".lede").textContent = "A working copy of my private study tool, loaded with six MIT Sloan core courses from MIT OpenCourseWare. Ask about a real business situation: answers cite the exact course, lecture and page.";
    $(".suggest-list").innerHTML = DEMO_SUGGESTIONS.map(q => `<button type="button" class="pill">${esc(q)}</button>`).join("");
  }

  function creditFor(course) {
    const c = state.stats?.credits?.[String(course).replace(/^OCW /, "")];
    if (!c) return "";
    const who = (c.instructors || []).join(", ");
    return `<p class="credit"><strong>MIT OpenCourseWare</strong> · ${esc(c.course)} ${esc(c.title)}, ${esc(c.term)}${who ? ` · ${esc(who)}` : ""}.
      <a href="${esc(c.url)}" target="_blank" rel="noopener">Course page</a> ·
      <a href="${esc(c.license)}" target="_blank" rel="noopener">CC BY-NC-SA 4.0</a></p>`;
  }

  // ------------------------------------------------------------------ course filter

  const optionByKey = key => state.options.flatMap(g => g.items).find(o => o.key === key);

  function filterLabel(keys) {
    if (!keys.length) return "All courses";
    const full = state.options.find(g => g.items.length > 1 && g.items.length === keys.length && g.items.every(o => keys.includes(o.key)));
    if (full) return `All of ${full.term}`;
    const codes = keys.map(k => (optionByKey(k) || { short: k }).short);
    return codes.length <= 2 ? codes.join(", ") : `${codes.length} courses`;
  }

  function syncFilterUI() {
    const keys = [...state.selected];
    el.pickerLabel.textContent = filterLabel(keys);
    el.pickerBtn.classList.toggle("on", keys.length > 0);
    el.pickerCount.textContent = keys.length ? `${plural(keys.length, "course")} selected` : "Searching everything";
    for (const box of el.pickerBody.querySelectorAll("input[type=checkbox]")) box.checked = state.selected.has(box.value);
    for (const g of el.pickerBody.querySelectorAll(".sem-group")) {
      const boxes = [...g.querySelectorAll("input")];
      $(".link", g).textContent = boxes.every(b => b.checked) ? "Clear" : "Select all";
    }
    for (const t of el.tiles.querySelectorAll(".tile")) {
      const on = state.selected.has(t.dataset.key);
      t.classList.toggle("on", on);
      t.setAttribute("aria-pressed", String(on));
    }
  }

  function setSelected(keys) {
    state.selected = new Set(keys);
    syncFilterUI();
  }

  function openPicker(open) {
    el.pickerPop.hidden = !open;
    el.pickerBtn.setAttribute("aria-expanded", String(open));
    if (open) (el.pickerBody.querySelector("input:checked") || el.pickerBody.querySelector("input"))?.focus({ preventScroll: true });
  }

  // ------------------------------------------------------------------ turns

  function newTurn(q, mode, parent = null) {
    document.body.classList.add("has-thread");
    el.newBtn.hidden = false;
    const courses = parent ? parent.courses : [...state.selected];
    const node = document.createElement("article");
    node.className = "turn" + (parent ? " turn--deeper" : "");
    const chips = [parent && `<span class="chip chip--deep">Deep dive</span>`,
                   courses.length && `<span class="chip chip--accent">${esc(filterLabel(courses))}</span>`].filter(Boolean).join("");
    node.innerHTML = `
      <h2 class="turn-q">${esc(q)}</h2>
      ${chips ? `<div class="turn-filters">${chips}</div>` : ""}
      <p class="status"><span class="spin"></span><span class="status-text">${parent ? "Reading more of your materials…" : "Searching your materials…"}</span></p>
      <div class="answer"></div>
      <div class="actions" hidden></div>
      <section class="sources" hidden></section>`;
    el.thread.appendChild(node);
    const turn = { q, mode, courses, node, sources: [], answer: "", done: false, deeper: !!parent };
    state.turns.push(turn);
    requestAnimationFrame(() => node.scrollIntoView({ behavior: matchMedia("(prefers-reduced-motion: reduce)").matches ? "auto" : "smooth", block: "start" }));
    return turn;
  }

  function setStatus(turn, text, done = false, warn = false) {
    const s = $(".status", turn.node);
    s.innerHTML = `<span class="${done ? "done-dot" : "spin"}${warn ? " warn" : ""}"></span><span class="status-text">${esc(text)}</span>`;
  }

  function renderSources(turn, heading) {
    const box = $(".sources", turn.node);
    const n = turn.sources.length;
    if (!n) { box.hidden = true; return; }
    box.hidden = false;
    box.classList.toggle("collapsed", n > 5);
    box.innerHTML = `
      <div class="sources-head"><p class="label">${esc(heading)}</p></div>
      <div class="sources-list">${turn.sources.map(s => `
        <button type="button" class="src" data-n="${s.n}" data-doc="${esc(s.doc_id)}" data-seq="${s.seq}">
          <span class="src-n">${s.n}</span>
          <span class="src-top">
            ${s.course ? `<span class="chip chip--accent">${esc(s.course)}</span>` : ""}
            <span class="chip">${esc(TYPE_ONE[s.type] || s.type)}</span>
            ${s.locator ? `<span class="chip">${esc(s.locator)}</span>` : ""}
          </span>
          <span class="src-title">${esc(s.title)}</span>
          <span class="src-where">${esc([s.course_name, s.module, s.term || s.date].filter(Boolean).join(" · "))}</span>
          ${s.snippet ? `<span class="src-snip">${marks(s.snippet)}</span>` : ""}
        </button>`).join("")}
      </div>
      ${n > 5 ? `<button type="button" class="btn btn--ghost btn--sm more">Show all ${n} sources</button>` : ""}`;
  }

  function renderActions(turn) {
    const box = $(".actions", turn.node);
    const btns = [];
    const canDeepen = turn.mode === "ask" && turn.answer && !turn.deeper && !turn.deepened;
    if (canDeepen) {
      btns.push(`<button type="button" class="btn btn--primary btn--sm" data-act="deeper">
        <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M12 5v14M19 12l-7 7-7-7"/></svg>
        Go deeper</button>`);
    }
    if (turn.sources.length) {
      btns.push(`<button type="button" class="btn ${canDeepen ? "btn--ghost" : "btn--primary"} btn--sm" data-act="claude">
        <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M12 3l1.9 5.6L19.5 10l-5.6 1.9L12 17.5l-1.9-5.6L4.5 10l5.6-1.4z"/><path d="M19 15l.8 2.2L22 18l-2.2.8L19 21l-.8-2.2L16 18l2.2-.8z"/></svg>
        ${turn.answer ? "Ask Claude for a deeper answer" : "Ask Claude to answer from these"}</button>`);
    }
    if (turn.mode === "ask" && turn.answer) {
      btns.push(`<button type="button" class="btn btn--ghost btn--sm" data-act="copy">
        <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><rect x="9" y="9" width="12" height="12" rx="2"/><path d="M5 15V5a2 2 0 0 1 2-2h10"/></svg>
        Copy answer</button>`);
    }
    if (turn.mode === "search") {
      btns.push(`<button type="button" class="btn btn--ghost btn--sm" data-act="answer">Write an answer from these</button>`);
    }
    box.innerHTML = btns.join("");
    box.hidden = !btns.length;
  }

  function notice(turn, html, plain = false) {
    $(".answer", turn.node).insertAdjacentHTML("beforeend", `<div class="notice${plain ? " notice--plain" : ""}">${html}</div>`);
  }

  // ------------------------------------------------------------------ ask (streamed)

  async function ask(q, parent = null) {
    const turn = newTurn(q, "ask", parent);
    const history = parent ? [{ q: parent.q, a: parent.answer }]
      : state.turns.filter(t => t !== turn && t.mode === "ask" && t.done && t.answer)
        .slice(-2).map(t => ({ q: t.q, a: t.answer }));
    const ansEl = $(".answer", turn.node);
    let raf = 0;
    const paint = () => { raf = 0; ansEl.innerHTML = renderAnswer(turn.answer, turn.sources.length); };

    try {
      const res = await fetch("/api/ask", {
        method: "POST", headers: { "content-type": "application/json" },
        body: JSON.stringify({ q, courses: turn.courses, history, deeper: !!parent }),
      });
      if (!res.ok || !res.body) throw new Error((await res.text()) || `HTTP ${res.status}`);
      const reader = res.body.getReader();
      const dec = new TextDecoder();
      let buf = "", errored = false;

      const handle = (event, data) => {
        if (event === "sources") {
          turn.sources = data.sources || [];
          const docs = new Set(turn.sources.map(s => s.doc_id)).size;
          if (turn.sources.length) {
            setStatus(turn, `Found ${plural(turn.sources.length, "passage")} in ${plural(docs, "document")} · writing`);
            renderSources(turn, "Sources");
            ansEl.classList.add("streaming");
          }
        } else if (event === "empty") {
          setStatus(turn, "No matching passages", true, true);
          notice(turn, `<strong>Nothing in your materials matches.</strong> Try the name of a framework, a course number, or different words, or switch to <em>Search</em> to browse.`, true);
        } else if (event === "cached") {
          turn.cached = true;
        } else if (event === "error" && data.code === "demo_limit") {
          errored = true;
          setStatus(turn, "Live answers used up", true, true);
          notice(turn, data.scope === "visitor"
            ? `<strong>You’ve used today’s live answers for this demo.</strong> It runs on a free AI allowance. The suggested questions still answer instantly, and <strong>Search</strong> and <strong>Ask Claude</strong> keep working. The sources for your question are below.`
            : `<strong>The demo’s live answers for today are used up.</strong> It runs on a free AI allowance that resets at 00:00 UTC. The suggested questions still answer instantly, and <strong>Search</strong> and <strong>Ask Claude</strong> keep working. The sources for your question are below.`);
        } else if (event === "error") {
          errored = true;
          setStatus(turn, data.code === "quota" ? "Free answers used up for today" : "Couldn’t write an answer", true, true);
          notice(turn, data.code === "quota"
            ? `<strong>Today’s free answers are used up.</strong> They reset at 00:00 UTC (7–8 pm in Boston). Your sources are below. <strong>Ask Claude</strong> turns them into an answer in one click.`
            : `<strong>The answer model didn’t respond.</strong> Your sources are below. Use <strong>Ask Claude</strong>, or try again in a minute.`);
        } else if (event === "message") {
          if (data === "[DONE]") return;
          let obj; try { obj = JSON.parse(data); } catch { return; }
          const piece = obj.response ?? obj.choices?.[0]?.delta?.content ?? "";
          if (typeof piece === "string" && piece) {
            turn.answer += piece;
            if (!raf) raf = requestAnimationFrame(paint);
          }
        }
      };

      for (;;) {
        const { value, done } = await reader.read();
        if (done) break;
        buf += dec.decode(value, { stream: true }).replace(/\r\n/g, "\n");
        let i;
        while ((i = buf.indexOf("\n\n")) !== -1) {
          const block = buf.slice(0, i); buf = buf.slice(i + 2);
          let event = "message", data = [];
          for (const line of block.split("\n")) {
            if (line.startsWith("event:")) event = line.slice(6).trim();
            else if (line.startsWith("data:")) data.push(line.slice(5).replace(/^ /, ""));
          }
          if (!data.length) continue;
          const payload = data.join("\n");
          let parsed = payload;
          if (event !== "message") { try { parsed = JSON.parse(payload); } catch { parsed = {}; } }
          handle(event, parsed);
        }
      }
      if (raf) cancelAnimationFrame(raf);
      turn.answer = turn.answer.trim();
      if (turn.answer) paint();
      ansEl.classList.remove("streaming");
      if (turn.answer && !errored) {
        const used = new Set([...turn.answer.matchAll(/\[(\d{1,2})\]/g)].map(m => +m[1])).size;
        setStatus(turn, `Answered from ${plural(turn.sources.length, "source")}${used ? ` · ${used} cited` : ""}${turn.cached ? " · saved answer" : ""}`, true);
      }
    } catch (err) {
      ansEl.classList.remove("streaming");
      setStatus(turn, "Something went wrong", true, true);
      notice(turn, `<strong>Couldn’t reach the brain.</strong> ${esc(String(err.message || err).slice(0, 240))}`);
    }
    turn.done = true;
    renderActions(turn);
  }

  // ------------------------------------------------------------------ search (no AI)

  async function search(q) {
    const turn = newTurn(q, "search");
    try {
      const p = new URLSearchParams({ q });
      for (const c of turn.courses) p.append("course", c);
      const res = await fetch(`/api/search?${p}`);
      if (!res.ok) throw new Error(await res.text());
      const data = await res.json();
      turn.sources = data.results;
      if (!turn.sources.length) {
        setStatus(turn, "No matching passages", true, true);
        notice(turn, `<strong>No passages match.</strong> Search looks for the words themselves: try a framework name, a course number, or a synonym.`, true);
      } else {
        const docs = new Set(turn.sources.map(s => s.doc_id)).size;
        setStatus(turn, `${plural(turn.sources.length, "passage")} in ${plural(docs, "document")}`, true);
        renderSources(turn, "Best matches");
      }
    } catch (err) {
      setStatus(turn, "Something went wrong", true, true);
      notice(turn, `<strong>Search failed.</strong> ${esc(String(err.message || err).slice(0, 240))}`);
    }
    turn.done = true;
    renderActions(turn);
  }

  // ------------------------------------------------------------------ Claude hand-off

  function claudePrompt(turn) {
    const src = turn.sources.map(s => {
      const head = [s.course && `${s.course}${s.course_name ? " " + s.course_name : ""}`, s.title].filter(Boolean).join(" — ");
      const where = [TYPE_ONE[s.type] || s.type, s.locator, s.module, s.term].filter(Boolean).join("; ");
      return `[${s.n}] ${head} (${where})\n${(s.text || s.snippet || "").replace(/[]/g, "").trim()}`;
    }).join("\n\n---\n\n");
    return `${state.stats?.demo
      ? "Below are excerpts from MIT Sloan course materials published on MIT OpenCourseWare. Use them to answer my question."
      : "I'm an MIT Sloan MBA student. Below are excerpts from my own Sloan course materials, notes and conversations. Use them to answer my question."}

- Lead with what I should do or think, then the reasoning.
- Cite excerpts by number, like [2]. Name the course and framework when the excerpt gives them.
- Say plainly where the excerpts don't cover something. Keep general knowledge clearly separate from what Sloan taught.

My question: ${turn.q}

Excerpts:

${src}`;
  }

  async function toClaude(turn) {
    const prompt = claudePrompt(turn);
    const copied = await copy(prompt);
    const url = prompt.length < 6000 ? `https://claude.ai/new?q=${encodeURIComponent(prompt)}` : "https://claude.ai/new";
    window.open(url, "_blank", "noopener");
    toast(copied ? (url.includes("?q=") ? "Opening Claude. The prompt is also on your clipboard." : "Prompt copied. Paste it into Claude.")
                 : "Couldn’t copy. Opening Claude anyway.");
  }

  // ------------------------------------------------------------------ reader

  let lastFocus = null;
  async function openReader(docId, seq) {
    lastFocus = document.activeElement;
    const r = el.reader;
    $("#reader-title").textContent = "Loading…";
    $("#reader-sub").textContent = "";
    $("#reader-meta").innerHTML = "";
    $("#reader-body").innerHTML = "";
    r.classList.add("open");
    r.setAttribute("aria-hidden", "false");
    document.documentElement.style.overflow = "hidden";
    $(".reader-panel", r).focus();
    try {
      let doc = state.docs.get(docId);
      if (!doc) {
        const res = await fetch(`/api/doc/${encodeURIComponent(docId)}`);
        if (!res.ok) throw new Error(await res.text());
        doc = await res.json();
        state.docs.set(docId, doc);
      }
      $("#reader-meta").innerHTML = [doc.course && `<span class="chip chip--accent">${esc(doc.course)}</span>`,
        `<span class="chip">${esc(TYPE_ONE[doc.type] || doc.type)}</span>`].filter(Boolean).join("");
      $("#reader-title").textContent = doc.title;
      const sub = [doc.course_name, doc.term, doc.module, doc.date].filter(Boolean).map(esc);
      const ocw = doc.source === "MIT OpenCourseWare";
      if (doc.url && /^https?:/.test(doc.url)) sub.push(`<a href="${esc(doc.url)}" target="_blank" rel="noopener noreferrer">Original on ${ocw ? "OpenCourseWare" : "Canvas"} ↗</a>`);
      $("#reader-sub").innerHTML = sub.join(" · ") + (ocw ? creditFor(doc.course) : "");
      $("#reader-body").innerHTML = doc.chunks.map(c => `
        <section class="passage${c.seq === seq ? " hit" : ""}" data-seq="${c.seq}">
          ${(c.locator || c.heading) && !/^\s*\[(?:Slide|Page|Sheet) /.test(c.text) ? `<p class="passage-loc">${esc(c.locator || c.heading)}</p>` : ""}
          <div class="md">${md(c.text)}</div>
        </section>`).join("");
      const hit = $(`.passage[data-seq="${seq}"]`, r);
      const panel = $(".reader-panel", r);
      panel.scrollTop = 0;
      if (hit && hit !== $(".passage", r)) {
        requestAnimationFrame(() => { panel.scrollTop = hit.offsetTop - $(".reader-head", r).offsetHeight - 12; });
      }
    } catch (err) {
      $("#reader-title").textContent = "Couldn’t open this document";
      $("#reader-body").innerHTML = `<p class="notice">${esc(String(err.message || err))}</p>`;
    }
  }

  function closeReader() {
    el.reader.classList.remove("open");
    el.reader.setAttribute("aria-hidden", "true");
    document.documentElement.style.overflow = "";
    if (lastFocus) lastFocus.focus({ preventScroll: true });
  }

  // ------------------------------------------------------------------ events

  function submit() {
    const q = el.q.value.trim();
    if (!q || state.busy) return;
    el.q.value = "";
    autosize();
    state.busy = true;
    el.send.disabled = true;
    (state.mode === "search" ? search(q) : ask(q)).finally(() => {
      state.busy = false;
      el.send.disabled = false;
    });
  }

  function autosize() {
    el.q.style.height = "auto";
    el.q.style.height = Math.min(el.q.scrollHeight, 220) + "px";
  }

  function setMode(mode) {
    state.mode = mode;
    for (const b of document.querySelectorAll(".seg button")) b.setAttribute("aria-checked", String(b.dataset.mode === mode));
    el.send.setAttribute("aria-label", mode === "search" ? "Search" : "Ask");
    el.q.placeholder = mode === "search"
      ? "Search words or a framework, e.g. price elasticity, Little’s Law, SBI"
      : "e.g. How should I price a product when competitors are cutting prices?";
  }

  function reset() {
    state.turns = [];
    el.thread.innerHTML = "";
    document.body.classList.remove("has-thread");
    el.newBtn.hidden = true;
    window.scrollTo({ top: 0 });
    el.q.focus();
  }

  el.form.addEventListener("submit", e => { e.preventDefault(); submit(); });
  el.q.addEventListener("keydown", e => {
    if (e.key === "Enter" && !e.shiftKey && !e.isComposing) { e.preventDefault(); submit(); }
  });
  el.q.addEventListener("input", autosize);
  el.pickerBtn.addEventListener("click", () => openPicker(el.pickerPop.hidden));
  $("#picker-done").addEventListener("click", () => { openPicker(false); el.q.focus(); });
  $("#picker-all").addEventListener("click", () => setSelected([]));
  el.pickerBody.addEventListener("change", e => {
    const box = e.target.closest("input[type=checkbox]");
    if (!box) return;
    box.checked ? state.selected.add(box.value) : state.selected.delete(box.value);
    syncFilterUI();
  });
  el.pickerBody.addEventListener("click", e => {
    const b = e.target.closest("[data-sem]");
    if (!b) return;
    const keys = [...b.closest(".sem-group").querySelectorAll("input")].map(i => i.value);
    const all = keys.every(k => state.selected.has(k));
    for (const k of keys) all ? state.selected.delete(k) : state.selected.add(k);
    syncFilterUI();
  });
  document.addEventListener("click", e => {
    if (!el.pickerPop.hidden && !e.target.closest("#picker")) openPicker(false);
  });
  document.querySelector(".seg").addEventListener("click", e => {
    const b = e.target.closest("button[data-mode]");
    if (b) { setMode(b.dataset.mode); el.q.focus(); }
  });
  $("#suggest").addEventListener("click", e => {
    const b = e.target.closest(".pill");
    if (b) { el.q.value = b.textContent.trim(); submit(); }
  });
  el.tiles.addEventListener("click", e => {
    const t = e.target.closest(".tile");
    if (!t) return;
    const key = t.dataset.key, code = (optionByKey(key) || { short: key }).short;
    if (state.selected.has(key)) state.selected.delete(key); else state.selected.add(key);
    syncFilterUI();
    toast(state.selected.has(key)
      ? `Searching in ${filterLabel([...state.selected])}.`
      : state.selected.size ? `Removed ${code}.` : "Searching all courses again.");
  });
  el.newBtn.addEventListener("click", reset);
  $("#home-link").addEventListener("click", e => { e.preventDefault(); reset(); });

  el.thread.addEventListener("click", e => {
    const turnNode = e.target.closest(".turn");
    const turn = state.turns.find(t => t.node === turnNode);
    if (!turn) return;
    const cite = e.target.closest(".cite");
    if (cite) {
      const card = $(`.src[data-n="${cite.dataset.n}"]`, turn.node);
      if (card) {
        $(".sources", turn.node).classList.remove("collapsed");
        $(".more", turn.node)?.remove();
        card.scrollIntoView({ behavior: "smooth", block: "center" });
        card.classList.add("hot");
        setTimeout(() => card.classList.remove("hot"), 1600);
      }
      return;
    }
    const src = e.target.closest(".src");
    if (src) return openReader(src.dataset.doc, Number(src.dataset.seq));
    if (e.target.closest(".more")) {
      $(".sources", turn.node).classList.remove("collapsed");
      e.target.closest(".more").remove();
      return;
    }
    const act = e.target.closest("[data-act]")?.dataset.act;
    if (act === "claude") toClaude(turn);
    if (act === "copy") {
      const refs = turn.sources.map(s => `[${s.n}] ${[s.course, s.title, s.locator].filter(Boolean).join(", ")}`).join("\n");
      copy(`${turn.answer}\n\nSources:\n${refs}`).then(ok => toast(ok ? "Answer copied with its sources." : "Couldn’t copy."));
    }
    if (act === "deeper" && !state.busy) {
      turn.deepened = true;
      renderActions(turn);
      state.busy = true;
      el.send.disabled = true;
      ask(turn.q, turn).finally(() => { state.busy = false; el.send.disabled = false; });
    }
    if (act === "answer") {
      setMode("ask");
      setSelected(turn.courses);
      el.q.value = turn.q;
      submit();
    }
  });
  el.thread.addEventListener("mouseover", e => {
    const cite = e.target.closest(".cite");
    if (!cite) return;
    const card = $(`.src[data-n="${cite.dataset.n}"]`, cite.closest(".turn"));
    if (card) { card.classList.add("hot"); cite.addEventListener("mouseleave", () => card.classList.remove("hot"), { once: true }); }
  });

  el.reader.addEventListener("click", e => { if (e.target.closest("[data-close]")) closeReader(); });
  document.addEventListener("keydown", e => {
    if (e.key === "Escape" && el.reader.classList.contains("open")) { closeReader(); return; }
    if (e.key === "Escape" && !el.pickerPop.hidden) { openPicker(false); el.pickerBtn.focus(); return; }
    if (e.key === "/" && document.activeElement !== el.q && !/INPUT|TEXTAREA|SELECT/.test(document.activeElement.tagName)) {
      e.preventDefault(); el.q.focus();
    }
  });

  $("#theme-btn").addEventListener("click", () => {
    const root = document.documentElement;
    const dark = root.getAttribute("data-theme")
      ? root.getAttribute("data-theme") === "dark"
      : matchMedia("(prefers-color-scheme: dark)").matches;
    const next = dark ? "light" : "dark";
    root.setAttribute("data-theme", next);
    try { localStorage.setItem("theme", next); } catch {}
  });

  setMode("ask");
  loadStats();
  if (matchMedia("(hover: hover)").matches) el.q.focus();
})();
