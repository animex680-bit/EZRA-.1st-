# Stream B — THE INTERFACE
## Digital Product / Tech / AI / Spatial

> "The interface is the product. Make it feel like the future remembered."

---

## 1. Identity

THE INTERFACE is the body stream — the architecture that holds ideas. It draws from premium SaaS product design, spatial computing, AI/ML visual language, generative art, and the best-in-class digital products: Linear, Raycast, Pitch, Apple Vision Pro, Figma.

Defining reference images:
- **Festina One Page Award** — minimalist portfolio (Linear, Pitch, Raycast, Spline) — pure white space, elegant type, portfolio-grade restraint
- **Liquid Glass UI Kit** — frosted glass components, Nitestudio, modern glassmorphism
- **Neumorphic design system** — `#EFF2F9` family, Campton + Avenir Next, soft directional shadows
- **Apple Vision Pro profile UI** — spatial UI in mixed reality, depth layers, translucent panels
- **FrsionOS / IRIS_AI** — premium AI product hero: "WHERE AI MERGES with // YOUR VISION"
- **Observatory app** — dark mode wellness AI: "Reality Checks", "Your Aura", "You're a badass!"
- **Nike AI concept "DESTINY"** — dark AI-powered athletic interface
- **Generative art**: "emerge from code, 3D holographic projections made by tiny white dots, minimalism, pure black background"

**The feeling**: You are looking at something that was designed. Not decorated — designed. Every element is where it is for a reason.

---

## 2. Color System

### Dark Mode (Primary)
```json
{
  "bg_void":        { "hex": "#0C0C10" },
  "surface_l1":     { "hex": "#141418" },
  "surface_l2":     { "hex": "#1E1E26" },
  "surface_l3":     { "hex": "#28282F" },
  "border_subtle":  { "hex": "#2A2A35" },
  "border_medium":  { "hex": "#3A3A48" },
  "text_primary":   { "hex": "#F0F0F6" },
  "text_secondary": { "hex": "#9090A8" },
  "text_muted":     { "hex": "#5C5C72" }
}
```

### Light Mode — Neumorphic (exact reference spec)
```json
{
  "bg":            "#EFF2F9",
  "surface":       "#E4EBF1",
  "muted":         "#B5BFC6",
  "text":          "#6E7F8D",
  "shadow_light":  "#FAFBFF",
  "shadow_dark":   "rgba(22, 27, 29, 0.23)"
}
```

### Glass System
```json
{
  "glass_fill":    "rgba(255,255,255,0.06)",
  "glass_fill_med":"rgba(255,255,255,0.10)",
  "glass_border":  "rgba(255,255,255,0.12)",
  "glass_strong":  "rgba(255,255,255,0.20)",
  "glass_backdrop":"blur(20px) saturate(1.8)"
}
```

### Accent Colors
```json
{
  "blue":   "#3B82F6",
  "teal":   "#0EA5E9",
  "purple": "#8B5CF6",
  "emerald":"#10B981",
  "amber":  "#F59E0B",
  "rose":   "#F43F5E"
}
```

### Gradient Recipes
```css
/* Hero — deep space */
background: radial-gradient(ellipse 80% 50% at 50% 0%, rgba(59,130,246,0.15) 0%, transparent 70%),
            radial-gradient(ellipse 60% 40% at 80% 100%, rgba(139,92,246,0.10) 0%, transparent 70%),
            #0C0C10;

/* Particle field tint */
background: radial-gradient(ellipse 100% 100% at 50% 50%, rgba(14,165,233,0.08) 0%, transparent 100%), #0C0C10;
```

---

## 3. Typography

### Font Stack
```
DISPLAY:  SF Pro Display, Geist, Inter Display, Campton
HEADING:  SF Pro Text, Inter, Campton Book
BODY:     SF Pro Text, Avenir Next, Inter, Campton Light
MONO:     JetBrains Mono, Fira Code, SF Mono
LABEL:    Inter, Campton — tracking 0.1em, weight 500
```

### Exact Neumorphic Font Spec
```
Campton Book       — UI labels, button text
Campton Light      — body, descriptions
Avenir Next Medium — headings, numbers
```

### Type Scale
```
hero:  80-120px / weight 700-800 / tracking -0.04em
2xl:   56px     / weight 700     / tracking -0.04em
xl:    40px     / weight 600     / tracking -0.03em
lg:    28px     / weight 600     / tracking -0.02em
md:    20px     / weight 500     / tracking -0.01em
base:  16px     / weight 400     / tracking 0       / line-height 1.6
sm:    14px     / weight 400     / tracking 0
label: 11px     / weight 500     / tracking +0.1em  / ALL CAPS
mono:  13px     / weight 400     / tracking 0
```

---

## 4. Motion Language

**Micro-interactions** (hover, press): 150–200ms, ease-out
**Component transitions** (modal, panel): 250–350ms, cubic-bezier(0.32, 0.72, 0, 1)
**Page/hero reveals**: 400–600ms, cubic-bezier(0.16, 1, 0.3, 1)
**Atmospheric loops** (shimmer, particles): 2000–6000ms, ease-in-out

### Spring Physics
```
Standard: stiffness 200, damping 20, mass 1
Snappy:   stiffness 400, damping 30, mass 1
Gentle:   stiffness 100, damping 15, mass 1
```

---

## 5. Component Patterns

### Glass Card
```css
background: rgba(255, 255, 255, 0.06);
border: 1px solid rgba(255, 255, 255, 0.12);
border-radius: 16px;
backdrop-filter: blur(20px) saturate(1.8);
box-shadow: 0 4px 32px rgba(0, 0, 0, 0.4), inset 0 1px 0 rgba(255,255,255,0.1);
```

### Neumorphic Card (exact reference spec)
```css
/* bg: #EFF2F9, surface: #E4EBF1 */
.neuro-sm  { box-shadow: -5px  -5px  10px #FAFBFF, 5px  5px  10px rgba(22,27,29,0.23); }
.neuro-md  { box-shadow: -10px -10px 20px #FAFBFF, 10px 10px 20px rgba(22,27,29,0.23); }
.neuro-lg  { box-shadow: -20px -20px 40px #FAFBFF, 20px 20px 40px rgba(22,27,29,0.23); }
.neuro-in  { box-shadow: inset -5px -5px 10px #FAFBFF, inset 5px 5px 10px rgba(22,27,29,0.23); }
```

---

## 6. Particle Field Spec

```
Background:   #000000 or #0C0C10
Color:        #FFFFFF, opacity 0.4–0.8 (randomized)
Size:         1–2px crisp (no blur on particles)
Density:      2000–6000 per 1920×1080
Motion:       0.1–0.5 px/frame slow drift
Depth:        z-sim via size (near 2px, far 0.5px)
Variant:      swap white → accent_teal at 30%
```

---

## 7. Anti-Patterns

- Gradients with 5+ stops without generative purpose
- Mixing glass AND neumorphism without intention
- Rounded corners above 24px (except modals: max 32px)
- Particle fields below 30fps
- Typography sized by feel, not the scale
- Dark mode as just `background: #000000`
