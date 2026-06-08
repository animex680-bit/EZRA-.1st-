# Motion Principles
## How Things Move, Timing Rules & Easing

---

## The Core Philosophy

**Everything moves on the beat. Nothing moves for no reason.**

Every animation, transition, cut, text entrance, and effect must be locked to a musical event — a kick drum, snare, hi-hat, vocal hit, bass drop, or melodic phrase. If you can't point to the exact audio cue that triggers a motion event, that event shouldn't be there.

---

## Beat Mapping — The Foundation

Before animating a single thing, map the music.

### Step 1: Find the BPM
- In After Effects: use a free plugin like **BeatEdit** or manually tap the spacebar in time
- In DaVinci Resolve: use Fairlight to view waveform and mark beats

### Step 2: Set up a Beat Grid
- Calculate frame interval: `(60 / BPM) × frame_rate = frames per beat`
- At 24fps, 120BPM: `(60/120) × 24 = 12 frames per beat`
- At 24fps, 140BPM: `(60/140) × 24 ≈ 10 frames per beat`
- Mark every beat as a composition marker (M key in AE)
- Also mark downbeats (every 4 beats) with a different color marker

### Step 3: Identify Key Hits
- Kick drums = primary animation cue (scale punches, cuts)
- Snare / clap = secondary cue (text exits, flash effects)
- Bass sub drops = biggest moments (Twixtor end, scene climax)
- Vocal phrase starts = text entrances

---

## Animation Timing Rules

| Motion Type | Duration | Rule |
|---|---|---|
| Hard cut (scene change) | 0 frames | Must land exactly on beat |
| Text entrance | 6-12 frames | Starts 2-4 frames BEFORE the beat so it resolves ON the beat |
| Text exit | 4-8 frames | Exits on the beat after its hold duration |
| Shape graphic appear | 4-6 frames | On beat |
| Shape graphic disappear | 2-4 frames | Hard disappear or very fast scale-out |
| Twixtor slow-mo begin | 0 frames | Ramp begins on beat or 2 frames before |
| Transition (wipe/zoom) | 8-16 frames | Begins on beat, resolves on next beat |
| Gradient gradient animation | Continuous loop | Smoothly looping, not beat-locked |
| Camera shake | 4-8 frames | Peaks on the hit, decays over next 4 frames |

---

## Easing Curve Reference

These are the actual curve shapes to use in the Graph Editor (After Effects) or Fusion (Resolve):

### Ease Out — "Punch In"
Used for: Text entrances, shape appearances, scale punches
```
Start: Very fast
End: Comes to a stop smoothly
Bezier handles: Right handle pulled far left (steep departure)
Shortcut feeling: Like a ball thrown hard that stops abruptly
```

### Ease In — "Soft Exit"
Used for: Elements leaving screen, Twixtor ramp-down
```
Start: Slow
End: Accelerates away
Bezier handles: Left handle pulled far right
```

### Overshoot (Ease Out with bounce)
Used for: Scale punches, impact moments
```
Scale keyframes: 100% → 110% → 98% → 100%
Over frames:    0  →  3   →  6  →  9
Creates a "thump" feeling without actual spring physics
```

### Linear — "Snap"
Used for: Hard cuts, flash frames, glitch effects
```
No easing handles — straight line
Creates mechanical, aggressive motion
```

### Custom S-Curve
Used for: Smooth position moves (camera parallax, floating elements)
```
Slow start → fast middle → slow end
Classic "cinematic" camera move feel
```

---

## Speed Ramping with Twixtor

Speed ramping is one of the most important motion techniques in this style.

### Standard Speed Ramp Pattern
```
Normal speed (100%) → 
  Build up over 0.5s → 
    Peak normal (or slight fast, 110-120%) → 
      SNAP to ultra slow (8-15%) at the hit → 
        Hold slow for 1-3 seconds →
          Ramp back to normal (100%) over 0.5-1s
```

### Twixtor Settings for Smoothest Results
- Source frame rate: Match to your footage (24, 30, 60fps)
- Output frame rate: Match to your comp (usually 24fps)
- Motion Sensitivity: 0.5-1.5 (lower = less ghosting on complex motion)
- Smart Blend: ON
- Enable Frame Blending: Pixel Motion (best quality)
- Source: Set to the CLIP'S original fps before ramping

### Best Footage for Twixtor
- 60fps source ramps to 24fps comp = excellent (250% stretch headroom)
- 120fps or 240fps source = near-perfect slow-mo with Twixtor
- 24fps source = works but will show artifacts at extreme slow speeds — keep above 20% speed

### Where to Place Speed Ramps
- Just before the drop or bass hit (the anticipation)
- During a subject's turn, hair movement, fabric motion
- On a gesture (hand raise, pointing, throwing something)
- At the emotional peak of a lyric

---

## Transitions — Motion Rules

Full detail in `02-technical/02-transitions.md`, but the motion principles:

1. **Transitions resolve on the beat** — the new scene lands exactly on the musical hit
2. **Direction is consistent within a sequence** — don't mix left-wipe and right-wipe in the same edit
3. **Zoom direction** — zoom IN when energy increases, zoom OUT when pulling back
4. **Flash frames** — a single white or black frame (1-2 frames) on a hard cut amplifies impact
5. **Transitions are not decoration** — use only when the music or narrative calls for them. Default is hard cut.

---

## Particle and Floating Element Motion

Background particles (bokeh, dust, embers) always:
- Move upward (subtle, slow drift)
- Speed: 5-20% of frame height per second
- Opacity: 10-30% max
- Scale variation: random 10-80% of base size
- Never move sideways — always vertical drift

---

## Camera Motion (for tripod or handheld footage)

If the source footage is stabilized (or shot on tripod), you can ADD synthetic camera motion:
- `Warp Stabilizer` to lock it down first
- Then apply `CC Jitter` or position keyframes to simulate very subtle drift
- On beats: add `Camera Shake` via expressions or preset — max 10-15px horizontal/vertical

---

## The "Gravity Rule" for Text Position

Text elements follow a gravity metaphor:
- **Entrances:** Text arrives from below (slides up) — gravity being overcome
- **Exits:** Text leaves upward (continues the momentum) or drops down (gravity wins)
- Never have text exit in the opposite direction it entered without a reason
- Exception: A "snap back" glitch-style exit (reverses the entrance path) is acceptable as a stylistic choice
