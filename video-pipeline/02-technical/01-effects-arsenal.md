# Effects Arsenal
## Every Effect Used in This Style — With Settings

---

## Core Effects Stack

These effects are used in virtually every single edit. Consider them mandatory.

---

### 1. Cinematic Letterbox Bars

**What it does:** Black bars at top and bottom. Always on. Instantly cinematic.

**How to build in AE:**
```
1. Create a new Solid layer (Cmd/Ctrl + Y): Black, full comp size
2. With the Solid selected, use the Rectangle Mask tool
3. Draw a mask covering the MIDDLE portion of the frame
   — Leave ~9-10% exposed at top, ~9-10% at bottom
4. Set Mask Mode: Subtract
5. Lock this layer — it should NEVER move
6. Name it: "CINEMATIC BARS — DO NOT TOUCH"
7. Place it at the very top of the layer stack
```

**Settings reference:**
- Bar height: ~100-115px at 1080×1920 (about 5.7-6% per side)
- Softness: 0px (hard edges — no feathering)
- Color: Pure Black `#000000`

---

### 2. Film Grain Overlay

**What it does:** Adds organic texture that prevents the flat digital look.

**Option A — Use a grain footage file:**
```
1. Import a grain/noise .mov file (8mm or 16mm film grain recommended)
2. Place it above your footage pre-comp
3. Set Blend Mode: Overlay or Soft Light
4. Opacity: 15-25%
5. Scale to fill frame if needed
6. Loop it (Layer → Time → Enable Time Remapping, then loop expression)
```

**Loop expression for grain:**
```javascript
loopOut("cycle")
```

**Option B — Generate with AE:**
```
1. Create a new Solid layer (White, full size)
2. Effect → Noise & Grain → Add Grain
3. Settings:
   Intensity: 0.5 – 0.8
   Size: 1.0 – 1.5
   Softness: 0.3
   Color: Monochromatic checked
4. Set Blend Mode: Overlay
5. Opacity: 20-30%
```

---

### 3. Reactive Gradient Character Treatment

**What it does:** Maps an animated gradient onto the subject's silhouette, making them look like a glowing entity.

**Setup (AE):**
```
Step 1 — Isolate the subject
  Method A: Use Roto Brush 2 (best for moving subjects)
  Method B: Use Subject Select (Premiere Beta / AE Beta)
  Method C: Manual roto with Mask Path (for still or slow-moving subjects)

Step 2 — Create the gradient layer
  1. Create a Solid (any color, full size)
  2. Apply Effect → Generate → Gradient Ramp
  3. Settings:
     Start Color: #8B00FF (Deep Purple)
     End Color:   #00C2FF (Electric Blue)
     Start Point: bottom-left of frame (animate this)
     End Point:   top-right of frame (animate this)
     Ramp Shape:  Linear

Step 3 — Add animation to the gradient
  1. Keyframe Start Point: moves across frame over 2-4 seconds
  2. Add a second Gradient Ramp with different colors on a separate solid
  3. Blend them with Screen or Add mode at 50% opacity

Step 4 — Apply subject as alpha matte
  1. Place gradient solid ABOVE the subject footage
  2. Set Alpha Matte (TrkMat) to the subject footage below
  3. This maps the gradient only where the subject exists

Step 5 — Add glow
  1. Apply Effect → Stylize → Glow to the gradient layer
  2. Glow Threshold: 50-60%
  3. Glow Radius: 20-40px
  4. Glow Intensity: 0.5-1.0
  5. Glow Colors: A & B colors (pick from palette)
```

**Color Cycle Animation (advanced):**
```
On the Gradient Ramp → Start Color expression:
  offset = time * 60; // degrees per second
  hue = (offset % 360);
  // Use wiggle + manual keyframes for organic feel
```

---

### 4. Camera Shake

**What it does:** Adds an impact "punch" feeling on beats.

**Setup (AE):**
```
Method A — Position Expression:
  1. Select the footage/pre-comp layer
  2. Press P for Position
  3. Alt/Option + click stopwatch → add expression:

  freq = 8;  // shake frequency
  amp = 10;  // shake intensity (pixels)
  t = time;  // current time
  decay = 0.5;  // how fast it dies out
  x = amp * Math.sin(freq * 2 * Math.PI * t) * Math.exp(-decay * t);
  y = amp * Math.sin(freq * 2.3 * Math.PI * t) * Math.exp(-decay * t);
  [value[0] + x, value[1] + y]

Method B — Wiggle expression (simpler):
  wiggle(15, 8)  // (frequency, amplitude)
  Use Enable/Disable via expressions or keyframes

Method C — CC Force Motion Blur + Wiggle:
  1. Apply CC Force Motion Blur to layer
  2. Add wiggle expression to position
  3. Higher motion blur = more violent shake feel
```

---

### 5. Speed Ramp (Twixtor Pro)

