---
name: web3d-shaders
description: GLSL shader programming for the web — custom materials, vertex displacement, particles, fluid/noise effects, post-processing, and the "signature moment" that templates can't produce. Use when a 3D web project needs custom visual effects beyond stock materials. Part of the web3d pipeline.
---

# web3d-shaders — GLSL (the moat)

This is the single biggest gap between our slop and premium work. Stock materials look stock. Custom shaders are why Active Theory / Resn sites feel impossible. At least one real custom shader per premium project.

## Mental model

- **Vertex shader** moves points (displacement, morphing, waves, particle position).
- **Fragment shader** colors pixels (gradients, fresnel, lighting, patterns, post FX).
- Drive everything with **uniforms**: `uTime`, `uMouse`, `uScroll`, `uResolution`, `uProgress`.

In R3F, author custom materials with `shaderMaterial` (drei) or raw `ShaderMaterial`; load `.glsl` via `vite-plugin-glsl`. To extend PBR (keep lighting, add an effect) use `onBeforeCompile` or `CustomShaderMaterial`.

## The high-value effects (learn/keep these)

1. **Fresnel / rim** — `pow(1.0 - dot(normal, viewDir), p)`. Instant premium edge glow / iridescence / holographic look.
2. **Vertex displacement by noise** — feed position into curl/simplex noise + `uTime` for organic, breathing, liquid surfaces. The "expensive blob" effect.
3. **GPU particles** — positions computed in shader (or FBO/GPGPU ping-pong for 100k+). Morph particles between shapes on scroll = a classic signature moment.
4. **Gradient/grain backgrounds** — animated noise gradients + film grain; cheap, gorgeous, brand-defining.
5. **Scroll/mouse-reactive distortion** — displacement RGB-split on images (the "WebGL image hover" Codrops staple). Easy win that reads as high-craft.
6. **Fluid / flowmap** — mouse trails, ink, smoke. Higher effort, huge wow.
7. **Post-processing passes** — custom fragment passes for transitions, dithering, halftone, CRT, bloom shaping.

## Toolkit

- Noise: pack `glsl-noise` (simplex/curl) or paste Ashima/`cnoise`. Don't reinvent.
- `lygia` shader library for reusable functions (noise, sdf, color, lighting).
- Debug with `leva` to live-tune uniforms; iterate in the browser, not by guessing.
- Reference + learn: The Book of Shaders, Codrops tutorials, ShaderToy (port effects).

## Craft rules

- Keep fragment math cheap — it runs per pixel per frame. Move work to the vertex stage or precompute when possible.
- Animate via uniforms, never by rebuilding geometry each frame.
- Always provide a non-shader fallback for the signature element (image/video) for low-end/no-WebGL.
- One *great* shader beats five mediocre ones. The signature moment is usually a single, perfected effect.

Carries the `web3d-concept` signature moment; performance-bounded by `web3d-perf`.
