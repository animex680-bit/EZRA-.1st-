# Website Building 3.0

**An adaptive, self-improving pipeline for designing, building, and selling premium
3D websites with Claude Code.**

Built 2026-06-12 from researching how the top personal brands in the 3D-website
space actually work — 14 creators analyzed, 50/50 Instagram/YouTube, last 1–2
months of content (see [`research/CREATORS.md`](research/CREATORS.md)). The
patterns they share became this system's skills, agents, and workflow.

## What's in the box

| File | What it is |
|------|-----------|
| [`PLAN.md`](PLAN.md) | The master plan: thesis, design doctrine, business plan, roadmap |
| [`WORKFLOW.md`](WORKFLOW.md) | The phase-gated runbook that turns a brief into a shipped site |
| [`ADAPT.md`](ADAPT.md) | The adaptation protocol — every "no" rewrites the rules + the user taste profile |
| [`FEEDBACK_LOG.md`](FEEDBACK_LOG.md) | Append-only record of every rejection and win |
| [`research/`](research/) | The evidence: 14 creators analyzed + the distilled playbook ([`PATTERNS.md`](research/PATTERNS.md)) |
| [`projects/`](projects/) | One folder per website built (brief, concept, manifest, QA verdicts) |

## The skills (`.claude/skills/`)

- **`wb3`** — orchestrator: boot sequence, phases, gates, agents, non-negotiables.
- **`wb3-research`** — re-analyze the top IG/YouTube creators every ~6 weeks; findings must change skill files.
- **`wb3-assets`** — every asset slot routed: free CC0 online, procedural GLSL, or a precise **2K–4K request to the user**. Never stretched, never faked.
- **`wb3-adapt`** — the feedback engine: capture → diagnose → edit the rule → rebuild.
- **`web3d` + 8 craft skills** — concept, assets, build, shaders, motion, perf, business, evolve (the proven WebGL pipeline, upgraded with this research: tokens-before-generation, TSL/WebGPU frontier, debug-UI-day-one, productization flywheel).

## The agents (`.claude/agents/`)

- **`logic-check`** — mandatory QA gate: does everything make sense, is it pleasing
  to the eye, are there mistakes, is it honest. Returns SHIP or a fix list —
  **no SHIP, no delivery**.
- **`conversion-critic`** — audits the site as an 8-second buyer and a conversion
  strategist. Sites must sell, not just impress.
- **`asset-scout`** — routes the asset manifest (free / procedural / user ask).
- **`trend-scout`** — the research agent (spawn ×2: YouTube + Instagram).

## How it adapts (the point of "3.0")

1. **Per feedback** — a "no" gets logged verbatim, the rule that produced it gets
   diagnosed and edited, the build is redone. The same rejection cannot happen twice.
2. **Per project** — retro → LEARNINGS → skill edits (the supreme rule, inherited
   from web3d-evolve).
3. **Per month** — trend-scouts refresh the creator research; stale patterns die.
4. **Per miss** — anything QA should have caught becomes a permanent logic-check rule.

## Quickstart (in a Claude Code session)

```
"Build a website for <client>" → Claude reads .claude/skills/wb3/SKILL.md,
scans FEEDBACK_LOG.md + ADAPT.md, and runs WORKFLOW.md phase by phase.
Say "no" or "don't like X" at any point → the wb3-adapt loop fires.
```

---

*ADAPT. LEARN. GROW. — a project that ships without upgrading the pipeline has failed.*
