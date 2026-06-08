# Caption Style Guide
## Caption Appearance, Animation & Rules

---

## Caption Philosophy

In the 0x100x style, captions are not utilitarian subtitles slapped on a video. They are a **visual design element** that happens to also communicate words. The appearance of the text is as important as the words themselves.

**Key principle:** Every caption should feel like it belongs in the frame — like it was designed as part of the scene, not added afterward.

---

## Caption Types

### Type 1: Lyric Caption (most common)
Used to display song lyrics synced to the music.

**Appearance:**
```
Font:       Bebas Neue / Druk Wide Bold
Size:       90-140px (fills roughly 40-60% of frame width)
Case:       ALL CAPS
Color:      White #FFFFFF
Weight:     Heaviest available
Tracking:   -10 to 0 (tight)
Position:   Horizontally centered
            Vertically: 50-65% from top (middle-lower area)
Shadow:     None
Outline:    None (clean fill only)
Background: None (no box behind text)
```

**Animation:** Clip Mask Reveal (slides up from below a hidden mask)
- In: 8-10 frames, Ease Out
- Hold: duration of the lyric phrase
- Out: either hold until next line OR quick upward exit (4-6 frames)

---

### Type 2: Statement / Quote Caption
Used for motivational text, key phrases, non-lyric statements.

**Appearance:**
```
Font:       Bebas Neue / Druk Wide Bold
Size:       120-180px (very large — this IS the visual)
Case:       ALL CAPS
Color:      White #FFFFFF
            OR Electric Gold #FFB800 for special emphasis
            OR Gradient (purple → cyan) for peak moments only
Weight:     Heaviest available
Tracking:   -20 to -10 (very tight for condensed look)
Position:   Center of frame, can be 40-60% vertically
Lines:      Maximum 2 lines for a single statement
            If more needed, break into separate timed captions
```

**Animation:** Scale Punch
- Scale: 120% → 100% in 5 frames, Ease Out
- Optionally: Character Stagger (each word enters separately, 3-frame delay)

---

### Type 3: Supporting Subtitle
Used below a headline for secondary information (name, date, stat).

**Appearance:**
```
Font:       Inter Bold / Neue Haas Grotesk Bold
Size:       32-48px
Case:       ALL CAPS or Mixed case
Color:      Light Grey #CCCCCC or White
Weight:     Bold
Tracking:   +20 to +40 (open/spaced)
Position:   Directly below the Type 1/2 caption, 10-20px gap
```

**Animation:** Fade in (Opacity 0 → 100% over 8 frames) OR same Clip Mask Reveal as parent

---

### Type 4: Auto-Caption (spoken word sync)
Used when the video includes speech (voiceover, talking head, podcast clip).

**Appearance:**
```
Font:       PP Neue Montreal Medium / Satoshi Medium
Size:       36-44px
Case:       Sentence case (capitalize first word only)
Color:      White #FFFFFF
Weight:     Medium (500)
Max width:  80% of frame width
Alignment:  Center
Position:   65-75% vertically from top (lower third area)
```

**Animation:** Word-by-word appear (each word pops in as spoken)
- In: Clip Mask Reveal, 4-5 frames per word
- Active word: can be slightly bolder / different color briefly
- Out: entire line fades when next line appears

**Background option (if readability is poor):**
```
Shape behind text:
  Type: Rounded Rectangle pill
  Color: Black at 50% opacity
  Padding: 12px horizontal, 6px vertical
  Border Radius: 8px
  Blur: Gaussian blur 4px behind (frosted glass look)
```

---

### Type 5: Account Handle / CTA
The closing text — usually the last thing on screen.

**Appearance:**
```
Font:       Inter SemiBold or Bebas Neue
Size:       48-70px (@handle) or 60-90px (CTA text)
Case:       @handle = lowercase; CTA = ALL CAPS
Color:      White or Electric Gold
Position:   Bottom center, above cinematic bar, 15-20px clearance
            OR center of frame if full-screen CTA moment
```

**Animation:**
- Fade in from below (Opacity + Y position)
- Or simple Opacity fade: 0% → 100% over 12-16 frames
- Holds for 2-5 seconds
- Exit: either hold to end or fade out

---

## Caption Rules — Absolute

1. **Never use the default caption styling** from CapCut, TikTok, or Premiere's auto-captions — always restyle to match the above
2. **No yellow highlights** on active words — the 0x100x style does not use the "word karaoke" look
3. **No caption boxes** except for auto-captions (Type 4) when background is complex
4. **Max 2 lines on screen at once** — if a lyric is longer, break it into two timed segments
5. **No italic text** — ever
6. **No mixed fonts in a single caption** — one font per caption layer
7. **Text must not touch the cinematic bars** — maintain at least 20px clearance
8. **Test readability at phone size** — if text is unreadable at 375px wide, it's too small

---

## Caption Sizing Comparison

At 1080px wide × 1920px tall frame:

| Caption Type | Font Size | Lines visible | Impact level |
|---|---|---|---|
| STATEMENT (full-frame) | 160-200px | 1 | Maximum |
| LYRIC (standard) | 90-140px | 1-2 | High |
| SUBTITLE (supporting) | 32-48px | 1 | Medium |
| AUTO-CAPTION (spoken) | 36-44px | 2-3 | Low |
| HANDLE/CTA | 48-70px | 1 | Medium |

---

## Gradient Text (Special Occasions Only)

Reserve gradient text for the single most impactful moment in the edit — one use per video maximum.

**How to apply gradient to text in AE:**
```
1. Create text layer
2. Duplicate it
3. Top copy: Blend Mode = Normal (this is the gradient version)
4. Create a Gradient Solid above the text
5. Set gradient solid as Alpha Matte for the text using the BOTTOM text copy
6. The gradient will now show only through the text shapes
```

**Gradient:** Use the signature gradient from `01-style-guide/01-color-palette.md`
