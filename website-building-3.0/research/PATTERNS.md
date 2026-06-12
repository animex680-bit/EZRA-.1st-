# PATTERNS.md — The Distilled Creator Playbook

Research date: **2026-06-12** (refresh when older than ~6 weeks — see wb3-research).
Evidence: `CREATORS.md` (14 creators, 50/50 IG/YouTube). This file is what the
pipeline actually executes against.

## 1. The consensus process spine (what nearly every top creator does)

1. **Reference first.** Start from an award-winning site or luxury-brand reference;
   isolate ONE signature effect to own. (Codegrid, Larose, Mancini)
2. **Design system / tokens BEFORE code or AI generation.** Type scale, palette,
   spacing, components defined up front and fed to the agent — the documented fix
   for "AI sites look generic". (Oliur/Relume, Gary Simon via Figma MCP)
3. **Assets through Blender.** Model → retopo → **bake AO/PBR high→low poly** →
   compressed glTF. (Wawa Sensei's baking guide, Bruno Simon)
4. **Debug tooling on day one.** lil-gui/leva in the scaffold. (Bruno Simon)
5. **Scroll is the spine.** GSAP ScrollTrigger + Lenis drives camera, model state,
   and section transitions. (Mancini, Codegrid, Larose, Bruno)
6. **One signature shader moment** — the thing templates can't do: refraction/
   diamond materials, GPGPU particles, SSGI, dissolve. **2026 shift: GLSL → TSL/
   WebGPU** (r183; Safari 26 made WebGPU universal). (Mancini, Wawa, Greenheck, Heckel)
7. **Performance pass as a gate** before ship. (Bruno's perf chapter)
8. **Ship and productize.** Deploy to Vercel/Pages; release starters as marketing;
   version premium components. (Mancini, Greenheck, Snellenberg)

→ This maps 1:1 onto WORKFLOW.md phases 1–7. The spine is validated.

## 2. The consensus 2026 stack

three.js / React Three Fiber + drei · GSAP + ScrollTrigger · Lenis smooth scroll ·
Blender (bake + glTF) · Vite or Next.js · Vercel/Pages · **WebGPU + TSL as the new
frontier** (with WebGL/GLSL fallback). No-code tier: Figma → Spline → Webflow/Framer.

## 3. AI-in-the-loop patterns (verified, concrete — our lane)

- **Skills close the API gap.** Base models don't know three.js r18x; markdown
  skill packs (SKILL.md + REFERENCE + docs + working examples + templates) in
  `.claude/skills/` stop hallucinated APIs. (Greenheck's webgpu-claude-skill,
  updated Apr 2026; CloudAI-X/threejs-skills)
- **Tokens-in, brand-out.** Feed the agent the design system before generating
  anything; every page inherits the brand. (Oliur/Relume, Apr 2026)
- **MCP as design handoff.** Figma MCP server lets the agent read the actual design
  file, not screenshots. (Gary Simon)
- **Routines for repeatable production** — e.g. Oliur's ~15-min SEO-page routine.
- **AI output = first draft.** Premium quality consistently takes 2–3 directed
  revision rounds; **direction specificity (exact timings, named animations, named
  references) is the main quality lever.** (Oliur, Greenheck)
- **The unoccupied lane:** AI speed-run content ships generic sites; premium-WebGL
  people don't do AI speed-runs. **AI-agent pipeline + real WebGL signature tech is
  mostly empty** — and Niccolò Miranda (Codex + Claude Code + Cursor over three.js/
  SDF/WebGPU, clients: Prada, Meta) proves it works at the $50k+ tier.

## 4. What wins attention (Instagram findings → portfolio/marketing layer)

- The shareable unit is **5–15 seconds**: a perfect loop, a micro-interaction
  close-up, a UI-motion concept — NOT full-site walkthroughs.
- **Before/after transformation** framing is evergreen; redesign reels built the
  biggest account in the niche (586K).
- **Process is the new portfolio**: node graphs, prompts, timelines, big text
  overlays for silent viewing; hook in the first 3 seconds.
- "Watch AI build this in 20 minutes" is the breakout 2025–26 hook format.
- A rendered *concept* of how a site could move sells before any code exists (Minh Pham).

## 5. How attention converts to money (the business map)

- **>100K followers → sell education/products** ($99–$1,497 courses; free assets/
  mini-courses as the universal lead magnet).
- **10–50K followers → sell client work + memberships**, with **awards as the trust
  signal** — in this tier an Awwwards SOTD outweighs 100K followers (Snellenberg,
  Miranda).
- **The flywheel to copy:** ship premium work → extract its techniques into short
  content → productize the building blocks (snippets/components/skills, Osmo-style
  €20–25/mo or versioned products like Water Pro) → recurring revenue funds the
  next award-bait build.
- Value ladder confirms web3d-business: $3–8k polished animated → $15–40k custom
  WebGL with portfolio → $50k+ studio-grade with prestige signals.

## 6. Divergences from our taste profile (taste wins; logged)

None material yet. The creator meta (scroll-driven, signature moments, living
micro-interactions, editorial type) aligns with the ADAPT.md taste profile. Watch:
the IG "perfect loop" aesthetic favors abstract neon (Ducky 3D) — user taste so far
favors business-grounded footage + procedural shader backdrops; don't drift neon
without a sign-off.

## 7. Skill edits made from this research (supreme rule receipts)

- `web3d-build`: tokens-before-generation rule; TSL/WebGPU frontier note with
  WebGL fallback; debug UI on day one.
- `web3d-shaders`: TSL/WebGPU shift + reference-implementation rule (work from
  documented current APIs, not memory).
- `web3d-business`: productization flywheel (skills/components/templates as
  recurring revenue); award-as-trust-signal at the 10–50K tier; the unoccupied
  AI+WebGL lane as positioning.
- `wb3` (orchestrator): 2–3 directed revision rounds budgeted into every build;
  direction specificity as the quality lever.
