# Motion Graphics — Rules
## For CapCut, After Effects, Remotion, and any motion overlay work

---

## When to Use Motion Graphics

Motion graphics are an *overlay* — they sit on top of video. Their job is to:
1. **Amplify** what the video is already saying
2. **Guide** the viewer's eye to what matters
3. **Punctuate** key moments
4. **Add depth** without competing with the main content

They must NEVER:
- Cover the subject's face or lips during speech
- Appear at the same time as critical on-screen text in the video
- Compete with the audio for attention
- Feel busy or decorative for its own sake

---

## Stream Selection

| Video Content Type | Primary Stream |
|---|---|
| Tech / product / AI content | B 70% |
| Personal brand / editorial | A 60% |
| Finance / business | B 60% |
| Lifestyle / fashion | A 70% |
| Music / cultural | A 50% + B 50% |
| Tutorial / explainer | B 80% |

---

## Layout Rules (Vertical Video — 1080×1920)

**Safe Zones** — never place critical elements outside these:
```
Top safe:    y > 14% = y > 269px
Bottom safe: y < 82% = y < 1574px
Left safe:   x > 4%  = x > 43px
Right safe:  x < 96% = x < 1037px
```

**Placement Strategy**:
- Lower third: 75%–85% height (inside safe zone)
- Title card: 15%–40% height
- Kinetic text: center-ish but offset — never perfectly centered
- Decorative elements: hug the safe zone edges

---

## Typography in Motion Graphics

**Preferred Fonts**:
- Stream A overlay: Cormorant Garamond, Didot (thin/light weight)
- Stream B overlay: Inter, Geist, SF Pro (medium/bold)
- Hybrid: Inter for structured info, Cormorant for emotional beats

**Size Guidelines**:
- Primary kinetic text: 80–140pt
- Supporting text: 24–48pt
- Labels/callouts: 16–24pt, ALL CAPS, wide tracking
- Subtitles/captions: 32–42pt, high contrast

---

## Approved Moves

### Lower Thirds
```
Entry:  Slide from left + fade, 300ms ease-out (Stream B)
        OR: Fade in over 800ms (Stream A)
Hold:   Static, no movement
Exit:   Fade to 0, 400ms ease-in
Timing: Appears 0.5s after cut, disappears 0.5s before next cut
```

### Kinetic Typography
```
Entry:     Scale punch (scale 0.92→1.18→1.0), or clip reveal
Timing:    Sync to audio beat or speech start
Color:     White default; gradient (teal→purple→orange) for emphasis
Peak scale:1.15–1.18 MAX — never 1.30+
Exit:      Fade or scale down 0.95 + fade, 200ms
```

### Sweep Lines
```
Lines constrained to safe margins ALWAYS:
  sl = 4% + 12px from left
  sr = 96% - 12px from right
Opacity: 0.2–0.4 (subtle)
Animation: draw 0%→100% over 400–600ms
```

### Corner Brackets
```
Anchored to safe area corners:
  Top-left:     (4%+12px, 14%+12px)
  Top-right:    (96%-12px, 14%+12px)
  Bottom-left:  (4%+12px, 82%-12px)
  Bottom-right: (96%-12px, 82%-12px)
Size: 40–60px per arm
Animation: draw in from corner, 300ms each arm (staggered)
```

---

## Pacing Rules

- **Never monotonous**: vary type of motion graphic every 3–5 seconds
- **Never constant**: at least 1–2 seconds of bare video between overlays
- **Sync to audio**: text entries align with speech starts or beats
- **Breathing room**: after kinetic typography, let video breathe 1.5s+

---

## Glass Overlay Panels

```css
background: rgba(0, 0, 0, 0.5);
backdrop-filter: blur(12px);
border: 1px solid rgba(255,255,255,0.15);
border-radius: 12px;
```

---

## Quality Check

- [ ] No critical content hidden under graphics
- [ ] All text within safe zones
- [ ] Corner brackets / sweep lines do NOT cross safe zone boundaries
- [ ] Peak kinetic scale ≤ 1.18
- [ ] Minimum 1 second between overlapping graphic events
- [ ] Every graphic has a purpose tied to content
- [ ] High contrast text legible on actual footage (not just on black)
- [ ] No linear easing anywhere
