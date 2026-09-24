# Exercises and assessments

## Contents
1. Designing MCQs with diagnostic power
2. Faded examples and fill-in-the-blanks
3. Parsons problems
4. Code and run (and its variants)
5. Tracing and modification exercises
6. Diagrams, matching, ranking, summarizing
7. Higher-level thinking: code review with a rubric
8. Automatic grading
9. Choosing an exercise type

---

## 1. Designing MCQs with diagnostic power
A good MCQ doesn't just check whether someone knows a fact — its wrong answers show *which* misunderstanding the learner has, telling you what to explain next.

Example: "What is 37 + 15?" → 52 (correct); 42 (drops the carry); 412 (treats columns as separate problems); 43 (carries back into the same column). Each distractor is **plausible** (could look right) and has **diagnostic power** (points to a specific fix).

How to build them:
1. Name the concept and the misconceptions you expect. Sources: questions learners asked before; your own past confusion; colleagues; the history of the field (old misconceptions persist); Q&A sites; open-ended questions in an earlier class.
2. Write the stem so the misconception would lead to a specific answer.
3. One correct answer; 2–3 distractors, each mapped to one misconception.
4. Optionally include "I don't know" to discourage guessing.
5. For each distractor, note what you'll reteach if many pick it.
6. No joke options — they reveal nothing and aren't funny twice.

In class: have everyone answer at once (coloured or numbered cards, a poll), let them talk to neighbours briefly, and vote **publicly** so they commit (hypercorrection). Use **peer instruction** (see delivery.md) for questions that split the room.

MCQs can go beyond recall — e.g. asking the order in which subtraction, a function call, and assignment happen in `price = add_taxes(cost - discount)`.

**Short-answer questions** with 2–5 word answers are also scalable. **Concept inventories** are validated MCQ sets that pinpoint misconceptions.

## 2. Faded examples and fill-in-the-blanks
- Start with a complete worked example of a strategy, then give a series of similar problems with progressively more blanks, ending with a blank function.
- Example series (accumulator pattern): full `total_length(words)` → fill in the loop parts of `word_lengths` → fill in initialization and update of `join_all` → write `make_acronym` from scratch.
- Choose what to fade based on the strategy being taught. Each step adds one new thing.
- **Fill in the blanks** is code-and-run with starter code: less intimidating and easier to check, because answers are more predictable.

## 3. Parsons problems
- Give the lines needed to solve a problem, jumbled; learners put them in order (and indent, if relevant). Strip indentation or braces so structure isn't given away.
- Focuses on control flow and data dependencies, avoiding the blank page and vocabulary recall. Takes less time than writing, with similar learning.
- **Harder variants:** add distractor lines that aren't needed, or require a few new lines.
- Labelled subgoals improve Parsons performance.
- Works for non-code too (recipe steps, shell pipelines).

## 4. Code and run
- **Code and run:** write code that produces a given output. In class, keep it short with only one or two plausible solutions. For novices, calling a named function is enough; for advanced learners, finding which function to call is more engaging. Can combine with an MCQ whose answer requires running something.
- **Trade-offs:** hard to assess — correct but unexpected solutions get rejected by auto-graders (demoralizing), and output-only checks give no feedback on process. **Mitigation:** give learners a small test suite to run before submitting; run a fuller one on submission.
- **Inverted code and run:** learners write tests to discover which of several listed bugs a function has. Teaches testing.

## 5. Tracing and modification
- **Tracing execution order:** list the order in which labelled lines execute (inverse of Parsons). Have learners write the sequence out — don't make it an MCQ, which adds search load.
- **Tracing values:** a table with variables as columns and lines (or iterations) as rows. Tracing variable values is the most effective sketching strategy for debugging.
- **Predict the output** before running — quick, and prompts "what if" questions.
- **Reverse execution:** find the input that produced a given output or error (good with error messages).
- **Minimal fix:** make (or pick) the smallest change that fixes a bug.
- **Theme and variation:** make a small change that alters the output in a specified way (swap a call, change an initial value, swap nested loops, reorder conditions). Tweaking working code is a real-world skill.
- **Refactoring:** change code without changing output. Many valid answers, so usually needs human grading.
- **Mangled code:** reconstruct code with comments removed and lines deleted, moved, or altered. Correlates well with code-writing ability and is cheaper to mark.
- **Reading error messages:** give practice interpreting them; reading them is as hard as reading code.

## 6. Diagrams, matching, ranking, summarizing
- **Free-form concept maps and diagrams:** reveal thinking, but need human judgment.
- **Labelling diagrams:** nearly as informative and much easier to scale (which variable points where; which code produced which part of a chart; order of nodes in a tree traversal).
- **Arranging diagram pieces:** a visual Parsons problem with as much skeleton as needed.
- **Matching:** one-to-one (equal lists) or many-to-many (harder — some items match several or none). Collect answers as pairs, not MCQs of pairs.
- **Ranking:** order items by speed, robustness, and so on. "Speed" rankings lean on recall; "robustness" rankings need judgment.
- **Summarization:** pick or write the best description of what code does or how output changes — higher-order and useful for bug reports. Short free-form answers work well with peer grading.

## 7. Higher-level thinking: code review with a rubric
Large projects, open discussion, and twitch coding are valuable but don't scale. Code review does:
- Give a rubric of fault types (e.g. poor variable name, unused variable, undefined variable, missing return value); learners attach comments to specific lines.
- Novices: tell them how many of each fault to find. Advanced learners: give only the fault types.
- Use **calibrated peer review** so learners see models of good feedback.

## 8. Automatic grading
- Satisfaction ≠ outcomes: disliked auto-graded weekly tests can still halve failure rates.
- **Fuzz testing** against a reference implementation catches errors that hand-written tests miss.
- **Unlocking tests:** learners must predict a test's expected result before they can run it — reduces confusion and questions.
- Off-the-shelf **style checkers don't match human grading** (over-penalize repeated minor issues; reward unchanged starter code).
- **Auto-feedback trap:** learners come to depend on the instructor's tests; misunderstood requirements pass anyway. Give hints only when learners have earned them by writing their own tests.
- Many auto-graders say *what* failed, not *how to fix it*, and are hard to adapt.
- **Sharing results:** showing expected outputs invites hard-coding; pass/fail only frustrates; comparing a **hash of the expected output** proves correctness without revealing the answer (best balance, more setup).
- When budgeting exercise time, include how often "simple" things fail (e.g. a file saved in the wrong folder).

## 9. Choosing an exercise type
| Goal | Good choices |
|---|---|
| Quick in-class check of understanding | MCQ with diagnostic distractors, predict the output, Parsons |
| Teach a new problem-solving strategy | Worked → faded examples, labelled subgoals |
| Build tracing and debugging skill | Trace values/order, reverse execution, minimal fix, error-message reading |
| Practise applying skills | Fill in the blanks, code and run, theme and variation |
| Teach testing | Inverted code and run, unlocking tests |
| Higher-order judgment | Ranking by robustness, summarization, code review with rubric |
| Check conceptual structure | Labelled diagrams, matching, concept maps |
| Summative | A final authentic task, plus items in formats learners have practised |
