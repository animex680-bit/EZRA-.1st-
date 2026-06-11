---
name: reels-color
description: Color grade spec for the reel — the dark cinematic 0x100x grade, per-scene Lumetri parameters, LUT selection, peak gradient bloom. Outputs grade.json. Part of the reels pipeline.
---

# reels-color — The Grade

## Master grade — "Dark Cinematic" (the base everywhere)

Resolve / Lumetri equivalent:

```
Lumetri Basic:
  Exposure   -0.30
  Contrast   +28
  Highlights -15
  Shadows    -12
  Blacks     -35

Color Wheels:
  Shadows:    slight teal push (Y -2, U +12, V -6)
  Midtones:   neutral
  Highlights: very slight warm amber (Y +1, U -4, V +6)

HSL Secondary:
  Skin tones: -8 saturation, +4 luminance
  Reds (NOT skin): +6 saturation

LUT (top):
  LUT_DarkCinematic.cube at 65% mix
```

Implemented in Python as a numpy LUT (`luts/dark_cinematic.cube` → 3D array). For AE handoff, ships the .cube file and a Lumetri preset .prfpset.

## Per-scene deltas

| Scene | Deltas vs master | Notes |
|---|---|---|
| 1 HOOK | gradient bg radial bloom @ 0.55 | subtle purple radial glow behind text |
| 2 BUILD 1 | — | standard |
| 3 BUILD 2 | slow zoom 100→105% over scene | psychological forward push |
| 4 BUILD 3 | vignette +20%, exposure -0.15 | each "NO" gets darker |
| 5 PRE-PEAK | desaturate -25 over scene, ramp into drop | tension |
| 6 PEAK ★ | gradient bg @ 0.70, glow @ 1.2, grain +5% | the signature look |
| 7 RESOLUTION | gold tint @ 0.30, vignette +15% | warm landing |
| 8 CTA | gradient bg @ 0.00, blacks -10 | near-black close |

## What you produce: `grade.json`

```json
{
  "master": {
    "lut": "LUT_DarkCinematic.cube",
    "lut_mix": 0.65,
    "lumetri": {
      "exposure": -0.30, "contrast": 28,
      "highlights": -15, "shadows": -12, "blacks": -35
    },
    "wheels": {
      "shadow_uv": [12, -6], "shadow_y": -2,
      "mid_uv": [0, 0],
      "highlight_uv": [-4, 6], "highlight_y": 1
    },
    "hsl_secondary": [
      {"range": "skin", "sat_delta": -8, "lum_delta": 4},
      {"range": "reds", "sat_delta": 6}
    ]
  },
  "per_scene": [
    {"scene": 1, "bg_glow": {"color": "#8B00FF", "intensity": 0.55}},
    {"scene": 3, "zoom": {"from": 1.00, "to": 1.05, "ease": "ease_in_out"}},
    {"scene": 4, "vignette_delta": 0.20, "exposure_delta": -0.15},
    {"scene": 5, "saturation_curve": [[0.0, 1.0], [1.0, 0.75]]},
    {"scene": 6, "bg_glow": {"color": "#8B00FF", "intensity": 0.70},
                  "glow_global": 1.2, "grain_delta": 0.05},
    {"scene": 7, "tint": {"color": "#D4AF37", "amount": 0.30}, "vignette_delta": 0.15},
    {"scene": 8, "blacks_delta": -10}
  ],
  "grain": {"overlay": "overlays/grain_8mm.mov", "opacity": 0.20, "blend": "screen"},
  "letterbox": {"top_px": 100, "bottom_px": 100, "color": "#000000"}
}
```

## Implementation notes

The Python compositor approximates Lumetri with these primitives (already in `video-pipeline/compositor/grade.py`):
- crush blacks: `clip(arr - blacks_amount, 0, 255)`
- contrast: `clip((arr - 128) * c + 128, 0, 255)`
- color wheels: per-channel multiplier banded by luma
- LUT: 3D nearest-neighbor (sufficient for grading preview); AE handoff does the real LUT application.

The real LUT files live in `video-pipeline/03-assets/luts/`. They're free for the user to swap.

## Sign-off

Output two reference stills before the full render:
- A mid-scene frame at master grade (scene 3 or 4)
- The peak frame at peak grade

User OKs the look, locked.
