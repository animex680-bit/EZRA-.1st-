# Project Settings
## After Effects & DaVinci Resolve Configuration

---

## Adobe After Effects — New Project Setup

### Composition Settings
```
Name:           [Client_ProjectName_v01]
Width:          1080 px
Height:         1920 px
Pixel Aspect:   Square Pixels (1.0)
Frame Rate:     24 fps  (or 30fps if client specifies)
Resolution:     Full
Duration:       [Match your music clip length + 2s buffer]
Background:     Black
```

### Preview Settings (for performance)
```
Resolution:     Half or Third (preview only)
Frame Rate:     Skip Every Other Frame
GPU:            Enable GPU Preview rendering (CUDA / Metal)
```

### Project Settings
```
Color Depth:    32 bpc (bits per channel — maximum quality)
Color Profile:  sRGB IEC61966-2.1 (for social media delivery)
Working Space:  sRGB
```

### Pre-comp Structure (recommended)
```
MASTER COMP (1080×1920)
  ├── PRE-COMP: [FOOTAGE]
  │     └── Raw clips + Twixtor + basic grade
  ├── PRE-COMP: [GRAPHICS]
  │     └── All shape layers, text, UI elements
  ├── PRE-COMP: [GRADIENT_CHARACTER]
  │     └── Subject + gradient treatment
  └── ADJUSTMENT LAYERS (on top of everything)
        ├── Grain overlay
        ├── Lumetri Color (final grade)
        └── Cinematic bars (top/bottom)
```

---

## DaVinci Resolve — Project Setup

### Project Settings (File → Project Settings)
```
Master Settings:
  Timeline Resolution:  1080 × 1920
  Timeline Frame Rate:  24 fps
  Video Format:         HD 1080p
  Pixel Aspect Ratio:   Square
  
Image Scaling:
  Input Scaling:        Scale Full Frame With Crop (if needed)
  
Color Management:
  Color Science:        DaVinci YRGB Color Managed  
  Input Color Space:    Rec.709 (for standard cameras)
                        Log C3/C4 (for ARRI)
                        S-Log3 (for Sony)
  Timeline Color Space: DaVinci Wide Gamut
  Output Color Space:   Rec.709
  
Optimized Media:
  Format:              DNxHR / ProRes LT (for speed)
  Resolution:          Half resolution for proxy editing
```

### Timeline Setup
```
Timeline name: [ProjectName_Master]
Create proxy:  Yes — generate before editing
Frame display: Timecode
Audio:         48kHz, Stereo
```

---

## File / Folder Structure Per Project

Every project should be saved with this exact folder layout:

```
[ClientName_ProjectDate]/
├── 01_RAW/
│   ├── FOOTAGE/         ← Original unedited video files
│   ├── MUSIC/           ← Audio tracks, SFX
│   └── ASSETS/          ← Client-provided images, logos
│
├── 02_PROXY/            ← Transcoded proxy files (auto-generated)
│
├── 03_PROJECT_FILES/
│   ├── AE/              ← After Effects .aep file
│   └── RESOLVE/         ← DaVinci Resolve .drp file
│
├── 04_WORKING/
│   ├── PRECOMPS/        ← Any pre-rendered pre-comps
│   ├── FRAMES/          ← Still frame exports if needed
│   └── DRAFTS/          ← Version exports (v01, v02, etc.)
│
├── 05_ASSETS_USED/
│   ├── FONTS/           ← Font files used in this project
│   ├── LUTs/            ← LUT files applied
│   ├── OVERLAYS/        ← Grain, flares, bars files
│   └── SFX/             ← Sound effect files
│
└── 06_FINAL_EXPORT/
    ├── [ProjectName]_MASTER_v01.mp4      ← Highest quality
    ├── [ProjectName]_INSTAGRAM_v01.mp4   ← Optimized for Reels
    └── [ProjectName]_PREVIEW_v01.mp4     ← Watermarked draft
```

---

## Naming Conventions

| Item | Convention | Example |
|---|---|---|
| Project folder | `ClientName_YYYYMMDD` | `Ezra_20260608` |
| AE project | `ProjectName_vNN.aep` | `Ezra_v03.aep` |
| Final export | `ProjectName_PLATFORM_vNN.mp4` | `Ezra_REELS_v02.mp4` |
| Raw clip | `RAW_CamName_ClipNN.mp4` | `RAW_Sony_001.mp4` |
| Pre-comp | `PC_[type]_[name]` | `PC_GRAD_SubjectA` |
| Font file | `FontName-Weight.otf/ttf` | `DrukWide-Bold.otf` |
| LUT file | `LUT_Name_StrengthPct.cube` | `LUT_Phantom_65.cube` |

---

## Performance Tips

1. **Always proxy before editing** — import proxies instead of originals
2. **Purge cache** before final render (Edit → Purge → All Memory & Disk Cache)
3. **Pre-render heavy precomps** — right-click pre-comp → Pre-render
4. **Close background apps** during final render
5. **Enable Multi-Frame Rendering** in AE (Edit → Preferences → Memory & Performance)
6. **GPU preview** — ensure GPU is selected in Preview panel, not CPU
