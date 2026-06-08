# Color Palette
## Exact Colors, Grading Approach & LUTs

---

## Primary Color System

### Background Tones (darkest layer)

| Name | Hex | RGB | Usage |
|---|---|---|---|
| Pure Black | `#000000` | 0, 0, 0 | Absolute background, letterbox bars |
| Deep Void | `#0A0A0A` | 10, 10, 10 | Default background (slightly lifted black) |
| Dark Charcoal | `#141414` | 20, 20, 20 | Secondary bg, shape layer fills |
| Midnight | `#1A1A2E` | 26, 26, 46 | Background with subtle dark-blue tint |

### Text & Foreground (brightest layer)

| Name | Hex | RGB | Usage |
|---|---|---|---|
| Pure White | `#FFFFFF` | 255, 255, 255 | Primary headline text |
| Warm White | `#F5F0E8` | 245, 240, 232 | Body text, secondary labels |
| Light Grey | `#CCCCCC` | 204, 204, 204 | Supporting text, fine details |

### Accent Palette (the signature pops)

| Name | Hex | RGB | Usage |
|---|---|---|---|
| Electric Gold | `#FFB800` | 255, 184, 0 | Premium accents, highlight strokes |
| Classic Gold | `#D4AF37` | 212, 175, 55 | Luxury elements, border lines |
| Electric Blue | `#00C2FF` | 0, 194, 255 | Gradient edge, tech/crypto elements |
| Neon Cyan | `#00FFE5` | 0, 255, 229 | Reactive gradient highlight |
| Vibrant Purple | `#8B00FF` | 139, 0, 255 | Gradient anchor, shadow tones |
| Deep Magenta | `#FF00A0` | 255, 0, 160 | High-energy accent, rarely used |
| Ember Orange | `#FF6B00` | 255, 107, 0 | Warm gradient anchor |

---

## Signature Gradient — The Character Gradient

This gradient is the most recognizable visual element of the 0x100x style. It maps onto the character/subject silhouette and animates over time.

**Gradient stops (standard version):**
```
Position 0%  → #8B00FF  (Deep Purple)
Position 30% → #00C2FF  (Electric Blue)  
Position 60% → #00FFE5  (Neon Cyan)
Position 100%→ #FF6B00  (Ember Orange)
```

**Gradient stops (gold/luxury version):**
```
Position 0%  → #1A1A2E  (Midnight)
Position 40% → #D4AF37  (Classic Gold)
Position 70% → #FFB800  (Electric Gold)
Position 100%→ #FFFFFF  (White)
```

**Animation:**
- The gradient offset animates from 0% to 100% over 2-4 seconds in a loop
- Use `Gradient Ramp` effect + animated `Start Point` and `End Point` in After Effects
- Or use `CC Light Sweep` for a "sweeping glow" variation
- Angle: typically 130-145° (diagonal, bottom-left to top-right)

---

## Color Grading — The Cinematic Dark Grade

### In DaVinci Resolve

**Node structure:**
```
Node 1 — Log Correction
  Lift:    R -0.05  G -0.05  B -0.02
  Gamma:   R -0.10  G -0.10  B -0.05
  Gain:    R  1.00  G  0.98  B  0.95

Node 2 — Contrast + Crush
  Contrast:   +0.25
  Pivot:       0.40
  Shadow lift: -0.08

Node 3 — Color Balance (Teal-Orange look)
  Shadows:  push toward Teal/Blue  (+Cb tilt)
  Highlights: push toward Warm/Orange (+Y tilt)

Node 4 — Saturation
  Global saturation: 0.75 (desaturate midtones)
  Hue vs Sat: boost only Cyan and Orange

Node 5 — Vignette (subtle)
  Center vignette: -0.3 strength, soft edges
```

### In Adobe After Effects (Lumetri Color)

```
Basic Correction:
  Exposure:      -0.3
  Contrast:      +25
  Highlights:    -15
  Shadows:       -10
  Whites:        -10
  Blacks:        -30

Creative:
  Vibrance:      -15
  Saturation:    90

Curves:
  RGB:    S-curve (slight) — pull blacks down, keep highlights
  Blue:   Lift shadows slightly (adds cold tint to darks)
  Red:    Slight rolloff in highlights (cinematic)

Color Wheels:
  Shadows:   Push toward cyan/teal
  Midtones:  Neutral to very slightly warm
  Highlights: Slightly warm amber
```

---

## LUT Recommendations

Apply LUT as the final node/layer, strength at 50-70% (never 100% — always blend).

| LUT Name | Source | Feel |
|---|---|---|
| **Phantom** | AEJuice / free community | Dark, neutral, cinematic |
| **Dark Shadows** | Motion Array | Crushed blacks, cool mids |
| **Teal & Orange Cinematic** | Lutify.me / free | Classic Hollywood color separation |
| **Noir Premium** | Various | Near-monochrome with warm highlights |
| **Crypto Dark** | Custom / community | Purpose-built for this style |

**How to apply in DaVinci Resolve:**
1. Add a new serial node after your grade
2. Right-click → Add 3D LUT
3. Set node Opacity (Key Output) to 50-70%

**How to apply in After Effects:**
1. Apply `Apply Color LUT` effect to an adjustment layer above all footage
2. Set Blend Mode of the adjustment layer to **Normal** at **60% opacity**

---

## Background Texture Treatment

When using pure black backgrounds (lower thirds, text cards, graphic scenes):

- Add a subtle radial gradient from `#1A1A2E` center to `#000000` edges
- Overlay a noise texture at 5-8% opacity (adds depth, avoids flat digital look)
- Optional: animated subtle particle field at 3-5% opacity (bokeh dots moving upward)

---

## Color Don'ts

- Never use fully saturated primary colors (no pure `#FF0000` red unless extreme effect)
- Never use flat white backgrounds
- Never use yellow-green (`#ADFF2F`) — clashes with the palette
- Never use more than 3 accent colors in a single edit
- Never let skin tones go orange — the grade should preserve skin while shifting the environment
