# Course Rules

This file defines how the English learning project is maintained.

Last updated: 2026-07-04

## Main Goal

Build real practical English skills for QA Automation, technical communication, meetings, interviews, and daily work.

Target path:

```text
A2 → B1 → B2 → C1
```

The goal is not to "know all grammar rules". The goal is to communicate naturally, accurately, and fast enough for real work: meetings, bug discussions, interviews, demos, incidents, and written technical communication.

## Chat Separation Rule

Use different chats for different purposes.

### Context / Management Chat

This chat is used for:

- course rules;
- methodology;
- Progress Tracker updates;
- Grammar Tracker updates;
- Vocabulary Tracker updates;
- Mistake Journal / Error Knowledge Base;
- planning future lessons;
- changing the learning strategy;
- keeping long-term course context.

### Lesson Chats

Separate lesson chats are used for:

- grammar lessons;
- speaking practice;
- writing practice;
- listening / reading tasks;
- homework checking;
- live correction.

The context chat is the control center. Lesson chats are execution spaces.

## Core Principles

1. Do not learn grammar as isolated formulas.
2. Learn grammar through meaning, context, and real work situations.
3. Do not move too fast. A topic is continued until it becomes usable.
4. A grammar topic is not completed after explanation. It is completed only after automatic use in realistic speech/writing.
5. New vocabulary is added to the dictionary and reused in later lessons.
6. Repeated mistakes are stored in the Mistake Journal / Error Knowledge Base.
7. Every lesson must include active practice, not only theory.
8. Reading and listening should reinforce the current grammar and vocabulary.
9. The repository is the main source of truth. Chat is used for practice, explanations, and temporary interaction.
10. Course context, grammar, vocabulary, lesson notes, mistakes, and progress must be synchronized with this repository regularly.
11. The course plan may be changed when learner data shows a better path.
12. QA / IT English must be present regularly, not as a separate optional block.

## Learning Model

Each topic passes through four stages.

### Stage 1 — Learn

Understand the idea and the meaning behind the structure.

Example: do not memorize only the formula of Present Perfect Continuous. Understand what the speaker wants to emphasize: activity, duration, recent visible effect, or unfinished process.

### Stage 2 — Recall

Return to the topic later without hints.

This uses active recall and spaced review. If the learner cannot retrieve the structure without help, the topic is not stable yet.

### Stage 3 — Production

Use the topic in real speaking and writing.

Examples:

- Daily stand-up;
- bug discussion;
- Jira comment;
- production incident explanation;
- technical interview answer;
- demo presentation.

### Stage 4 — Automation

Use the topic naturally without translating from Russian/Ukrainian first.

Only at this stage can the topic be considered truly learned.

## Lesson Structure

Each lesson should usually include:

1. Short review of weak points.
2. One grammar or vocabulary focus.
3. Real QA / work examples.
4. Speaking or writing practice.
5. Error correction with explanation.
6. Repository update when new reusable material appears.
7. Mini homework, reading, or listening task.

Recommended distribution:

| Block | Share | Purpose |
|---|---:|---|
| Review | 10% | Spaced repetition and active recall |
| Grammar / form | 20% | Only what is needed for real communication |
| Speaking / production | 40% | Fluency, speed, automaticity |
| QA / IT English | 20% | Professional communication |
| Vocabulary / collocations | 10% | Natural phrases, not isolated words |

## Correction Style

Corrections should explain:

- what is wrong;
- why it is wrong;
- how to say it naturally;
- what thinking pattern caused the mistake;
- how to avoid the same mistake later.

If a sentence is grammatically correct but unnatural, mark it as unnatural and provide a natural work-safe version.

## Error Knowledge Base

Repeated or important mistakes must be tracked.

Each error should include:

- original incorrect phrase;
- corrected phrase;
- explanation;
- category: grammar / vocabulary / collocation / pronunciation / spelling / style;
- date noticed;
- status: active, reviewing, resolved.

A mistake is resolved only if it does not reappear for several lessons and the learner can produce the correct form under pressure.

## QA / IT Focus

Every stage of the course should include professional topics:

- Daily stand-up;
- Sprint Planning;
- Sprint Review;
- Retrospective;
- Bug discussion;
- Root Cause Analysis;
- Production incident;
- Release / deployment;
- Logs analysis;
- Test automation;
- Code review;
- API testing;
- Performance testing;
- CI/CD;
- Databases;
- Docker;
- Kafka;
- Security;
- Technical interviews;
- Customer communication;
- Demos and presentations.

Vocabulary should be learned as phrases and collocations, not as isolated words.

Examples:

```text
verify the fix
verify the deployment
reproduce the issue
investigate the root cause
roll back the deployment
run regression tests
check the logs
raise a blocker
clarify the acceptance criteria
```

## Repository Maintenance Rules

After a lesson, update relevant files when there is new reusable material:

- Grammar pages;
- Vocabulary pages;
- Mistake Journal;
- Cheat Sheet;
- Lesson notes;
- Progress Tracker;
- Homework / Reading / Listening if needed.

## Vault Synchronization Protocol

The GitHub repository `english-learning-vault` is the long-term storage for the course.

The chat is temporary. The repository is permanent.

At the end of each lesson or after any important correction, update the Vault when there is new reusable material.

Priority update order:

1. `09-Progress/Progress Tracker.md` — current topic, status, next steps, weak points.
2. `03-Mistakes/Mistake Journal.md` — repeated or important mistakes.
3. `02-Dictionary/` — new words, phrases, examples, QA vocabulary.
4. `01-Grammar/` — new rules, tense comparisons, usage notes, common mistakes.
5. `05-Lessons/` — lesson summary and what was practiced.
6. `06-Homework/`, `07-Reading/`, `08-Listening/` — only when new tasks/materials are assigned.

Do not duplicate the same rule in many places. Use links between files instead.

Do not mark a topic as completed only because the rule was explained. Mark it as completed only when the learner can use it in realistic work examples.

## Current Learning Strategy

Focus on understanding meaning and context before memorizing rules.

Use a practical combination of:

- comprehensible input;
- active recall;
- spaced repetition;
- meaningful output;
- interaction and correction;
- fluency training with familiar language;
- QA / IT domain practice.

Important recurring principle:

> Do not choose the tense based on the Jira status. Choose the tense based on what information the listener needs.

## Teacher Operating Rules

The teacher should:

- be direct and correction-focused;
- avoid artificial praise;
- challenge weak answers;
- prevent random topic jumping;
- adjust the plan based on recurring mistakes;
- keep QA / IT relevance high;
- increase English usage gradually;
- keep the Vault updated without waiting for explicit reminders when an update is clearly needed.
