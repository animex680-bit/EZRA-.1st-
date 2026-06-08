# Pre-Production
## Footage Selection, Music Choices & Edit Planning

---

## Step 1 — Receive the Brief

Before touching any software, answer these questions:

```
[ ] What is the content type?
    → Music lyric video
    → Lifestyle / personality edit  
    → Brand / product showcase
    → Motivational / quote edit
    → Crypto / financial content

[ ] What is the target duration?
    → 15s / 30s / 60s / 90s

[ ] What music is provided or allowed?
    → Client-provided track
    → Free-use from Epidemic Sound / Artlist
    → Client chose a specific song (check licensing)

[ ] What footage is provided?
    → Raw footage files (list them)
    → Screen recordings
    → B-roll provided
    → Need to source stock footage?

[ ] What text/lyrics need to appear?
    → Full lyrics
    → Key quotes / statements
    → Account handle only
    → CTA (call to action)

[ ] Platform(s) for delivery?
    → Instagram Reels / TikTok / YouTube Shorts / All
```

---

## Step 2 — Music Analysis

The music drives everything. Analyze it before choosing or cutting a single clip.

### BPM & Structure Map
1. Open the audio file in AE, Resolve, or Audition
2. Find the BPM (use BeatEdit plugin in AE, or manually)
3. Mark these moments on the timeline:
   ```
   [ ] Intro start
   [ ] First strong beat / kick comes in
   [ ] First verse start
   [ ] Pre-chorus / build (if exists)
   [ ] CHORUS / DROP — biggest moment
   [ ] Second verse (if applicable)
   [ ] Final chorus / outro
   [ ] End point
   ```
4. Note the energy level at each section: LOW / MID / HIGH / PEAK

### Music Suitability Checklist
```
[ ] Does the energy match what we're editing? (e.g., slow ballad ≠ fast lifestyle cuts)
[ ] Is there a clear drop/peak for the Twixtor moment?
[ ] Is the intro short enough to not waste the viewer's attention?
[ ] Is the track licensed for the delivery platform?
[ ] Is the audio quality high enough? (minimum 320kbps MP3 or WAV)
```

---

## Step 3 — Footage Audit

Go through every clip and fill this out:

```
CLIP AUDIT TABLE
────────────────────────────────────────────────────────
File Name        | Duration | Quality | Usability | Notes
─────────────────────────────────────────────────────────
clip_001.mp4     | 0:23     | 1080p   | HIGH      | Face close-up, stable
clip_002.mp4     | 1:04     | 4K      | MED       | Walking shot, slightly shaky
clip_003.mp4     | 0:45     | 1080p   | HIGH      | Perfect for Twixtor (hair movement)
clip_004.mp4     | 0:12     | 1080p   | LOW       | Out of focus — discard
─────────────────────────────────────────────────────────
```

### What Makes Footage "HIGH" Usability?
```
[ ] In focus (sharp on the subject)
[ ] Stable OR stable-enough for Warp Stabilizer to fix
[ ] 60fps or higher (needed for Twixtor slow-mo peaks)
[ ] Good exposure — not blown out, not too dark
[ ] Interesting movement (hair, fabric, gesture — something for Twixtor)
[ ] Clean background or easily maskable subject
[ ] Emotionally resonant expression or pose on subject
```

### What to Do With Low-Quality Footage
- Out of focus: discard unless stylistically appropriate
- Overexposed: can sometimes recover; use in non-critical moments only
- 24fps only: fine for non-slow-mo moments, cannot do quality Twixtor
- Shaky: run through Warp Stabilizer first; if still bad, discard

---

## Step 4 — Edit Plan (the Map)

Create a rough edit plan BEFORE opening After Effects. This prevents wasted time.

### Template
```
EDIT PLAN: [ProjectName] — [Date]
Total Duration: [XX] seconds
Music: [track name, artist, BPM]

SECTION BREAKDOWN:
────────────────────────────────────────────
00:00 – 00:02   HOOK
  - Clip: [clip name]
  - Text: "[exact text to appear]"
  - Effect: [gradient treatment / bold text only / etc.]

00:02 – 00:08   BUILD
  - Clips: [list 3-4 clips with approximate durations]
  - Text: [what text appears]
  - Beat notes: [where the strong hits are]

00:08 – 00:22   PEAK
  - Twixtor clip: [which clip, what moment to slow]
  - Text: "[main lyric / statement]"
  - Drop moment: [exactly where in the music]

00:22 – 00:30   RESOLUTION + CLOSE
  - Clips: [list]
  - Text: [outro text, account handle]
  - Exit: [hard cut to black / fade / loop back]
────────────────────────────────────────────
```

---

## Step 5 — Asset Preparation

Before building the edit, have everything ready:

```
[ ] Music file: [filename] — in 01_RAW/MUSIC/
[ ] All footage: transcoded to proxy in 02_PROXY/
[ ] Fonts installed: Bebas Neue, Inter, Space Mono at minimum
[ ] LUTs in LUT folder: at least LUT_DarkCinematic and LUT_Phantom
[ ] Grain overlay: grain_8mm_overlay.mov available
[ ] SFX: sfx_sub_bass_boom.wav, sfx_whoosh_deep.wav, sfx_impact_thud.wav at minimum
[ ] AE project file created with correct comp settings: 1080×1920, 24fps
[ ] Folder structure created: 01_RAW through 06_FINAL_EXPORT
```

---

## Step 6 — Gather References

Before editing, pull 3-5 reference frames from the @0x100x Instagram:

1. Open the account on your phone/browser
2. Screenshot or screen-record 3-5 reels that match the vibe of THIS specific project
3. Save them to `01_RAW/ASSETS/REFERENCES/` in the project folder
4. Keep them open on a second screen while editing

**What to reference specifically:**
- The exact weight of the text relative to the frame
- How much of the subject is visible vs how much is filled with graphic
- The exact moment Twixtor kicks in (watch for it in the original videos)
- How much breathing room there is between text elements
