# Website Building 3.0 — Project Instructions

This repo IS the product: an adaptive, self-improving system for designing and shipping
premium 3D websites that sell. It was built from the analyzed workflows of the top
3D-web creators on YouTube and Instagram (see `research/`), and it is required to get
measurably better every time it is used.

## Read order (every session that builds a website)

1. `.claude/skills/wb3/SKILL.md` — the orchestrator. Always start here.
2. `FEEDBACK_LOG.md` — what the user has said NO to. Never repeat a logged rejection.
3. `.claude/skills/web3d-evolve/LEARNINGS.md` — technical lessons from past builds.
4. `research/PATTERNS.md` — the distilled creator playbook the pipeline encodes.

## The three laws (priority order)

1. **ADAPT.** Every "no", "don't like it", or lukewarm reaction is data. Run the
   `wb3-adapt` protocol: log it, diagnose the rule that produced it, edit that rule,
   rebuild. The system updates itself — the user should never have to reject the
   same mistake twice.
2. **SELL.** Every site must be built to produce business results — clear offer,
   proof, CTA path, conversion logic (`web3d-business`, `conversion-critic` agent).
   Beautiful but unsellable = failure.
3. **VERIFY.** Nothing ships without the `logic-check` agent's QA pass and the
   `web3d-perf` gate. No blank screens, no lorem ipsum, no stretched low-res assets,
   no broken claims.

## Assets — the 2K/4K rule

Sites need real assets. Per `wb3-assets`: either **ask the user for 2K–4K source
assets with a precise spec**, or **source free CC0 assets online** (Poly Haven,
ambientCG, Pexels, Google Fonts) — with procedural GLSL as the in-sandbox fallback.
Never silently stretch low-res material. Never fake-final a placeholder.

## Delivery (non-negotiable)

Commit → push → live URL (GitHub Pages or Vercel) handed to the user. Never close a
delivery without a clickable link. In sandboxes that block `*.github.io`, verify the
deploy via the GitHub API and ask the user to confirm the render.

## Evolution (supreme rule, inherited from web3d)

After every project: retro → append to `LEARNINGS.md` → edit the skill files to encode
what was learned. A project that ships without upgrading the pipeline has failed.
