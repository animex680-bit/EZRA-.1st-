---
name: web3d-motion
description: Motion design system for 3D and high-end websites — smooth scroll (Lenis), GSAP ScrollTrigger choreography, easing curves, transition systems, and scroll-driven camera/animation. Use when implementing animation and scroll behavior on a 3D or premium web build. Part of the web3d pipeline.
---

# web3d-motion — Motion System

Slop animates with ad-hoc `requestAnimationFrame` loops and linear timing. Premium sites have a *motion language*: one easing family, choreographed timing, and scroll as the narrative spine.

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
