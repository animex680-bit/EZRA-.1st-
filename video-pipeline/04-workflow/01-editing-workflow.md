# Editing Workflow
## The Step-by-Step Edit Process in After Effects

---

## Phase 0 — Project Setup (10 minutes)

```
1. Create folder structure (see 02-technical/00-project-settings.md)
2. Open After Effects → New Project
3. Comp Settings: 1080 × 1920, 24fps, 32bpc, background black
4. Import all assets:
   - All footage clips
   - Music track
   - Grain overlay file
   - SFX files
5. Transcode to proxy if not done (right-click clips → Create Proxy → Movie)
6. Save AE project to: 03_PROJECT_FILES/AE/[ProjectName]_v01.aep
```

---

## Phase 1 — Music First (20 minutes)

**Do not place any footage yet. Start with audio.**

```
1. Drag music into the composition timeline
2. Play through the entire track
3. Add beat markers (M key) at:
   - Every strong kick/beat
   - Every major transition point (chorus, drop, bridge)
   - Highlight the DROP/PEAK moment with a different color marker
4. Zoom into the timeline: CMD/CTRL + scroll to see frame-by-frame at beat points
5. Note exact frame numbers for:
   - The main DROP (the most important single frame in the edit)
   - The BUILD start
   - The RESOLUTION start
```

---

## Phase 2 — Rough Cut (30-45 minutes)

**Goal: Get all footage in the right order, roughly in time, no effects yet.**

```
1. Create pre-comp: PC_FOOTAGE
2. Place all clips in the comp in rough order matching your Edit Plan
3. Trim clips so their best moments align with your markers
4. Rough beat-sync: each cut falls within 3-4 frames of a beat marker
   (don't perfect-sync yet — just get it close)
5. Identify the Twixtor clip: place it at the DROP marker
6. At this stage: NO effects, NO text, NO color grade
7. Play back. Does the cut feel right emotionally?
   Yes → proceed to Phase 3
   No → reorder clips, try different cuts
```

**Common Rough Cut Mistakes:**
- Cutting too many clips in — less is more, especially in the BUILD phase
- Not saving the best clip for the PEAK — don't use it in the build
- Ignoring the music — if a cut feels wrong, it's probably off-beat, not the wrong clip

---

## Phase 3 — Gradient Character Treatment (45-60 minutes)

**This is the signature element — give it time.**

```
1. Select your primary subject clip (the one at or near the PEAK)
2. Apply Roto Brush 2 to isolate the subject:
   - Select the Roto Brush tool
   - Paint green strokes over the subject
   - Paint red strokes over background areas you DON'T want
   - Advance through frames, correcting propagation errors
   - Freeze once satisfied
3. Create a new Solid layer above the rotoscoped clip
4. Apply Effect → Generate → Gradient Ramp
5. Set gradient colors (see 01-style-guide/01-color-palette.md for the exact gradient)
6. Set as Alpha Matte using the rotoscoped clip below
7. Set Blend Mode: Add or Screen (experiment — both can work)
8. Add Glow effect (Threshold 55%, Radius 25px, Intensity 0.8)
9. Animate gradient Start/End Points over 2-4 seconds
10. Pre-comp these layers as: PC_GRADIENT_[subject name]
```

---

## Phase 4 — Shape Layer Graphics (30-45 minutes)

**Build the UI-style graphic overlay package.**

```
1. Create a new pre-comp: PC_GRAPHICS
2. Inside this pre-comp, build:
   
   A) Corner frames:
      - 4 thin lines (2px stroke) at each corner of the frame
      - Each corner: an L-shape, 40-80px long per arm
      - Animate: scale from 0 to full, ease out, on the first beat
      - Color: White at 80% opacity

   B) Horizontal accent lines:
      - 1-3 thin horizontal lines (1px) that appear across the frame
      - Animate: scale (width) from 0% to 100% on beat hits
      - Position: at interesting points — below text, at 1/3 height, etc.
      - Color: White at 50-70% opacity

   C) Animated bracket/box:
      - A rectangle outline (no fill, 2px stroke) that rapidly scales in
      - Scale: 110% → 100% in 4 frames (punch in)
      - Use to frame the subject or a key text element

3. Pre-comp all shapes and bring into main comp
4. Set opacity: 60-80% for subtlety
```

---

## Phase 5 — Typography (45-60 minutes)

