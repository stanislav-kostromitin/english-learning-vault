---
type: grammar-guide
status: active
tags:
  - grammar-system
---
# Grammar Note Guidelines

Use this guide when creating or improving files in `01-Grammar/`.

## Explanation Rules

1. Start with meaning, not a formula.
2. Explain what the speaker wants the listener to understand.
3. Give the smallest useful structure after the meaning is clear.
4. Use QA/work examples before general textbook examples.
5. Add contrast with the nearest confusing form.
6. Add common mistakes with a wrong sentence, better sentence, and reason.
7. Finish with active production: stand-up, Jira/Slack update, bug discussion, or interview answer.

## Document Structure

Every grammar note should include:

- frontmatter with `type: grammar`, `stage`, `status`, and `flashcards/grammar`;
- `Meaning`;
- `Structure`;
- `QA / Work Examples`;
- `Contrast`;
- `Common Mistakes`;
- `Practice`;
- `Key Idea`;
- `Related Topics`;
- `#flashcards/grammar` cards in `Front::Back` format.

## Status And Stage

- `status: planned` means the note is only a placeholder.
- `status: active` means the topic is in current rotation.
- `status: reviewing` means it was covered but still needs recall/production.
- `stage: learn` is the default for new or weak topics.
- Do not use `stage: automation` unless the learner can produce the grammar naturally under pressure.

## Flashcards

Keep cards short and focused:

```text
When do we use Present Continuous?::For actions happening now or temporary situations around now.
I am investigate this issue. Correct it.::I am investigating this issue.
```

Do not add or edit scheduling comments manually. The Spaced Repetition plugin owns scheduling.
