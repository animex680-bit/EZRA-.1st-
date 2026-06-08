# Lyric Sync Workflow
## Beat-Perfect Lyrics from Raw Audio to Finished Edit

---

## Step 1 — Get the Lyrics

### If lyrics are provided by client:
- Paste into a plain text file: `lyrics_[songname].txt`
- Save to: `01_RAW/MUSIC/lyrics_[songname].txt`
- Verify against the actual audio — artists and clients often have wrong versions

### If no lyrics provided:
1. Use Genius.com for the most accurate lyrics
2. Search the song title + artist name
3. Copy and paste into a text file — do NOT trust lyric sites blindly
4. Listen through once, following the text, fixing any errors
5. Note: for non-English lyrics, get a verified translation if captioning in English

### Lyric Preparation Format
Before syncing, format the lyrics into segments the way they'll appear on screen:

```
Example raw lyrics:
"I was running through the night, the city lights below me"

Break into caption segments:
Line 1: "RUNNING THROUGH THE NIGHT"
Line 2: "CITY LIGHTS BELOW ME"

Or single-word punch style:
Word 1: "RUNNING"
Word 2: "THROUGH"
Word 3: "THE NIGHT"

Choose based on:
- Energy level (single word = highest energy)
- Line length (very long lines = must break up)
- Natural speech phrasing (break where the singer breathes/pauses)
```

---

## Step 2 — Load Audio and Set Up Markers

### In After Effects:
```
1. Drag the music track into the comp
2. RAM Preview or play through using the period key (.) on numpad
3. At each lyric hit moment, press the * key on the numpad
   — This places a composition marker at the current frame
4. After placing all markers, go back and RENAME each marker:
   - Right-click marker → Settings
   - Type the lyric text in the Comment field
   - This makes it easy to see what goes where without playing back
```

### In DaVinci Resolve:
```
1. Place audio on a track in the Edit or Cut page
2. Play through
3. At each lyric moment, press M to add a marker
4. Right-click marker → Edit Marker → add lyric text as the note
```

---

## Step 3 — Choose a Lyric Sync Style

Select the approach that fits the music and energy level of the edit:

### Style A: Full Line at Once
- **How it works:** An entire lyric line appears at the start of the phrase and holds until the next line
- **Best for:** Slower music, introspective/emotional content, spoken word
- **Example:** "RUNNING THROUGH THE NIGHT" → holds for 3 seconds → replaced by "CITY LIGHTS BELOW ME"

### Style B: Word-by-Word
- **How it works:** Each word pops in exactly when sung, replacing the previous word
- **Best for:** Fast-paced, high-energy music, trap/drill/hip-hop
- **Most like 0x100x:** This is the most commonly used style in this aesthetic
- **Example:** "RUNNING" (appears) → "THROUGH" (replaces) → "THE" → "NIGHT" each on their syllable

### Style C: Stacked Reveal
- **How it works:** Words build up on screen, each added to the stack on each beat
- **Best for:** Mid-tempo music, motivational content, when building to a statement
- **Example:**
  - Beat 1: "RUNNING" appears
  - Beat 2: "RUNNING" stays + "THROUGH THE NIGHT" appears below

### Style D: Split / Emphasis
- **How it works:** Different words in a line get different sizes or colors
- **Best for:** When one word in a line is more important than others
- **Example:** "RUNNING THROUGH THE **NIGHT**" — "NIGHT" is 2x larger

---

## Step 4 — Place Lyrics in Timeline

### For Word-by-Word (Style B) — the primary method:

```
1. Create a new Text Layer for the first word
   - Type the word, style it (Bebas Neue, 120px, White, ALL CAPS)
   - Set In Point at the marker for that word
   - Apply Clip Mask Reveal animation (8-10 frames, Ease Out)
   - Set Out Point: 2 frames before the NEXT word's marker

2. Duplicate that text layer for the second word
   - Change the text content
   - Shift In Point to second word's marker
   - Shift Out Point to before third word
   
3. Repeat for every word in the lyric

4. Alternative using one text layer (faster method):
   - Use a single text layer
   - Keyframe the Source Text property
   - At each marker: change the text value to the new word
   - Note: this makes animation harder to control per-word
```

### For Full Line (Style A) — when appropriate:

```
1. One text layer per lyric line
2. In Point: at the start of the line in audio
3. Out Point: just before the next line starts
4. Apply Clip Mask Reveal animation
5. Add a subtle exit: either Clip Mask Exit (text exits upward)
   OR just abruptly cut off at the Out Point (on a beat)
```

---

## Step 5 — Sync Verification

After placing all lyrics:

```
1. RAM Preview the full edit (not just scrubbing)
2. Watch only the text — does each word appear when it's sung?
3. For any words that feel even slightly early or late:
   - Select the text layer
   - Slide the In Point by 1-3 frames
   - Preview again
4. The tolerance is tight: within 2 frames of the sung word
   (at 24fps: 2 frames = 0.083 seconds — you will notice if it's wrong)
5. Pay special attention to:
   - Words that start with hard consonants (P, T, K) — appear slightly BEFORE the sound
   - Words that start with vowels — appear exactly on the sound
   - Long vowels / held notes — the word can appear slightly late
```

---

## Step 6 — Emphasis & Highlight Words

Every lyric edit should have 2-3 "highlight" words — words that are given extra visual treatment.

**How to identify highlight words:**
- The most emotionally important word in the line
- The word that lands on the biggest beat
- The word that the edit's whole message revolves around

**How to treat them:**
```
Option A: Scale up — 130-160% size vs surrounding words
Option B: Color — White → Gold #FFB800 on that word
Option C: Gradient text — apply the signature gradient (one use per edit)
Option D: Duration — hold the word 2x longer than others before next word appears
Option E: Add shape graphic — a bracket or underline appears beneath this word simultaneously
```

---

## Step 7 — Line Break Rules

When splitting long lyrics into two lines, use these rules:

1. **Break on a natural speech pause** — where the singer takes a breath or natural phrasing ends
2. **Never break a compound word or idiom** across two lines
3. **Balance line lengths** — aim for similar length on each line visually
4. **Test at phone size** — if both lines are too long to read comfortably, simplify further

```
WRONG: "I WAS RUNNING THROUGH"  /  "THE NIGHT THE CITY"
RIGHT: "RUNNING THROUGH THE NIGHT"  /  "THE CITY LIGHTS"
```

---

## Lyric Timing Quick Reference

| Music type | Frames per word | Beat sync type |
|---|---|---|
| Trap/Drill (140+ BPM) | 4-8 frames | Hard cut on beat, each word |
| Hip-Hop (90-110 BPM) | 8-14 frames | Cut or reveal on beat |
| R&B (70-90 BPM) | 12-24 frames | Reveal, words hold longer |
| Ambient/Electronic | Hold line for 2-4 bars | Full line approach |
| Pop chorus | Mix — hook words fast, verses slower | Varies |
