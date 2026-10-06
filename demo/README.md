# Public demo (demo.fabio.cool)

The same app as brain.fabio.cool, public, loaded with MIT Sloan core courses
that MIT publishes on OpenCourseWare under CC BY-NC-SA 4.0. Only files OCW itself
marks with that license are imported; `credits.json` holds the attribution the
app shows on every document.

| Course | OCW edition |
|---|---|
| 15.010 Economic Analysis for Business Decisions | Fall 2004 |
| 15.060 Data, Models, and Decisions | Fall 2014 |
| 15.280 Communication for Managers | Fall 2016 |
| 15.311 Organizational Processes | Fall 2003 |
| 15.515 Financial Accounting | Fall 2003 |
| 15.761 Introduction to Operations Management | Spring 2013 |

## Rebuild

Download each course's zip from its OCW page ("Download course") into `demo/ocw/`, then:

    python brain/ocw_import.py demo/ocw/*.zip --out demo
    git add demo && git commit -m "Rebuild demo corpus" && git push

The deploy workflow syncs `demo/corpus` into the demo's D1 and publishes the
Worker with `wrangler deploy --env demo`.

## Limits

The demo shares the Cloudflare account's free Workers AI allowance with the
private brain, so live answers are capped (`DEMO_DAILY`, `DEMO_PER_VISITOR` in
`app/wrangler.toml`). Every answer is cached, so repeated questions, including
the suggested ones, cost nothing.
