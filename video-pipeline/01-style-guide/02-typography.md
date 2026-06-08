# Typography
## Fonts, Sizes, Hierarchy & Text Animations

---

## Font Stack

### Primary Headline Font — DRUK
- **Family:** Druk Wide Bold / Druk Wide Super
- **Use for:** Main statements, lyric highlights, impact words
- **Character:** Ultra-condensed, extremely heavy, all-caps dominant
- **License:** Commercial — available via Commercial Type
- **Free alternative:** Bebas Neue (tall, condensed, all-caps — close but narrower)
- **Second free alternative:** Anton (Google Fonts — good substitute)

### Secondary / Body Font — NEUE HAAS GROTESK (or similar Neo-Grotesque)
- **Family:** Neue Haas Grotesk Display Pro / Text Pro
- **Weights used:** Light (200), Regular (400), Medium (500), Bold (700)
- **Use for:** Supporting text, lower thirds, stats, captions below headlines
- **License:** Commercial — available via Linotype/Monotype
- **Free alternative:** Inter (Google Fonts), Helvetica Neue if licensed

### Accent / Tech Font — SPACE MONO or SOURCE CODE PRO
- **Family:** Space Mono (Google Fonts — free)
- **Weights used:** Regular, Bold
- **Use for:** Timestamps, coordinates, counter numbers, UI-style readouts
- **Character:** Monospaced, technical, gives a code/crypto aesthetic

### Tertiary / Caption Font — PP NEUE MONTREAL (or SATOSHI)
- **Family:** PP Neue Montreal (Pangram Pangram — free for personal)
- **Weights used:** Medium (500), SemiBold (600)
- **Use for:** Auto-captions, lyric lines, explanatory text
- **Free alternative:** Satoshi (Fontshare — free)

---

## Typography Hierarchy

```
LEVEL 1 — IMPACT HEADLINE
  Font:    Druk Wide Bold / Bebas Neue
  Size:    120-200px (at 1080px width)
  Case:    ALL CAPS
  Color:   White #FFFFFF or Electric Gold #FFB800
  Tracking: -20 to 0 (tight)
  Leading: 80-90% of point size
  Position: Center or slightly below center

LEVEL 2 — STATEMENT LINE
  Font:    Druk Wide Bold / Bebas Neue
  Size:    60-90px
  Case:    ALL CAPS
  Color:   White #FFFFFF
  Style:   Sometimes with outline/stroke only (no fill) for variety

LEVEL 3 — SUPPORTING TEXT
  Font:    Neue Haas Grotesk Bold or Inter Bold
  Size:    28-45px
  Case:    Mixed or ALL CAPS
  Color:   Light Grey #CCCCCC or White
  Tracking: +20 to +50 (slightly spaced)

LEVEL 4 — CAPTION / LYRIC
  Font:    PP Neue Montreal Medium / Satoshi Medium
  Size:    32-48px
  Case:    Sentence case or ALL CAPS
  Color:   White #FFFFFF
  BG:      Optional semi-transparent pill/box behind text

LEVEL 5 — UI READOUT / COUNTER
  Font:    Space Mono Bold
  Size:    20-30px
  Case:    All caps / numbers
  Color:   Electric Blue #00C2FF or Neon Cyan #00FFE5
  Style:   Monospaced, sometimes with blinking cursor
```

---

## Text Animation Techniques

### Technique 1: Clip Mask Reveal (most common)
The text slides upward from behind a rectangle mask that hides it initially.
```
AE Setup:
1. Create text layer
2. Create shape rectangle above the text (same size)
3. Set text as Alpha Matte for the rectangle
4. Keyframe text Position: Y starts at +80px (hidden), moves to 0 (revealed)
5. Duration: 8-12 frames
6. Easing: Ease Out (Fast start, slow finish)
```

### Technique 2: Scale Punch
Text scales from 130% → 100% on the beat hit.
```
AE Setup:
1. Keyframe Scale: 130% at frame 0, 100% at frame 6-8
2. Add Motion Blur
3. Add slight overshoot: 100% → 97% → 100% over 3 frames
4. Easing: Linear to Ease In (sharp deceleration)
```

### Technique 3: Character Stagger
Each character in the word animates separately with a slight delay.
```
AE Setup:
1. Text layer → Animate → Position (set Y offset +60px)
2. Add Selector → Range Selector
3. Keyframe Offset: from 0% to 100% over 15-20 frames
4. Enable Per-character 3D
5. Add Opacity animator: 0% to 100% with same offset
```

### Technique 4: Glitch Appear
Text glitches into existence (random horizontal displacement then snaps into place).
```
AE Setup:
1. Apply Displacement Map or Wave Warp to text layer
2. Keyframe Displacement: high value (40-80px) → 0 over 6-8 frames
3. Add CC Scatter: high → 0 over same duration
4. Optionally add a 2-frame flash of Invert effect on frame 1
```

### Technique 5: Word-by-Word Build (Lyric sync)
Each word appears sequentially on each beat or syllable.
```
AE Setup:
1. Create separate text layers for each word
2. Stagger In Point of each layer to match beat timing
3. Each uses Clip Mask Reveal (Technique 1)
4. Duration per word: 0.5-2 beats depending on lyric phrasing
5. Words exit: either hold throughout or fade out / clip out just before next line
```

---

## Text Sizing Reference (1080 × 1920 frame)

| Element | Font Size | Frames on screen |
|---|---|---|
| Main lyric / statement | 100-160px | 1-3 seconds |
| Supporting subtitle | 40-60px | 2-4 seconds |
| Lower-third name | 50-70px | 2-3 seconds |
| Caption (auto) | 38-48px | Duration of spoken word |
| UI counter / stat | 24-36px | Varies |
| Fine print / detail | 20-28px | 3+ seconds |

---

## Text Styling Rules

1. **Stroke vs Fill:** Alternate between filled text (solid white) and outline text (0 fill, 2-4px white stroke) for visual variety across a single edit. Never use both fill AND stroke on the same word.
2. **No drop shadows:** Drop shadows look cheap in this style. Use subtle glows instead (`Glow` effect at low threshold) if text needs to separate from background.
3. **Tracking:** Impact headlines get tight tracking (-20 to 0). Supporting text gets open tracking (+20 to +50).
4. **No italic:** This style uses upright text exclusively. Italics break the hard, architectural feel.
5. **Gradient text:** On very special moments only — map the signature gradient (purple → cyan → orange) to the text using a gradient overlay track matte.

---

## Caption-Specific Rules
(See also `05-caption-lyrics/caption-style-guide.md` for full detail)

- Captions are centered on-screen
- Position: vertically centered at 55-65% from top
- No caption boxes or backgrounds unless they are minimal semi-transparent pills
- Auto-captions must be restyled to match the font stack above
- Never use default CapCut/TikTok caption styling
