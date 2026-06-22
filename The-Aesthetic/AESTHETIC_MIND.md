# AESTHETIC MIND — Master Reference

> "Every pixel is a decision. Every decision is a statement. The statement is always the same: precision, depth, silence."

This document is the single source of truth for all visual output. Read it before starting any creative work.

---

## 1. The Foundation (both streams)

### 1.1 Core Identity

The aesthetic is built on **three immovable pillars**:

1. **Silence** — Empty space is not absence. It is presence at rest. Every composition breathes.
2. **Depth** — Flat is dead. Everything has layers: light falling on form, glass catching reflection, shadows with weight.
3. **Precision** — Nothing is approximate. Type is set with intention. Color is chosen not decorated. Motion has a reason.

### 1.2 What This Aesthetic Is NOT

These must never appear in any output:

- Busy, overcrowded compositions
- Gradient abuse (more than 2 stops unless intentionally generative)
- Stock photography feeling
- Comic Sans, Papyrus, or any display font used ironically
- Neon for neon's sake without purpose
- Drop shadows with soft pink or yellow tones
- Lens flares as decoration
- Cheap plastic texture
- Symmetry without intention (centered everything, no hierarchy)
- Oversaturated color without restraint

### 1.3 Shared Color Philosophy

Both streams operate in a **dark-first** world. Light modes exist but dark is the default emotional register.

**Universal neutrals** (apply to both streams):
```
Obsidian    #0A0A0C  — true black with blue undertone
Void        #111115  — the primary dark background
Smoke       #1C1C22  — elevated surface
Ash         #2E2E38  — border, divider
Fog         #8A8A9A  — muted text, placeholder
Ghost       #C8C8D8  — secondary text
Bone        #F0EFE8  — warm off-white, not pure white
Pure White  #FFFFFF  — sparingly, for maximum contrast moments
```