**Setup in After Effects:**
```
1. Apply Twixtor Pro to your footage layer
2. In Twixtor controls:
   - Speed: This is your ramp value (100% = normal, 8% = very slow)
   - Frame Interp: Motion-Compensated (best quality)
   - Motion Sensitivity: 0.3-1.0 (start at 0.5)
   - Smart Blend: ON
3. Keyframe the Speed parameter:
   Frame 0:   100% (normal)
   Frame 12:  100% (still normal, building anticipation)
   Frame 15:  10%  (SNAP to slow — the drop)
   Frame 80:  10%  (hold slow)
   Frame 100: 100% (ramp back to normal)
4. Use Ease Out easing on the drop keyframe
5. Use Ease In easing on the ramp-back keyframe
```

---

### 6. Glitch Effect

**What it does:** Visual digital distortion — RGB channel separation, horizontal slice displacement.

**Setup (AE):**
```
Method A — Channel Shift:
  1. Duplicate your footage 3 times (R, G, B copies)
  2. Each copy: Effect → Channel → Shift Channels
     Red copy:   Shift R channel +5px right, set Blend Mode Screen
     Green copy: No shift, set Blend Mode Screen  
     Blue copy:  Shift R channel -5px left, set Blend Mode Screen
  3. Animate the shift amounts: 0 → 10-30px → 0 over 4-6 frames

Method B — Displacement Map:
  1. Create a white solid with Noise effect (Add Noise, 40%)
  2. Apply Displacement Map effect to footage
  3. Source: the noise solid (above)
  4. Max Horizontal Displacement: 20-60px
  5. Max Vertical Displacement: 5px
  6. Keyframe displacement values: spike on beat → back to 0 in 3-4 frames

Method C — Bad TV / AEJuice plugin:
  If you have AEJuice Pack Manager installed, use their Glitch presets
  Adjust intensity, duration, and timing to match beats
```

---

### 7. Chromatic Aberration

**What it does:** Subtle or extreme color fringing that feels analog/cinematic.

**Setup (AE):**
```
1. Duplicate footage layer twice
2. Top copy: Effect → Channel → Shift Channels
   Set "Get Red from" to Red, everything else Alpha Off
   Move this layer +3-8px right
   Blend Mode: Screen
3. Middle copy: Original (no shift)
4. Bottom copy: Effect → Channel → Shift Channels  
   Set "Get Blue from" to Blue, everything else Alpha Off
   Move this layer -3-8px left
   Blend Mode: Screen
5. Pre-comp all three → easier to manage
6. Animate the shift amounts for a "pulse" on beats
```

---

### 8. Light Leaks / Flares

**What it does:** Organic light burst that sells the high-production feel.

**Setup (AE):**
```
Option A — Footage overlay:
  1. Import a light leak .mov file (many free ones available)
  2. Place above footage
  3. Blend Mode: Screen or Add
  4. Opacity: 20-50%
  5. Time the flash to a beat hit

Option B — Generate with Optical Flares (plugin):
  Effect → Video Copilot → Optical Flares
  Preset: Studio → choose a subtle lens flare
  Brightness keyframe: 0 → 100 → 0 over 8-12 frames on beat
  
Option C — Lens Flare (built-in, less premium):
  Effect → Generate → Lens Flare
  Brightness: 60-80%
  Lens Type: 50-300mm Zoom
  Animate source position across frame
```

---

### 9. Vignette

**What it does:** Darkens the edges, focuses the viewer's eye to center.

**Setup (AE):**
```
1. Create a new Solid layer (Black, full size)
2. Apply Ellipse Mask:
   - Draw an oval covering ~70% of frame
   - Feather: 200-400px (very soft)
   - Mask Mode: Subtract
3. Layer Opacity: 40-60%
4. Place above footage but below grain/grade layers
```

---

### 10. Glow (text and subject)

**What it does:** Premium luminous feel on text and gradient elements.

**Setup (AE)for text:**
```
1. Select text layer
2. Effect → Stylize → Glow
3. Settings:
   Glow Threshold:  50-70%
   Glow Radius:     15-30px
   Glow Intensity:  0.5-1.2
   Glow Operation:  Add
   Glow Colors:     Original colors (preserves text color)
4. For a colored glow: set Colors to "A & B Colors"
   Color A: match text color
   Color B: Electric Blue #00C2FF or Gold #FFB800
```

---

## Effect Order Checklist (per clip)

Apply effects in this order within each footage layer:
```
1. Warp Stabilizer (if footage is shaky)
2. Twixtor Pro (if speed ramping)
3. Lumetri Color (base grade — exposure, contrast)
4. Hue/Saturation (selective desaturation)
5. Chromatic Aberration (if using)
6. Glow (if subject needs it)
```

Adjustment layers (on top of everything, in order):
```
1. Lumetri Color (final creative grade + LUT)
2. Grain overlay solid/footage
3. Vignette solid
4. Cinematic bars solid
```
