# Apps — Rules
## Mobile, Web App, and UI Design

---

## Stream Selection

Apps are predominantly Stream B. Stream A infuses emotional moments — onboarding, empty states, hero illustrations.

**Default**: Stream B 85% / Stream A 15%

---

## Design System Foundation

Every app must have a token-based design system before any component is built.
Use `/tokens/colors.json` (stream_b section) as the starting point.

1. Color tokens defined (not hardcoded)
2. Typography scale defined (`/tokens/typography.json`)
3. Spacing system: 8px base unit
4. Shadow/depth system (`/tokens/shadows.json`)
5. Dark mode first — light mode added second if needed

---

## Component Hierarchy

```
Level 0: bg_void    #0C0C10  — Page background
Level 1: surface_l1 #141418  — Cards, panels
Level 2: surface_l2 #1E1E26  — Modal base, overlays
Level 3: surface_l3 #28282F  — Dropdowns, tooltips
Glass:   rgba(255,255,255,0.06) — Special glass panels
```

### Interactive States (all 5 required)
```
Default → Hover (+brightness, 150ms)
        → Focus (2px outline, accent color)
        → Active/Press (scale 0.97, 100ms)
        → Disabled (opacity 0.4, not-allowed)
```

---

## Dark Mode (Correct Approach)

1. Background: `#0C0C10` (blue-tinted, NOT pure black)
2. Elevate surfaces with lighter values (not opacity alone)
3. Text layers: `#F0F0F6` → `#9090A8` → `#5C5C72`
4. Borders: `#2A2A35` to `#3A3A48`
5. Colors may be more saturated in dark mode

**Never**: `filter: invert(1)` or `background: #000000`

---

## Glass Components

```css
.glass {
  background: rgba(255, 255, 255, 0.06);
  border: 1px solid rgba(255, 255, 255, 0.12);
  border-radius: 16px;
  backdrop-filter: blur(20px) saturate(1.8);
  -webkit-backdrop-filter: blur(20px) saturate(1.8);
}
/* Limit backdrop-filter to 3-5 elements per screen */
```

---

## Neumorphism (Light Mode)

Exact spec from reference "Virtual assistant app in neomorphic design":

```css
/* bg: #EFF2F9, surface: #E4EBF1 */
.neuro-card  { background: #E4EBF1; border-radius: 16px;
               box-shadow: -5px  -5px  10px #FAFBFF, 5px  5px  10px rgba(22,27,29,0.23); }
.neuro-large { box-shadow: -20px -20px 40px #FAFBFF, 20px 20px 40px rgba(22,27,29,0.23); }
.neuro-press { box-shadow: inset -5px -5px 10px #FAFBFF, inset 5px 5px 10px rgba(22,27,29,0.23); }
```

Font: Campton Book / Campton Light (exact reference spec)

---

## Micro-interactions

```javascript
// Button press
{ scale: 0.97, duration: 0.1, ease: 'power2.out' }
{ scale: 1.0,  duration: 0.15, ease: 'power2.inOut' }

// Toggle switch
{ duration: 0.2, ease: 'power2.out' }   // thumb
{ duration: 0.15 }                       // bg color

// Card hover
{ y: -4, boxShadow: 'deeper', duration: 0.2, ease: 'power2.out' }

// Modal open
{ opacity: '0→1', scale: '0.96→1.0', duration: 0.3, ease: 'cubic-bezier(0.32, 0.72, 0, 1)' }

// Drawer
{ x: '100%→0%', duration: 0.35, ease: 'cubic-bezier(0.32, 0.72, 0, 1)' }
```

---

## Emotional UI Moments (Stream A infusion)

1. **Onboarding**: Full dark, editorial photography or sculpture, large Cormorant serif, slow fade
2. **Empty states**: Editorial photography or abstract art — not generic icons
3. **Achievement**: Particle burst + slow drift, not confetti
4. **Premium reveal**: Glass surface lifts, slow reveal, dramatic type
5. **Error states**: Deep crimson (#A01830), cold, precise — not panicked

---

## Quality Check

- [ ] Color tokens used (no hardcoded values in components)
- [ ] All 5 interactive states implemented
- [ ] Dark mode designed (not inverted)
- [ ] Typography follows `/tokens/typography.json`
- [ ] Tap targets ≥ 44×44px (iOS) / 48×48dp (Android)
- [ ] Backdrop-filter elements ≤ 5 per screen
- [ ] Loading states: skeleton screens preferred
- [ ] Error states designed
- [ ] No layout shift during data load
