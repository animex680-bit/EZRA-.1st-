# Overlays Library
## Grain, Flares, Cinematic Bars, VHS, Light Leaks & More

---

## Overlay Usage Rules

1. All overlays sit ABOVE the footage but BELOW the text and shape graphics
2. Exception: grain sits at the very TOP (above everything, including text)
3. Never stack more than 3 overlay types at once
4. Less is more — start at low opacity and increase if needed
5. Every overlay file should be loopable (use the loop expression)

**Loop expression for overlay footage layers (AE):**
```javascript
loopOut("cycle")
```

---

## Category 1 — Film Grain

Film grain is always on. No exceptions.

### Primary: 8mm Film Grain
- **Appearance:** Fine organic grain, resembles shot-on-film texture
- **Blend Mode:** Overlay or Soft Light
- **Opacity:** 15-25%
- **Source:** ActionVFX (free tier) — actionvfx.com
- **Alternative:** FilmConvert Nitrate (plugin) — generates grain procedurally
- **File name when acquired:** `grain_8mm_overlay.mov`

### Secondary: 16mm Film Grain
- **Appearance:** Slightly coarser grain — use on grittier, more intense moments
- **Blend Mode:** Overlay
- **Opacity:** 10-20%
- **Source:** ActionVFX or free from Rocketstock (rocketstock.com/free)
- **File name:** `grain_16mm_overlay.mov`

### Generated Grain (in AE — no file needed)
- **How to build:** White Solid → Effect: Add Grain → Blend Mode: Overlay, Opacity 20%
- **Settings:** Intensity 0.6, Size 1.2, Softness 0.3, Monochromatic: ON
- **Use when:** No overlay file available, need something fast

---

## Category 2 — Cinematic Bars

Always on. Built directly in AE (no separate file needed).
See `02-technical/01-effects-arsenal.md` for full build instructions.

- **Height per bar:** ~100-115px at 1920px height (~5.7-6%)
- **Color:** Pure Black #000000
- **Softness:** 0 (hard edges)
- **Layer name:** `CINEMATIC BARS — DO NOT TOUCH`

---

## Category 3 — Light Leaks

Used at transitions and peak moments for high-production organic warmth.

### Warm Lens Leak
- **Appearance:** Golden/amber light flare sweeping across frame
- **Blend Mode:** Screen
- **Opacity:** 30-50%
- **Duration:** 0.5-1.5 seconds (triggered on beats)
- **Source:** Rocketstock (rocketstock.com/free-light-leaks) or Detonation Films
- **File name:** `lightleak_warm_01.mov`, `lightleak_warm_02.mov`

### Cool Blue Flash
- **Appearance:** Quick blue/white light pulse
- **Blend Mode:** Add or Screen
- **Opacity:** 20-40%
- **Duration:** 0.3-0.8 seconds
- **Use:** High-energy moments, crypto/tech aesthetic hits
- **File name:** `lightleak_cool_blue.mov`

---

## Category 4 — Bokeh / Particle Backgrounds

Used as background texture when the subject is isolated or as atmospheric overlay.

### Bokeh Circles
- **Appearance:** Soft out-of-focus light circles drifting upward
- **Blend Mode:** Add or Screen
- **Opacity:** 10-20%
- **Motion:** Gentle upward drift
- **Source:** Pexels (free), or generate in AE with Particular plugin
- **File name:** `bokeh_particles_dark.mov`

### Dust Particles
- **Appearance:** Fine dust motes floating slowly
- **Blend Mode:** Screen
- **Opacity:** 5-15%
- **Source:** ActionVFX free tier, Mixkit
- **File name:** `dust_particles_dark.mov`

### Generated Particles (AE Particular plugin)
```
Emitter Type:   Point
Particles/sec:  30-50
Velocity:       50 (upward Y direction)
Particle Size:  3-8px
Opacity:        Random, 20-60% per particle
Color:          White or accent color at low saturation
Physics:        Air Resistance: 0.2, Wind: subtle random
```

---

## Category 5 — Glitch Textures

Used for glitch effect moments and transitions.

### Digital Glitch Overlay
- **Appearance:** Horizontal scan lines, digital noise bursts
- **Blend Mode:** Screen or Overlay
- **Opacity:** 40-80% (higher than other overlays — it's intentional)
- **Duration:** Very short — 6-15 frames per use
- **Source:** Motion Array, AEJuice Glitch Pack, or generate in AE
- **File name:** `glitch_digital_01.mov`

### VHS Noise
- **Appearance:** VHS-style noise lines, slight tracking error
- **Blend Mode:** Screen
- **Opacity:** 15-30%
- **Use:** Retro-premium moments, nostalgic sections
- **File name:** `vhs_noise_overlay.mov`

---

## Category 6 — Atmospheric Backgrounds (full scene backgrounds)

Used when building graphic/lyric cards that need a background beyond pure black.

### Subtle Noise Texture
- **Appearance:** Very fine noise pattern on near-black background
- **Use:** Behind text-only scenes to prevent "flat digital" look
- **How to make:** Solid (dark grey) + Effect: Fractal Noise → Scale: 400, Contrast: 0.4, Opacity: 8%

### Animated Gradient Background
- **Appearance:** Slowly shifting gradient (e.g., dark purple to deep black)
- **How to make:** Two solids (dark purple #1A1A2E and near-black #0A0A0A) → blended with feathered mask that animates position slowly

---

## Storage and File Format

All overlay files should be:
- **Format:** .MOV (ProRes 4444 Alpha or standard ProRes 422) for maximum quality
- **Resolution:** 1080 × 1920 or larger
- **Frame rate:** 24fps or 30fps (match to project)
- **Loopable:** Yes — seamlessly loopable for any duration

**Physical storage location in repo:**
```
03-assets/overlays/files/
  ├── grain_8mm_overlay.mov
  ├── grain_16mm_overlay.mov
  ├── lightleak_warm_01.mov
  ├── lightleak_warm_02.mov
  ├── lightleak_cool_blue.mov
  ├── bokeh_particles_dark.mov
  ├── dust_particles_dark.mov
  ├── glitch_digital_01.mov
  └── vhs_noise_overlay.mov
```
