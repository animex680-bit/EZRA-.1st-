# Sound Effects Library
## Every SFX Used — With Descriptions, Timing, and Sources

---

## SFX Philosophy

Sound design is half the impact of this editing style. A perfectly placed audio hit makes a visual element feel physical and real. Every SFX should have a reason to exist. If you remove the SFX and the edit still feels the same, the SFX was wrong.

**Volume rule:** Individual SFX should sit at -10 to -18dBFS so they blend under the music without overpowering it. The music is the star — SFX support it.

---

## Category 1 — Impact & Hit SFX

Used when text, shapes, or subjects slam into screen.

### SFX-01: Hard Impact / Thud
- **Description:** Low-end thud, like something heavy hitting a surface
- **Use:** When bold text punches in, on Twixtor snap moments, at the beat drop
- **Duration:** ~0.3-0.5 seconds
- **Volume:** -12dBFS (under music)
- **Source:** Freesound.org — search "impact thud"
- **File name:** `sfx_impact_thud.wav`

### SFX-02: Sub Bass Hit / Boom
- **Description:** Deep 808-style bass boom — felt more than heard
- **Use:** At the biggest moment in the edit (the DROP), major scene transitions
- **Duration:** ~0.5-1.0 seconds
- **Volume:** -8dBFS (prominent — this should be felt)
- **Source:** Splice.com free tier, or search "808 sub hit free SFX"
- **File name:** `sfx_sub_bass_boom.wav`

### SFX-03: Cinematic Impact Reverse
- **Description:** Reversed impact — builds tension BEFORE a hit
- **Use:** In the 0.5 seconds BEFORE a major impact (creates anticipation)
- **Duration:** ~0.3-0.7 seconds
- **Volume:** -14 to -16dBFS (subtle)
- **Source:** Artlist.io, Epidemic Sound, or Freesound.org
- **File name:** `sfx_impact_reverse.wav`

---

## Category 2 — Whoosh / Swipe SFX

Used during transitions and fast-moving elements.

### SFX-04: Fast Whoosh Left-to-Right
- **Description:** Air displacement sound, fast, directional
- **Use:** Shape wipe transitions, text sliding in from side
- **Duration:** ~0.2-0.4 seconds
- **Volume:** -14 to -16dBFS
- **Source:** Freesound.org — search "whoosh fast"
- **File name:** `sfx_whoosh_fast.wav`

### SFX-05: Deep Whoosh / Transition
- **Description:** Slower, deeper whoosh — more cinematic weight
- **Use:** Major scene transitions, the moment before the DROP
- **Duration:** ~0.5-0.8 seconds
- **Volume:** -12dBFS
- **Source:** Artlist.io, Freesound.org — search "cinematic whoosh deep"
- **File name:** `sfx_whoosh_deep.wav`

### SFX-06: Riser / Build Up
- **Description:** Tension-building rising tone/noise — creates anticipation
- **Use:** During the BUILD phase to increase energy; right before the PEAK
- **Duration:** 2-4 seconds (fades into the drop)
- **Volume:** -14 to -10dBFS (increases as it rises)
- **Source:** Many free cinematic SFX packs include risers
- **File name:** `sfx_riser_build.wav`

---

## Category 3 — Glitch & Digital SFX

Used on glitch effects, tech moments, crypto/digital aesthetic elements.

### SFX-07: Digital Glitch Burst
- **Description:** Short burst of digital noise, corrupted-data sound
- **Use:** Glitch transitions, distortion effects, error-code style moments
- **Duration:** ~0.1-0.3 seconds (very short)
- **Volume:** -12 to -14dBFS
- **Source:** Zapsplat.com (free with account), Freesound.org
- **File name:** `sfx_glitch_digital.wav`

### SFX-08: UI Click / Ping
- **Description:** Clean, crisp click — like a high-end UI interface
- **Use:** When tech/UI-style shape graphics appear, on counter animations
- **Duration:** ~0.05-0.1 seconds
- **Volume:** -16 to -18dBFS (very subtle)
- **Source:** Freesound.org, Zapsplat
- **File name:** `sfx_ui_click.wav`

### SFX-09: Static Burst
- **Description:** Brief static/electricity sound
- **Use:** At glitch moments, RGB channel split effects, on hard glitch cuts
- **Duration:** ~0.15-0.25 seconds
- **Volume:** -14dBFS
- **Source:** Freesound.org — search "static burst electricity"
- **File name:** `sfx_static_burst.wav`

---

## Category 4 — Texture / Atmospheric SFX

Used to add depth to quiet moments or behind lyric cards.

### SFX-10: Vinyl Crackle
- **Description:** Classic vinyl record surface noise — organic warmth
- **Use:** Behind slower, more introspective lyric moments; adds humanity
- **Duration:** Loops continuously (or until cut)
- **Volume:** -18 to -20dBFS (barely audible — more felt)
- **Source:** Freesound.org, many free vinyl loops available
- **File name:** `sfx_vinyl_crackle_loop.wav`

### SFX-11: Heart Beat / Deep Pulse
- **Description:** Low rhythmic pulse — felt in the chest
- **Use:** During the RESOLUTION phase; emotional slow-mo moments
- **Duration:** Looping pulse at ~60-80 BPM
- **Volume:** -14dBFS
- **File name:** `sfx_heartbeat_pulse.wav`

---

## Category 5 — Transition Specific SFX

Pre-matched to specific transition types (see `02-technical/02-transitions.md`).

| Transition Type | SFX to use | Timing |
|---|---|---|
| Hard Cut on Beat | Sub Bass Hit (02) | On the cut frame |
| Shape Layer Wipe | Deep Whoosh (05) | Starts 2 frames before wipe |
| Zoom Push | Fast Whoosh (04) | Simultaneous with zoom |
| Glitch Cut | Glitch Burst (07) + Static (09) | On the glitch frames |
| Color Flash | Sub Bass Hit (02) | On the flash frame |
| Slow-mo snap cut | Hard Impact (01) | On the hard cut frame |

---

## SFX Layering Guide

For maximum impact at the DROP/PEAK moment, layer these simultaneously:

```
Layer 1: Sub Bass Boom (SFX-02) — -8dBFS
Layer 2: Impact Reverse (SFX-03) — starts 0.5s before, -16dBFS
Layer 3: Riser (SFX-06) — fades into the drop, -12dBFS fading
```

All three timed to the exact beat hit. This is what makes the impact feel physical.

---

## SFX Storage Location in Repo

```
03-assets/sfx/files/
  ├── sfx_impact_thud.wav
  ├── sfx_sub_bass_boom.wav
  ├── sfx_impact_reverse.wav
  ├── sfx_whoosh_fast.wav
  ├── sfx_whoosh_deep.wav
  ├── sfx_riser_build.wav
  ├── sfx_glitch_digital.wav
  ├── sfx_ui_click.wav
  ├── sfx_static_burst.wav
  ├── sfx_vinyl_crackle_loop.wav
  └── sfx_heartbeat_pulse.wav
```
