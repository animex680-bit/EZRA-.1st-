# Scene Structure
## Video Anatomy, Pacing & Beat Architecture

---

## Standard Reel Structure (20-60 seconds)

Every 0x100x video follows a predictable emotional arc. The exact timestamps flex based on music length, but the proportions stay constant.

```
┌─────────────────────────────────────────────────────────┐
│  HOOK           0s – 2s    (0 – 8% of total duration)   │
├─────────────────────────────────────────────────────────┤
│  BUILD          2s – 10s   (8% – 33%)                   │
├─────────────────────────────────────────────────────────┤
│  PEAK / DROP    10s – 25s  (33% – 65%)                  │
├─────────────────────────────────────────────────────────┤
│  RESOLUTION     25s – 35s  (65% – 90%)                  │
├─────────────────────────────────────────────────────────┤
│  LOOP / CLOSE   35s – end  (90% – 100%)                 │
└─────────────────────────────────────────────────────────┘
```

---

## Phase Breakdown

### Phase 1: HOOK (0 – 2s)
**Goal:** Stop the scroll. Demand attention instantly.

**What happens:**
- The first frame is visually LOUD — either a bold text statement filling the screen, or the gradient character reveal at its most vibrant
- No slow fade-ins. The edit starts at full intensity
- Audio: Either drops straight into the beat, or opens on a single sound design hit
- Camera: The most compelling framing of the subject is on screen by frame 3

**Common patterns:**
- Full-frame bold text: "DON'T SCROLL." or the first lyric line
- Subject silhouette with gradient — zoomed into face/eyes
- Hard cut from black with audio hit simultaneously

**Anti-patterns to avoid:**
- Fade from black (too slow)
- Logo/intro card
- Silence before music starts

---

### Phase 2: BUILD (2s – 10s)
**Goal:** Establish the visual world. Introduce the subject, the rhythm, the look.

**What happens:**
- First 3-4 scene clips play — each 1-3 seconds long
- Beat-synced cuts establish the edit's rhythm
- Typography begins appearing — supporting text, name cards, first lyric fragments
- Color grade is now fully present
- Shape layer graphics start appearing on beats
- Energy rises progressively

**Common patterns:**
- 3-5 quick cuts of the subject from different angles
- Each cut paired with a text element
- Cinematic bars confirmed (always on by this point)
- Background particle system visible
- Speed ramp: one minor ramp as a preview of what's coming

**Clip length in this phase:**
- Clips: 1.0 – 2.5 seconds each
- Number of clips: 4-6 total
- Total cuts: matches beats (1 per beat or 1 per 2 beats)

---

### Phase 3: PEAK / DROP (10s – 25s)
**Goal:** Maximum visual and emotional impact. This is the reason the video exists.

**What happens:**
- The biggest Twixtor slow-mo moment happens here
- The gradient character animation plays at its most complex/vibrant
- The most important lyric or statement is on screen
- Highest density of visual layers: video + gradient + shape graphics + text + particles + overlays
- Camera shake on the hit
- Optional: brief flash frame (1-2 frames of white or black) at the drop moment

**Common patterns:**
- Slow-mo peak → snap back to normal speed → hard cut
- Text statement fills screen while gradient plays
- Stack of elements: subject (bottom) + gradient treatment + shape frame + bold text + grain overlay
- Multiple text layers cycling through stacked statements

**Clip length in this phase:**
- Pre-ramp clip: 2-4 seconds (building)
- Ramp/slow-mo clip: 1.5-4 seconds (stretched)
- Post-ramp clips: 1-2 seconds each (faster cutting now)
- Total clips: 5-8 in this phase

---

### Phase 4: RESOLUTION (25s – 35s)
**Goal:** Release the energy. Let the viewer breathe but stay engaged.

**What happens:**
- Pacing slightly relaxes (2-3s clips instead of 1-2s)
- Typography becomes secondary — subject is the focus
- Last important lyric or statement on screen
- Gradient treatment may simplify (single color shift rather than full spectrum)
- Energy plateaus rather than continues rising

**Common patterns:**
- Subject in profile or partial silhouette
- Single line of text holding on screen longer (3+ seconds)
- Music may transition to a quieter or melodic section
- Shape graphics fewer and simpler

---

### Phase 5: LOOP / CLOSE (35s – end)
**Goal:** Satisfying exit or loop point for Reels algorithm engagement.

**What happens:**
- Either: a direct call to action ("FOLLOW", "SAVE THIS", account handle)
- Or: returns to the visual energy of the Hook for a seamless loop
- The final 1-2 seconds often intentionally create curiosity (partial text, fading gradient) to encourage replay
- Outro logo/brand mark if applicable — very minimal, bottom center

**Common patterns:**
- Bold account handle (@0x100x style) fades in at bottom
- Final text hold: the most quotable line of the edit
- Hard black cut (abrupt end — this is intentional, not sloppy)
- Or hard return to opening frame (true loop)

---

## Scene Cutting Frequency Guide

| Phase | Avg clip length | Cuts per 4 beats |
|---|---|---|
| Hook | 0.5 – 1.5s | 4-8 cuts |
| Build | 1.0 – 2.5s | 2-4 cuts |
| Peak | 0.5 – 2.0s (varies with ramp) | 2-6 cuts |
| Resolution | 2.0 – 3.5s | 1-2 cuts |
| Close | 3.0 – 5.0s | 0-1 cuts |

---

## Layer Stack (what's on screen at the same time)

At peak density (during the PEAK phase), the layer order in the comp from bottom to top:

```
Layer 8: Grain overlay (Screen, 15-20%)
Layer 7: Color grade (Adjustment layer — Lumetri)
Layer 6: Cinematic bars (Top + Bottom black bars, locked)
Layer 5: Shape layer graphics (UI frames, lines)
Layer 4: Text layers (Lyrics / Statement)
Layer 3: Particle system (Multiply or Add, 10-15%)
Layer 2: Gradient treatment (subject with gradient matte)
Layer 1: Raw subject footage (bottom)
```

---

## Asset Density Rule

- **Minimum layers at any moment:** 3 (video + grade + bars)
- **Maximum layers at peak:** 8-10 (everything stacked)
- **Never zero text on screen for more than 3 seconds** — if no lyrics, use the account handle, a relevant stat, or an ambient graphic

---

## Scene-to-Scene Continuity Rules

1. **Tone continuity:** Adjacent clips must share the same emotional energy or deliberately contrast (slow vs fast is fine; happy vs dark is not)
2. **Color continuity:** The grade unifies everything — don't cut from a warm clip to a cold clip without transition treatment
3. **Subject continuity:** The subject should face the same screen direction within a sequence unless you're using a J-cut or transition
4. **Audio continuity:** Sound design bridges clips — a whoosh starting in clip A lands in clip B, connecting them subconsciously
