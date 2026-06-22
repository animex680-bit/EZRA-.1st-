# Websites — Rules
## Web Design & 3D Web Experiences (Vite, Three.js, R3F, GSAP)

---

## Stream Selection

| Project Type | Primary | Secondary |
|---|---|---|
| Agency / creative studio | A 50% | B 50% |
| SaaS product site | B 70% | A 30% |
| Personal brand | A 60% | B 40% |
| 3D immersive WebGL | A texture + B structure | — |
| Portfolio | B 60% | A 40% |
| AI/tech product | B 80% | A 20% |

---

## Layout & Grid

- Base unit: 8px
- Max content width: 1200px centered
- Gutters: 24px mobile, 32px tablet, 48px desktop
- Hero: minimum 90vh (not 100vh — allow scroll hint)
- Section spacing: 120px–180px between sections

---

## CSS Variables

```css
:root {
  --bg:           #0C0C10;
  --surface:      #141418;
  --surface-2:    #1E1E26;
  --border:       #2A2A35;
  --text:         #F0F0F6;
  --text-2:       #9090A8;
  --text-3:       #5C5C72;
  --accent:       #3B82F6;
  --accent-2:     #0EA5E9;
  --glass:        rgba(255,255,255,0.06);
  --glass-border: rgba(255,255,255,0.12);
}
```

---

## Typography

```css
.h-hero { font-size: clamp(56px, 8vw, 96px); font-weight: 700; letter-spacing: -0.04em; }
.h1     { font-size: clamp(40px, 5vw, 64px);  font-weight: 700; letter-spacing: -0.03em; }
.h2     { font-size: clamp(28px, 4vw, 48px);  font-weight: 600; letter-spacing: -0.02em; }
.h3     { font-size: clamp(20px, 3vw, 32px);  font-weight: 600; letter-spacing: -0.01em; }
.body   { font-size: 16px; font-weight: 400; line-height: 1.6; }
.label  { font-size: 11px; font-weight: 500; letter-spacing: 0.1em; text-transform: uppercase; }

/* Stream A editorial moments */
.editorial { font-family: 'Cormorant Garamond', serif; font-weight: 300; letter-spacing: 0.08em; }
```

---

## Glass Card

```css
.glass-card {
  background: rgba(255, 255, 255, 0.06);
  border: 1px solid rgba(255, 255, 255, 0.12);
  border-radius: 16px;
  backdrop-filter: blur(20px) saturate(1.8);
  box-shadow: 0 4px 32px rgba(0,0,0,0.4), inset 0 1px 0 rgba(255,255,255,0.10);
}
.glass-card:hover {
  background: rgba(255, 255, 255, 0.09);
  border-color: rgba(255, 255, 255, 0.18);
  transition: all 200ms cubic-bezier(0.2, 0, 0, 1);
}
```

---

## GSAP + ScrollTrigger

```javascript
// Section reveal
gsap.fromTo('.section-element',
  { opacity: 0, y: 40 },
  { opacity: 1, y: 0, duration: 0.8, ease: 'power3.out',
    scrollTrigger: { trigger: '.section-element', start: 'top 85%', once: true } }
);

// Staggered list
gsap.from('.list-item', { opacity: 0, y: 24, stagger: 0.08, duration: 0.6, ease: 'power2.out' });

// Parallax hero
gsap.to('.hero-bg', { yPercent: -20, ease: 'none',
  scrollTrigger: { trigger: '.hero', start: 'top top', end: 'bottom top', scrub: true } });
```

**Lenis**: `new Lenis({ lerp: 0.08, smoothWheel: true })`

---

## Three.js / R3F

```javascript
// Scene
scene.background = new THREE.Color(0x0C0C10);
scene.fog = new THREE.FogExp2(0x0C0C10, 0.015);

// Chrome material (Stream A)
const chrome = new THREE.MeshStandardMaterial({ color: 0xB2BFC9, metalness: 0.95, roughness: 0.05, envMapIntensity: 1.5 });

// Glass material (Stream B)
const glass = new THREE.MeshPhysicalMaterial({ transparent: true, opacity: 0.15, roughness: 0.05, transmission: 0.9, thickness: 0.5 });

// Post-processing
// Bloom: threshold 0.9, strength 0.3, radius 0.5
// Vignette: darkness 0.5
// Chromatic aberration: 0.002 (very subtle)
```

### Performance Gate
- 60fps on mid-tier laptop (2021 MacBook M1)
- 30fps minimum on iPhone 13+
- First frame under 3 seconds
- No texture above 2048×2048
- No mesh above 100k tris without LOD

---

## Awwwards Quality Bar

- [ ] Unique concept — not a clone
- [ ] 60fps desktop, 30fps mobile
- [ ] Typography precisely set (scale, tracking, weight)
- [ ] All transitions use custom easing
- [ ] Dark mode is the design, not an afterthought
- [ ] Every interaction has feedback
- [ ] Mobile experience not broken (simplified, not broken)
- [ ] Load screen considered
- [ ] No Lorem Ipsum in delivery
- [ ] Glows / gradients / particles are restrained and purposeful
