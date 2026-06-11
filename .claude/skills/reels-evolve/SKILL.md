---
name: reels-evolve
description: The self-improvement loop — the SUPREME rule of the reels pipeline. Read LEARNINGS.md before every reel. After every reel run the retro, append learnings, and edit the affected skill files. The pipeline must measurably get better every time. Part of the reels pipeline.
---

# reels-evolve — The Supreme Rule

If a reel ships and the pipeline didn't improve, the project failed.

## On project START

1. Open `.claude/skills/reels-evolve/LEARNINGS.md`.
2. Read every entry tagged `OPEN` or `RECURRING`.
3. Apply them. If a learning says "captions kept clipping the right side — bump safe-side from 4% to 6%," then for this project use 6%.
4. If unclear how to apply a learning, ask before assuming.

## On project END (after watcher PASS + delivery)

Run the retro. Six questions:

1. **What did the watcher catch on the first render?** (Even if eventually PASSed.)
2. **What did the user catch that the watcher missed?** (Add a new watcher rule.)
3. **Which sub-agent took the most rework?** (Tighten its skill file.)
4. **Where did manual hand-off cost time?** (Automate or document.)
5. **What footage / SFX / font was missing and slowed the project?** (Add to a "next time, prep this" list.)
6. **Which scene had the highest engagement (if known)?** (Lock that pattern in.)

Write the answers into `LEARNINGS.md` as a new entry:

```markdown
## 2026-06-08 · #001 Building Websites — v3 PASS

**Watcher catches on first render:**
- 52 safe_area fails — text bbox went outside top 14% / bottom 18% band
  (root cause: y_frac values calculated from natural rest position not bbox after font scaling)
- 97 dead frames — most of scene 1, 5, 8 were just black behind text
  (root cause: no footage was loaded, scene relied on solid bg)

**User caught:**
- The "sweep lines" at the peak read as display glitches not as design
  → reels-motion now requires sweep lines to fade in/out rather than appear hard

**Rework hotspot:**
- reels-captions had to be rebuilt twice — first time forgot that anchor='mm' means y is center not top
  → reels-captions skill now documents anchor explicitly

**Hand-off pain:**
- No Whisper installed → user had to upload vo_words.json manually
  → reels-voice updated with the one-liner local script (already there)

**Missing assets:**
- No actual footage in the project — the user expected text-on-black to look like 0x100x
  → reels (orchestrator) now says explicitly: "no footage = slop. ask, don't invent."

**Pattern lock:**
- Gradient text on the peak word ("ONE CLIENT.") landed when it was on screen 2.0s+ minimum
  → reels-captions: signature-moment caption min hold = 48 frames

### Skill edits applied
- [x] `reels/SKILL.md` — added "no footage = slop" rule
- [x] `reels-captions/SKILL.md` — documented anchor='mm', signature-moment min hold
- [x] `reels-motion/SKILL.md` — sweep lines must fade in/out
- [x] `reels-watcher/SKILL.md` — (no change, watcher worked)
```

Then **edit the skill files** you listed. The learning isn't real until the skill is updated.

## The format

`LEARNINGS.md` lives at `.claude/skills/reels-evolve/LEARNINGS.md`. One entry per project, newest at top. Entries with `OPEN` tag survive until they're applied.

## Cadence

Every reel. No exceptions. Even a perfect reel teaches something — "what worked" is also a learning.
