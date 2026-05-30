# web3d — LEARNINGS (append-only evolution log)

This file is the memory of the pipeline. Read it at the start of every 3D web project; append to it at the end. Recurring lessons get promoted into the SKILL.md files (that's the evolution). See `web3d-evolve`.

---

## 2026-05-30 — Pipeline founding / diagnosis of past work
- Context: prior output ("Tala" pages) was diagnosed as slop and the web3d pipeline was created to replace the old "single CSS-transform HTML file + push a link" habit.
- Worked: clean deploy + live-link delivery habit (keep this).
- Failed / avoid (root causes of slop):
  - Fake 3D via CSS `perspective`/`translate3d` instead of real WebGL.
  - Zero custom shaders (the missing moat).
  - No concept / no signature moment — "tiles that move" is not an idea.
  - Procedural placeholder assets, no art direction.
  - Anti-performance: one 8MB HTML file with 4 autoplaying videos.
  - Multiple competing rAF loops instead of one motion system.
  - Output recognizably AI/tool-generated (bundler export).
- Tooling baseline: free/OSS web stack (three / R3F / GSAP / Lenis / Vite) + Meshy (AI base meshes) + Blender (hub) + UE5 (cinematics/baking only — no live web deploy).
- SKILL EDITS made from this project: created web3d, web3d-concept, web3d-assets, web3d-build, web3d-shaders, web3d-motion, web3d-perf, web3d-business, web3d-evolve.

---

## 2026-05-30 — Aluminium Windows Cape Town (unsolicited concept piece / outbound)
- Stack: React Three Fiber + drei + Lenis (default). Why: first real RTF run; fit the default profile.
- Concept / signature moment: "We frame the light." Signature = scroll-driven aluminium STACKING DOOR whose 4 leaves slide open over a 220vh sticky reveal, dissolving the wall to a Cape Town vista with god-rays flooding in. Honest fit: regional building-products SMB = ~$2–6k client, but ideal web3d-business outbound target ("money + weak digital"); concept doubles as portfolio.
- Worked:
  - Custom GLSL **glass shader** (fresnel rim + tint + moving sheen) — exactly the "moat" the pipeline demands; cheap and mobile-safe.
  - **God-ray** additive shader gated by an `uIntensity` uniform tied to door progress (light floods as it opens).
  - Scroll→progress via a tall sticky "reveal" section + Lenis raf loop writing to a `progressRef`, eased in `useFrame` (no linear snapping). Clean separation of DOM content over a fixed Canvas.
  - `prefers-reduced-motion`: skips Lenis and opens the door immediately. Built in from the start (per web3d-motion), not bolted on.
  - Vite build succeeded first try after 2 fixes.
- Failed / avoid (caught in review, fixed before ship):
  - drei `<GradientTexture>` REQUIRES `stops` + `colors` props — bare usage throws at runtime. ALWAYS pass both.
  - Setting `.opacity` on a `ShaderMaterial` does NOTHING — alpha comes from the fragment shader. Animate a real uniform instead.
  - Had duplicate/overwritten leaf-position assignment in the loop — sloppy, simplified.
  - **Perf gate flag:** single JS bundle 1,045KB (293KB gzip) — three.js is the bulk. Over the 500KB warning. NEXT TIME: manualChunks to split three/vendor, and lazy-load the Canvas so first paint isn't blocked. (Acceptable for a concept; would fix before a paid delivery.)
- Constraint reconfirmed: sandbox cannot render-test WebGL (no browser engine) and `*.github.io` is firewalled from the agent side — so visual verification is the user's, every time. Deploy verified via GitHub API + local static smoke test (HTTP 200 + node --check on the bundle).
- Business: no quote yet (outbound concept). Intended play: DM the live link as proof. Quoted/landed: n/a.
- SKILL EDITS made from this project:
  - web3d-build: add explicit rules — drei GradientTexture needs stops+colors; never animate ShaderMaterial.opacity (use a uniform); lazy-load Canvas + manualChunks to beat the 500KB bundle warning.
