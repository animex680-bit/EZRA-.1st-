---
name: wb3-assets
description: Asset acquisition decision layer for Website Building 3.0 — for every asset slot, either request 2K–4K source material from the user with a precise spec, or source free CC0 assets online (Poly Haven, ambientCG, Pexels, Google Fonts, Meshy→Blender), with procedural GLSL as the sandbox fallback. Use during the ASSETS phase, with the asset-scout agent. Wraps web3d-assets.
---

# wb3-assets — Get the right pixels, never fake them

`web3d-assets` covers the production pipeline (Meshy → Blender → compressed glTF).
This skill covers the **acquisition decision** that comes first: for every asset the
concept needs, choose one of three paths — and never ship a fourth (the silent
placeholder/stretch).

## Step 1 — Asset manifest

From the signed-off concept, list every asset slot in a table:

| slot | purpose | type | display size | min source res | loop? | path (step 2) |
|------|---------|------|--------------|----------------|-------|---------------|

Display size determines the resolution floor (RESOLUTION RULE, web3d-assets):
fullscreen/hero-cover → **2K (2048px) minimum, 4K preferred**; large tile → 1080p+;
small tile → native size only.

## Step 2 — Route each slot (in this order)

1. **FREE** — can a CC0/free source genuinely fill it at the required resolution?
   - HDRIs / PBR textures / 3D models: **Poly Haven**, **ambientCG** (CC0)
   - Photos / video: **Pexels**, **Unsplash**, **Pixabay** (check license terms)
   - Type: **Google Fonts** / **Fontshare** (characterful pairings only — type is the hero)
   - Base meshes: **Meshy** free tier → Blender cleanup (never ship raw)
   - Sandbox caveat: many of these hosts are firewalled from the agent side
     (Poly Haven, Unsplash, Wikimedia returned 403 — see LEARNINGS). If blocked,
     either give the user the exact download links + filenames to drop into the
     repo, or fall through to PROCEDURAL.
2. **PROCEDURAL** — author it: GLSL backdrop/sky/silhouette shaders, generative
   particles, CSS/SVG textures, geometry built in code. A few KB, original,
   license-free, on-brand. Often *better* than stock (proven: AluCape vista).
3. **ASK THE USER (2K–4K)** — when the slot needs real footage/photos of the actual
   business, or nothing free/procedural can carry it. This is not a fallback of
   shame; bespoke 2K–4K source material is what separates a premium site from a
   template. Ask early — at concept sign-off, not mid-build.

## The ask format (always this precise)

Group ALL asks into one list so the user shoots/collects once:

```
ASSET REQUEST — [project]
1. Hero video — the workshop in motion, slow pan.
   Spec: 3840×2160 (4K) or min 2560×1440 · landscape 16:9 · 8–15s · loopable ·
   H.264/H.265 MP4 · steady camera or gimbal.
2. Product stills — 6–10 photos of finished installations.
   Spec: min 2048px on the long edge · JPEG/HEIC fine · daylight, no filters.
...
Why: anything below these resolutions cannot be shown large without looking soft —
small sources will only ever appear as small tiles (quality rule, non-negotiable).
```

## Hard rules (inherited, never skip)

- **RESOLUTION RULE**: never stretch sub-1080p sources; fullscreen needs 2K+.
- **ASK-FOR-ASSETS RULE**: a missing right-res asset = a written ask, never a silent
  stretch or a fake-final placeholder. Label every placeholder visibly.
- Licensing: CC0 preferred; anything else, record source + license in the manifest.
- Everything 3D still flows through web3d-assets: Blender → Draco/meshopt glTF +
  KTX2; hero model < 2–3MB; no 8K HDRIs to the browser.
- No ffmpeg in sandbox: video must arrive web-ready (H.264/H.265 MP4) — put that in
  the spec so the user's files need no transcode.

Output of this skill = completed manifest, every slot routed, asks sent. That is the
phase-3 gate: build does not start while a slot is unrouted.
