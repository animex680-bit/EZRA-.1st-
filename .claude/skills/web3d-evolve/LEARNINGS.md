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
