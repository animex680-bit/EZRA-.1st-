---
name: web3d-perf
description: Performance engineering and QA gate for 3D websites — frame budgets, draw-call reduction, instancing, LOD, asset compression checks, Lighthouse, and real-device testing. Use before delivering any 3D web build; it is a required gate. Part of the web3d pipeline.
---

# web3d-perf — Performance & QA Gate

A 3D site that stutters is slop no matter how it looks. This is a **gate**: a build does not ship until it passes. Our old 8MB single-file-with-4-videos page would fail every line here.

## Budgets (targets, tune per project)

- **60fps** on a mid-tier phone (e.g. ~iPhone SE / mid Android). 30fps is the floor, never below.
- **Initial payload** ideal < ~5MB; lazy-load everything below the fold / later scenes.
- **Per model** < 2–3MB (hero), < 500KB (secondary), Draco/meshopt + KTX2 always.
- **Draw calls** low — instance repeats, merge static geometry, atlas textures.
- **First meaningful paint** fast; the WebGL scene can stream in behind a real loader.

## The checklist (run before delivery)

- [ ] Pixel ratio capped (`Math.min(devicePixelRatio, 2)`).
- [ ] `frameloop="demand"` / render-on-demand where the scene isn't constantly moving.
- [ ] Repeated objects use `InstancedMesh`.
- [ ] Geometry compressed (Draco/meshopt); textures KTX2/Basis; no 4k+ textures shipped.
- [ ] HDRI env map small (1–2k), not 8k.
- [ ] Lazy-load offscreen scenes/models; code-split heavy routes.
- [ ] Resources disposed on unmount (geometry/material/texture/renderer).
- [ ] No layout-thrashing animations (transform/opacity only).
- [ ] `prefers-reduced-motion` honored.
- [ ] WebGL-unavailable fallback renders (image/video, not a blank screen).
- [ ] Tested on a **real phone**, not just a desktop with a good GPU.
- [ ] Lighthouse run; Performance reasonable given the 3D (don't chase 100, but no obvious red flags).
- [ ] No console errors; memory stable over time (no leak from undisposed objects).

## Measurement

- `stats.js` / R3F `Perf` (drei) for FPS, draw calls, memory during dev.
- Chrome DevTools Performance + Memory tabs; watch for GC sawtooth and rising heap.
- Throttle CPU 4–6x and test to simulate mobile.

## How to claw back frames

Reduce draw calls (instance/merge) → cut texture sizes / KTX2 → lower DPR → simplify/skip postprocessing on mobile → render-on-demand → reduce particle counts / shader cost → LOD or hide distant detail → serve a lighter mobile scene.

Record the final FPS + payload numbers into the project's LEARNINGS entry (`web3d-evolve`).
