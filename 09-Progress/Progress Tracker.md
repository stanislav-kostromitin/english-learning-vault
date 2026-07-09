# Progress Tracker

Last major sync: 2026-07-04

This file is the main recovery point after chat history cleanup.

## Current Level

Current working level: A2 → B1.

Target path:

```text
A2 → B1 → B2 → C1
```

Main goal: practical English for QA Automation, technical communication, meetings, interviews, and daily work.

## Project Operating Mode

The course now uses two types of chats.

### Context / Management Chat

Used for:

- course rules;
- methodology;
- planning;
- Progress Tracker updates;
- Grammar Tracker updates;
- Vocabulary Tracker updates;
- Error Knowledge Base;
- QA / IT topic coverage;
- long-term course memory.

### Lesson Chats

Used for actual lessons:

- grammar;
- speaking;
- writing;
- listening;
- reading;
- homework;
- live correction.

The repository remains the source of truth. The context chat controls the system. Lesson chats execute the lesson.

## Learning Method

A topic is tracked through four stages:

| Stage | Meaning | Completion signal |
|---|---|---|
| Learn | Understand the concept | Can explain the basic idea |
| Recall | Retrieve later without hints | Can answer after delay |
| Consolidating | Between Recall and Production — recall is stable, but real-time use is still slow/hesitant | Can answer quickly without hints, but still pauses in live speech |
| Production | Use in speech/writing | Can use in QA/work examples |
| Automation | Use without translation | Can speak naturally under pressure |

No topic should be marked as completed after theory only.

## Grammar Progress

| Topic | Status | Confidence | Stage | Notes |
|---|---:|---:|---|---|
| Past Simple | 🟩 | 95% | Automation | Good understanding. Needs automatic usage in stories and work reports. |
| Present Simple | 🟨 | 90%* | Learn | Reverted from Automation during 2026-07-09 audit — no demonstrated pressure-tested use was on record, per CLAUDE.md §4 policy. Confidence % needs reassessment against the Learn stage. |
| Present Continuous | 🟩 | 90% | Consolidating | Understood: now, temporary situations, arrangements. Needs occasional review with state verbs. |
| Present Simple vs Present Continuous | 🟩 | 90% | Production | Important contrast: fact/routine vs current temporary action. |
| Present Perfect | 🟩 | 85% | Consolidating | Good understanding of result, experience, recent completed actions. |
| Present Perfect vs Past Simple | 🟩 | 85% | Production | Understood conceptually. Needs faster automatic choice in speaking. |
| Present Perfect Continuous | 🟨 | 75–85% | Production | Main active topic. Needs deeper practice with completed time blocks, duration, and activity focus. |
| Present Perfect vs Present Perfect Continuous | 🟨 | 70% | Learn → Production | Next priority. Need to feel result vs activity/duration. |
| Comparative Adjectives | 🟩 | 80% | Recall | Covered. Needs light review only. |
| Quantifiers | 🟩 | 80% | Recall | Covered: much/many/a lot of/few/little etc. Needs periodic review. |
| First Conditional | 🟩 | 75% | Recall | Covered. Needs speaking practice. |
| Passive Voice | 🟨 | 65% | Learn | Basics covered. Needs structured review and QA examples. |
| Articles | 🟨 | 60% | Learn | Frequent errors with a/an/the/no article. Needs focused practice. |
| Prepositions | 🟨 | 60% | Learn | Frequent work phrases: in a meeting, on a call, at work, work on, switch to. |
| State verbs | 🟨 | 0%* | Learn | Note frontmatter set to learn/active during 2026-07-09 audit sync — confidence % not yet assessed, treat as just-started, still the next grammar support topic before deeper continuous tense work. |
| Past Continuous | 🟥 | 0% | Not Started | Not started as a focused topic. |
| Past Perfect | 🟥 | 0% | Not Started | Not started as a focused topic. |
| Future forms | 🟥 | 0% | Not Started | Not started as a focused topic. |
| Modal Verbs | 🟥 | 0% | Not Started | Not started as a focused topic. |
| Conditionals | 🟥 | 25% | Learn | First Conditional covered; other conditionals not started. |
| Reported Speech | 🟥 | 0% | Not Started | Not started. |
| Relative Clauses | 🟥 | 0% | Not Started | Not started. |

