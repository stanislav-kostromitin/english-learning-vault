---
name: vault-maintainer
description: Use periodically (roughly every 5-10 active sessions, or whenever the person asks to check/clean up the vault) to audit the English Learning Vault for broken wikilinks, contradicting data between files, stale or duplicate notes, and frontmatter drift, then propose fixes as a dry-run diff before writing anything. Also use proactively at the end of an active session if new notes were created, to catch duplicates or broken links introduced during that session before they accumulate.
---

# Vault Maintainer

## Why this exists

The vault had three real, found-in-practice failure modes before this skill existed:
duplicate notes for the same word with disagreeing spaced-repetition history (real
progress data at risk of being silently lost), two files tracking the same word's
status with contradicting values, and lesson/topic numbering drifting out of sync
between `Progress Tracker.md` and `Lessons Index.md`. This skill exists to catch
these automatically instead of relying on an external audit each time.

Modeled on the `wiki-lint --consolidate` pattern from Ar9av/obsidian-wiki: find
issues, propose a dry-run diff, get confirmation, only then write.

## Checks to run

1. **Broken wikilinks.** Every `[[note name]]` should resolve to an actual file.
   Exception: intentional forward-references already documented as a known gap
   (see the notes at the top of `01-Grammar/Grammar Index.md` and
   `05-Lessons/Lessons Index.md`) - don't re-flag those unless the gap list itself
   is out of date (i.e. a linked note now exists but is still listed as missing).

2. **Duplicate notes for the same concept.** Same word or grammar topic tracked in
   more than one file (e.g. `word.md` and `word1.md`, or the same word appearing in
   both `02-Dictionary/Words/` and a table in `02-Dictionary/QA English
   Dictionary.md`). As of this pass, exact near-duplicate filenames in
   `01-Grammar/`/`02-Dictionary/Words/` are also blocked in real time by
   `.claude/hooks/check-duplicate-note.py` (PreToolUse hook) - this check here is
   the periodic sweep for anything the hook didn't cover (cross-folder duplicates,
   duplicates predating the hook, or the same concept under genuinely different
   names). If found: **never delete either file outright.** Check both for
   spaced-repetition scheduling comments (`<!--SR:...-->`) - if either has real
   review history, that history must be preserved in the merged result. Merge into
   the more recently-updated / more complete file (check `git log --follow`), keep
   the union of flashcards, then remove the duplicate and fix every reference to it.

3. **Contradicting status data.** Same word/topic with different status (🟥/🟨/🟩 or
   stage values) in different files. Resolve by recency (`git log`), flag the
   losing value in the merged note as "carried over, worth re-checking" rather than
   silently picking one - the person's actual current ability is not something to
   guess.

4. **Numbering/reference drift.** Lesson numbers, next-lesson plans, and topic
   references across `Progress Tracker.md`, `Lessons Index.md`, and `Grammar
   Index.md` should agree. Cross-check before proposing a fix.

5. **Frontmatter schema drift.** New notes should use the field names defined in
   `10-Templates/*.md` (`stage`, not a mix of `stage` and `status` meaning
   different things for the same concept). Flag inconsistent schemas across notes
   of the same `type`.

6. **Stale "known gap" notes.** If a gap note (e.g. in Grammar Index) lists a topic
   that now has a real file, update the gap note - don't leave it claiming
   something is missing when it isn't.

## Workflow

1. Run all checks above, collect findings.
2. Present findings as a list, grouped by severity: data-loss risk (duplicates with
   review history) first, then contradictions, then drift, then stale docs.
3. For each finding, show the proposed change as a diff-style before/after, not just
   a description.
4. Wait for confirmation before writing, unless the person has explicitly granted
   standing permission for this session ("go ahead and fix what you find").
5. After writing, run the broken-wikilink check again to confirm the fix didn't
   introduce a new one.

## What this skill does NOT do

- Does not fabricate missing lesson or grammar content to fill gaps - a gap gets
  documented, not invented (see `CLAUDE.md`, antipatterns).
- Does not touch `COURSE_RULES.md` methodology - only structural/data consistency.
- Does not change spaced-repetition scheduling data except to relocate it intact
  during a merge.
