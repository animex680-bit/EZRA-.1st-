# Storyboard — #002 Save The Company

Target: 32s · 24fps · 1080×1920 · 120 BPM (0.5s/beat = 12 frames/beat)

## Beat grid (drop at f336 = 14.00s)

| Beat # | Frame | t (s) | What happens |
|---|---|---|---|
| 1 | 0   | 0.00  | HOOK — "EVERY DEAD COMPANY" scale-punch + sub bass |
| 2 | 24  | 1.00  | "HAD A DEAD WEBSITE." clip-reveal (gold) + ui_click |
| 3 | 48  | 2.00  | CUT → Scene 2 + "BUSINESSES NEED YOU." scale-punch + impact_thud |
| 4 | 60  | 2.50  | "THEY DON'T KNOW IT YET." clip-reveal |
| 5 | 96  | 4.00  | CUT → Scene 3 + "BAD WEBSITE." (gold) word-swap |
| 6 | 108 | 4.50  | word-swap → "NO LEADS." |
| 7 | 120 | 5.00  | word-swap → "NO COMPANY." (gold) |
| 8 | 168 | 7.00  | CUT → Scene 4 + "NO WEBSITE." three-punch begins |
| 9 | 180 | 7.50  | "NO LEADS." |
|10 | 192 | 8.00  | "NO REVENUE." (gold) |
|11 | 240 | 10.00 | CUT → Scene 5 + "ONE WEBSITE" reveal + RISER starts |
|12 | 252 | 10.50 | "FIXES IT ALL." reveal |
|13 | 312 | 13.00 | impact_reverse — pre-drop tension |
|14 | 324 | 13.50 | impact_thud — drop primer |
|★ | 336 | 14.00 | **DROP** — CUT → Scene 6 + "$5,000 PER BUILD." scale-punch + sub_bass_boom + impact_thud + sweep lines |
|15 | 348 | 14.50 | "ONE CLIENT A WEEK." clip-reveal |
|16 | 360 | 15.00 | **★ SIGNATURE MOMENT** — "$250,000 A YEAR." scale-punch with gradient-text matte |
|17 | 528 | 22.00 | CUT → Scene 7 + "BUILD WEBSITES." reveal |
|18 | 552 | 23.00 | "SAVE COMPANIES." (gold) reveal |
|19 | 672 | 28.00 | CUT → near-black + CTA fades |

## Shot list

| Scene | t_in | t_out | shot_type | footage need | speed | gradient | grade_id | text id |
|---|---|---|---|---|---|---|---|---|
| 1 HOOK     | 0.00  | 2.00  | extreme close-up | empty office / desk / dust on a closed laptop | 100% | OFF | dc_max | HOOK_01 + HOOK_02 |
| 2 BUILD 1  | 2.00  | 4.00  | wide low-angle | person at desk, dark room, building | 100% | OFF | dc_std | B1_01 + B1_02 |
| 3 BUILD 2  | 4.00  | 7.00  | screen-grab | a flat / outdated website, slow zoom | 100% | OFF | dc_std | B2_01..03 (word swap) |
| 4 BUILD 3  | 7.00  | 10.00 | medium walk | confident walk through corridor/street | 100% | OFF | dc_std | B3_01..03 |
| 5 PRE-PEAK | 10.00 | 14.00 | portrait close | subject reflected in laptop screen, 60fps | 100→10% | OFF | dc_std | PP_01 + PP_02 |
| 6 PEAK ★   | 14.00 | 22.00 | portrait slow-mo | twixtor continues from 5, **gradient sweep** on subject | 10% | ON | dc_peak | PEAK_01..03 |
| 7 RES      | 22.00 | 28.00 | confident static | direct eye contact, calm, dimly lit | 100% | gold soft | dc_resolution | RES_01 + RES_02 |
| 8 CTA      | 28.00 | 32.00 | near-black (or scene 7 hold) | — | — | — | dc_cta | CTA_01 + CTA_02 |

## Signature moment ★

- **Where:** Scene 6, frame 360 → 528 (t = 15.0s → 22.0s, hold 7s)
- **What:** "$250,000 A YEAR." rendered with the purple→cyan→orange gradient as an alpha matte. Subject in slow-motion behind. Camera shake 8 frames at f336.
- **AE handoff:** Required for Twixtor speed ramp + reactive gradient on subject. Python rough cut shows freeze frame placeholder.

## Sign-off

Before any VO recording, confirm:
1. The script lines (above)
2. The beat assignment (drop lands at f336 — does that fit your music?)
3. The signature moment placement (gradient text on "$250,000 A YEAR.")
4. The handle (`@animex680` — change if different)
