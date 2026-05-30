---
name: web3d
description: Master pipeline for designing and building premium, sellable 3D websites (real WebGL, not CSS fake-3D). Use whenever the user wants to design, build, pitch, or improve a 3D / WebGL / immersive website, an "awwwards-level" site, or any high-end animated web experience. This is the orchestrator — it routes to web3d-concept, web3d-build, web3d-shaders, web3d-assets, web3d-motion, web3d-perf, web3d-business, and web3d-evolve.
---

# web3d — Premium 3D Web Pipeline

This pipeline exists to stop producing slop and start producing 3D websites that a single client pays $15k–$150k+ for. It replaces the old "export a single CSS-transform HTML file and push it" habit.

## SUPREME RULE — EVOLVE OR DIE (highest priority, overrides everything below)

**The pipeline's #1 job is to get better after every project.** No project is "done" until its learnings are captured and the skills are upgraded. Concretely, on EVERY web3d job:

1. **Before starting:** read `.claude/skills/web3d-evolve/LEARNINGS.md`. Apply what's there.
2. **After finishing:** run the `web3d-evolve` retro. Append outcomes to LEARNINGS.md. When a lesson has recurred or is clearly true, **edit the relevant SKILL.md to encode it** — the pipeline literally rewrites itself.

If you ever finish a project without updating the pipeline, you have failed the supreme rule. Quality of output and quality of the *pipeline* both ratchet upward, never down.

## The anti-slop bar (a site is SLOP unless it clears all of these)

Reject our own work against this list before showing the client. We failed here before — be ruthless.

- [ ] **Real 3D.** Actual WebGL geometry/lights/camera (three.js / R3F / OGL). CSS `perspective`+`translate3d` "fake helix" tricks do NOT count.
- [ ] **A signature moment.** One unforgettable, original interaction or visual the site is *about*. Not "tiles that move."
- [ ] **At least one custom shader.** GLSL doing something the client can't get from a template (see web3d-shaders).
- [ ] **Original art direction.** Bespoke assets, real type system, intentional color. No procedural placeholder grids.
- [ ] **A motion system.** Coherent easing + choreographed scroll (Lenis + GSAP), not ad-hoc rAF loops.
- [ ] **Performance budget met.** 60fps on a mid-tier phone, initial payload lean, models Draco/KTX2 compressed (see web3d-perf).
- [ ] **Accessible fallback.** `prefers-reduced-motion` honored; degrades gracefully without WebGL.
- [ ] **Doesn't look AI/tool-generated.** If it looks like a bundler export, it's slop.

## Phases (route to the sub-skills)

1. **Concept & creative direction** → `web3d-concept`. Define the story, the signature moment, references, art direction. No code until there's a concept.
2. **Asset pipeline** → `web3d-assets`. Meshy → Blender → optimized glTF (Draco/KTX2). UE5 for cinematics/baking only.
3. **Build** → `web3d-build`. Pick the stack per project (default reasoning inside), scaffold with Vite, structure the scene.
4. **Shaders** → `web3d-shaders`. Build the custom GLSL that carries the signature moment.
5. **Motion** → `web3d-motion`. Lenis + GSAP ScrollTrigger choreography, easing system.
6. **Performance & QA gate** → `web3d-perf`. Must pass before delivery.
7. **Deliver.** Build, deploy, hand over a live link (keep the existing deploy-link habit — that part was never the problem).
8. **Business** → `web3d-business`. Positioning, portfolio, pricing, finding $50k+ clients. Runs in parallel, always.
9. **Evolve** → `web3d-evolve`. The supreme rule. Always last, never skipped.

## Stack decision (user chose "decide per project")

Default reasoning, fastest-to-strongest-result first:
- **React Three Fiber + drei + GSAP + Lenis** — default for most content/marketing 3D sites. Component model, ecosystem, speed.
- **Vanilla three.js + Vite** — when bundle size / fine control matters or the site is one bespoke scene.
- **OGL / raw WebGL** — shader-first, ultra-light, hero pieces where every kb counts.
- **Pre-rendered (UE5/Blender video) + light DOM** — when the "3D" is cinematic, not interactive. Cheapest to ship, often the smartest call.

Pick explicitly and write the choice + reason into the project's LEARNINGS entry.

## Definition of done

Anti-slop bar fully checked ✓ · perf gate passed ✓ · live link delivered ✓ · LEARNINGS.md updated and relevant skills edited ✓ (supreme rule).
