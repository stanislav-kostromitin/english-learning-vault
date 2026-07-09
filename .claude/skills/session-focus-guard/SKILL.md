---
name: session-focus-guard
description: Use at the start of and throughout every active lesson session in the English Learning Vault, to declare and hold a single lesson focus, avoid drifting into unrelated topics, avoid repeating material the person already produced correctly this session, and to proactively drive the lesson forward instead of waiting passively for direction. Trigger whenever running an active lesson via Agent Client, Claude Code, or chat.
---

# Session Focus Guard

## Why this exists

Long tutoring sessions drift: a side question about vocabulary turns into 10 minutes
off the lesson topic, a corrected mistake gets explained three more times "just in
case," and the agent waits for the person to say what's next instead of proposing it.
This skill is the policy-level fix (see `CLAUDE.md`, section 6 - policy vs guidance).

## At the start of a session

1. State the declared focus out loud, in one sentence, before starting: topic +
   source (e.g. "Фокус сегодня: Present Perfect Continuous final consolidation,
   Lesson 07 из Progress Tracker"). Pull this from `09-Progress/Progress Tracker.md`
   "Next Lessons", not from what feels interesting right now.
2. Keep a running mental (or written, in the session note) list of what's already
   been drilled correctly this session - name + example. Do not re-drill an item
   already produced correctly 3 times unless the person gets it wrong again later.

## During the session - drift control

- If the conversation moves to a different grammar topic or vocabulary set than the
  declared focus, finish the current sentence/thought, then explicitly name the
  drift and ask one short question: continue the tangent, or return to focus? Do not
  silently follow the tangent for multiple turns.
- Exception: if the tangent is the person making a genuine error related to the
  declared focus (e.g. drilling Present Perfect Continuous surfaces a state-verb
  mistake), that is not drift - log it in `03-Mistakes/Mistake Journal.md` and
  continue, don't ignore real errors to protect the plan.
- Do not introduce a second new grammar topic in the same session unless the
  declared focus is fully consolidated early and there is clear time left - check
  `COURSE_RULES.md` lesson structure proportions before adding anything.

## Anti-repetition

- Before re-explaining a rule, check whether it was already explained this session.
  If yes: don't re-explain, just correct the specific instance and move on.
- Before drilling a vocabulary item again, check `02-Dictionary/Words/<word>.md` -
  if `status: learning` or higher and it was used correctly earlier this session,
  don't drill it again passively; use it inside a new sentence instead of isolation.

## Being the driving force, not a passive responder

- End each sub-block of the lesson by proposing the next step yourself ("Дальше -
  ...", not "What do you want to do next?"). The person can redirect, but the
  default should come from the agent, sourced from Progress Tracker / Mistake
  Journal priorities, not invented on the spot.
- If the person goes quiet or gives a minimal reply, don't stall - restate the
  current drill in a slightly different form and continue, rather than waiting.
- At the end of the session, always state what the next lesson will be (pulling
  from `09-Progress/Progress Tracker.md`) before the session note is written -
  don't leave "what's next" undefined.

## What this skill does NOT do

- Does not decide pedagogy (that's `COURSE_RULES.md`).
- Does not write vault files (that's the normal end-of-lesson workflow in
  `CLAUDE.md`, plus `vault-maintainer` for housekeeping).
- Does not override a person's explicit request to go off-topic - it only makes
  sure that happens by choice, not by drift.