Legend:

- 🟩 usable / mostly learned
- 🟨 active review / partially learned
- 🟥 not started or weak

## Current Focus

Do not start a new large grammar block yet.

Current learning focus:

1. Finish Present Perfect Continuous.
2. Practice Present Perfect vs Present Perfect Continuous.
3. Add State verbs because they affect Continuous usage.
4. Keep Daily Stand-up speaking practice in every lesson.
5. Continue QA vocabulary and phrase building.
6. Start tracking repeated mistakes in a more explicit Error Knowledge Base format.
7. Increase active recall and spaced review instead of repeating theory passively.

## Next Lessons

1. Lesson 07 — Present Perfect Continuous final consolidation.
2. Lesson 08 — Present Perfect vs Present Perfect Continuous.
3. Lesson 09 — State verbs: know, understand, believe, like, see, think, have.
4. Lesson 10 — Articles for QA communication.
5. Lesson 11 — Daily stand-up simulation with correction.
6. Lesson 12 — Passive Voice for bugs, APIs, deployments, and reports.

## Vocabulary Progress

| Area | Status | Notes |
|---|---:|---|
| QA Daily vocabulary | 🟨 | Needs repeated speaking use. |
| Bug discussion phrases | 🟨 | Reproduce, investigate, root cause, workaround, intermittent. |
| Meeting phrases | 🟨 | Clarification and disagreement phrases started. Needs practice. |
| Interview phrases | 🟥 | Needs structured preparation. |
| Technical API vocabulary | 🟨 | Used in work context, needs English phrasing practice. |
| Grammar vocabulary | 🟨 | Need stable terms: result, duration, completed action, state verb. |
| Natural collocations | 🟨 | Priority: learn phrases, not isolated words. |

## Known Weak Points

### Grammar

- Articles: a/an/the/no article.
- Prepositions in work phrases.
- Present Perfect Continuous vs completed time blocks.
- Present Perfect vs Present Perfect Continuous.
- State verbs with Continuous forms.
- Passive Voice in technical reports.

### Vocabulary / Spelling

Common repeated spelling issues:

- feature
- investigate
- production
- meeting
- cause
- deployed
- sentence
- first
- automation
- switch

### Thinking Mistakes

Important recurring principles:

- `worked on` does not mean `finished`.
- Jira status does not define English tense.
- `from 9 to 11` is a completed time block, so Past Simple is usually better.
- Present Perfect Continuous emphasizes activity or duration; it does not always mean the action is unfinished.
- Choose tense based on what the listener needs to know.

## Error Knowledge Base Rules

Repeated mistakes should be logged with:

- wrong phrase;
- corrected phrase;
- reason;
- category;
- date;
- status: active / reviewing / resolved.

A mistake is resolved only after it disappears from several lessons and the learner can use the correct form under pressure.

## QA / IT Topics To Cover

High-priority professional topics:

- Daily stand-up
- Bug discussion
- Sprint planning / review
- Root cause analysis
- Production incident
- Release and deployment
- Logs analysis
- API testing
- Automation framework explanation
- CI/CD
- Performance testing
- Jira comments
- Technical interview answers
- Demo speech

## Lesson Format To Continue After Chat Cleanup

Each lesson should follow this structure:

1. Short review of weak points.
2. One grammar/vocabulary focus only.
3. QA/work examples.
4. Speaking or writing practice.
5. Error correction with explanation.
6. Update Vault if new reusable material appears.
7. Mini homework, reading, or listening task.

## Recovery Prompt After Chat Cleanup

Use this prompt in a new lesson chat:

```text
Продолжим обучение по English Learning Vault. Проверь Progress Tracker и начни следующий урок с текущего места.
```

Use this prompt in the context/management chat:

```text
Обновим English Learning Vault. Проверь Course Rules, Progress Tracker, текущий план и предложи корректировки курса.
```
