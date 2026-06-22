# Stream A — THE VOID
## Fine Art / Sculptural / Editorial

> "The mask does not hide the face. The mask IS the face."

---

## 1. Identity

THE VOID is the soul stream. It draws from fine art, high-fashion editorial, contemporary sculpture, and museum-quality visual culture. It is not commercial. It is not friendly. It is **witnessed**.

The reference images that define this stream:
- Mannequin heads bathed in soft pastel light — skin-tone resin, smooth, inhuman but intimate
- Chrome face masks reflecting the entire world in their surface — the observer becomes the observed
- Contemporary painting with raw textural brushwork — gestural, abstract, emotionally charged
- Sculptural objects in dramatic chiaroscuro — single light source, deep shadow, form as protagonist
- High-contrast editorial photography — subjects as objects, objects as subjects

**The feeling**: You walked into an empty gallery after closing. Everything is still. Everything is precise. The work looks back at you.

---

## 2. Color System

### Primary Palette
```json
{
  "void_black":   { "hex": "#0D0D0F", "use": "Primary background — near-black with subtle warmth" },
  "warm_dark":    { "hex": "#1A1612", "use": "Elevated surface — warm dark brown undertone" },
  "charcoal":     { "hex": "#2C2820", "use": "Border, divider, secondary surface" },
  "bone":         { "hex": "#EDE8E0", "use": "Primary light tone — warm off-white, never pure white" },
  "porcelain":    { "hex": "#F5F2ED", "use": "Maximum light — used sparingly for key highlights" }
}
```

### Sculptural Accent Palette
```json
{
  "dusty_rose":   { "hex": "#C4A89A", "use": "Skin warmth, intimacy, the human element" },
  "ash_lavender": { "hex": "#9E97B0", "use": "Ethereal, dream-like distance" },
  "chrome_silver":{ "hex": "#B2BFC9", "use": "Metallic reflection, precision, the mask" },
  "teal_shadow":  { "hex": "#1D4E52", "use": "Deep shadow with color — prevents dead blacks" },
  "muted_gold":   { "hex": "#A8924A", "use": "Subtle luxury accent — used in tiny quantities" },
  "terracotta":   { "hex": "#8E5840", "use": "Raw material energy, clay, earth" }
}
```

### Color Usage Rules
- Background is always dark. Light mode does not exist in Stream A.
- Maximum 3 colors in any single composition (not counting neutrals).
- The dominant accent color should cover no more than 15% of total frame area.
- Gradients: only 2-stop, low contrast, often just a tonal shift within one hue family.
- Chrome/metallic should appear as highlight, not fill.

---

## 3. Typography

### Font Stack
```
DISPLAY (Hero, titles):   Cormorant Garamond, Didot, Freight Display, Playfair Display
SUBHEADING:               Helvetica Neue Light, Neue Haas Grotesk, GT America Light
BODY (if needed):         Helvetica Neue UltraLight, Optima, Garamond Regular
ACCENT (labels, dates):   Helvetica Neue, Inter — ALL CAPS, wide tracking
```

### Type Rules
- Headlines: Cormorant or Didot — **LARGE**. 80pt minimum for hero type. 120–200pt for editorial.
- Tracking on headlines: +60 to +120 (0.06em to 0.12em)
- Tracking on all-caps labels: +200 minimum (0.2em)
- Never bold a serif headline. Weight comes from size, not stroke.
- Never center-align body copy. Left-align always.
- Mixed case for headlines — NOT ALL CAPS (except labels).
- Color: Bone white on dark, or charcoal on light surfaces. No colored type.
- One typeface for brand moments. Two at absolute maximum.

### Example Type Hierarchy
```
DISPLAY:  140pt Cormorant Garamond Italic, #EDE8E0, tracking: +80
SUBTITLE: 28pt Helvetica Neue Light, #C4A89A, tracking: +40
BODY:     16pt Helvetica Neue UltraLight, #8A8A9A, tracking: 0
LABEL:    11pt Helvetica Neue, #5A5A6A, tracking: +200, ALL CAPS
```

---

## 4. Motion Language

### Principles
THE VOID moves like breath. Slow. Deliberate. Never urgent.

- **Minimum animation duration**: 600ms
- **Standard reveal**: 900ms–1400ms
- **Long atmospheric reveal**: 2000ms–4000ms
- **Ease function**: `cubic-bezier(0.25, 0.10, 0.0, 1.0)` — gradual start, definitive finish
- **No spring/bounce** — ever
- **No rapid cuts** — minimum 1.5s between hard cuts

### Approved Moves (Stream A)
1. **Slow fade + upward drift**: `opacity: 0→1`, `translateY: 20px→0`, over 1200ms
2. **Clip reveal from black**: element revealed by mask moving aside, 1400ms
3. **Long dissolve**: cross-fade between images, 2000ms+ ease
4. **Parallax depth**: background moves at 0.3× speed of foreground
5. **Chrome shimmer**: slow specular highlight sweeping across surface, 3000ms loop
6. **Dust particles**: very subtle ambient particle field, near-static
7. **Scale breathe**: very slow 100%→101%→100% loop, 8000ms (for hero stills)

### Forbidden Moves (Stream A)
- Bounce
- Rapid flash cuts
- Snappy spring physics
- Wiggle or shake
- Pop-in from below at high speed
- Spinning objects (unless 3D, very slow, purposeful)

---

## 5. Texture and Material

### Approved Textures
- **Resin/porcelain**: smooth, slightly translucent, catches light at edges
- **Cast concrete**: subtle grain, not rough — architectural surface
- **Brushed metal**: directional, anisotropic reflection, chrome or gunmetal
- **Silk/matte fabric**: pure matte with soft edge shadows
- **Oil painting**: visible brushstroke texture, impasto at edges
- **Raw canvas**: unprimed fabric weave visible, warm undertone
- **Aged paper**: minimal grain, no yellow — cool or warm-neutral tone

### Light Quality
- **Single-source dramatic**: strong directionality, sharp shadow edge
- **Diffused ambient**: soft box quality, nearly shadowless, reveals form
- **Rim light only**: subject appears to glow from behind, face/form in shadow
- **Colored gel light**: pastel single color wash (rose, lavender, cool blue) — like mannequin reference

---

## 6. Composition

- Golden ratio preferred for key element placement
- Deliberate negative space — the void earns its name
- Subject at ~30% of frame is acceptable (not always centered)
- Strong horizontal lines (gallery shelf, horizon) ground the composition
- Asymmetric balance over symmetric
- Portrait orientation preferred (9:16 for social, A4 for print)

---

## 7. Application — Stream A Specific

| Use Case | How to Apply |
|----------|--------------|
| Brand reveal moments | Full-bleed dark image, single word or logo, slow fade in |
| Editorial Instagram post | Mannequin/sculpture photograph, minimal caption, wide tracking type |
| Video intro/outro | Black frame, slow fade to sculptural visual, minimal music |
| Hero sections (website) | Dark background, high-contrast sculptural imagery, serif headline |
| 3D assets | Chrome materials, dark environment map, single key light, ultra-clean render |
| Poster / print | Museum-quality layout: image dominant, type precise, extreme white space |

---

## 8. Reference Color Harvest (Drive images)

```
Mannequin pastel study:  #E8D5C8 (warm skin), #8BA8B2 (cool lavender light), #1E1A16 (void bg)
Chrome mask:             #9EACB4 (chrome mid), #D4DDE2 (chrome highlight), #0C0C0C (reflection bg)
Contemporary painting:   #3D2E28 (dark sienna), #C08860 (warm ochre), #7090A0 (cool blue)
```