**Universal accent system** (choose per project, don't mix more than 2):
```
Chrome      #B8C4CC  — metallic neutral
Teal        #0E9DA8  — tech, precision, intelligence
Lavender    #9B8FD4  — creativity, depth
Amber       #C8962A  — gold, value, premium
Crimson     #A01830  — urgency, power
```

---

## 2. Stream A — THE VOID

*Full spec in /streams/STREAM_A_THE_VOID.md*

### Quick Reference

**Emotional register**: Silent luxury. Like walking into a museum at closing time.
**Visual anchors**: Mannequin heads with chrome masks. Pastel light on sculptural form. Abstract painting texture. Chrome reflecting the world.

**Color palette (Stream A)**:
```
Background   #0D0D0F   — near-black with a warmth
Surface      #1A1612   — warm dark brown-black
Bone White   #EDE8E0   — primary light tone
Dusty Rose   #C4A89A   — skin, warmth, softness
Chrome       #B2BFC9   — reflective metal
Teal Shadow  #1D4E52   — deep teal shadow tone
Muted Gold   #A8924A   — subtle luxury
```

**Typography (Stream A)**:
- Headlines: Didot, Cormorant Garamond, or any high-contrast serif
- Body: Helvetica Neue Light, or a geometric sans at light weight
- Hierarchy: SIZE does the work. Weight variation is subtle.
- Tracking: Wide (+100 to +200) for headlines. Tight (-20 to -40) for subheads.
- Never use bold serifs for body. Never mix two serifs.

**Motion (Stream A)**:
- Slow reveals. Fades over 800ms–2000ms.
- Objects drift, they do not snap.
- Parallax depth: layers move at different rates.
- Nothing bounces. No spring physics.
- Ease: custom cubic-bezier(0.25, 0.1, 0.0, 1.0) — starts slow, finishes decisive.

---

## 3. Stream B — THE INTERFACE

*Full spec in /streams/STREAM_B_THE_INTERFACE.md*

### Quick Reference

**Emotional register**: Premium tech intelligence. Like the OS of the future, already here.
**Visual anchors**: Glassmorphism / liquid glass surfaces. Neumorphic depth. Spatial computing (Apple Vision Pro aesthetic). Midjourney generative dot-matrix art. AI product hero sections.

**Color palette (Stream B)**:
```
Background   #0C0C10   — near-black, slight blue
Surface L1   #141418   — primary card/panel background
Surface L2   #1E1E26   — elevated panel
Surface L3   #28282F   — modal/overlay
Glass        rgba(255,255,255,0.06)  — frosted glass fill
GlassBorder  rgba(255,255,255,0.12)  — glass edge
Accent Blue  #3B82F6   — primary interactive
Accent Teal  #0EA5E9   — AI, data, intelligence
Accent Purple #8B5CF6  — creativity, generative
Muted        #6E7F8D   — text-secondary (neumorphic spec)

Neumorphic light mode:
  BG          #EFF2F9
  Surface     #E4EBF1
  Muted       #B5BFC6
  Text        #6E7F8D
```

**Typography (Stream B)**:
- Headlines: SF Pro Display, Campton, Inter, or Geist
- Body: Campton Book, Avenir Next Medium, or Inter Regular
- Code/data: JetBrains Mono, Fira Code
- All-caps labels: tight tracking, 0.1em letter-spacing
- Never serif in UI contexts (except decorative hero moments)

**Motion (Stream B)**:
- Fast, precise micro-interactions: 150–250ms
- Longer transitions: 400–600ms
- Spring physics for UI state changes (stiffness 200, damping 20)
- Glassmorphism shimmer: slow, ~3000ms loop
- Particle/generative art: 60fps minimum, emergent, not mechanical

---

## 4. Stream Blending Rules

You may blend both streams in a single project. Rules:

| Context | Stream A weight | Stream B weight |
|---------|----------------|----------------|
| Brand identity / hero moment | 80% | 20% |
| Product UI | 20% | 80% |
| Motion graphics (social) | 50% | 50% |
| Landing page | 40% | 60% |
| 3D asset render | 70% | 30% |
| Pitch deck | 30% | 70% |
| Document / report | 10% | 90% |

**The blend rule**: Stream A controls the *emotional quality* (color mood, pacing, texture) and Stream B controls the *structure* (layout, type hierarchy, interactive states).

---

## 5. Image and Photography Direction

### Stream A Photography
- Subject isolation on dark or neutral backgrounds
- Dramatic single-source lighting (often top or side)
- Subjects: sculptural objects, mannequins, masks, hands, fabric, skin
- Color grading: desaturated midtones, preserved shadows, slightly warm highlights
- No lifestyle photography. No models smiling at camera.
- Editorial: the subject is unaware of being watched.

### Stream B Photography / Illustration
- Product UI screenshots on device mockups
- Midjourney-style generative art: dots, particles, holograms, pure black background
- Clean 3D renders of tech objects (phones, laptops, abstract geometric forms)
- No stock photography. No obvious cheerful teamwork photos.
- CGI: metallic, glass, high specularity, environment reflections

---

## 6. Motion Principles (Universal)

### Hierarchy of Motion
1. **Purpose** — Every animation must communicate a state change or guide attention.
2. **Restraint** — Less animation = more impact when animation appears.
3. **Timing** — Easing is everything. Linear is mechanical. All movement uses easing.
4. **Spatial logic** — Elements that enter from the left come from "before". Elements from the top come from "above".

### Forbidden Motion
- Spinning logos
- Slide-in from random directions without spatial logic
- Bounce that doesn't relate to the content's weight
- Full-screen flash transitions
- Rapid random cuts (strobe without purpose)
- Parallax that is so heavy it breaks readability

### Approved Motion Vocabulary
- **Fade + scale**: opacity 0→1 combined with scale 0.95→1.0
- **Clip reveal**: content reveals from behind a mask (top-down or left-right)
- **Drift**: subtle Y-axis translation (-8px to 0) during fade-in
- **Glassmorphism shimmer**: slow light sweep across surface, opacity 0→0.15→0
- **Particle emergence**: dots/particles materializing from void
- **Text snap**: kinetic typography with punch-in scale, snap to rest
- **Sweep line**: horizontal or vertical line that wipes across frame

---

## 7. Composition Rules

### Grid System
- **Base unit**: 8px
- **Gutters**: 24px (mobile), 32px (desktop)
- **Max content width**: 1200px centered
- **Safe zones for vertical video (1080×1920)**:
  - Top: 14% (IG UI, sticker zone)
  - Bottom: 18% (IG UI, caption zone)
  - Sides: 4%

### White Space (Empty Space) Doctrine
- Never fill a space just because it exists.
- The void is part of the composition.
- Breathing room around key elements should be at least 2× the element's own size.
- Crowded = amateur. Breathable = premium.

### Hierarchy
1. ONE primary message per screen/frame. Not two. One.
2. Supporting info at 50-60% visual weight of primary.
3. Tertiary info at 25-30% visual weight.
4. Labels and metadata: near invisible until needed.

---

## 8. Application Matrix

| Output Type | Stream Primary | Key Ref | Mood Instruction |
|-------------|---------------|---------|------------------|
| Instagram Reels | A+B 50/50 | Kinetic type, chrome, glass | Confident. Moves with purpose. |
| Instagram Feed | A 70% | Sculpture, editorial photography | Stop the scroll with silence. |
| Website Hero | B 60% + A 40% | Glass panel over dark field | First impression of intelligence. |
| 3D WebGL Scene | B primary, A texture | Spatial computing, particle field | The user is inside the product. |
| Mobile App | B 90% | Neumorphic / glassmorphic | Every tap feels earned. |
| Pitch Deck | B 70% + A 30% | Clean grid, hero moments | Premium but human. |
| Document | B 95% | Minimal, typographic | Respect the reader's time. |
| 3D Asset | A 70% | Chrome, sculptural, editorial | Object as protagonist. |
| Brand Video | A primary | Dramatic pacing, single subjects | Cinema. Not commercial. |
| Motion Graphics (overlay) | B 60% | Glass panels, data viz, kinetic | Informative but beautiful. |

---

## 9. Anti-Slop Checklist

Before delivering ANY creative work, verify:

- [ ] The composition breathes — empty space has been intentionally placed
- [ ] Typography has no more than 2 typefaces
- [ ] Color palette has no more than 4 colors (+ accent)
- [ ] Animation has purpose — every moving element is communicating something
- [ ] Dark tones have blue or warm undertones, not flat grey
- [ ] No stock photography aesthetic
- [ ] No centered-everything lazy symmetry
- [ ] No gradient abuse
- [ ] Motion timing uses custom easing, not linear
- [ ] The work could appear in a premium brand context without embarrassment

---

*This document evolves. Add to it after every project in the retro.*
