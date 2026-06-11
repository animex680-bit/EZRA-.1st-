---
name: reels-captions
description: Designs and times every caption / lyric / statement on screen — fonts, sizes, positions, animations, highlight words — synced to vo_words.json within ±1 frame. Produces captions.json consumed by the renderer. Part of the reels pipeline.
---

# reels-captions — The Words On Screen

Every word on screen is here. Wrong size, wrong position, late by 2 frames — it all reads as amateur.

## The five caption types (per `video-pipeline/05-caption-lyrics/caption-style-guide.md`)

1. **Lyric** — Bebas Neue, 90–140px, ALL CAPS, white. Most common.
2. **Statement** — Bebas Neue 120–180px, ALL CAPS, white or gold or gradient. The big landings.
3. **Supporting subtitle** — Inter Bold 32–48px, light grey. Sits below a statement.
4. **Auto-caption** — Satoshi Medium 36–44px, sentence case. For spoken-word content.
5. **Handle / CTA** — Inter SemiBold 48–70px for the @handle; Bebas Neue 80px for CTA copy.

Pick the type per line based on its role in the script.

## The eight animations

| Anim | Use it for |
|---|---|
| `clip_reveal` | Default lyric entrance — slides up from behind hidden mask |
| `scale_punch` | Statement entries — 130% → 100% in 5 frames |
| `char_stagger` | "EVERY WEBSITE / IS A MONEY MACHINE." word-by-word |
| `glitch_in` | Cyber/tech topics — 3-frame RGB-split flicker |
| `word_swap` | "NO DEGREE. / NO BOSS. / NO OFFICE." — same position, swap text |
| `fade_in` | CTA handle, supporting subtitle |
| `gradient_fill` | The signature moment (one per reel) — apply gradient as alpha matte |
| `glow_pulse` | Behind statement text — Gaussian-blurred copy at 60% opacity |

## Inputs

- `script.md`
- `text_plan.json` (from `reels-storyboard`)
- `vo_words.json` (from `reels-voice`)
- `beats.json` (from `reels-storyboard`)

## What you produce: `captions.json`

```json
{
  "comp": {"w": 1080, "h": 1920, "fps": 24, "safe": {"top": 0.14, "bot": 0.18, "side": 0.04}},
  "captions": [
    {
      "id": "HOOK_01",
      "text": "MOST PEOPLE",
      "type": "statement",
      "font": "BebasNeue",
      "size": 160,
      "color": "#FFFFFF",
      "x_frac": 0.5, "y_frac": 0.44, "anchor": "mm",
      "anim_in":  {"kind": "scale_punch", "frames": 5, "ease": "ease_out"},
      "anim_out": {"kind": "hold"},
      "in_frame": 0, "out_frame": 48,
      "glow": null,
      "matte": null
    },
    {
      "id": "HOOK_02",
      "text": "SCROLL PAST THIS.",
      "type": "statement",
      "font": "BebasNeue",
      "size": 100,
      "color": "#FFB800",
      "x_frac": 0.5, "y_frac": 0.575, "anchor": "mm",
      "anim_in":  {"kind": "clip_reveal", "frames": 8, "ease": "ease_out"},
      "in_frame": 8, "out_frame": 48
    },
    {
      "id": "PEAK_03",
      "text": "ONE CLIENT.",
      "type": "statement",
      "font": "BebasNeue", "size": 164,
      "color": "#FFB800",
      "x_frac": 0.5, "y_frac": 0.685, "anchor": "mm",
      "anim_in":  {"kind": "scale_punch", "frames": 6, "ease": "ease_out"},
      "in_frame": 348, "out_frame": 528,
      "glow":  {"color": "#FFB800", "blur": 24, "alpha": 200},
      "matte": {"kind": "gradient",
                  "stops": [[0.0, "#8B00FF"], [0.35, "#00C2FF"], [0.65, "#00FFE5"], [1.0, "#FF6B00"]],
                  "anim": {"offset_per_s": 0.28}}
    }
  ]
}
```

## Rules (the watcher enforces these — break them and the reel fails)

1. **In safe area.** Compute bbox from font metrics; verify `(y_frac*H - h/2) >= 0.14*H` and `(y_frac*H + h/2) <= 0.82*H` and similar for sides.
2. **One signature moment.** Exactly one caption may have `matte.kind == "gradient"`. Reject anything else.
3. **±1 frame of the word.** For lyric/auto-caption types, `in_frame` must equal `round(vo_words[w].s * fps)` ± 1.
4. **Max 2 lines on screen at once.** Compute overlap windows; ≥ 3 simultaneous captions = invalid.
5. **No yellow karaoke highlight.** Active word coloring on auto-captions uses subtle scale (1.06x), not color swap to yellow.
6. **No default fonts.** Reject any caption whose `font` is system-default.
7. **Highlight cadence.** Out of every 10 captions, 2–3 are highlight words (gold or scale-up). Not more — overuse kills impact.

## Highlight-word selection (auto)

For a list of captions in the same scene:
- The longest word? No.
- The dollar amount, the number, the verb that does the work? Yes.
- The last word of the parallel structure? Yes ("WEALTH." in "BUILD WEALTH.").

Mark `highlight: true` on chosen captions; the renderer applies +size or color swap.

## On-face talking head captions (auto-caption style)

For on-face scenes, every spoken word becomes its own caption entry:
- `type: "auto_caption"`, `font: "Satoshi"`, `size: 40`, `y_frac: 0.72`
- Each word lives from `s` to `s + (e-s)*1.15` (slight tail so the eye catches up)
- Active word: `+1.05x scale` for the frame range, then back to 1.0

This is the part most editors get wrong (laggy / mis-cased). Word timings come from `vo_words.json`, no guessing.

## Sign-off

Render a preview: a single PNG per major caption showing its position + scale on a black frame with the safe-area rectangle drawn. Save to `productions/NNN-slug/preview_captions/`. User OKs visual style before render.
