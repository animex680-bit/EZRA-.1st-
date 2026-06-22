# Approved Stack — Tools by Medium

Quick reference for what tools to use per output type.

---

## Web / 3D Web

| Layer | Tool | Notes |
|-------|------|-------|
| Bundler | Vite | Always. No exceptions. |
| 3D | Three.js or @react-three/fiber | Choose per project complexity |
| Physics | @react-three/rapier | When physics needed |
| Helpers | Drei | Camera controls, environment, etc. |
| Animation | GSAP + ScrollTrigger | Scroll-driven, page transitions |
| Smooth scroll | Lenis | `lerp: 0.08` default |
| Shaders | GLSL via vite-plugin-glsl | Custom shaders always in .glsl files |
| Fonts | Fontsource or Google Fonts CDN | Load only what's used |
| CSS | Tailwind CSS or CSS Modules | No vanilla CSS sprawl |
| Post-processing | @react-three/postprocessing | Bloom, vignette, chromatic aberration |

**HDRIs**: Poly Haven (CC0, free) — always use for environment maps.

---

## Motion Graphics

| Task | Tool |
|------|------|
| CapCut (overlay work) | CapCut desktop or mobile |
| Professional compositing | After Effects |
| Code-based motion (Reels/web) | Remotion (React-based) |
| Kinetic typography (advanced) | After Effects + Lottie export |

---

## 3D Assets

| Stage | Tool |
|-------|------|
| AI base mesh generation | Meshy |
| Modeling, retopo, UV | Blender |
| High-poly sculpt → bake | Blender Sculpt + Cycles bake |
| Material authoring | Blender BSDF nodes |
| Texture optimization | gltf-transform |
| Pre-render / lookdev | Unreal Engine 5 (baking/rendering only) |
| Free PBR textures | Poly Haven (CC0) |
| Export format | glTF / glb (web), EXR sequences (compositing) |

---

## Design & UI

| Task | Tool |
|------|------|
| UI design | Figma |
| Prototyping | Figma Interactive Prototypes |
| Design tokens | Tokens Studio (Figma plugin) |
| Icon library | Phosphor Icons or Lucide React |
| 3D in design | Spline (embedded into Figma or web) |
| Color check | Figma contrast check, or polypane.app |

---

## Generative Art

| Output | Tool |
|--------|------|
| Canvas generative | p5.js or vanilla Canvas API |
| WebGL particle fields | Three.js (PointsMaterial) |
| Custom shaders | GLSL in Three.js / R3F |
| AI-generated references | Midjourney (v6+) |
| Noise/math | Simplex noise, sin/cos fields |

---

## Documents / Presentations

| Tool | Use Case |
|------|----------|
| Figma | Premium decks (export to PDF) |
| Pitch | Collaborative team decks |
| Notion | Internal documents, wikis |
| Linear | Project/task management |
| Keynote / PowerPoint | Client-facing if required |

---

## Color

| Tool | Use Case |
|------|----------|
| `/tokens/colors.json` | Single source of truth — always start here |
| Coolors | Palette exploration |
| Palettte | Smooth gradient creation |
| Polypane | Cross-device/dark mode testing |
| APCA contrast | Better than WCAG for dark UI |

---

## Typography Sources

| Type | Source |
|------|--------|
| Cormorant Garamond | Google Fonts (free) |
| Inter | Google Fonts / rsms.me/inter (free) |
| Campton | MyFonts (paid) |
| Avenir Next | Adobe Fonts or system (paid) |
| Geist | Vercel (free, open source) |
| JetBrains Mono | JetBrains (free) |
| SF Pro Display | Apple (system font — use Inter as substitute) |

---

## What's NOT Approved

- Wix, Squarespace, Webflow (for premium deliverables)
- Bootstrap or jQuery (outdated)
- React Native Paper or Material UI (generic)
- Canva (external work — internal brainstorming only)
- Stock photo services (Getty, Shutterstock)
