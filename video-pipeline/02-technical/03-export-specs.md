# Export Specifications
## Final Delivery Settings for Every Platform

---

## Instagram Reels (Primary Delivery)

### Video Settings
```
Format:        H.264 (MP4) or H.265 (HEVC)
Resolution:    1080 × 1920 (9:16 vertical)
Frame Rate:    24fps or 30fps (match composition)
Bitrate:       10-20 Mbps (use VBR 2-pass for best quality)
Profile:       High
Level:         4.2
Color Space:   sRGB / Rec.709
Chroma:        4:2:0
```

### Audio Settings
```
Codec:         AAC
Sample Rate:   44.1 kHz or 48 kHz
Bit Rate:      320 kbps (stereo)
Channels:      Stereo
Loudness:      -14 LUFS integrated (Instagram standard)
               True Peak max: -1 dBTP
```

### Duration Limits
```
Minimum:  3 seconds
Maximum:  90 seconds (Reels)
Sweet spot for algorithm: 15-30 seconds
```

### After Effects → Adobe Media Encoder Export
```
1. Composition → Add to Adobe Media Encoder Queue (Ctrl+Alt+M)
2. Format: H.264
3. Preset: Match Source - High Bitrate
4. Then manually adjust:
   - Target Bitrate: 15 Mbps
   - Max Bitrate: 20 Mbps
   - VBR, 2 Pass: YES
   - Render at Maximum Depth: YES
   - Use Maximum Render Quality: YES
5. Output Name: [ProjectName]_REELS_v01.mp4
```

---

## TikTok

### Video Settings
```
Format:        H.264 (MP4)
Resolution:    1080 × 1920 (9:16 vertical)
Frame Rate:    30fps (TikTok algorithm handles 30fps best)
Bitrate:       8-12 Mbps
Color Space:   Rec.709
```

### Audio Settings
```
Codec:         AAC
Sample Rate:   44.1 kHz
Bit Rate:      192-320 kbps
Loudness:      -14 LUFS
```

### Notes
```
- TikTok compresses aggressively — export at higher bitrate to compensate
- If exporting from Reels version: re-export at 30fps, don't upload Reels version to TikTok
- Maximum file size: 287.6 MB (under 2 minutes)
```

---

## YouTube Shorts

### Video Settings
```
Format:        H.264 or H.265 (MP4)
Resolution:    1080 × 1920 (9:16 vertical)
Frame Rate:    24fps or 30fps
Bitrate:       15-20 Mbps (YouTube preserves quality better than others)
Color Space:   Rec.709
```

### Audio Settings
```
Codec:         AAC
Sample Rate:   48 kHz
Bit Rate:      320 kbps
Loudness:      -14 LUFS
```

---

## Preview / Draft Export (for client review)

```
Format:        H.264 (MP4)
Resolution:    540 × 960 (half res)
Bitrate:       3 Mbps
Frame Rate:    24fps
Quality:       Lower — this is just for review, not delivery
Watermark:     Add a subtle semi-transparent "DRAFT — [date]" text overlay
File size:     Keep under 50MB for easy sharing
```

---

## Master Archive Export (highest quality, for future re-edit)

```
Format:        ProRes 4444 (Mac) or DNxHR 444 (Windows)
Resolution:    1080 × 1920
Frame Rate:    Match composition
Bitrate:       Very high (ProRes will be ~1-3 GB per minute — this is expected)
Color Space:   Rec.709
Purpose:       Long-term archiving, future platform optimizations
Storage:       Keep in 06_FINAL_EXPORT/ folder
```

---

## Pre-Export Checklist

Before exporting the final deliverable, verify:

- [ ] Cinematic bars are on and locked
- [ ] Grain overlay is at correct opacity (15-25%)
- [ ] Color grade adjustment layer is active
- [ ] Audio levels: music peaks at -6dBFS, no clipping
- [ ] SFX levels: each SFX no louder than -10dBFS
- [ ] Total loudness: -14 LUFS integrated (use Loudness Meter or Resolve Fairlight)
- [ ] No visible compression artifacts in dark areas
- [ ] Text is readable at phone size (test at 375px wide = iPhone screen width)
- [ ] No accidental frame holds or duplicates
- [ ] First frame and last frame look intentional (not a freeze or mid-transition)
- [ ] Video duration matches music (no silence at end)

---

## Loudness Normalization

Instagram, TikTok, and YouTube all normalize audio to approximately -14 LUFS. If your audio is louder, they will turn it down. If quieter, it will feel weak compared to other videos. Target -14 LUFS exactly.

**In DaVinci Resolve Fairlight:**
```
1. Open Fairlight page
2. Add a Loudness Meter plugin to the master bus
3. Play the full edit and read the Integrated LUFS number
4. If too loud: reduce Master Fader until Integrated = -14 LUFS
5. If too quiet: increase, but check True Peak stays below -1 dBTP
```

**In After Effects:**
```
1. Export audio only first
2. Check in Adobe Audition or Premiere Pro:
   Window → Loudness Radar
3. Adjust your master audio level and re-export
```
