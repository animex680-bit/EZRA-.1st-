---
name: reels-render
description: Final composition — loads cut footage, applies grade, draws captions + shape graphics, layers grain + letterbox, mixes audio, exports REELS/TIKTOK/PREVIEW. Two modes: python (rough composite, deterministic) or ae-handoff (.jsx for the polish pass). Part of the reels pipeline.
---

# reels-render — Composite & Export

## Two modes

### Mode 1: `python` (default, runs here)

Tool: `video-pipeline/compositor/compose.py`. Pipeline:

```
for each scene:
   load cut clip (footage) → scale/crop to 1080×1920
   apply per-scene grade   (LUT + Lumetri delta)
   apply bg glow / vignette (from grade.json)
for each frame in timeline:
   compose footage layer
   compose shape layers   (dividers, brackets, sweeps) from motion.json
   compose caption layers (text + glow + matte) from captions.json
   compose grain overlay
   compose letterbox bars
encode H.264 via ffmpeg pipe
mux audio (audio.json render OR user-provided mixed track)
```

What it can do:
- Real footage compositing (FFmpeg + Pillow)
- Bebas Neue text with Gaussian glow
- Gradient text via RGBA alpha matte
- Numpy color grade (3D LUT)
- Animated grain
- All shape layers
- Hard cuts, color flash, simple zoom

What it can't (sent to AE):
- True Twixtor speed ramps with optical-flow interpolation
- Reactive gradient character treatment with roto matte
- Motion blur swipes

### Mode 2: `ae-handoff`

Tool: `video-pipeline/compositor/ae_handoff.py`. Generates:
- `productions/NNN-slug/ae-handoff/project.jsx` (After Effects ExtendScript)
- `productions/NNN-slug/ae-handoff/assets/` (cuts, LUTs, fonts, grain)
- `productions/NNN-slug/ae-handoff/MANIFEST.md` (what to import + load order)

The user opens AE, runs `File → Scripts → Run Script File…` on `project.jsx`. AE rebuilds the full comp with proper Twixtor + character gradient. User exports the final master from AE.

The Python rough cut runs the same timeline so the AE comp is identical structure — the user just gets cinematic-grade interpolation on top.

## Inputs

```
productions/NNN-slug/
  cuts/                   ← from reels-footage
  captions.json           ← from reels-captions
  motion.json             ← from reels-motion
  grade.json              ← from reels-color
  audio.json              ← from reels-sound  (or user-mixed audio.wav)
  vo.wav                  ← from reels-voice
```

## Outputs (per render iteration)

```
productions/NNN-slug/
  vNN.mp4                 ← master, H.264 CRF 17, 1080×1920, 24fps
  vNN_REELS.mp4           ← compressed deliverable, CRF 22
  vNN_TIKTOK.mp4          ← 30fps version
  vNN_PREVIEW.mp4         ← 540×960 for review
  vNN_PNG_seq/             ← frame dumps (optional, for AE re-import)
  qa-vNN/                 ← reels-watcher report goes here
```

## Hard rules

1. **Never render without `vo_words.json` + `shotlist.json` populated.** If a scene has no `cut_path`, the renderer refuses and routes back to `reels-footage`.
2. **Always run `reels-watcher` immediately after render.** Do not show the user the video before the watcher returns its verdict.
3. **Iterate, don't excuse.** If watcher fails, fix what it caught and re-render. Do not hand the user the failing render with caveats.
4. **Master + REELS export are separate passes.** Render the master once at CRF 17, then transcode to CRF 22 / TIKTOK / PREVIEW from that — don't re-render from scratch (slow + non-reproducible).

## CLI

```bash
# Rough python composite
python3 video-pipeline/compositor/compose.py \
    --production productions/001-x/ --version 1 --mode python

# AE handoff (writes project.jsx + asset bundle)
python3 video-pipeline/compositor/compose.py \
    --production productions/001-x/ --version 1 --mode ae-handoff

# Both
python3 video-pipeline/compositor/compose.py \
    --production productions/001-x/ --version 1 --mode both
```

## Sign-off (delivery)

After watcher PASS:
1. Deliver REELS export to the user via SendUserFile (`status: proactive` when running async).
2. Attach `qa-vNN/report.md` so the user can see what was checked.
3. If `ae-handoff` was emitted, send the zip and a 1-line instruction: "Open AE → File > Scripts > Run Script File → project.jsx. Render master from there."
4. Commit, push.
5. Trigger `reels-evolve` retro.
