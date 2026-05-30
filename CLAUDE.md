# Claude Code — Project Instructions

## PRIMARY DIRECTIVE: the web3d pipeline

This project builds **premium, sellable 3D websites** — real WebGL, not CSS fake-3D. For ANY work involving 3D / WebGL / immersive / "awwwards-level" / high-end animated websites, use the **`web3d`** pipeline (`.claude/skills/web3d/`), which orchestrates:
`web3d-concept` · `web3d-assets` · `web3d-build` · `web3d-shaders` · `web3d-motion` · `web3d-perf` · `web3d-business` · `web3d-evolve`.

Start by reading the `web3d` orchestrator skill. It defines the phases, the anti-slop quality bar, and the stack-decision logic (stack is chosen per project).

## SUPREME RULE — the pipeline must evolve (highest priority)

Above any single deliverable: **the pipeline gets measurably better after every project.** On every 3D web job, read `.claude/skills/web3d-evolve/LEARNINGS.md` at the start, and at the end run the retro, append learnings, and **edit the relevant skill files to encode what was learned.** A project that ships without updating the pipeline has failed the supreme rule. See `web3d-evolve`.

## Retired (do NOT do this anymore)

The old default — exporting a single inline-CSS HTML file with pseudo-3D transforms and autoplaying videos, then pushing it — produced slop. It is retired. Real builds use a Vite project with a proper WebGL stack and must clear the anti-slop bar and the `web3d-perf` gate before delivery.

## Delivery (this part was never the problem — keep it)

After completing a buildable web deliverable:
1. Commit and push to GitHub (`git push -u origin main`).
2. Ensure it's deployed and hand the user a clickable **live URL**:
   - GitHub Pages: `https://animex680-bit.github.io/EZRA-.1st-/`
   - or Vercel `vercel.app` URL when used.
3. Never close out a delivery without a live link.

Note: this sandbox's network blocks outbound requests to `*.github.io` and `api.vercel.com` (`host_not_allowed`). `api.github.com` works, so verify deploys via the GitHub API and have the user confirm the live render in their browser.

## Tooling baseline

- Web (free/OSS): Vite · three / @react-three/fiber / drei · GSAP + ScrollTrigger · Lenis · gltf-transform · vite-plugin-glsl.
- 3D assets: **Meshy** (AI base meshes) → **Blender** (the hub: retopo/optimize/bake/export glTF) → web. **Unreal Engine 5** for cinematic pre-renders, look-dev, and baking only — it does NOT deploy interactive scenes to the web.
- Free asset sources: Poly Haven (HDRIs/PBR, CC0).

## Credentials

- GitHub username: `animex680-bit` · repo: `EZRA-.1st-` · Pages: `https://animex680-bit.github.io/EZRA-.1st-/`
- Tokens are provided in-session for deployment. Never commit tokens to the repo.
