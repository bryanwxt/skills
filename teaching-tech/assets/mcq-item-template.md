# Formative MCQ item template

Each distractor must be **plausible** and **diagnostic**: map it to a specific misconception and say what you'll do if many learners pick it.

```
ID: <lesson>-<n>
Objective / concept: <what this checks>
Bloom level: <remember / understand / apply / analyze / evaluate>
When to use: <after episode X / as a pre-check>

Stem:
  <question, code snippet if any>

Options:
  A) <correct answer>
  B) <distractor>  — misconception: <…>  — if chosen by many: <reteach plan>
  C) <distractor>  — misconception: <…>  — if chosen by many: <reteach plan>
  D) <distractor>  — misconception: <…>  — if chosen by many: <reteach plan>
  E) I don't know (optional)

Answer: A
Explanation to give after the vote: <2–3 sentences>
Follow-up (if split): peer discussion 2–3 min, revote
```

Worked example:
```
Stem:
  grade = 65
  total = grade + 10
  grade = 80
  print(total)

A) 75
B) 90   — misconception: variables update like spreadsheet cells — reteach: assignment copies the current value once; trace values line by line
C) 80   — misconception: `total` refers to `grade` itself — reteach: names vs values; draw memory boxes
D) Error — misconception: can't reassign a variable after using it — reteach: variables can be rebound any time
Answer: A
```

Rules:
- Order options randomly when delivered (the recommended-first rule applies to alignment questions for the user, not to learner quizzes).
- No joke options.
- Offer "I don't know" to reduce guessing when stakes are low.
- For peer instruction, pick questions that are likely to split the room.
