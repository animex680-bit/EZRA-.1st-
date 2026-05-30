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

## 2026-05-30 (b) — AluCape vista upgrade (real Cape Town backdrop)
- Goal: replace the placeholder gradient behind the door with a real Cape Town vista.
- BLOCKER discovered: sandbox network allowlist blocks ALL the usual CC0 photo/HDRI hosts — upload.wikimedia.org, images.unsplash.com, commons.wikimedia.org, dl.polyhaven.org all return 403. Only raw.githubusercontent.com (301/reachable). So "download a free photo" is NOT available in-sandbox.
- Decision: built a **procedural Cape Town vista shader** instead (Vista.jsx) — sunset sky + sun glow, Table Mountain flat-top silhouette with Devil's Peak + Lion's Head, atmospheric haze, shimmering waterline, film grain + vignette; warms/brightens via `uReveal` tied to door progress. Cost: +1.3KB (vs a multi-hundred-KB photo). Original, instant, on-brand, no licensing.
- Worked: procedural backdrop is a strong default when assets can't be fetched; doubles as more "moat." Reused the same eased-uniform pattern (uReveal lerp in useFrame).
- Caveat: a hand-tuned silhouette in GLSL is approximate — needs the user's eyes to judge if Table Mountain reads correctly (can't render here). If they want photoreal, they must supply an image file directly (I can base64/import it) since I can't fetch one.
- SKILL EDITS made from this project (b):
  - web3d-assets: document the sandbox asset-host block + "procedural backdrop as fallback" pattern, and that user-supplied image files are the path to photoreal here.

## 2026-05-30 (c) — CRITICAL: shipped a blank WebGL screen, twice. Pivoted to video.
- What happened: user reported "don't see anything" on the live R3F page. I had shipped TWO WebGL versions I could never render-test (no browser engine in sandbox + github.io firewalled from agent side). Almost certainly blank.
- ROOT CAUSE (high confidence): `<Environment preset="sunset" />` (drei) **fetches an HDRI from a CDN at runtime** and was inside the SAME `<Suspense>` as the whole scene. If that fetch is slow/blocked/CORS-fails in the user's browser, NOTHING in the Suspense mounts → black screen. There was also no error boundary and no non-WebGL fallback actually visible.
- THE REAL LESSON (promote hard): **Never ship WebGL I cannot render-test as the primary deliverable.** When I can't open a browser, an unverifiable WebGL page is a coin-flip. Default to something that renders deterministically (static HTML + `<video>`), and treat WebGL as an enhancement only when there's a way to verify it.
- Additional rules learned:
  - drei `<Environment preset=...>` = runtime CDN fetch. For self-contained/offline-safe builds, DON'T use presets; use a bundled local HDRI or a plain lighting rig. Never put a network-dependent loader as the sole child of the only Suspense.
  - Always include a VISIBLE fallback + an error boundary around the Canvas, so a WebGL/asset failure shows content, not black.
- THE FIX SHIPPED: rebuilt /alucape/ as a dependency-free static page (no build step, no WebGL, no CDN except Google Fonts) driven by the user's TWO real aluminium animation videos (H.264, 8s, ~1MB each): hero = looping bg video; reveal = sticky video scrubbed by scroll (currentTime tied to scroll progress) + zoom-out. This WILL render.
- Videos provided by user are ideal: H.264/avc1, web-ready, no transcode needed.
- SKILL EDITS made (c): web3d-build — add the "don't ship unverifiable WebGL / Environment preset = network fetch / always have visible fallback+error boundary" rules, and a "video-driven page" as the safe default when WebGL can't be verified.

## 2026-05-30 (d) — Feedback: "bland". Direction crystallized into a real motion language.
- User feedback verbatim intent: the procedural topography (Table Mountain shader) AND the text animations were **bland/"blend"**. Plain fade-up reveals are not enough. Static anything reads as cheap.
- The vision the user actually wants (this is now a core anti-slop standard — promote to web3d-motion):
  1. **Scroll CREATES the words.** As you scroll and text is about to appear, the characters should look like they're being *generated and arranging themselves in sync with the scroll* — scrubbed letter-by-letter, not a one-shot transition. Scroll back = they un-create. The scroll position IS the timeline.
  2. **Scroll drives the video, you don't travel.** Pinned stage (sticky): scrolling scrubs the video forward; stop scrolling = video freezes; scroll up = plays backward. The viewport doesn't "go down" — the scroll is a scrubber, not a translator. (Sticky + tall track + currentTime scrub; lerp for glide.)
  3. **Seamless section blips — NO hard edges.** When the video ends you don't hit a boundary; you slip into another section. Continuous background, crossfades, no visible dividers between sections. "Feels like a blip / a transition without a seam."
  4. **Tiles are never stagnant.** Every tile (word or video) perpetually drifts — up/down, some left/right — slightly, smoothly (never violent). On cursor proximity tiles REACT: mostly evade, but some are drawn toward the cursor. Living, physical, playful.
  5. **Typography must be super aesthetic.** Bland system-ish type kills it. Use a characterful, editorial pairing and treat type as the hero.
- Implementation decision: deliver ALL of this in plain DOM/CSS/JS + scrubbed `<video>` (no WebGL) — keeps it within the verifiability rule (renders deterministically) while being far from bland.
- SKILL EDITS made (d): web3d-motion — add "scroll-creates-the-words" scrubbed text assembly, scroll-as-scrubber pinned video, seamless/edgeless section transitions, and perpetual + cursor-reactive (evade/attract) tiles as required techniques; web3d (orchestrator) anti-slop bar — add "no stagnant tiles" and "no hard section edges".
