# WORKFLOW.md — The Website-Creation Workflow

The executable, phase-gated workflow that turns a brief into a shipped, selling
website. Orchestrated by the `wb3` skill; this file is the operator's runbook.
Every phase names its skill(s), its agent(s), its output, and its GATE — work does
not cross a gate until the gate condition is true.

```
0 RESEARCH → 1 BRIEF → 2 CONCEPT ▮ → 3 ASSETS ▮ → 4 BUILD → 5 MOTION
                              → 6 QA ▮ → 7 DELIVER → 8 FEEDBACK ↺ → 9 EVOLVE
                                              (▮ = hard gate, ↺ = adaptation loop)
```

## Phase 0 — RESEARCH (skill: wb3-research · agent: trend-scout ×2)

Skip if `research/PATTERNS.md` is fresher than ~6 weeks and the niche is known.
Otherwise spawn two trend-scouts (YouTube + Instagram, 50/50), fold findings into
CREATORS.md / PATTERNS.md, and make the skill edits they justify.
**Output:** current PATTERNS.md. **No gate.**

## Phase 1 — BRIEF

One page, written before any creative work:
- Client + niche + what their buyers trust (visual language of the niche).
- Business goal: the ONE action a visitor must take (call, book, buy, DM).
- Budget tier (web3d-business ladder: $3–8k / $15–40k / $50k+) — this sets scope:
  tier 1 = video-driven page + motion system; tier 2 = custom WebGL + 1–2 shaders;
  tier 3 = full bespoke scene + signature tech.
- Success metric (leads/week, conversion %, award submission — something measurable).
- Constraints check: read FEEDBACK_LOG.md + ADAPT.md taste profile + LEARNINGS.md.
**Output:** `projects/<name>/BRIEF.md`. **Gate: user confirms the brief.**

## Phase 2 — CONCEPT (skill: web3d-concept) ▮ HARD GATE

Story, ONE signature moment, art direction (type pairing, palette, references),
section map with the seamless-transition plan. Apply PATTERNS.md (what wins
attention now) filtered through the taste profile (which always wins conflicts).
**Output:** `projects/<name>/CONCEPT.md` + reference set.
**GATE: user signs off on concept. No code, no assets, before sign-off.**
(When user is unavailable and has pre-authorized: proceed, but flag every taste
assumption made.)

## Phase 3 — ASSETS (skill: wb3-assets · agent: asset-scout) ▮ HARD GATE

Build the asset manifest from the concept. asset-scout routes every slot:
**FREE** (CC0 links + filenames) / **PROCEDURAL** (GLSL/generative plan) /
**USER ASK** (grouped 2K–4K spec, sent immediately so collection overlaps build).
**Output:** routed manifest; asks sent. **GATE: no slot unrouted.** Build may start
on structure while user assets are in transit — with labelled placeholders only.

## Phase 4 — BUILD (skills: web3d-build, web3d-shaders)

Stack per the web3d decision (default R3F + drei + GSAP + Lenis; vanilla three for
single bespoke scenes; **video-driven DOM page whenever WebGL can't be render-
verified** — never ship unverifiable WebGL). Vite scaffold, scene architecture,
the signature moment's custom shader. Error boundary + visible fallback always.
**Output:** running build, `npm run build` clean. **No gate (QA is the gate).**

## Phase 5 — MOTION (skill: web3d-motion)

The motion system, not ad-hoc animations: Lenis smooth scroll, scroll-creates-the-
words text assembly, scroll-as-scrubber pinned media, seamless section blips
(iris/crossfade), perpetual tile drift + cursor evade/attract, magnetic glowing
buttons, settled-text-clean rule. `prefers-reduced-motion` path from the start.
**Output:** choreographed page. **No gate (QA is the gate).**

## Phase 6 — QA (agents: logic-check + conversion-critic, parallel · skill: web3d-perf) ▮ HARD GATE

- **logic-check**: sense / eye / correctness / honesty audit → SHIP or FIX list.
- **conversion-critic**: 8-second buyer + strategist audit → BLOCKING/MAJOR/MINOR.
- **web3d-perf**: budgets (60fps mid-tier phone, lean payload, compressed assets).
Fix everything CRITICAL/BLOCKING/MAJOR, re-run logic-check until **SHIP**.
**GATE: SHIP verdict + no blocking conversion findings + perf budgets met.**

## Phase 7 — DELIVER

Commit → push (`git push -u origin main`, retry w/ backoff) → deploy (GitHub Pages
/ Vercel) → verify via API where the sandbox blocks direct fetch → hand the user
the **live URL** + one-paragraph summary of what to look at (esp. anything
logic-check marked UNVERIFIED for human eyes).
**Output: clickable live link. Never close without it.**

## Phase 8 — FEEDBACK ↺ (skill: wb3-adapt)

Present. Then:
- **"No" / "don't like X" / lukewarm** → run the ADAPT.md loop: log verbatim →
  diagnose the producing rule → edit that skill file → rebuild → re-present.
  The diagnosis names the re-entry phase (taste→2, assets→3, motion→5, copy→6).
  Repeat until approval. Same category rejected twice = structural rewrite + new
  logic-check rule.
- **Approval** → mark log entries RESOLVED, log what landed as a WIN.

## Phase 9 — EVOLVE (skill: web3d-evolve) — always last, never skipped

Retro → append to LEARNINGS.md → edit the skill files to encode the lessons →
note pricing/objection data into web3d-business. A project that ships without
upgrading the pipeline has failed the supreme rule.

---

## Standing rules across all phases

1. Taste profile (ADAPT.md) > research trends > personal default.
2. Honesty: estimates labelled, placeholders labelled, UNVERIFIED renders declared.
3. One motion system, one rAF loop, one source of truth for scroll progress.
4. Every project folder: BRIEF.md, CONCEPT.md, asset manifest, QA verdicts —
   so any future session can reconstruct context in minutes.
