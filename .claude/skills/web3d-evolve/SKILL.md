---
name: web3d-evolve
description: The self-improvement loop for the web3d pipeline — the SUPREME rule. Use at the start of every 3D web project (read LEARNINGS) and at the end (run the retro, append learnings, and edit the skill files to encode what was learned). The pipeline must get better after every project. Part of the web3d pipeline.
---

# web3d-evolve — Evolve or Die (SUPREME RULE)

The pipeline's highest-priority job is to improve itself. Every other skill serves the work; this skill makes the *pipeline* compound. A project is not done until this runs.

## The loop

### At project START
1. Read `LEARNINGS.md` (in this skill's folder).
2. Apply relevant past lessons. If a lesson contradicts a current skill, the lesson wins (it's newer evidence) — and you should fix the skill.

### At project END (mandatory retro — never skip)
1. **Score the output** against the web3d anti-slop bar. What raised quality? What dragged it toward slop?
2. **Record hard numbers**: stack chosen + why, final FPS, payload size, asset sizes, build time, what broke.
3. **Capture craft lessons**: which shader/effect/technique worked, what to reuse, what to never do again.
4. **Capture business lessons**: price quoted vs landed, objections, what the client reacted to.
5. **Append an entry to `LEARNINGS.md`** (template below).
6. **PROMOTE recurring/proven lessons into the skills** — actually edit the relevant `SKILL.md`. This is the evolution. New default easing? Edit web3d-motion. Found a faster asset path? Edit web3d-assets. A new anti-slop criterion? Edit the web3d orchestrator's bar.
7. If the pipeline structure itself was clumsy, **restructure it.** The pipeline may rewrite any part of itself, including this rule's mechanics — except the principle that it must keep evolving.

## LEARNINGS.md entry template

```
## [date] — <project name>
- Stack: <choice> — why: <reason>
- Concept / signature moment: <what it was, did it land>
- Perf: <fps on device>, payload <MB>, key models <sizes>
- Worked: <techniques/effects/decisions to reuse>
- Failed / avoid: <what dragged toward slop or broke>
- Business: quoted <$>, landed <$>, objection: <...>, what sold them: <...>
- SKILL EDITS made from this project: <which files, what changed>  ← proves the loop ran
```

## The one rule that cannot be deleted

> The pipeline must get measurably better after every project. Growth is priority #1, above any single deliverable.

If a project ships without a LEARNINGS entry and at least a considered "should any skill change? (yes/no + why)", the supreme rule was violated.
