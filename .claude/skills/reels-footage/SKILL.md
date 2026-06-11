---
name: reels-footage
description: Selects, cuts, and prepares B-roll or on-face footage per scene of the storyboard. Verifies every scene actually has footage (no scene ends up as text-on-black). Produces stabilized, color-prep'd clips ready for the compositor. Part of the reels pipeline.
---

# reels-footage — Real Footage Or No Render

The #1 reason reels look like slop is that they're "text on black" instead of text on real footage. This skill exists to prevent that.

## Hard rule

**Every scene in `shotlist.json` must resolve to at least one source clip.** If a scene has no available footage, you do one of:
1. Ask the user to record/upload the missing shot.
2. Use a curated stock fallback (Pexels / Pixabay / user's own archive) tagged with the scene id.
3. **Negotiate the storyboard** with `reels-storyboard` to merge or restructure scenes so the available footage covers the timeline.

You do NOT pass an empty scene to `reels-render` and hope text-on-black looks OK. It does not.

## Inputs

- `shotlist.json` (from `reels-storyboard`)
- `inputs/footage/*.{mp4,mov,mkv}` — user's clips
- (optional) `inputs/footage/index.json` — user-provided tags

## Steps

### 1) Index user footage

Probe every clip in `inputs/footage/`:
- duration, fps, resolution, codec
- whether 60fps (required for Twixtor scenes)
- average luma (dark scenes prefer darker clips)
- horizontal vs vertical orientation
- has audio? (irrelevant — we mute it)

Write `inputs/footage/index.json`:
```json
[
  {"path": "kbd_close_60.mp4", "dur": 18.4, "fps": 60.0, "w": 3840, "h": 2160,
   "luma": 38, "orient": "h", "tags": ["hands","keyboard","close"]}
]
```

### 2) Auto-match scenes → clips

For each scene in `shotlist.json`, find best-matching clip:
- tag overlap with `footage_need`
- fps meets scene speed requirement (Twixtor needs ≥ 48fps)
- duration ≥ scene length + 0.5s safety pad

If no match → flag as `MISSING` and surface to the user immediately. Do not silently skip.

### 3) Cut + prep

For each chosen clip:
```bash
# crop to 9:16, soft stabilize, normalize length, mute audio
ffmpeg -ss <in_offset> -i <clip> -t <scene_dur+0.5> \
    -vf "vidstabdetect=shakiness=4:result=/tmp/_s.trf" -an -f null - 
ffmpeg -ss <in_offset> -i <clip> -t <scene_dur+0.5> \
    -vf "vidstabtransform=input=/tmp/_s.trf:smoothing=12, \
         scale=if(gt(a,9/16),-2,1080):if(gt(a,9/16),1920,-2), \
         crop=1080:1920" \
    -an -c:v libx264 -crf 18 -preset fast \
    cuts/scene_<NN>_<clip-slug>.mp4
```

For on-face scenes: add face-detect crop so the subject lives in the upper-middle third (where text doesn't sit). For Twixtor scenes: keep original frame rate and document the speed curve for the AE handoff.

### 4) Per-scene record

Update `shotlist.json` with resolved `cut_path` per scene + write `footage_resolution.md`:

```markdown
# Footage Resolution — NNN-slug

✓ Scene 1 — kbd_close_60.mp4 → cuts/scene_01_kbd_close.mp4 (60fps OK)
✓ Scene 2 — desk_wide.mp4    → cuts/scene_02_desk_wide.mp4
✗ Scene 3 — MISSING (need: website-on-screen, slow zoom)
✓ Scene 4 — walk_corridor.mp4 → cuts/scene_04_walk.mp4
✓ Scene 5 — portrait_60.mp4   → cuts/scene_05_portrait.mp4 (60fps OK for Twixtor)
✓ Scene 6 — (continues from 5, 60fps, Twixtor target)
✓ Scene 7 — portrait_static.mp4 → cuts/scene_07_static.mp4
○ Scene 8 — cut to black (no footage needed)
```

If anything is `✗ MISSING`, stop and ask the user. Do not proceed.

## On-face vs faceless

- **Faceless reels**: scenes 1–8 all use B-roll. The subject is implied (hands, screens, walking shot).
- **On-face reels**: scenes 1, 5, 6, 7 are the user's talking head; scenes 2, 3, 4 can be B-roll or screen-grab. The PEAK is always the user on camera.

For on-face: VO is synced to the user's mouth on the talking-head scenes. If the user's VO take was a separate recording, the talking-head clip is muted and the VO drives the timeline; lip-sync is approximate. Mark this in the storyboard so the user knows.

## Outputs

```
productions/NNN-slug/
  cuts/                      ← stabilized, cropped, prepped per-scene
    scene_01_*.mp4
    scene_02_*.mp4
    ...
  footage_resolution.md      ← what mapped to what, what's missing
  inputs/footage/index.json  ← indexed source library
```

## Handoff

`reels-render` reads `shotlist.json` (now with `cut_path` populated) to load the right clip for each scene. `reels-watcher` will fail any reel where a scene was rendered as solid black.
