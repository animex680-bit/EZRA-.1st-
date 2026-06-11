---
name: reels-voice
description: Ingests the user's voice recording, cleans it (denoise + de-ess + level), and produces word-level timings (Whisper) used by reels-captions for ±1-frame caption sync. Use after the script is approved and the user has recorded VO. Part of the reels pipeline.
---

# reels-voice — VO Ingest & Word-Timing

The user records the script in their own voice. This skill takes that raw audio and turns it into a clean VO track + a JSON of word-level timings used by every downstream skill.

## Inputs

`productions/NNN-slug/inputs/voice/` — one or more of:
- `vo_raw.wav` (preferred — uncompressed 48k/24bit)
- `vo_raw.mp3` / `vo_raw.m4a` (lossy is OK; user phone is fine)

Multiple takes welcome — files named `take_01.wav`, `take_02.wav` etc. The user marks the chosen take.

## What you do

### 1) Clean

```bash
# normalize, light denoise, de-ess via ffmpeg
ffmpeg -i inputs/voice/take_02.wav \
    -af "highpass=f=80, lowpass=f=12000, \
         afftdn=nr=12:nf=-40, \
         acompressor=threshold=-22dB:ratio=2.5:attack=8:release=180, \
         loudnorm=I=-16:TP=-1.5:LRA=8" \
    vo.wav
```

If `rnnoise` or `ffmpeg --enable-libspeexdsp` is available, prefer those. If the user has `Whisper` installed locally and prefers to denoise in iZotope RX, accept the cleaned `vo.wav` directly and skip cleaning.

### 2) Transcribe with word timings

Whisper (faster-whisper or openai-whisper) outputs a JSON with per-word `start` and `end` seconds:

```json
{
  "duration": 27.84,
  "words": [
    {"w": "MOST",   "s": 0.16, "e": 0.46},
    {"w": "PEOPLE", "s": 0.46, "e": 1.08},
    {"w": "SCROLL", "s": 1.30, "e": 1.66},
    {"w": "PAST",   "s": 1.66, "e": 1.94},
    {"w": "THIS",   "s": 1.94, "e": 2.30},
    ...
  ]
}
```

Save as `vo_words.json`. This is the single source of truth for caption timing.

### 3) If Whisper isn't installed

This environment may not have Whisper. Two fallbacks:

**Fallback A (best):** Ask the user to run Whisper locally on `vo.wav` and upload `vo_words.json`. Provide a one-liner:
```bash
pip install -U faster-whisper
python -c "from faster_whisper import WhisperModel; m=WhisperModel('large-v3'); s,_=m.transcribe('vo.wav', word_timestamps=True); import json; json.dump({'words':[{'w':w.word.strip().upper(),'s':w.start,'e':w.end} for seg in s for w in seg.words]}, open('vo_words.json','w'), indent=2)"
```

**Fallback B (rough):** Use `silero-vad` (already in many envs) for voice-activity segments, then estimate word boundaries by dividing each segment proportionally to the script word counts. Less accurate but unblocks the pipeline.

### 4) VO mix prep

Output a second file `vo_mix.wav` — same content but with:
- target loudness -16 LUFS (will sit at -12 after music duck)
- 30ms fade-in / 60ms fade-out per line
- 250ms head silence (gives mix room before the first word)

## Outputs

```
productions/NNN-slug/
  vo.wav                ← cleaned VO, full length
  vo_mix.wav            ← VO with fades + headroom for mixing
  vo_words.json         ← per-word timings (the spine of caption sync)
  vo_meta.json          ← {duration, take_used, loudness_LUFS, peak_dBFS}
```

## Handoff

Pass `vo_words.json` + `vo_meta.json` to `reels-storyboard` so the storyboard can assign each script line to its real time on the timeline.
