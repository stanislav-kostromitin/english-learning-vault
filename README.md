# English Learning Vault

Personal English learning system focused on QA Automation, technical communication, grammar, vocabulary, speaking, reading, and listening.

## Dashboard

### Current Focus

- [[01-Grammar/Present Continuous|Present Continuous]]
- [[01-Grammar/Present Perfect|Present Perfect]]
- [[01-Grammar/Present Perfect Continuous|Present Perfect Continuous]]
- [[01-Grammar/Past Simple|Past Simple]]
- Daily stand-up speaking practice
- QA vocabulary for real work situations

### Quick Navigation

| Area | Link |
|---|---|
| Course rules | [[COURSE_RULES]] |
| Grammar index | [[01-Grammar/Grammar Index]] |
| Vocabulary index | [[02-Dictionary/Vocabulary Index]] |
| Mistake journal | [[03-Mistakes/Mistake Journal]] |
| QA cheat sheet | [[04-Cheat-Sheets/QA English Cheat Sheet]] |
| Lessons index | [[05-Lessons/Lessons Index]] |
| Homework | [[06-Homework/Homework Index]] |
| Reading | [[07-Reading/Reading Index]] |
| Listening | [[08-Listening/Listening Index]] |
| Progress tracker | [[09-Progress/Progress Tracker]] |
| Dashboard (Dataview) | [[09-Progress/Dashboard]] |
| CEFR checklist | [[09-Progress/CEFR Checklist]] |
| Operating agent (Claude Code) | [[CLAUDE]] |
| Setup / plugins | [[SETUP]] |
| Future skills outline | [[Skills-Outline]] |
| Real agent skills | `.claude/skills/` (session-focus-guard, content-preparation, vault-maintainer) |
| Architecture review vs 10 reference projects | [[ARCHITECTURE-REVIEW]] |

## Current Goal

A2 → B1 → B2 → C1

Primary focus:

- Daily stand-ups
- Bug discussions
- Sprint planning / review
- Technical interviews
- QA Automation vocabulary
- Grammar through real work situations

## Working Process

1. Before a lesson, pull updates.

```bash
git pull
```

2. Use ChatGPT for the lesson and speaking/writing practice, or the **Agent Client**
   plugin (Claude Code inside Obsidian - see `CLAUDE.md`, `SETUP.md`) for an
   alternative that reads/writes this repository directly, no copy-pasting needed.
3. After the lesson, the AI updates this repository.
4. Pull again (or let Obsidian Git sync) to see updated grammar notes, vocabulary, mistakes, reading, listening, and homework.

## Main Rule

Do not learn grammar as isolated formulas. Learn how native speakers choose tense based on meaning, context, and what the listener wants to know.

## Repository Structure

```text
01-Grammar/
02-Dictionary/
03-Mistakes/
04-Cheat-Sheets/
05-Lessons/
06-Homework/
07-Reading/
08-Listening/
09-Progress/
10-Templates/
```
