# LEARNINGS — reels pipeline

Newest at top. Tags: `RECURRING`, `OPEN`, `LOCKED-IN`.

---

## 2026-06-08 · #001 Building Websites — v3 FAIL (seed entry)

This entry seeds the pipeline based on the two failed attempts before the pipeline existed.

### What was tried
Rendered the entire reel as pure kinetic typography in Python + Pillow + numpy — text on a black background. Twice. Both ugly. Watcher proved it: 52 safe-area failures, 97 dead frames on the supposedly "fixed" v2.

### Root causes
1. **`RECURRING` `LOCKED-IN`** — **No footage = slop.** A 0x100x-style reel without real footage is not a reel, it's a slideshow. The orchestrator skill now refuses to render without footage unless the brief is explicitly "kinetic typography only."
2. **`RECURRING` `LOCKED-IN`** — **Text positions were calculated from natural rest position, not bbox after font-scaled rendering.** Result: text bleeds outside IG-safe area. `reels-captions` now requires safe-area math in font metrics, not centerline guesses.
3. **`RECURRING` `LOCKED-IN`** — **No watcher in the loop.** Every render shipped without a programmatic verification step, so visual "looks fine" beat actual frame-by-frame checks. The watcher is now non-negotiable.
4. **`LOCKED-IN`** — **No real Twixtor / character-gradient possible in Python.** The signature 0x100x look needs After Effects. Pipeline now produces an AE handoff (.jsx + assets) for those scenes — Python renders the rough cut.

### Watcher findings on v2 (proof)
- `safe_area × 52` — bbox of "EVERY WEBSITE / IS A MONEY MACHINE" went 64px above safe-top and 142px below safe-bottom. Bbox of "$3,000 A MONTH" went 43px past both sides.
- `dead_frame × 97` — most of scenes 1, 2, 5, 8 were just black. Mean luma < 10. (because there was no footage layer at all.)
- `caption_coverage = 71.9%` — 28% of frames had no caption AND no footage. Visual dead air.

### Skill edits applied (from this learning)
- [x] `reels/SKILL.md` — anti-slop bar #1: "real footage present" (refuses without)
- [x] `reels-watcher/SKILL.md` — created from scratch; runs after every render
- [x] `reels-footage/SKILL.md` — created from scratch; hard rule that every scene must have a `cut_path`
- [x] `reels-captions/SKILL.md` — added "rules the watcher enforces": safe area, ±1 frame, max 2 lines, no yellow karaoke
- [x] `reels-render/SKILL.md` — added "always run watcher immediately after render; do not show user before verdict"

### Open items
- `OPEN` — No Whisper installed in the env. Fallback documented (user runs locally + uploads `vo_words.json`) but not auto-tested. Validate on next reel.
- `OPEN` — No real SFX library in `03-assets/sfx/` yet. The skill references filenames; the user needs to populate the folder before `reels-sound` can run.
- `OPEN` — AE handoff `compose.py --mode=ae-handoff` is documented in the skill but not implemented in code. Implement when needed for next on-face reel.

---

(Future entries below.)
