---
name: reels-storyboard
description: Builds the scene-by-scene storyboard for the reel — beat map (from music BPM + VO word timings), shot list, text-per-beat plan, and signature-moment placement. Use after script + VO are locked. Part of the reels pipeline.
---

# reels-storyboard — The Plan Before The Edit

You turn a script + VO + music into a frame-accurate plan. Nothing renders until this is signed off.

## Inputs

- `script.md`
- `vo_words.json` (from `reels-voice`)
- `inputs/music/<track>.wav` + `inputs/music/meta.json` with `bpm`, `drop_t`
- `brief.md` (target duration, platform, angle)

## Beat grid

1. Read music BPM. At 120 BPM → 0.5s/beat at 24fps = 12 frames/beat.
2. Identify the **drop** (peak/snap moment in the track) — this is where the signature moment lives.
3. Compute beat markers across the full duration: `beats = [b * (60/BPM) for b in range(0, ceil(duration*BPM/60))]`.
4. Save as `beats.json` so the watcher can verify sync later.

## Scene anatomy (32s master)

```
SCENE 1  HOOK         0.00 – 2.00s    1 line, scale punch, sub bass hit
SCENE 2  BUILD 1      2.00 – 4.00s    1 line, 2 cuts, beat sync
SCENE 3  BUILD 2      4.00 – 7.00s    B-roll: subject doing the thing
SCENE 4  BUILD 3      7.00 – 10.00s   three-beat punch, word swap
SCENE 5  PRE-PEAK     10.00 – 14.00s  twixtor ramp up, riser SFX
SCENE 6  PEAK / DROP  14.00 – 22.00s  THE statement, gradient text, signature shot
SCENE 7  RESOLUTION   22.00 – 28.00s  resolution line, calmer grade
SCENE 8  CTA          28.00 – 32.00s  handle + follow
```

If music drop ≠ 14s, **reshape the scene boundaries** so the PEAK lands on the drop. The drop drives the structure.

## Shot list

For each scene, produce one row:

| Scene | t_in | t_out | shot_type | footage_need | speed | gradient | grade_id | text_layer |
|---|---|---|---|---|---|---|---|---|
| 1 | 0.00 | 2.00 | extreme close-up | hands on keyboard, 60fps, dark room | 100% | OFF | dc_max | HOOK_01 |
| 2 | 2.00 | 4.00 | wide | subject at desk, low angle | 100% | OFF | dc_std | BUILD_01 |
| 3 | 4.00 | 7.00 | screen-grab | website on monitor, slow zoom-in | 100% | OFF | dc_std | BUILD_02 |
| 4 | 7.00 | 10.00 | medium | walking shot, freedom angle | 100% | OFF | dc_std | BUILD_03 |
| 5 | 10.00 | 14.00 | portrait close | subject reflection in screen, 60fps | 100→10% | OFF | dc_std | PRE_PEAK |
| 6 | 14.00 | 22.00 | portrait slow-mo | twixtor continues from 5, gradient on subject | 10% | ON | dc_peak | PEAK_01 |
| 7 | 22.00 | 28.00 | confident portrait | static, eye contact | 100% | gold soft | dc_resolution | RESOLUTION |
| 8 | 28.00 | 32.00 | cut to black or scene 7 hold | — | — | — | dc_cta | CTA |

Save as `shotlist.json`.

## Text-per-beat plan

For each line in `script.md`, assign:
- the exact time it enters (from `vo_words.json` — appears within ±1 frame of the spoken word)
- the time it exits
- the animation style (see `reels-captions` and `reels-motion`)
- the visual emphasis (highlight word, color)

Save in `text_plan.json` — `reels-captions` consumes this.

## Signature moment placement

Exactly **one** signature moment per reel. By default:
- Faceless / wealth-angle reels → gradient text on the peak word ("ONE CLIENT.")
- On-face reels → reactive gradient character treatment on the subject during the drop, held for 1.5–2.0s
- Educational reels → screen-grab UI annotation with corner brackets + gradient sweep

Mark the moment in the storyboard with **★** so every downstream skill knows where to spend its budget.

## Sign-off rule

Hand the user `storyboard.md` rendered as a one-page document with:
- the scene table
- the beat map
- which line lands where
- where the signature moment is

User confirms before any motion/caption/render work begins.

## Output files

```
productions/NNN-slug/
  storyboard.md
  shotlist.json
  beats.json
  text_plan.json
```
