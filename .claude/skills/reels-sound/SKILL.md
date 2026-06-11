---
name: reels-sound
description: SFX placement, music ducking, and final mix to -14 LUFS for IG. Optional — user often handles audio manually in their DAW. When invoked, produces audio.json (event list) + mixed audio.wav. Part of the reels pipeline.
---

# reels-sound — Mix To -14 LUFS

The user has flagged that the AI often "sucks" at audio. So: **default to NOT touching audio unless the user says to.** When invoked, do exactly what's specified, document every event, and let the user override anything in their DAW.

## When you're invoked

The user has either:
1. Said "do the audio" / "mix it" / "add SFX", OR
2. Approved a SFX plan you previewed.

Otherwise: produce `audio.json` as a plan (event list with timestamps + SFX file references), hand it to the user, do NOT render the mix.

## The SFX vocabulary (0x100x grammar)

| SFX | When | dBFS |
|---|---|---|
| `sub_bass_boom.wav` | the drop, hook opener | -8 (drop) / -10 (hook) |
| `impact_thud.wav` | each text statement entrance | -12 to -14 |
| `whoosh_deep.wav` | transition into peak | -12 |
| `whoosh_fast.wav` | quick text reveals | -16 |
| `riser_build.wav` | 1–3s into the drop | -10 building to -8 |
| `impact_reverse.wav` | 0.5s before the drop | -12 |
| `glitch_short.wav` | glitch transitions | -16 |
| `ui_click.wav` | small text in (subtitles) | -18 |
| `vinyl_crackle_loop.wav` | resolution + CTA bed | -22 to -20 |
| `heartbeat.wav` | tension scenes (rare) | -18 |

The library lives at `video-pipeline/03-assets/sfx/`. Filenames match exactly.

## The mix recipe (for -14 LUFS IG target)

```
Bus structure:
  music    →  comp 4:1 (-18 thresh) → -16 LUFS pre-duck
  vo       →  EQ + de-ess (in reels-voice) → -14 LUFS
  sfx      →  glue comp 2:1 → variable

Sidechain:
  vo  → ducks music by 6 dB with 40ms attack / 250ms release
  vo  → ducks vinyl_crackle by 8 dB (always under VO)

Master:
  loudnorm I=-14 TP=-1 LRA=8 (IG/TikTok target)
  brick-wall limiter at -0.8 dBFS
```

## What you produce: `audio.json`

```json
{
  "target_lufs": -14,
  "music":   {"file": "inputs/music/track.wav",
              "in_s": 0.00, "out_s": 32.00,
              "gain_db": -6, "duck_db": 6, "duck_attack_ms": 40, "duck_release_ms": 250},
  "vo":      {"file": "vo_mix.wav", "in_s": 0.00, "gain_db": 0},
  "sfx": [
    {"file": "sub_bass_boom.wav",    "at_s":  0.00, "gain_db": -10},
    {"file": "ui_click.wav",          "at_s":  0.33, "gain_db": -18},
    {"file": "impact_thud.wav",       "at_s":  2.00, "gain_db": -12},
    {"file": "whoosh_fast.wav",       "at_s":  2.50, "gain_db": -16},
    {"file": "impact_thud.wav",       "at_s":  4.00, "gain_db": -13},
    {"file": "impact_thud.wav",       "at_s":  4.50, "gain_db": -16},
    {"file": "riser_build.wav",       "at_s": 11.00, "gain_db": -10},
    {"file": "impact_reverse.wav",    "at_s": 13.50, "gain_db": -12},
    {"file": "sub_bass_boom.wav",     "at_s": 14.00, "gain_db":  -8},
    {"file": "impact_thud.wav",       "at_s": 14.00, "gain_db": -12},
    {"file": "vinyl_crackle_loop.wav","at_s": 22.00, "gain_db": -20, "loop": true},
    {"file": "whoosh_deep.wav",       "at_s": 28.00, "gain_db": -12}
  ],
  "master_chain": "loudnorm=I=-14:TP=-1:LRA=8, alimiter=limit=0.92"
}
```

## Render (only when asked)

Pipe through FFmpeg amix + sidechain:

```bash
ffmpeg -y \
  -i music.wav -i vo_mix.wav \
  -i sub_bass_boom.wav -i impact_thud.wav  ... etc \
  -filter_complex "
    [0:a] volume=-6dB [m];
    [1:a] volume=0dB  [v];
    [m][v] sidechaincompress=threshold=0.06:ratio=8:attack=40:release=250 [duckm];
    [2:a] adelay=0|0,volume=-10dB [sfx1];
    [3:a] adelay=2000|2000,volume=-12dB [sfx2];
    ...
    [duckm][v][sfx1][sfx2]... amix=inputs=N:normalize=0,
    loudnorm=I=-14:TP=-1:LRA=8,
    alimiter=limit=0.92
  " -ac 2 -ar 48000 audio_mix.wav
```

The watcher will verify peak < 0.95 and no clipping.

## Sign-off

Before mixing: show the user `audio.json` as a printable cue sheet so they can see every SFX, its time, and its level. They can change values or strike events before render.

If the user prefers their DAW: hand them `audio.json` + the muxed video (without sound) and stop.
