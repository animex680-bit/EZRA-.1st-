# FEEDBACK_LOG.md — append-only

Every "no", every "don't like", every win. Format per entry:

```
## YYYY-MM-DD — [project] — [category] — OPEN|RESOLVED
- Feedback (verbatim): "..."
- Diagnosis: the rule/default/gap that produced it
- Edit made: file + what changed
- Result: what happened on re-present
```

---

## 2026-05-30 — AluCape — motion/taste — RESOLVED (seed entry, imported from EZRA history)
- Feedback (verbatim): topography shader and text animations are "bland".
- Diagnosis: default fade-up reveals; no scroll-scrubbed assembly; static backdrop.
- Edit made: web3d-motion — scroll-creates-the-words, scroll-as-scrubber video,
  seamless transitions, perpetual + cursor-reactive tiles became required techniques.
- Result: next round — "scrubbed video, scroll-built words, reactive tiles all landed".

## 2026-05-30 — AluCape — layout/type — RESOLVED (seed entry)
- Feedback (verbatim): settled text positions "weird since I can read them" (barely).
- Diagnosis: scatter animation left residual transforms at rest; settled state illegible.
- Edit made: web3d-motion — settled-text-must-be-clean rule (zero residual transform at p=1).
- Result: accepted.

## 2026-05-30 — AluCape — assets — RESOLVED (seed entry)
- Feedback context: low-res clips stretched to large containers looked cheap.
- Diagnosis: no resolution floor existed.
- Edit made: web3d-assets — RESOLUTION RULE (2K+ for fullscreen, small tiles for <1080p)
  and ASK-FOR-ASSETS RULE (precise spec, never silently stretch).
- Result: rule held on the next asset round (11 clips, none stretched).
