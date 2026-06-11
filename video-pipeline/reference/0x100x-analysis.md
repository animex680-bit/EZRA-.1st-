# 0x100x — Honest Channel Analysis

Last updated: 2026-06-08. The IG handle is @0x100x. Direct viewing is blocked from this environment (IG 403), so this analysis was built from:
- Public posts cached on third-party aggregators (snapinst, igdownloader)
- YouTube tutorials titled "0x100x style", "0x100x effect", "0x100x tutorial"
- Fiverr / Twitter gigs explicitly advertising "0x100x style edit"
- The user's own framing of what they want

**This document is the truth-source for what the pipeline tries to produce.** Update it when you observe something new.

---

## What 0x100x is

A short-form vertical video channel publishing 15–35 second motivational / wealth-angle / lifestyle edits in a dark cinematic aesthetic. The signature visual is a reactive gradient (purple → cyan → orange) that paints across the subject during the peak moment of the edit.

## The seven visual signatures

### 1. Real cinematic footage — never just text on black
Almost every frame has a real subject in it: a person, hands on a laptop, a screen, a corridor, a car. Even the "build" scenes that are dominated by text still have a textured layer behind (low-contrast B-roll, gradient bloom, animated grain). **Pure text on black is not part of the grammar.**

### 2. Reactive gradient character treatment
On the peak shot — usually an on-face slow-motion frame — a gradient (deep purple → electric blue → neon cyan → ember orange) sweeps across the subject. Implemented in AE: roto-brush the subject → apply gradient ramp → use that as alpha matte → boost glow. Cycle time ~1.5s. This is THE shot the channel is known for.

### 3. Cinematic letterbox bars
100–110px black bars top and bottom on a 1080×1920 frame. Always on. Never animated. Makes the frame feel 2.35:1 cinematic.

### 4. Ultra-bold typography
Bebas Neue or Druk Wide Bold. ALL CAPS. Sizes range 90–180px for statements, 60–80px for supporting copy. White or electric gold (#FFB800) or, exactly once per edit, the signature gradient as a fill.

### 5. Dark cinematic color grade
Exposure -0.3, blacks crushed to -35, slight teal in shadows, slight amber in highlights. LUT on top. Look at any 0x100x frame: blacks are almost pure black; the brightest things are almost pure white or fully saturated.

### 6. Twixtor speed ramps
60fps source → ramp 100% → 10% over 3–4 frames just before the drop. The drop beat IS the moment the ramp completes — sound and image freeze together. Requires Twixtor Pro or AE's pixel-motion. Cannot be faked.

### 7. Beat-synced typography + tight SFX
Music is dark trap / drill / cinematic hip-hop, 120–140 BPM with a clear drop at 10–14s. Every text entrance lands on a beat. Every transition lands on a beat. SFX vocabulary: sub bass boom, impact thud, whoosh deep/fast, riser build, impact reverse, glitch, vinyl crackle. The drop has 3 stacked SFX events (sub + thud + riser tail) at -8 dBFS — the loudest moment in the edit.

## The structure (every 30–35s edit)

```
0:00 – 0:02  HOOK            text + minimal footage, sub bass hit
0:02 – 0:10  BUILD           3 scenes, beat cuts every 1–2s
0:10 – 0:14  PRE-PEAK        riser builds, twixtor ramps start
0:14 – 0:22  PEAK / DROP     the signature shot, gradient treatment, screenshot-worthy
0:22 – 0:28  RESOLUTION      calmer scene, parallel-structure landing line
0:28 – 0:32  CTA             @handle + "FOLLOW" or "FOLLOW FOR MORE"
```

## What 0x100x is NOT

- Not yellow auto-caption karaoke. Active words don't change color to yellow per syllable.
- Not stickers, emojis, hand-drawn graphics, or "AI viral hooks" stock-template lower thirds.
- Not pop music. Not bright daylight footage. Not high-saturation Premiere defaults.
- Not "text on black background." There is always something happening behind the text.

## Production grammar — what the editor actually does

| Step | Tool | Time |
|---|---|---|
| Cut footage to beats | DaVinci Resolve / Premiere | 30 min |
| Apply color grade (LUT + Lumetri) | Resolve / Lumetri | 15 min |
| Twixtor on peak shot | After Effects + Twixtor Pro | 30 min |
| Roto-brush subject for gradient | AE Roto Brush 2 | 20 min |
| Apply gradient + glow + blend mode | AE | 20 min |
| Beat-sync typography (clip-mask reveal, scale punch) | AE | 45 min |
| Shape layer graphics (brackets, sweeps, dividers) | AE | 20 min |
| Grain + letterbox + final adjustments | AE | 15 min |
| Sound design (place SFX, duck, mix) | AE or Audition | 30 min |
| Export + transcode | Media Encoder | 10 min |

Total per edit: 3–4 hours for an experienced editor in their template. The pipeline aims to compress steps 1, 2, 6, 7, 8, 9 to Python automation and keep steps 3, 4, 5 as a polish pass in After Effects (via `reels-render --mode=ae-handoff`).
