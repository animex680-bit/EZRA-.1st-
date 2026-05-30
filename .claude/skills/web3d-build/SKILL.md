---
name: web3d-build
description: Technical implementation of 3D websites — stack selection (React Three Fiber / vanilla three.js / OGL / pre-rendered), Vite scaffolding, scene architecture, loading models, camera and lighting setup. Use when implementing the actual 3D web build. Part of the web3d pipeline.
---

# web3d-build — Implementation

Turns the concept + assets into a real WebGL build. Stack is chosen per project (see web3d orchestrator). Default to React Three Fiber unless a reason says otherwise.

## Scaffold (always Vite, never a single inline HTML file again)

The old 8MB single-file export was a root cause of slop. Use a real project:

```
npm create vite@latest site -- --template react   # or vanilla
npm i three @react-three/fiber @react-three/drei gsap lenis
npm i -D vite-plugin-glsl gltf-transform
```

Project shape: `src/` with `scene/` (R3F components), `shaders/` (.glsl), `lib/`, `styles/`, and `public/models/` for .glb. Keep DOM/UI and WebGL cleanly separated.

## Scene architecture (R3F)

- `<Canvas>` with `dpr={[1, 2]}` (cap pixel ratio), `gl={{ antialias: true, powerPreference: 'high-performance' }}`.
- Use `frameloop="demand"` and `invalidate()` for sites that aren't constantly animating — huge battery/perf win.
- Load models with `useGLTF` (drei) + `<Suspense>` + a real loader screen (not a fake "Unpacking..." spinner).
- Lighting: prefer an **HDRI environment** (`<Environment>`) over ad-hoc point lights — instant premium look. Add 1 key light for shadows if needed.
- Camera: deliberate FOV (35–50 for product, wider for worlds). Animate the camera along the scroll storyboard, don't just spin objects.
- Postprocessing (`@react-three/postprocessing`): bloom, DOF, chromatic aberration, vignette — used with restraint, they sell "expensive."

## Vanilla three.js (when chosen)

Same principles: `WebGLRenderer({ antialias, powerPreference })`, `renderer.setPixelRatio(Math.min(devicePixelRatio, 2))`, `PMREMGenerator` for env maps, `GLTFLoader` + `DRACOLoader`/`KTX2Loader`, render-on-demand, dispose geometries/materials/textures on teardown.

## Patterns that separate premium from slop

- **Instancing** for any repeated object (`InstancedMesh`) — 1000s of objects, one draw call.
- **Scroll-driven camera** over object-spin. The camera is the storyteller.
- **Raycasting** for real interactivity (hover/click on 3D objects) — pointer events in R3F make this trivial.
- **A loader that earns the wait** — progress tied to actual asset load, branded, with an intentional reveal.
- **Real responsiveness** — recompute layout/camera on resize; design the mobile experience deliberately (often a lighter scene, not the desktop one shrunk).

## Gotchas (learned the hard way — see LEARNINGS)

- **drei `<GradientTexture>` requires `stops` AND `colors` props.** Bare usage throws at runtime. Always pass both, same length.
- **Never animate `ShaderMaterial.opacity`** — it does nothing; a ShaderMaterial's alpha comes from `gl_FragColor.a`. Drive a real uniform (e.g. `uIntensity`) and read it in the fragment shader instead.
- **Beat the 500KB bundle warning:** three.js alone is ~290KB gzip. Lazy-load the `<Canvas>` (dynamic import) so first paint isn't blocked, and split vendor with `build.rollupOptions.output.manualChunks`. Acceptable to skip for a throwaway concept; fix before any paid delivery (it's in the web3d-perf gate).
- **Scroll→3D wiring that works:** a tall sticky "reveal" section + a Lenis raf loop that computes progress from `getBoundingClientRect()` into a `progressRef`, then ease that ref inside `useFrame` (never apply raw scroll — it snaps). Keep DOM content in normal flow *over* a `position:fixed` Canvas.

## Don't

- Don't fake 3D with CSS transforms and call it a 3D site.
- Don't autoplay multiple heavy videos as a substitute for a scene.
- Don't ship without disposing resources / without a WebGL-unavailable fallback.

Hands the signature moment to `web3d-shaders`, motion to `web3d-motion`, and must clear `web3d-perf`.
