---
name: web3d-motion
description: Motion design system for 3D and high-end websites — smooth scroll (Lenis), GSAP ScrollTrigger choreography, easing curves, transition systems, and scroll-driven camera/animation. Use when implementing animation and scroll behavior on a 3D or premium web build. Part of the web3d pipeline.
---

# web3d-motion — Motion System

Slop animates with ad-hoc `requestAnimationFrame` loops and linear timing. Premium sites have a *motion language*: one easing family, choreographed timing, and scroll as the narrative spine.

## REQUIRED signature techniques (learned from real feedback — bland = rejected)

These are not optional flourishes; their absence is what made past work "bland". A premium scroll experience must do all of:

1. **Scroll CREATES the content — scrubbed, not triggered.** As text comes into view, characters should look like they are being *generated and arranging themselves in lock-step with the scroll position* — letter/word reveal scrubbed by scroll progress (split into chars/words, map each to a slice of the scroll range). Scroll up = they un-create. The scroll position IS the animation timeline, not a one-shot trigger. Never a single fade-up when blip/assembly is wanted.
2. **Scroll-as-scrubber, not travel.** Pin a stage (sticky), give it a tall scroll track, and map scroll progress to `video.currentTime` (or a timeline). Scrolling scrubs the video forward; stopping freezes it; scrolling up plays it backward. The viewport shouldn't feel like it "goes down" — the scroll is a playhead. Lerp the mapped value for glide.
3. **Seamless, edgeless section transitions.** NO hard boundaries between sections. When one stage's scrub completes, slip into the next (continuous/shared background, crossfade, no visible divider). It should feel like a blip/morph, not a page break.
4. **Nothing is ever stagnant.** Every tile (word, image, video card) perpetually drifts — gentle, smooth, varied (some vertical, some horizontal), never violent. Use per-tile phase offsets so the field breathes organically.
5. **Cursor-reactive tiles.** On pointer proximity, tiles react — mostly **evade** the cursor, but a few are **drawn toward** it. Spring/lerp back to base. Living and playful, not decorative.
6. **Typography is the hero.** A characterful editorial type pairing, treated as the centerpiece — never bland/default. Bland type alone makes a whole site read cheap.

7. **Settled text must be perfectly legible.** The scatter is for the *journey only*. At full progress (p=1) characters must land at a clean typographic baseline — zero residual rotation/offset/blur. Animate FROM scattered/blurred TO crisp rest; never leave an awkward in-between as the readable state.
8. **Circle-blip (iris) transitions.** A premium way to move between video stages: fade to dark, then grow a small circle (`clip-path: circle()`) from a point to full-screen, revealing what the darkness hid (the next video). Reversible on scroll.
9. **Buttons are reactive and glow.** No dead/flat buttons. On pointer proximity they should glow (box-shadow/radial bloom in the brand accent) and be slightly magnetic (translate toward the cursor, spring back). Applies to every clickable.
10. **Decorative "snake/ribbon" lines.** A long, slow-slithering ribbon (SVG path with animated control points, or stroke-dashoffset travel) can thread a section together. Rules: color blends with the background (low distraction), and it renders UNDER tiles/buttons (lower z-index) — never over interactive/content tiles.
11. **Spiral case-study gallery (the money mechanic).** Arrange project media in a downward near-spiral; tap a tile → it plays AND surfaces a case-study card with the **project cost** and **why it fits that customer**. Concrete proof + price + fit is what converts browsers to buyers (see web3d-business). Use this whenever a page must *sell*, not just impress.

(When WebGL can't be verified — see web3d-build verifiability rule — implement ALL of the above in plain DOM/CSS/JS + a scrubbed `<video>`. None of it requires WebGL.)

## The stack

- **Lenis** — smooth/inertial scroll. Foundation of the premium feel. Sync it to GSAP's ticker and to the R3F render loop.
- **GSAP + ScrollTrigger** — the choreography engine. Timelines, scrubbing, pinning, staggers.
- (Optional) **Theatre.js** — visual keyframing for complex camera/3D sequences.

Wire-up: drive `lenis.raf` from `gsap.ticker`, call `ScrollTrigger.update` on Lenis scroll, and in R3F read scroll progress into uniforms / camera each frame.

## Easing — pick a family and hold it

- Default expressive ease: `cubic-bezier(.2,.7,.2,1)` (the "premium glide" — decelerate hard).
- Use `power3/power4/expo` for entrances, `back`/`elastic` sparingly for personality.
- **Never linear** except continuous loops. Linear motion is the tell of an amateur build.
- One duration scale (e.g. 0.4 / 0.8 / 1.2s). Consistency = polish.

## Choreography principles

- **Stagger** related elements (60–120ms) so things arrive as a phrase, not a blast.
- **Orchestrate, don't decorate** — entrances should support the concept, not fire randomly.
- **Scroll-scrub the hero/3D** — tie camera position, shader `uProgress`, and section reveals to a single scroll timeline (the storyboard from web3d-concept).
- **Pin + reveal** for narrative sections (sticky scene, content advances).
- **Restraint** — premium = fewer, better moves. If everything moves, nothing reads.

## Performance of motion

- Animate **transform/opacity only** for DOM (GPU-composited). Never animate layout (width/top/left).
- For 3D, mutate object/material/uniform values in the loop; don't recreate objects.
- Respect `prefers-reduced-motion`: kill scrubbing/parallax, keep instant states. Build this in from the start, not as an afterthought.
- Throttle pointer/scroll handlers; ease pointer values (lerp) instead of using raw input.

## Don't

- Don't stack independent rAF loops fighting each other (our old bug). One loop / one ticker.
- Don't animate everything. Don't use bounce/elastic on a luxury brand.

Implements the storyboard from `web3d-concept`; bounded by `web3d-perf`.
