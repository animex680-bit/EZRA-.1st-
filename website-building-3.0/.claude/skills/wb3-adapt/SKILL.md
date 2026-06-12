---
name: wb3-adapt
description: The adaptation engine of Website Building 3.0 — run on EVERY piece of user feedback, especially "no", "don't like it", or lukewarm reactions. Captures feedback verbatim, diagnoses the rule that produced the rejection, edits that rule in the skill files, rebuilds, and maintains the user's taste profile. The system must never repeat a logged rejection.
---

# wb3-adapt — Rejections rewrite the rules

The full protocol lives in `ADAPT.md` at the repo root (capture → diagnose →
classify → edit → rebuild → confirm). This skill is the executable summary.

## When to invoke

- The user says no / don't like it / bland / meh / "change this".
- The user approves something previously experimental (log the WIN, promote to default).
- A reveal lands flat (silence/short reply = soft no — probe, then log).
- Before ANY design is presented: scan `FEEDBACK_LOG.md` and the `ADAPT.md` taste
  profile, and verify the work violates none of it. This pre-check is half the skill.

## The move, compressed

1. Quote the feedback verbatim into `FEEDBACK_LOG.md` (date, project, category, OPEN).
2. Name the rule/default/gap that produced the rejected output. Be honest: "no rule
   existed" is a diagnosis too.
3. Edit the skill file the classification table in `ADAPT.md` points at. The edit
   must be concrete enough that following it would have *prevented* this rejection.
4. If the category has now been rejected twice: rewrite the whole section AND add a
   matching check to `.claude/agents/logic-check.md` so the agent catches it
   pre-presentation forever after.
5. Update the taste profile in `ADAPT.md` (add ❌ or ✅ lines).
6. Rebuild the deliverable under the new rule; re-present; mark RESOLVED on approval.

## Why this is the differentiator

Templates and one-shot AI builds produce the same output after every rejection.
This system converges on the user's taste: each "no" permanently removes a class of
mistakes. Ten rejections in, the pipeline has a ten-rule head start no fresh session
has. Guard the log files accordingly — they are the most valuable artifact in the repo.
