# Influencer Fail List — CapCut Build Guide

## What you're building
Three pill-shaped buttons that stagger in, left-aligned, calling out 3 things influencers fail to do. Dark premium feel — Stream B structure, Stream A mood.

---

## Canvas
- **1080 × 1920**, 30fps
- Background: `#0C0C10` (not pure black — add a solid color overlay or use a dark clip)

---

## Element 1 — Sweep Line (appears first, frames 0–8 = 0ms–267ms)

Create a **thin horizontal line**:
- Width: 880px, Height: 1px
- Color: `#F0EFE8` (bone white), Opacity: 25%
- Position: X=60, Y=698 (left-aligned, above the list)

**Animation**:
- Entry: Scale X from 0% → 100%, left-anchored (pin the left edge)
- Duration: 267ms
- Easing: Ease Out

---

## Element 2 — Pill 1 (frame 9 = 300ms)

### Shape (rounded rectangle — the card body):
- Width: 880px, Height: 76px
- Border-radius: 12px
- Fill: `#141418`
- Border: 1px, Color: `rgba(255,255,255,0.12)` — in CapCut use white at ~12% opacity
- Position: X=60, Y=720

### Left accent bar (inside the pill):
- Width: 4px, Height: 76px
- Color: `#A01830` (crimson/deep red)
- Border-radius: 12px left side, 0px right side
- Position: X=60, Y=720 (flush left of the pill)

### Text:
- Text: `NO CLEAR PROMISE`
- Font: Inter SemiBold (or Montserrat SemiBold if Inter not available)
- Size: 24px
- Color: `#F0EFE8`
- ALL CAPS, letter-spacing: wide (+10%)
- Position: X=92 (60 + 4px bar + 28px padding), Y centered in pill

**Animation (all 3 elements animate together as a group)**:
- Entry: Opacity 0% → 100% + Scale 92% → 100%
- Duration: 300ms
- Easing: Custom — fast start, soft finish (CapCut: "Decelerate" or "Ease Out")
- Start time: 300ms into the clip

---

## Element 3 — Pill 2 (frame 11 = 367ms)

Same structure as Pill 1, positioned below:

- Shape: X=60, Y=812 (pill 1 bottom + 16px gap)
- Accent bar: X=60, Y=812
- Text: `LACK OF SCROLL REASON`, same font/size/color
- Text position: X=92, Y centered at 812+(76/2)=850

**Animation**: Same as Pill 1, start at 367ms

---

## Element 4 — Pill 3 (frame 13 = 433ms)

- Shape: X=60, Y=904
- Accent bar: X=60, Y=904
- Text: `NO CTA`, same font/size/color
- Text position: X=92, Y centered at 904+(76/2)=942

**Animation**: Same, start at 433ms

---

## Hold
All 3 pills stay on screen for **3 seconds** after the last one appears.

---

## Exit (all fade together)
- Opacity 100% → 0%
- Duration: 267ms (8 frames)
- Easing: Ease In
- All 4 elements (line + 3 pills) exit at the same time

---

## Safe Zone Check
```
Sweep line Y=698      ✓ (safe: >269px)
Pill 1     Y=720-796  ✓
Pill 2     Y=812-888  ✓
Pill 3     Y=904-980  ✓ (safe: <1574px)
Left edge  X=60       ✓ (safe: >43px)
Right edge X=940      ✓ (safe: <1037px)
```

---

## Color Reference
```
Background:   #0C0C10
Pill surface: #141418
Pill border:  rgba(255,255,255,0.12)  →  white at 12% opacity
Accent bar:   #A01830
Text:         #F0EFE8
Sweep line:   #F0EFE8 at 25%
```

---

## CapCut Shortcut: Group Each Pill
After placing the 3 elements (shape + bar + text) for each pill, group them and animate the group as one unit. This keeps the fade+scale clean and consistent.
