---
name: wb3
description: Website Building 3.0 master orchestrator — the adaptive, research-driven pipeline for designing, building, QA-ing, and selling premium 3D websites. Use for ANY website job in this repo. Routes to wb3-research, wb3-assets, wb3-adapt, the web3d craft skills, and the four agents (trend-scout, asset-scout, logic-check, conversion-critic).
---

# wb3 — Website Building 3.0 (orchestrator)

One sentence: **research what the best are doing → build with the web3d craft skills →
gate through agents → ship a live link that sells → adapt on every piece of feedback.**

This skill is the entry point. It wraps the proven `web3d` pipeline in three loops
that the old pipeline didn't have: a research loop, an agent QA loop, and an
adaptation loop.

## Boot sequence (every job, before any work)

1. Read `FEEDBACK_LOG.md` — open rejections are constraints; resolved ones are law.
2. Read `ADAPT.md` taste profile — this is the user's taste model. It overrides trends.
3. Read `.claude/skills/web3d-evolve/LEARNINGS.md` — technical lessons.
4. Read `research/PATTERNS.md` — the creator playbook (refresh via `wb3-research` if
   older than ~6 weeks).

## The pipeline (phases with gates)

```
0. RESEARCH (wb3-research / trend-scout agent)        [refresh if stale]
1. BRIEF    — client, niche, business goal, budget tier, success metric
2. CONCEPT  (web3d-concept)                            GATE: user signs off on
            story + signature moment + art direction         concept BEFORE build
3. ASSETS   (wb3-assets / asset-scout agent)           GATE: every slot has a
            ask user for 2K–4K OR source free CC0            real or approved asset plan
4. BUILD    (web3d-build + web3d-shaders)
5. MOTION   (web3d-motion)
6. QA       (logic-check agent + conversion-critic     GATE: SHIP verdict required
            agent + web3d-perf)                              from logic-check
7. DELIVER  — commit, push, LIVE URL handed over
8. FEEDBACK (wb3-adapt)                                user says no → loop to the
                                                       phase the diagnosis points at
9. EVOLVE   (web3d-evolve)                             retro + skill edits, always
```

Phases 2–6 are the `web3d` craft core — its anti-slop bar and stack decision
(default React Three Fiber + GSAP + Lenis; video-driven page when WebGL can't be
verified) apply unchanged. This skill adds the loops around it.

## The agents (in `.claude/agents/`) — when to spawn each

- **trend-scout** — phase 0, or when entering a new niche. Refreshes the creator/
  technique research that PATTERNS.md is built from.
- **asset-scout** — phase 3. Given the concept's asset list, returns for each slot:
  FREE source plan, PROCEDURAL plan, or a precise USER ASK (2K–4K spec).
- **logic-check** — phase 6, mandatory. Audits coherence, visual quality, correctness.
  Its verdict is the ship gate: returns SHIP or a FIX list. No SHIP, no delivery.
- **conversion-critic** — phase 6 for any site meant to sell (i.e., all of them).
  Audits offer clarity, proof, CTA path. Findings above "minor" block delivery.

Run logic-check and conversion-critic in parallel; fix everything they raise, then
re-run logic-check until SHIP.

## Revision-rounds doctrine (research 2026-06)

Across every verified AI-assisted workflow (Oliur, Greenheck): **agent output is a
first draft, and premium quality takes 2–3 directed revision rounds.** Budget them
into every build — phase 4–6 is a loop, not a line. The main quality lever is
**direction specificity**: exact timings, named easings, named reference sites,
named animations — never "make it better."

## Non-negotiables (inherited + new)

- The `web3d` anti-slop bar, in full (real WebGL or verified video-driven; signature
  moment; custom shader when WebGL; no stagnant tiles; no hard section edges; type is
  the hero; perf budget; reduced-motion fallback).
- **Never ship unverifiable WebGL as the primary deliverable** (LEARNINGS 2026-05-30c).
- The RESOLUTION and ASK-FOR-ASSETS rules (wb3-assets).
- logic-check SHIP verdict before any delivery.
- Live URL or it didn't happen.
- LEARNINGS + FEEDBACK_LOG updated, skills edited — every project (supreme rule).
