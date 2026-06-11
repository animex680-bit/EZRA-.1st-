---
name: reels
description: Master pipeline for producing premium Instagram Reels / TikTok / Shorts in the 0x100x dark-cinematic aesthetic — faceless OR on-face, using the user's voice. Use whenever the user wants to edit, plan, render, QA, or improve a short-form vertical video. This is the orchestrator — it routes to reels-script, reels-voice, reels-storyboard, reels-footage, reels-motion, reels-captions, reels-color, reels-sound, reels-render, reels-watcher, and reels-evolve.
---

# reels — Premium Vertical Video Pipeline (0x100x grammar)

This pipeline produces 9:16 vertical reels that match the @0x100x visual grammar: dark cinematic grade, reactive gradient character treatment, beat-synced typography, Twixtor speed ramps, cinematic letterbox bars, premium SFX. It works for **faceless** edits (B-roll + text + VO) and **on-face** edits (the user's talking head + cuts + captions).

## SUPREME RULE — every project must improve the pipeline

Same supreme rule as `web3d`: **before** every reel, read `.claude/skills/reels-evolve/LEARNINGS.md` and apply it. **After** every reel, append what was learned and **edit the affected skill files**. If a delivery happens without a pipeline update, that's a failed delivery. See `reels-evolve`.

## The anti-slop bar — a reel is SLOP unless it clears all of these

The watcher (`reels-watcher`) enforces this programmatically. **No delivery without a `PASS` verdict from the watcher.**

- [ ] **Real footage present.** If the brief includes faceless B-roll or on-face talking head, the final video must show that footage. A reel that is "just text on black" is slop — that's a slideshow, not a reel. (`reels-footage` is mandatory unless the project is explicitly a "kinetic typography only" exercise.)
- [ ] **Beat-synced typography.** Every caption appears within ±1 frame of its sung/spoken word or its assigned beat marker. Verified by the watcher.
- [ ] **Text in safe area.** All text sits inside the IG-safe rectangle (top 14% / bottom 18% / sides 4% reserved). Verified by the watcher.
- [ ] **No dead frames.** No stretch ≥ 4 sampled frames where mean luma < 10. If the visual is dark, there must still be **something** happening — gradient bloom, grain, subject silhouette, glow. Verified by the watcher.
- [ ] **One signature moment.** The peak/drop has a moment that gets screenshot-saved — gradient text, scale punch, twixtor freeze, character-painted gradient. Not the whole video — exactly one.
- [ ] **Premium type.** Bebas Neue / Druk Wide Bold or equivalent condensed display. No default system fonts. No yellow auto-caption karaoke look.
- [ ] **Dark cinematic grade.** Crushed blacks, teal-pushed shadows, warm highlights. Not flat. Not "Premiere default."
- [ ] **Letterbox bars.** 100–110px top and bottom, locked. Not optional.
- [ ] **Film grain overlay.** Subtle (15–25%) over the entire edit. Not optional.
- [ ] **Audio is mixed, not laid.** Music at -14 LUFS, VO 4–6 dB above, SFX punches sit underneath the VO, no clipping. Verified by the watcher.

## Inputs — what the user provides

A reel project lives in `video-pipeline/productions/NNN-slug/` and needs:

```
inputs/
  voice/        ← user's VO recordings (wav/mp3/m4a)
  footage/      ← B-roll clips OR talking-head takes
  music/        ← chosen music track (or marker file with title)
  brief.md      ← topic, angle, target duration, platform
```

If any of these are missing, the orchestrator asks the user — it does not invent footage and it does not pretend a pure-text-on-black render is a reel.

## Phases (sub-agent routing)

For every project, route in this order:

| Phase | Skill | Output |
|---|---|---|
| 1. Concept & script | `reels-script` | `script.md` (hook + build + peak + resolution + CTA) |
| 2. VO ingest | `reels-voice` | `vo.wav` (clean) + `vo_words.json` (Whisper word timings) |
| 3. Storyboard | `reels-storyboard` | `storyboard.md` (scene list + beat map + text-per-beat) |
| 4. Footage selection | `reels-footage` | `shotlist.json` (clip in/out per scene, with safety pass) |
| 5. Motion graphics | `reels-motion` | `motion.json` (animations per element: anim type, in/out, easing) |
| 6. Captions | `reels-captions` | `captions.json` (word/line entries, in/out per frame, style ref) |
| 7. Color grade | `reels-color` | `grade.json` (LUT + Lumetri params per scene) |
| 8. Sound design | `reels-sound` | `audio.json` (SFX placements, music ducking, target loudness) |
| 9. Render | `reels-render` | `vNN.mp4` master + REELS/TIKTOK exports |
| 10. QA gate | `reels-watcher` | `qa-vNN/report.md` (must say PASS) |
| 11. Evolve | `reels-evolve` | LEARNINGS.md append + skill edits |

The orchestrator is allowed to run phases 1–8 in concept-only mode (producing the JSON specs) without rendering — useful for the user to review the plan before any compositing happens.

## What the pipeline can actually do here vs locally

**Be honest about this with the user.** This environment has Python + Pillow + numpy + FFmpeg + Bebas Neue. It does NOT have After Effects, DaVinci Resolve, or Twixtor.

So the render skill (`reels-render`) does what's possible here:
- FFmpeg-based composition: load real footage, apply LUT, overlay text/captions, mix audio
- Pillow-based text rendering with gradient fills and Gaussian glow
- numpy-based color grade approximation of Lumetri
- A separate "AE handoff" mode where it outputs an After Effects project script (.jsx) the user can run on their machine to get the *true* Twixtor + character-gradient treatment

For the on-face Twixtor speed-ramp scenes and reactive-gradient character treatment, the pipeline **always** outputs an AE handoff project — the user runs that locally for the final cinematic frames. The pipeline render is the rough cut + caption/timing skeleton; AE is the final polish. The watcher runs on both.

## The watcher gate — non-negotiable

Every render is fed to `reels-watcher` before it is shown to the user. It checks (programmatically, in `video-pipeline/watcher/watcher.py`):

1. **Safe area** — text bbox inside [14% top, 82% bottom, 4–96% side]
2. **Edge clip** — no bright pixels in the outer 6px band of the frame
3. **Dead frames** — mean luma < 10 for ≥ 4 consecutive sampled frames
4. **Overexposure / low contrast** — readability sanity
5. **Audio clipping** — no samples at ±1.0
6. **Caption coverage** — ≥ 70% of frames show some text/caption
7. **Beat sync** — if `beats.json` is provided, every beat marker has a visible change within ±1 frame

If the watcher fails, the renderer does NOT hand the video to the user. Instead it reports the failures, the orchestrator routes back to the relevant sub-agent (e.g. `safe_area` failures → `reels-captions` to reposition; `dead_frame` failures → `reels-footage` because the visual is empty), then re-renders. Repeat until PASS.

## Folder layout (reference)

```
.claude/skills/
  reels/                ← this orchestrator
  reels-script/         ← script writing
  reels-voice/          ← VO ingest + word timing
  reels-storyboard/     ← scene + beat planning
  reels-footage/        ← footage selection / cuts
  reels-motion/         ← motion graphics spec
  reels-captions/       ← caption design + timing
  reels-color/          ← color grade spec
  reels-sound/          ← SFX + music mix
  reels-render/         ← FFmpeg compositor + AE handoff
  reels-watcher/        ← QA gate (the trust mechanism)
  reels-evolve/         ← supreme-rule retro + LEARNINGS

video-pipeline/
  watcher/
    watcher.py          ← programmatic frame + audio QA
  compositor/
    compose.py          ← FFmpeg-based composition
    text_layer.py       ← Bebas Neue + gradient + glow text rendering
    caption_sync.py     ← Whisper-style word-timed caption builder
    ae_handoff.py       ← exports .jsx for After Effects polish pass
  03-assets/
    fonts/              ← BebasNeue.ttf etc
    luts/               ← .cube color LUTs
    overlays/           ← grain, light leaks
    sfx/                ← organized SFX library
  reference/
    0x100x-analysis.md  ← honest deep analysis of the channel
    visual-grammar.md   ← the rules
  templates/
    reels-15s.json      ← timeline templates
    reels-30s.json
  productions/
    NNN-slug/
      inputs/           ← user-provided voice, footage, music
      script.md
      storyboard.md
      shotlist.json
      motion.json
      captions.json
      grade.json
      audio.json
      qa-vNN/           ← watcher reports per render
      vNN.mp4           ← render outputs
      ae-handoff/       ← .jsx + asset bundle for AE polish
  outputs/              ← final delivered files
```

## When the user says "make me a reel"

1. **Read `reels-evolve/LEARNINGS.md`** first.
2. Confirm what they have: brief, voice, footage, music. If anything is missing, **ask** — do not invent.
3. Create `productions/NNN-slug/` and route through phases 1→8.
4. Before any render, hand the user the storyboard + caption plan + motion spec for sign-off.
5. Render with `reels-render`. Run `reels-watcher` immediately. Iterate until PASS.
6. Deliver — give the user (a) the rendered REELS export, (b) the AE handoff zip if the project needs the cinematic polish pass, (c) the QA report so they can see what was checked.
7. **Run `reels-evolve` retro.** Append learnings. Edit skills. Push.

If a step is genuinely impossible in this env (e.g. Whisper is not installed), say so directly, propose the workaround (e.g. user runs Whisper locally and uploads `vo_words.json`), and continue.
