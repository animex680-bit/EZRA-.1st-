# 3D Assets — Rules
## Models, Renders, Illustrations, CGI

---

## Stream Selection

3D assets lean Stream A: **sculptural, editorial, material-obsessed**.
Stream B informs technical precision and geometry cleanliness.

**Default**: A 70% / B 30%

---

## Material Philosophy

### Stream A Materials

**Chrome / Reflective Metal**
```
Metalness:   0.95–1.0
Roughness:   0.0–0.08
Color:       #B2BFC9 (chrome mid) or #D4DDE2 (bright chrome)
Environment: High-contrast HDRI (interior, studio, or urban)
Key:         The reflection IS the subject. Render it clean.
```

**Porcelain / Resin (Mannequin)**
```
Metalness:   0.0
Roughness:   0.05–0.15
Color:       #EDE8E0 (bone) or #E8D5C8 (warm skin)
Subsurface:  Subtle SSS at 5–8% for skin warmth
Specular:    Tight highlight (IOR ~1.5)
Light:       Soft box or diffuse area from above/side
```

**Raw Concrete**
```
Metalness:   0.0
Roughness:   0.65–0.75
Color:       #666870 (mid grey) or #8C8880 (warm grey)
Normal map:  Subtle micro-grain
Light:       Dramatic side-lighting
```

**Matte Dark Surface**
```
Metalness:   0.0–0.05
Roughness:   0.85–0.95
Color:       #0D0D0F to #1A1A1E
```

### Stream B Materials

**Holographic / Iridescent**
```
Metalness:   0.6–0.8
Roughness:   0.0–0.05
Color shift: Changes with view angle (thin-film interference)
Environment: Dark HDRI, enhance the shift
```

**Dark Anodized Aluminum**
```
Metalness:   0.8
Roughness:   0.15–0.20
Color:       #1A1A20 (near-black with blue)
```

**Liquid Glass (3D)**
```
Transmission:0.85–0.95
IOR:         1.52
Roughness:   0.0
Color:       Slight tint of accent (blue, teal)
```

---

## Lighting Setups

### Setup 1: Editorial Drama (Stream A)
```
Key:    Area 1.5×1.5m, 45° from subject right, #FFF5E8, intensity 4.0
Fill:   Opposite, 0.5× key, #E8F0FF, intensity 1.0
Rim:    Behind subject, strip light, #0EA5E9 teal, intensity 2.0
BG:     #0D0D0F
```

### Setup 2: Soft Pastel (Stream A — Mannequin)
```
Key:    Large diffuse softbox overhead-front, #C4A89A, intensity 2.0
Fill:   Large diffuse panel opposite, #9E97B0 lavender, 0.7× intensity
BG:     Void black or very dark teal
```

### Setup 3: Product Studio (Stream B)
```
Key:    Small area at 45°, pure white
Fill:   Opposite large area, 0.3× intensity
Bounce: Subtle reflector below, 0.1× intensity
BG:     Pure black or very dark navy
```

### Setup 4: Particle Field (Stream B)
```
Environment: None (or very dark radiance-only HDRI)
BG:          Pure black
Particles:   White emissive, point sprites, 60fps
```

---

## Rendering Specifications

### Web (glTF/glb)
```
Polygon budget:  10k–50k tris hero, <10k secondary
Textures:        KTX2 compressed, 2048×2048 max
Normal maps:     Yes, baked from high-poly
File size:       <2MB per asset
Tools:           Blender → Draco compression → web
```

### High-Resolution (PNG/EXR)
```
Resolution:  2160×2160 min (4K for hero)
Color depth: 32-bit EXR for post
Samples:     1000+ Cycles
Denoising:   AI denoiser at export
DOF:         Shallow for product isolation
Color space: ACES or Linear for EXR, sRGB for PNG
```

---

## 3D Composition Rules

- Object fills no more than 60% of frame
- Camera: 15–30° elevation, slight 3/4 turn — not flat-on
- Depth of field: focused on face of object, background soft
- Always some reflection visible on specular surfaces
- Teal shadow fill: prevents dead blacks
- One hero light: more lights = flatter, less drama

---

## Quality Check

- [ ] Polygon count within budget for platform
- [ ] Textures power-of-two and compressed
- [ ] Normals clean (no flipped faces, no holes)
- [ ] PBR correct (metalness/roughness, not specular/gloss)
- [ ] Passes the "could this appear in a premium brand ad?" test
- [ ] No flat grey environments
- [ ] Teal undertone in shadows
- [ ] glTF export validated in three.js or model-viewer before delivery
