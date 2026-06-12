# ADAPT.md — The Adaptation Protocol

> The plan is not a document, it is a moving target. Every time the user says
> **"no"**, **"don't like it"**, **"bland"**, **"meh"**, or anything short of clear
> approval, the system itself must change — not just the deliverable.

This is the mechanism that makes Website Building 3.0 different from a static
checklist: rejections rewrite the rules that produced them.

## The loop (run on EVERY piece of negative or lukewarm feedback)

```
user feedback ("no" / "don't like X" / silence after a reveal)
        │
        ▼
1. CAPTURE   — quote the feedback verbatim into FEEDBACK_LOG.md (date, project, context).
        │
        ▼
2. DIAGNOSE  — find the RULE, DEFAULT, or GAP that produced the rejected output.
   Ask: which skill file told me to do the thing the user rejected?
   If no rule produced it, the gap IS the finding (an unwritten default failed).
        │
        ▼
3. CLASSIFY  — taste | concept | motion | assets | copy | layout | tech | business.
   This decides which skill file gets edited.
        │
        ▼
4. EDIT      — change the rule in the relevant SKILL.md (or add a new rule).
   The edit must be specific enough that following it would have PREVENTED
   the rejection. "Be better" is not an edit. Record the edit in FEEDBACK_LOG.md.
        │
        ▼
5. REBUILD   — apply the new rule to the current deliverable and re-present.
        │
        ▼
6. CONFIRM   — on the next approval, mark the log entry RESOLVED. If the same
   class of rejection occurs twice, the first edit was too shallow — escalate:
   rewrite the section, not the sentence.
```

## Hard rules

- **Never repeat a logged rejection.** Before presenting any design, scan
  FEEDBACK_LOG.md for open and resolved entries; check the new work against every one.
- **Two strikes = structural change.** Same category rejected twice → the skill section
  gets rewritten, and the `logic-check` agent gets a new check added so it is caught
  *before* the user ever sees it again.
- **Positive signal is logged too.** When the user says "this landed", record WHAT
  landed and WHY, and promote it from experiment to default.
- **Feedback outranks research.** If the top creators do X but the user rejects X,
  the user's taste wins in this repo. Note the divergence in PATTERNS.md.
- **Silence is feedback.** If the user moves on without enthusiasm, treat it as a
  soft no and probe what fell flat.

## Taste profile (grows over time — the system's model of the user)

Seeded from the EZRA project history; updated by every log entry:

- ❌ Static anything — "static reads as cheap". Tiles must drift and react to cursor.
- ❌ Plain fade-up text reveals. Scroll must *create* the words (scrubbed assembly).
- ❌ Hard section edges. Sections blend/blip (iris/circle reveals, crossfades).
- ❌ Bland/system typography. Type is the hero — characterful editorial pairings.
- ❌ Stretched low-res footage. Crisp small tile > soft big one, always.
- ✅ Scroll-as-scrubber pinned video. ✅ Cursor-reactive tiles (evade/attract).
- ✅ Case studies with price + fit shown in the page (the money mechanic).
- ✅ Living details: glowing magnetic buttons, ribbon/snake accents under content.

## Where edits land (classification → file)

| Category  | File to edit |
|-----------|--------------|
| taste / aesthetics | `ADAPT.md` taste profile + `web3d-concept/SKILL.md` |
| concept / story    | `web3d-concept/SKILL.md` |
| motion / animation | `web3d-motion/SKILL.md` |
| assets / resolution| `wb3-assets/SKILL.md` + `web3d-assets/SKILL.md` |
| copy / messaging   | `web3d-business/SKILL.md` |
| layout / type      | `web3d-concept/SKILL.md` + taste profile |
| tech / bugs        | `web3d-build/SKILL.md` |
| business / selling | `web3d-business/SKILL.md` |
| QA missed it       | `.claude/agents/logic-check.md` (add the check) |
