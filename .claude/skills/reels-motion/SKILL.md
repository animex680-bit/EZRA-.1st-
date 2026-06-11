---
name: reels-motion
description: Motion graphics spec — shape graphics (corner brackets, sweep lines, dividers), Twixtor speed ramps, camera shake, transitions, and signature reactive-gradient character treatment. Outputs motion.json. Part of the reels pipeline.
---

# reels-motion — Motion Graphics

The graphics that aren't captions: brackets, sweeps, dividers, ramps, shakes, transitions, the signature gradient sweep on the subject.

## The arsenal (per scene)

- **Cinematic letterbox bars** — 100–110px top/bottom, always on. Not a motion element, a constant.
- **Film grain overlay** — 15–25% opacity, animated noise tile. Not a motion element, a constant.
- **Thin divider line** — 1px white at 60% opacity, animates width 0→100% under hook text on the beat.
- **Corner brackets (L-shapes)** — 60–80px arms, 2px stroke, scale in 0→100% over 6 frames. Used on "EVERY WEBSITE / IS A MONEY MACHINE." style cards.
- **Sweep lines** — 3 thin horizontal lines (1px each, 70–80px apart), staggered left→right wipe across the drop. Used at PEAK only.
- **Twixtor speed ramp** — 100% → 10% over 4 frames, lands on the drop beat. Requires 60fps source.
- **Camera shake** — wiggle expression, 6–10px amplitude, 8 frames at the drop only.
- **Reactive gradient character treatment** — this is the 0x100x signature on on-face peaks: roto-brush the subject, apply the purple→cyan→orange gradient as a fill, glow at 1.2, blend mode = Add at 30%. Animated sweep, 1.5s full cycle.

## Transitions

| Transition | When | How |
|---|---|---|
| Hard cut (default) | 80% of cuts | beat-aligned, no transition effect |
| Shape wipe | scene 2→3 | a black bar slides across covering the cut |
| Zoom push | hook→build | scale up 1.0→1.08 in 4 frames, hard cut, scale back |
| Glitch cut | tech/cyber topics | 2-frame RGB-split + horizontal slice |
| Motion blur swipe | high-energy scenes | horizontal motion blur + slide direction-matched |
| Color flash | the drop | 1-frame white flash, then return |
| Slow-mo into cut | pre-peak → peak | last 8 frames of pre-peak slow to 10%, then hard cut to slow-mo peak |

Mark the transition in `motion.json` per scene boundary.

## What you produce: `motion.json`

```json
{
  "shape_layers": [
    {"scene": 1, "kind": "divider",
      "y_frac": 0.505, "in_frame": 6, "frames": 8, "ease": "ease_out",
      "color": "#FFFFFF", "alpha": 0.55, "weight": 1},

    {"scene": 3, "kind": "corner_brackets",
      "in_frame": 108, "frames": 6, "ease": "ease_out",
      "color": "#FFFFFF", "alpha": 0.72, "arm_px": 80, "weight": 2,
      "margin_px": 105},

    {"scene": 6, "kind": "sweeps",
      "in_frame": 336, "stagger_frames": 3, "frames_per_line": 14,
      "y_center_frac": 0.30, "spacing_px": 80, "lines": 3,
      "color": "#FFFFFF", "alpha": 0.40}
  ],

  "speed_ramps": [
    {"scene": 5, "kind": "twixtor",
      "in_frame": 264, "ramp_frames": 4, "from_pct": 100, "to_pct": 10,
      "source_fps": 60, "ae_handoff": true}
  ],

  "camera_shake": [
    {"scene": 6, "in_frame": 336, "duration_frames": 8,
      "amp_px": 8, "freq_hz": 24}
  ],

  "subject_gradient": [
    {"scene": 6, "in_frame": 336, "duration_frames": 192,
      "stops": [[0.0,"#8B00FF"],[0.35,"#00C2FF"],[0.65,"#00FFE5"],[1.0,"#FF6B00"]],
      "blend_mode": "Add", "alpha": 0.30, "glow_intensity": 1.2,
      "cycle_seconds": 1.5,
      "matte": "roto_subject",
      "ae_handoff": true}
  ],

  "transitions": [
    {"from_scene": 5, "to_scene": 6, "kind": "slow_mo_into_cut"},
    {"from_scene": 7, "to_scene": 8, "kind": "color_flash", "color": "#000000"}
  ]
}
```

## What lives in Python vs After Effects

- **Python (reels-render)** handles: dividers, corner brackets, sweep lines, simple camera shake, hard cuts, color flash. These are deterministic + cheap.
- **After Effects handoff (reels-render --mode=ae)** is required for: Twixtor speed ramps, reactive gradient character treatment, motion blur swipes. These need real interpolation engines.

Anything marked `"ae_handoff": true` in `motion.json` is exported to the .jsx AE project; the python render uses a placeholder (e.g. a freeze frame for Twixtor) so the rough cut still plays end-to-end.

## Sign-off

Render two preview GIFs (3–4s each) of:
- The signature moment area in the python rough
- An AE-handoff manifest showing what the user will need to bake locally

User OKs before the full render.