**Add all text layers, timed to the music.**

```
For each text element (lyric line, statement, caption):

1. Create a new Text Layer
2. Font: Bebas Neue or Druk Wide Bold (see typography guide)
3. Size: 100-160px for headlines, 40-60px for supporting
4. Color: White #FFFFFF
5. Position: Center horizontally; vertically at ~55-65% from top
6. In Point: place it 3-4 frames BEFORE the beat it should resolve on
7. Apply Clip Mask Reveal animation (see 01-style-guide/02-typography.md):
   - Parent text to a rectangle mask
   - Animate text Y position: +80px → 0 over 10 frames
8. Out Point: set to either:
   - The next beat (word-by-word lyric style)
   - Or hold through to next text line appears
9. Add Motion Blur: enable on all text layers

Repeat for every text element in the edit.
```

---

## Phase 6 — Speed Ramp / Twixtor (30 minutes)

```
1. Select the Twixtor clip (identified in Phase 2)
2. Apply Twixtor Pro effect (see 02-technical/01-effects-arsenal.md for settings)
3. Keyframe the Speed parameter:
   - Build up to the moment: 100%
   - The DROP frame: snap to 10-15%
   - Hold slow: for 1-3 seconds
   - Ramp back: to 100% over 0.5-1 second
4. Add Camera Shake to the frame RIGHT AFTER the slow-mo snaps back
   (wiggle expression, 4-8 frames only)
5. Preview and adjust: does the slow-mo moment look smooth?
   - If ghosting: reduce Motion Sensitivity in Twixtor
   - If choppy: ensure source footage is 60fps+
```

---

## Phase 7 — Color Grade (30 minutes)

```
1. Create an Adjustment Layer above all footage pre-comps
   (below text, graphics, grain, and bars)
2. Apply Lumetri Color effect
3. Basic correction:
   - Exposure: -0.3
   - Contrast: +25
   - Highlights: -15
   - Shadows: -10
   - Blacks: -30
4. Creative:
   - Vibrance: -15
   - Saturation: 90
5. Color Wheels:
   - Shadows: slight teal push
   - Highlights: slight warm push
6. Apply LUT (as separate adjustment layer above):
   - Apply Color LUT effect
   - Choose LUT_DarkCinematic or LUT_Phantom
   - Set adjustment layer opacity: 60%
```

---

## Phase 8 — Overlays (15 minutes)

```
1. Import grain_8mm_overlay.mov
2. Place at TOP of layer stack (above everything)
3. Blend Mode: Overlay
4. Opacity: 20%
5. Add loop expression: loopOut("cycle")
6. Apply Cinematic Bars (built as solid layer — see effects arsenal)
7. Lock both the grain and bars layers
```

---

## Phase 9 — Sound Design (30 minutes)

```
1. Import all needed SFX files
2. Go through the timeline, placing SFX at:
   - Every major cut: impact or whoosh
   - Every text entrance: subtle impact
   - The DROP: sub bass boom + riser (placed slightly before drop)
   - The Twixtor snap-back: hard impact
   - Every shape graphic appearance: UI click (subtle)
3. Adjust each SFX volume:
   - Sub bass boom: -8dBFS
   - Impacts: -12 to -14dBFS
   - Whooshes: -14 to -16dBFS
   - UI clicks: -18 to -20dBFS
4. Check overall mix: music should always be most prominent
5. Check loudness target: -14 LUFS (see export specs)
```

---

## Phase 10 — Review & Polish (20-30 minutes)

```
1. Watch the full edit 3 times through:
   - First watch: overall flow and emotion — does it feel right?
   - Second watch: beat sync — does every cut/text land on a beat?
   - Third watch: visual details — any flickering, clipping, misalignment?

2. Fix anything that stood out
3. Run through the Review Checklist (04-workflow/02-review-checklist.md)
4. Increment the version: Save As → [ProjectName]_v02.aep
5. Export (see 02-technical/03-export-specs.md)
```

---

## Version Naming

Every time you significantly change the edit, save a new version:
```
[ProjectName]_v01.aep  ← Initial rough cut
[ProjectName]_v02.aep  ← After client feedback
[ProjectName]_v03.aep  ← Final approved
[ProjectName]_vFINAL.aep ← Do not touch this one
```

Never overwrite a previous version. Always Save As with incremented number.
