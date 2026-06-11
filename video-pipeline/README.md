# video-pipeline

Premium short-form vertical video editing in the @0x100x aesthetic. Orchestrated by the `reels` skill set in `.claude/skills/reels*/`.

For the historical style-guide reference (color palette, motion principles, original style docs), see `STYLE-GUIDE.md` in this folder.

## TL;DR

```
When the user says "make me a reel":
  1. Read .claude/skills/reels-evolve/LEARNINGS.md
  2. Confirm inputs: script (or brief), voice, footage, music
  3. Invoke the reels skill — it routes through 11 sub-skills
  4. Watcher gates every render — no delivery without PASS
  5. Run reels-evolve retro at the end
```

## What's where

```
.claude/skills/
  reels/                 ← orchestrator (read this first)
  reels-script           ← writes the script in the 0x100x voice
  reels-voice            ← cleans user's VO, produces vo_words.json
  reels-storyboard       ← scene + beat plan + signature-moment placement
  reels-footage          ← selects & cuts B-roll / on-face shots
  reels-motion           ← motion graphics spec (motion.json)
  reels-captions         ← caption spec, ±1 frame sync (captions.json)
  reels-color            ← color grade spec (grade.json)
  reels-sound            ← SFX + mix spec (audio.json) — optional
  reels-render           ← FFmpeg composite + AE handoff
  reels-watcher          ← QA gate; programmatic frame inspection
  reels-evolve           ← supreme rule — pipeline improves every project

video-pipeline/
  watcher/
    watcher.py           ← run on every render; checks safe area, dead frames,
                            edge clip, overexposure, audio clipping, coverage
  compositor/            ← compose.py, text_layer.py, caption_sync.py,
                            ae_handoff.py  (TODO: implement on first real project)
  reference/
    0x100x-analysis.md   ← honest analysis of the channel grammar
  STYLE-GUIDE.md         ← the older long-form style guide
  01-style-guide/        ← color/typography/motion docs
  02-technical/          ← project settings, effects arsenal, exports
  03-assets/
    fonts/BebasNeue.ttf  ← installed
    luts/                ← put .cube LUTs here
    overlays/            ← grain, light leaks
    sfx/                 ← organized SFX library (user populates)
  04-workflow/           ← pre-production, editing workflow, review checklist
  05-caption-lyrics/     ← caption + lyric sync workflow docs
  templates/             ← reusable timeline templates (TBD)
  productions/
    NNN-slug/            ← one folder per reel
      inputs/{voice,footage,music}
      brief.md  script.md  storyboard.md
      shotlist.json  text_plan.json  motion.json
      captions.json  grade.json  audio.json
      cuts/                ← prepped per-scene footage
      preview_captions/    ← caption position previews for sign-off
      vNN.mp4              ← render outputs
      qa-vNN/              ← watcher reports per render
      ae-handoff/          ← .jsx + assets for AE polish pass
  outputs/                 ← final delivered files
```

## The watcher — the trust mechanism

Read `.claude/skills/reels-watcher/SKILL.md`. Tool at `video-pipeline/watcher/watcher.py`. Usage:

```bash
python3 video-pipeline/watcher/watcher.py \
    video-pipeline/productions/001-x/vNN.mp4 \
    --out video-pipeline/productions/001-x/qa-vNN/ \
    --every 4
```

Outputs `report.json`, `report.md`, and an `annotated/` directory of keyframes with the safe-area rectangle drawn (cyan) and any violation bboxes (red). The Read tool can view those frames — that's how the watcher agent does its work.

## Anti-slop bar (the orchestrator enforces)

See `.claude/skills/reels/SKILL.md`. A reel is slop unless:
- Real footage present (no text-on-black slideshows)
- Captions in IG-safe area (top 14% / bottom 18% / sides 4% reserved)
- No dead frames > 4 consecutive samples below luma 10
- Beat-synced typography
- One signature moment (not five)
- Premium type (Bebas Neue / Druk)
- Dark cinematic grade
- Letterbox bars on
- Grain overlay on
- Audio mixed to -14 LUFS, no clipping

The watcher checks the technical ones programmatically. Failures route back to the responsible sub-agent for fixes.

## Productions

See `productions/001-building-websites/` for the first project. The first two render attempts failed the watcher hard (52 safe-area fails, 97 dead frames). The QA report is preserved in `qa-v01/` as a regression test — any future render of this project should beat those numbers.
