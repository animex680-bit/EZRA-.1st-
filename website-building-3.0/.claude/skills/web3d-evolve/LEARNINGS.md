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

## 2026-05-30 (e) — Feedback round 2: text legibility, circle-blip transition, money-skill, longer page, snake line, spiral case-studies, RESOLUTION + ASK rules
- WINS: scrubbed video (1), scroll-built words (2), cursor-reactive tiles (3) all landed. Text *animation* good.
- FIX — text PLACEMENT: chars settle into positions that are hard to read ("weird since I can read them" = the in-between/settled layout is awkward). Lesson: the scatter is for the *journey*; the SETTLED state must be a clean, perfectly-legible baseline (no leftover rotation/offset). Animate FROM scatter TO a crisp typographic rest. Don't leave residual transform at p=1.
- NEW MECHANICS REQUESTED:
  - **Circle-blip transition** between video 1 → video 2: screen goes dark, then a small circle grows (iris/clip-path circle reveal) exposing the 2nd video that the darkness was hiding. Use it as the section-to-section reveal.
  - **All buttons reactive + glow** (hover/pointer-proximity glow, magnetic).
  - **Longer page** overall.
  - **Snake/worm line** in section 3: a long, 3–5cm-wide ribbon that slithers across/between tiles, color blends with bg (low distraction), and renders UNDER tiles/buttons (z below them), over the bg.
  - **Spiral case-study gallery**: photos/videos arranged in a downward near-spiral (like the start of inspiration_6.mp4). Tap a tile → it plays AND shows the project COST + why it's a fit for that customer (a recommendation/case-study card). This is the money/business mechanic — pulled from web3d-business: concrete case studies w/ price + fit = what converts.
  - Apply **web3d-business** thinking to the page itself: proof, case studies w/ price, clear CTA path.
- RESOLUTION RULE (now permanent in web3d-assets): never stretch low-res (<1080p) video; small footage → small tiles at native size only; fullscreen/stretch needs 2K+ source; if missing, ASK.
- ASK-FOR-ASSETS RULE (now permanent): proactively ask the user for assets at correct resolution with a precise spec; never silently stretch or fake-final a placeholder.
- inspiration_6.mp4: 1200px, 22s — reference for the spiral gallery look. (Reference only; not used as site footage — also <2K so wouldn't be stretched anyway.)
- No ffmpeg/ffprobe in sandbox — cannot transcode/resize video here; depend on user-supplied correctly-sized assets.
- SKILL EDITS made (e): web3d-assets — added RESOLUTION RULE + ASK-FOR-ASSETS RULE; web3d-motion — add circle-blip (iris) transition, reactive+glowing magnetic buttons, snake-ribbon-under-tiles, spiral case-study gallery w/ price+fit card; settled-text-must-be-clean rule.

## 2026-05-31 (f) — Real footage wired in
- User supplied ~11 real clips. Probed: ALL low-res (1024x768 or IG-reel sized), NONE 2K+. Per resolution rule: nothing stretched fullscreen; hero/reveal framed in a window, projects in small tiles. inspiration_6.mp4 + 7240a738 = spiral references only.
- Spiral gallery now 8 distinct real projects. Prices = ESTIMATED RANGES ("Est. R Xk-Yk"), clearly marked — real numbers unavailable and IG/site are firewalled (403) from sandbox. Honesty rule: never present invented figures as real; labelled estimates + asked user for actuals.
- Perf debt (TODO before any real delivery): ~48MB total media across 10 clips, 8 video pins all created up-front. Add preload=none / lazy attach for offscreen pins; still need a real 2K hero to ever do a fullscreen stretch.
- No ffmpeg/ffprobe in sandbox: cannot transcode/resize; fully dependent on user-supplied correctly-sized assets. Reinforces ASK-FOR-ASSETS rule.
- SKILL EDITS made (f): none to craft skills (wiring + assets round only).

## 2026-06-12 — Website Building 3.0: creator research + the wb3 system built
- Task: research the top 3D-website personal brands (14 creators, 50/50 IG/YouTube, last 1–2 months) and build an adaptive website-creation system from the data. Output: `website-building-3.0/` package (intended for its own repo "Website-building-3.0" — creation blocked: GitHub App token 403 on create_repository; needs the app installed on a user-created repo).
- Key research findings (full evidence in website-building-3.0/research/):
  - The consensus process spine across all top creators matches our pipeline (reference → tokens → Blender bake → scroll spine → signature shader → perf gate → ship → productize). Validation, not revolution.
  - NEW: tokens-before-generation (Oliur/Relume, Figma MCP) is the documented fix for AI-generic output; 2–3 directed revision rounds is the verified norm; direction specificity is the quality lever.
  - 2026 shader meta is shifting GLSL → TSL/WebGPU (r183, Safari 26); never write r18x APIs from memory (Greenheck built a Claude skill precisely for this).
  - Business: at the client tier, an Awwwards SOTD beats 100K followers; the "AI pipeline + real WebGL" lane is nearly unoccupied and validated at the top (Revelium: Claude Code + Cursor + Codex over three.js/SDF for Prada/Meta).
- New system pieces: wb3 orchestrator skill, wb3-research / wb3-assets / wb3-adapt skills, 4 agents (logic-check QA gate, conversion-critic, asset-scout, trend-scout), ADAPT.md rejection-rewrites-the-rules protocol + FEEDBACK_LOG.md + taste profile.
- SKILL EDITS made from this research: web3d-build (tokens-before-generation, debug-UI-day-one, TSL/WebGPU policy), web3d-shaders (TSL shift + no-APIs-from-memory), web3d-business (productization flywheel, awards-beat-followers, unoccupied-lane positioning), wb3 (revision-rounds doctrine). Edits made in the website-building-3.0 package copies — that package is the go-forward pipeline.
