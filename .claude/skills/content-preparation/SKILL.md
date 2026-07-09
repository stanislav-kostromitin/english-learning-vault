---
name: content-preparation
description: Use at the end of an active session, or when explicitly asked to prepare ahead, to draft the grammar note and/or vocabulary notes for the next 1-2 lessons in Progress Tracker's "Next Lessons" queue, marked as stage/status not-started or learn, with flashcards ready, so the next session starts with material already in place instead of being created live under time pressure.
---

# Content Preparation

## Why this exists

Creating a grammar or vocabulary note live, mid-lesson, competes with actually
teaching. Preparing the next lesson's reference material in advance - clearly
marked as not-yet-taught - lets the active session focus on practice instead of
note-writing, and is what makes the agent "a driving force forward" rather than
reactive.

## What to prepare

1. Read `09-Progress/Progress Tracker.md` "Next Lessons" - take the next 1-2 items
   not yet covered by an existing note in `01-Grammar/` or `02-Dictionary/Words/`.
2. For a grammar topic: create the note via `10-Templates/Grammar Note Template.md`,
   filled in with a real explanation (structure, QA examples, key idea) - this is
   reference material, not a record of a lesson that happened, so mark
   `stage: not-started` or `stage: learn` (whichever matches the current Progress
   Tracker confidence for that topic - don't invent a higher stage).
3. For vocabulary: create word notes via `10-Templates/Vocabulary Word Template.md`
   for words already listed in `02-Dictionary/Vocabulary Index.md`'s priority table
   but without their own note yet.
4. Add flashcards to new notes using the `::` format so they're immediately in the
   Spaced Repetition queue - but don't add fabricated review history
   (`<!--SR:...-->` comments) to unreviewed cards; only the plugin writes those,
   after a real review.

## Before writing - check for duplicates

Always check `02-Dictionary/Words/` and `01-Grammar/` for an existing note on the
same concept before creating a new one (case-insensitively, and check both the
filename and the `# Title` heading) - this is exactly how the `bug` / `bug1`
duplicate happened before. If unsure whether something already exists, run the
relevant check from `vault-maintainer` first.

## After preparing

- Update `01-Grammar/Grammar Index.md` or `02-Dictionary/Vocabulary Index.md` to
  link the new note - and if the note fills an item on the "known gap" list,
  remove it from that list (see `vault-maintainer`, stale gap notes).
- Do not change `Progress Tracker.md` stage/confidence values - preparing a
  reference note is not the same as teaching or practicing it. Only the actual
  lesson (and `session-focus-guard`'s production-check) changes progress.
- Mention in the session wrap-up that material for the next lesson is ready, so the
  person knows without having to check the vault themselves.
