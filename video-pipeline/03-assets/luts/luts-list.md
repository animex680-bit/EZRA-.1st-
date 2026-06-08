# LUT Library
## Color Grade LUTs — Names, Sources, Application

---

## What is a LUT?

A LUT (Look-Up Table) is a color transformation file (.cube or .3dl) that shifts the colors of your footage according to a preset "recipe." In this pipeline, LUTs are the final creative color layer applied after all other corrections.

**Always apply LUTs at reduced strength (50-70%) unless otherwise noted.**

---

## Primary LUTs (Must Have)

### LUT-01: Dark Cinematic
- **Style:** Crushed blacks, desaturated midtones, warm highlights — the "standard" look for this aesthetic
- **Strength:** 60-70%
- **Best for:** General-purpose use on all footage
- **Source:** Search "Dark Cinematic LUT free download" — multiple community sources available
- **File name:** `LUT_DarkCinematic_v1.cube`

### LUT-02: Teal & Orange Premium
- **Style:** Cool teal in shadows, warm orange in highlights — the classic Hollywood separation
- **Strength:** 50-65%
- **Best for:** Skin-tone subjects, exterior shots, high-contrast footage
- **Source:** Lutify.me (free tier), or many Patreon creator packs
- **File name:** `LUT_TealOrange_Premium.cube`

### LUT-03: Phantom
- **Style:** Near-neutral dark grade — very clean, slight blue-cool tint, preserved detail
- **Strength:** 55-65%
- **Best for:** Portraits, close-up shots, when you want grade without obvious stylization
- **Source:** AEJuice community pack, or search "Phantom LUT AEJuice free"
- **File name:** `LUT_Phantom_v2.cube`

---

## Secondary LUTs (Use for Variation)

### LUT-04: Noir Dark
- **Style:** Near black-and-white with slight warm tone in highlights. Very dramatic.
- **Strength:** 40-60%
- **Best for:** Maximum drama, emotional peak moments, monochrome-leaning scenes
- **Source:** Many free Noir LUT packs available on Gumroad and MotionArray
- **File name:** `LUT_NoirDark.cube`

### LUT-05: Crypto Blue
- **Style:** Pushes shadows toward deep blue, midtones cool, highlights bright — futuristic/Web3 feel
- **Strength:** 45-55%
- **Best for:** Tech content, cryptocurrency/NFT references, night scenes
- **Source:** Community-built — search Instagram/YouTube "crypto edit LUT free"
- **File name:** `LUT_CryptoBlue.cube`

### LUT-06: Amber Luxury
- **Style:** Warm amber highlights, desaturated but golden midtones — luxury, wealth aesthetic
- **Strength:** 50-65%
- **Best for:** Lifestyle content, luxury brand edits, wealth-themed videos
- **Source:** Multiple free sources including Motionarray.com
- **File name:** `LUT_AmberLuxury.cube`

---

## Subject-Specific Notes

### For Darker Skin Tones
When grading subjects with darker skin, be cautious of over-crushing the blacks — it can make the subject invisible against dark backgrounds. Adjust:
- Raise the Lift (black point) slightly in Resolve before applying the LUT
- Use lower LUT strength (40-50%) rather than 60-70%
- Ensure there's at least some separation between the subject's skin and the background via lighting or gradient treatment

### For Lighter Skin Tones
Standard settings apply. Watch for:
- Not blowing out facial highlights (keep below 80 IRE)
- The Teal & Orange LUT can make pale skin look greenish — reduce Teal saturation in that area

---

## How to Apply LUTs

### In DaVinci Resolve
```
Method A (Serial Node):
1. At end of color grade node chain, create a new serial node
2. Right-click → Add 3D LUT
3. Navigate to LUT file location
4. Select .cube file
5. Set node Key Output to 0.60 (= 60% strength)

Method B (LUT folder):
1. Copy .cube file to DaVinci LUT folder:
   Mac: ~/Library/Application Support/Blackmagic Design/DaVinci Resolve/LUT/
   Win: C:\ProgramData\Blackmagic Design\DaVinci Resolve\Support\LUT\
2. DaVinci Resolve → LUTs palette → your LUT appears there
3. Drag onto clip or node
```

### In Adobe After Effects
```
1. Create a new Adjustment Layer above all footage
2. Effect → Utility → Apply Color LUT
3. Choose LUT: navigate to your .cube file
4. Set the Adjustment Layer opacity to 60% (= 60% LUT strength)
```

### In Adobe Premiere Pro
```
1. Effects → Lumetri Color → Creative tab
2. "Look" dropdown → Browse → select .cube file
3. "Intensity" slider: set to 60-70%
```

---

## LUT Storage Location in Repo

```
03-assets/luts/files/
  ├── LUT_DarkCinematic_v1.cube
  ├── LUT_TealOrange_Premium.cube
  ├── LUT_Phantom_v2.cube
  ├── LUT_NoirDark.cube
  ├── LUT_CryptoBlue.cube
  └── LUT_AmberLuxury.cube
```

When you acquire a new LUT that works well, add it:
1. Place the .cube file in `03-assets/luts/files/`
2. Add an entry to this document with the same format above
