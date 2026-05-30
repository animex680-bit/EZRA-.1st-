---
name: web3d-assets
description: 3D asset production pipeline for the web — Meshy (AI generation) to Blender (cleanup/optimize) to compressed glTF, plus Unreal Engine 5 for cinematics and baking. Use when a 3D web project needs custom models, textures, HDRIs, or pre-rendered cinematic content. Part of the web3d pipeline.
---

# web3d-assets — Asset Pipeline (Meshy · Blender · UE5 → Web)

The web cannot eat raw 3D assets. Every model ships through Blender and leaves as compressed glTF. This is where "custom and original" beats "placeholder slop."

## Tool roles (be honest about each)

- **Meshy (AI 3D)** — fast text/image-to-3D for base meshes and ideation. Output is heavy, often non-manifold, bad topology, oversized textures. NEVER ship Meshy output directly. It's a starting block, not a deliverable.
- **Blender (the hub)** — everything passes through here: retopo/decimate, UV check, bake, material setup, and export. This is the single source of web-ready assets.
- **Unreal Engine 5** — **cannot deploy interactive scenes to a normal website** (web export deprecated; Pixel Streaming needs paid cloud GPUs, only on big budgets). Real UE5 jobs for us:
  1. **Cinematic pre-renders** (Sequencer → mp4 / image sequence) used as hero video or scroll-driven video textures. Often the smartest, cheapest "3D" for a marketing site.
  2. **Look-dev / lighting reference** (Lumen) to match in three.js.
  3. **Baking** high-detail Nanite meshes down to game-res + baked maps, then export to Blender → glTF.

## The web asset workflow

1. **Generate / source** — Meshy for bespoke base mesh, or model from scratch in Blender, or Poly Haven for HDRIs/PBR textures (free, CC0).
2. **Clean in Blender** — retopologize or `Decimate`; aim for the lowest tri-count that holds the silhouette. Apply transforms, recalc normals, single closed mesh where possible.
3. **UV + bake** — sane UVs; bake high→low for normal/AO if you sculpted detail. Combine maps where you can (ORM packing: AO/Roughness/Metalness into RGB channels).
4. **Texture budget** — resize to the smallest that looks right (512–2048). Power-of-two. You'll convert to KTX2 next.
5. **Export glTF (.glb)** with:
   - **Draco** geometry compression
   - or **meshopt** (often better for web + faster decode)
6. **Post-process** with `gltf-transform` (CLI):
   - `gltf-transform optimize in.glb out.glb --texture-compress ktx2` (or run `etc1s`/`uastc`)
   - prune unused, dedup, weld, resample animations.
7. **Verify** — drop into the build, check it renders, check size. Targets: hero model < ~2–3MB, secondary < 500KB.

## Sandbox constraint + procedural fallback (learned — see LEARNINGS)

In this remote environment the network allowlist **blocks the usual CC0 asset hosts** (Wikimedia/`upload.wikimedia.org`, Unsplash, Poly Haven `dl.polyhaven.org` all 403). You generally **cannot download a free photo/HDRI in-sandbox**. Two paths:
- **Procedural backdrop shader** — when you need a scene/sky/landscape and can't fetch one, author it in GLSL (sky gradient + sun glow + silhouettes + haze + grain). It's a few KB, original, instant, and on-brand — often a *better* call than a stock photo. (Done for the AluCape Table Mountain vista.)
- **User-supplied files** — the only route to photoreal here. Have the user drop an image/HDRI into the upload dir; import it (or base64-inline small ones). Then run it through the normal compression rules below.

## Hard rules

- No Meshy output ships unretopologized.
- No uncompressed glTF in production (Draco/meshopt + KTX2 always).
- HDRIs: use a small (1–2k) env map; don't ship 8k HDRIs to the browser.
- If the "3D" can be a pre-rendered UE5/Blender cinematic at 1/10th the engineering cost and risk, strongly consider it — interactive isn't always the right call.

Feeds `web3d-build` (load the .glb) and is gated by `web3d-perf` (sizes).
