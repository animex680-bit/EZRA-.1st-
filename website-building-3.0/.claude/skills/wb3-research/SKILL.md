---
name: wb3-research
description: Research refresh loop for Website Building 3.0 — re-analyze the top 3D-website creators and personal brands on YouTube and Instagram (50/50), extract their current processes, stacks, and techniques, and fold the findings into research/CREATORS.md, research/PATTERNS.md, and the craft skills. Run when PATTERNS.md is older than ~6 weeks, when entering a new niche, or when a build feels dated.
---

# wb3-research — Stay current or decay

The pipeline encodes what the best are doing *now*. Trends in 3D web move in weeks
(awwwards meta, new drei helpers, new AI tooling). Stale research = dated output.

## When to run

- `research/PATTERNS.md` header date is older than ~6 weeks.
- Starting work in a new niche (research that niche's best sites specifically).
- A delivered build gets a "looks dated / seen this before" reaction (also log via wb3-adapt).

## How to run

Spawn the **trend-scout** agent (`.claude/agents/trend-scout.md`) — two instances in
parallel, one per platform, keeping the 50/50 YouTube/Instagram balance:

- **YouTube**: tutorial/process creators — what they TEACH (stacks, step-by-step
  workflows, Claude Code / AI-agent usage, shader and motion techniques).
- **Instagram**: showcase/designer creators — what WINS ATTENTION (visual hooks,
  reel formats, styles that go viral, how attention converts to client work).

Scope each run to the last 1–2 months of content. Only top creators — strong
following or award-level work, verifiable activity. Mark every estimate as an
estimate; never invent counts or titles (honesty rule).

## What to extract per creator

1. Identity + platform + scale (followers/subs, est. ok if marked).
2. Signature style / niche.
3. Their step-by-step process (concept → assets → build → motion → ship).
4. Stack — especially Claude Code usage: skills, MCP servers, prompting patterns.
5. Monetization + pricing signals.
6. Reusable techniques worth encoding into our skills.

## Folding findings back (the point of the exercise)

1. Update `research/CREATORS.md` (per-creator analysis, dated).
2. Rewrite `research/PATTERNS.md` (the distilled playbook the pipeline uses).
3. **Edit the craft skills** where a finding changes practice — e.g. a new motion
   technique → web3d-motion; a pricing pattern → web3d-business. Research that
   doesn't change a skill file is trivia.
4. Note conflicts with the user's taste profile in ADAPT.md — **taste profile wins**;
   record the divergence rather than following the trend.
