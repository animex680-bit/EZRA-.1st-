# Transitions
## Transition Types, When to Use Each & How to Build Them

---

## The Rule Before Anything Else

**The default transition is a hard cut.** Every transition listed below is used purposefully — not as decoration. When in doubt, hard cut on the beat.

---

## Transition #1 — Hard Cut on Beat (DEFAULT)

**When to use:** 90% of cuts in this style. Maximum impact. No fluff.

**How:** Simply place the edit point exactly on the beat. No cross-dissolve, no fade, nothing. The snap is the effect.

**Enhanced version:** Add a single white or black flash frame (1-2 frames) at the edit point:
```
1. At the cut point, insert a 1-2 frame white solid layer
2. Blend Mode: Normal
3. Opacity: 100% for 1 frame, 60% for the 2nd frame (ramp down)
4. Align to the first frame of the incoming clip
```

---

## Transition #2 — Shape Layer Wipe

**When to use:** At major scene changes, verse-to-chorus transitions, or when switching subjects.

**How to build (AE):**
```
1. Create a new Shape Layer
2. Add a Rectangle shape, full width, zero height
3. Keyframe the Rectangle height:
   Frame 0:   H = 0px (invisible)
   Frame 8:   H = 1920px (covers entire frame)
   Frame 12:  H = 1920px (holds one moment)
   Frame 20:  H = 0px (wipes off revealing new clip)
4. Position: Start from bottom (Y position keyframed upward)
   OR: Start from center (scale from Y = 50% to full)
5. Fill Color: Pure Black #000000 or match accent color
6. Easing: Ease In on the wipe-on, Ease Out on the wipe-off
7. Place this layer in a new pre-comp — it's reusable
```

**Variation — Vertical slit wipe:**
```
Same as above but use multiple thin rectangles:
  3-5 rectangles, each ~20-30% wide
  Stagger their timing by 2-3 frames each
  Creates a "Venetian blind" wipe effect
```

---

## Transition #3 — Zoom Push

**When to use:** High-energy moments, entering the DROP/PEAK phase, or when the music gets louder.

**How to build (AE):**
```
Clip A (outgoing):
  Scale keyframes: 100% → 140% over 8-10 frames
  Opacity: 100% → 0% over last 4 frames
  Easing: Ease In (accelerating zoom)

Clip B (incoming):
  Scale keyframes: 120% → 100% over 8-10 frames
  Opacity: 0% → 100% over first 4 frames
  Easing: Ease Out (decelerating into position)

Overlap: Clips overlap by 6-8 frames at the transition point
```

**Tip:** Add Camera Shake (wiggle 20, 15) to the outgoing clip's last 4 frames for extra impact.

---

## Transition #4 — Glitch Cut

**When to use:** At moments of tension, drama, or as a stylistic punctuation on an important word.

**How to build (AE):**
```
1. At the cut point, insert 4-6 frames of "glitch overlap"
2. During these frames, apply to the outgoing clip:
   - Displacement Map: high horizontal value (50-80px), random noise source
   - CC Jitter: X = 15-25px, Y = 0px
   - Optionally duplicate 2x with slight RGB shift (see Glitch Effect in effects guide)
3. Frame 3-4: hard cut to incoming clip
4. Add a 2-frame flash between them
5. Pair with a "cut" sound effect or glitch audio hit
```

---

## Transition #5 — Motion Blur Swipe

**When to use:** Between clips of the same subject, smooth emotional transitions, not at peak energy.

**How to build (AE):**
```
1. Pre-comp the outgoing clip
2. On the pre-comp layer: keyframe Position, sliding the pre-comp off-screen
   in 10-15 frames (to the left, right, up, or down)
   Easing: Ease In
3. Apply Motion Blur (Enable Layer Motion Blur + Enable Composition Motion Blur)
4. The incoming clip slides in from the opposite direction simultaneously
5. Overlap by 5-8 frames
```

---

## Transition #6 — Color Flash

**When to use:** Bass drop, music peak, high-energy beat hit.

**How to build (AE):**
```
1. Create a Solid layer in the accent color (White, Gold, or Electric Blue)
2. At the beat hit point:
   Opacity keyframes: 0% → 100% → 0%
   Over: 2 frames up, 2 frames hold, 3 frames down (total 7 frames)
3. Blend Mode: Add (for a light flash) or Normal (for a color flash)
4. Apply to top of layer stack, same layer as the cut point
5. Pair with a "boom" or "sub hit" SFX
```

---

## Transition #7 — Slow-Mo Into Cut (Twixtor Bridge)

**When to use:** The signature 0x100x transition. Slow-mo on outgoing clip, then hard cut to next full-speed clip.

**How to build:**
```
1. Outgoing clip: Apply Twixtor, speed ramps from 100% → 8% over the last 1-2 seconds
2. The slow-mo hold: 1-3 seconds of ultra-slow footage (the peak moment)
3. At the beat hit: hard cut (no overlap, no fade) to incoming clip at 100% speed
4. The contrast between slow → sudden full speed IS the transition
5. Optional: add a 1-frame white flash at the hard cut point
```

---

## Transition Don'ts

| Transition | Why NOT to use |
|---|---|
| Cross dissolve | Too soft, too "wedding video", kills energy |
| Dip to black | Signals end of video — only use at true end |
| Star wipe / clock wipe | Never, under any circumstances |
| Slide transition (generic) | Without motion blur, looks like a PowerPoint |
| Morph cut (Premiere) | Looks AI-glitchy in a bad way |
| Long fades (>10 frames) | Kills momentum unless very intentionally slow |

---

## Transition Timing Reference

| Transition | Total duration | Placement |
|---|---|---|
| Hard Cut | 0 frames | Exactly on beat |
| Flash frame | 1-3 frames | On beat |
| Shape wipe | 16-24 frames | Starts 2 frames before beat |
| Zoom push | 12-18 frames | Starts 4 frames before beat |
| Glitch cut | 6-10 frames | On beat |
| Color flash | 7 frames | On beat |
| Slow-mo into cut | Variable | Cut lands on beat |
