# Exercise Types

> Source: Greg Wilson, *Teaching Tech Together* (2018), Ch. 12 "Exercise Types" (§12 intro, §12.1–§12.6). Licensed CC BY 4.0 (https://creativecommons.org/licenses/by/4.0/); condensed and restructured for skill use, with quotations marked. Rule IDs use prefix `EXR`.

## When a skill needs this
- Generating formative-assessment exercises for a programming or technical lesson, and choosing the right *type* for the skill being checked.
- Reviewing an exercise set for ambiguity, gradeability, cognitive load, or mismatch between type and goal.
- Designing or choosing an auto-grader, and deciding how much test information to reveal to learners.
- Building code-review, peer-review, or other higher-level exercises that need rubrics.
- Estimating time for in-class exercises, including time lost to "simple" failures.

## Catalog: pick an exercise type

"Auto-gradable" says how the book describes grading at scale. "Novice fit" is the book's guidance where it gives any; otherwise "—".

| Type | § | What it assesses | Auto-gradable? | Novice fit | Main pitfall |
|---|---|---|---|---|---|
| Multiple choice (MCQ) | 12.1 | Recall and understanding; can require judgment; diagnoses misconceptions via distractors | Yes | Good | Distractors that don't map to specific misconceptions |
| Code & Run (C&R) | 12.1 | Ability to write code that produces a specified output | Partly (tests or output) | Good if the function is named | Many valid answers; graders reject valid code |
| MCQ + C&R | 12.1 | Ability to run a command and interpret its result | Yes | Good | Answer depends on environment state |
| Inverted C&R (write tests) | 12.1 | Testing skill; checking code against a spec | Partly | — | Needs a precise spec and seeded bugs |
| Fill in the blanks | 12.1 | Targeted syntax or concept inside given structure | Yes (predictable answers) | Very good (less intimidating) | Blank ambiguity; multiple fills |
| Parsons Problem | 12.1 | Control flow, separately from vocabulary | Yes (with tools) | Very good | Distractor lines make it much harder |
| Tracing execution order | 12.2 | Control flow; loops, conditionals, evaluation order; debugging | Yes (sequence of labels) | Good | Presenting it as an MCQ adds load for no value |
| Tracing values | 12.2 | Variable state over time | Yes (list or table) | Good | Inconsistent trace notation |
| Reverse execution | 12.2 | Search and deduction; debugging from error output | Yes (check input) | — | Multiple valid inputs |
| Minimal fix | 12.2 | Debugging: locate and repair the smallest bug | Yes (as C&R or MCQ) | — | Several "minimal" fixes possible |
| Theme and variations | 12.2 | Modifying working code to change output | Yes (output) | — | Under-specified allowed changes |
| Refactoring | 12.2 | Restructuring without changing behaviour | Hard (human grading) | — | Too many valid refactorings to grade |
| Free-form diagram / concept map | 12.3 | Learner's mental model | No (human time) | — | Doesn't scale |
| Labelling a diagram | 12.3 | Structure and relationships, constrained | Yes (scales) | — | — |
| Arrange diagram pieces | 12.3 | Visual Parsons Problem; structure | Partly | Skeleton adjustable | Too little or too much skeleton |
| One-to-one matching | 12.3 | Higher-order associations | Yes, but answer format is hard | — | Text pair lists or MCQ of pairs are error-prone |
| Many-to-many matching | 12.3 | Higher-order associations, harder search | Yes, but answer format is hard | Harder (more load) | Can't eliminate easy matches first |
| Ranking | 12.3 | Recall (e.g. fastest→slowest) or judgment (e.g. robust→brittle) | Yes (list) | — | Criterion choice sets the level |
| Summarization (as MCQ) | 12.3 | Higher-order: describe behaviour in words (like bug reports) | Yes | — | Distractor wording |
| Short free-form answer | 12.3 | Concepts in a constrained domain | Not reliably (false ±) | — | Use peer grading |
| Test-unlock questions [Basu2015] | 12.4 | Understanding of the spec before coding | Yes | — | — |
| Large or self-directed projects | 12.5 | Integration; what classes build toward | No | — | Doesn't scale |
| Free-form discussion / twitch coding | 12.5 | Reasoning in groups | No | — | Doesn't scale |
| Code review with rubric | 12.5 | Spotting faults and style issues | Yes, if comments are matched to lines | Tell novices how many of each fault | Without calibration, poor feedback |
| Pencil-and-paper puzzle as programming assignment [Butl2017] | 12.6 | Programming plus metacognition | Varies | — | — |

> **Skill note:** a quick selector derived from the table.
> - *Novices or blank-page fear:* fill in the blanks, Parsons.
> - *Misconception diagnosis at scale:* MCQ with diagnostic distractors.
> - *Debugging:* tracing, reverse execution, minimal fix.
> - *Adapting code:* theme and variations.
> - *Code quality:* refactoring (human-graded) or code review with rubric.
> - *Structures and relationships:* labelling, matching, ranking.
> - *Big classes:* prefer the constrained types (labelling over free-form diagrams; rubric-driven review over open review).

## Key terms
| Term | Meaning (one line) |
|---|---|
| Formative assessment | Assessment during learning, giving learner and teacher feedback on actual understanding (glossary). |
| Canterbury Question Bank | Shared bank of CS1/CS2 MCQs by language and topic [Sand2013]. |
| Plausible distractor | A wrong MCQ answer that looks right; best when it probes a specific misconception (glossary; §2.1). |
| Code & Run (C&R) | Learner writes code that produces a specified output. |
| Inverted C&R | Learner writes tests to decide whether given code meets a spec (finds seeded bugs). |
| Fill in the blanks | C&R with starter code; learner completes the missing parts. |
| Parsons Problem | Learner reorders given lines (and indents them) into a working solution. |
| Blank screen of terror | Novices' paralysis when asked to write code from scratch (§12.1; Ch. 4). |
| Tracing execution | Learner lists the order in which labelled lines execute. |
| Tracing values | Learner lists values variables take over time, e.g. in a variables × lines table. |
| Reverse execution | Learner deduces the input that produced a given output or error [Armo2008]. |
| Minimal fix | Learner makes or identifies the smallest change that fixes a bug. |
| Theme and variations | Learner makes a small specified change to working code to alter its output. |
| Refactoring | Learner changes code's structure without changing its output. |
| Labelling | Learner places given labels on a given diagram. |
| One-to-one / many-to-many matching | Pair items from equal-length lists / unequal lists with multiple or no matches. |
| Ranking | Learner orders items by a criterion. |
| Summarization | Learner chooses or writes the best description of code behaviour. |
| Auto-grader | Tool that runs and assesses learner programs automatically. |
| Fuzz testing | Testing with randomly generated inputs, here compared against a reference implementation (glossary). |
| Hashing | Condensed pseudo-random key of data; same input gives same hash; can't be reversed (glossary). |
| Test unlocking | Learner must answer a question about a test's expected result before using that test [Basu2015]. |
| Calibrated peer review | Reviewers match the teacher's grades on samples before reviewing peers (§5.3). |
| Twitch coding | A group decides moment by moment what to add to a program next (glossary; §8.4). |

## Concepts

### §12 Chapter objectives and framing
After the chapter a teacher should be able to:
- describe four types of formative-assessment exercises for programming classes;
- describe two kinds of feedback on programming exercises that automated tools can give.

Framing: "Every good carpenter has a set of screwdrivers". Every good teacher has several kinds of formative exercise:
- to check what learners are actually learning;
- to help them practise new skills;
- to keep them engaged.

The chapter covers checkable exercise types, then the state of the art in auto-grading, then discussion, projects, and other work needing human attention. It draws on the Canterbury Question Bank [Sand2013].

### §12.1 The Classics
- **Multiple choice questions (MCQs).** Most effective when wrong answers probe specific misconceptions (§2.1). In Bloom terms (§6.2) they usually test recall and understanding ("What is the capital of Saskatchewan?"), but they can also require judgment.
  - *Book example:* the order of operations in `price = addTaxes(cost - discount)`. Options: subtraction, function call, assignment / function call, subtraction, assignment / function call, then assignment and subtraction simultaneously / none of the above.
- **Code & Run (C&R).** The learner writes code that produces a specified output. It can be as simple or complex as wanted, but **for in-class use, keep it brief, with only one or two plausible correct answers**.
  - *Novices:* asking them to call a specific function is often enough. Experienced teachers forget how hard it is to work out which parameters go where.
  - *More advanced learners:* figuring out *which* function to call is more engaging and a better gauge of understanding.
  - *Book example:* `picture` holds a full-color image; using one function, create a black-and-white version and assign it to `monochrome`.
- **MCQ + C&R.** An MCQ that can only be answered by running code. *Book example:* "You are in /home/greg. Which of these files is not in that directory?" (autumn.csv, fall.csv, spring.csv, winter.csv). It can only be answered by running `ls`.
- **C&R grading problem.** C&R practises the skills learners most want, but is hard to assess. Learners find many unexpected routes to the right answer, and are **demoralized when an auto-grader rejects their code because it doesn't match the instructor's**. Mitigations:
  - *Assess only output.* This removes false rejections but gives no feedback on *how* they program.
  - *Give a small test suite to run before submitting*, then grade against a more comprehensive suite. Learners discover gross misunderstandings of the exercise's intent before anything costs them grades.
- **Inverting C&R.** Learners write tests to decide whether code meets a spec. It is a useful skill in its own right, and may give learners "a bit more sympathy" for how hard teachers work.
  - *Book example:* `monotonic_sum` sums each strictly increasing run, so `[1, 3, 3, 4, 5, 1]` gives `[4, 12, 1]`. Learners write unit tests to find which bug it has:
    - treats every negative number as the start of a new run;
    - omits the first value of each run;
    - omits the last value of each run;
    - restarts only when values decrease, rather than when they fail to increase.
- **Fill in the blanks.** A refinement of C&R: starter code is given and the learner completes it. In practice most C&R exercises are already fill-in-the-blanks, because teachers add comments reminding learners of the steps.
  - Novices find it **less intimidating** than writing from scratch (Ch. 4).
  - Because the teacher provides the structure, submissions are **more predictable and easier to check**.
  - *Book example:* fill `text[____:____]` so that `text = 'all that it is'` prints `'hat'`.
- **Parsons Problems.** These also avoid the "blank screen of terror" (Ch. 4). The learner gets the needed lines and must put them in order.
  - Effective because they let learners **concentrate on control flow separately from vocabulary** [Pars2006, Eric2015, Morr2016, Eric2017].
  - **Giving more lines than needed (distractors), or asking learners to rearrange some lines and add others, makes them significantly harder** [Harm2016].
  - Online tools exist [Ihan2011]. They can be emulated, "somewhat clumsily", by having learners rearrange lines in an editor.
  - *Book example:* rearrange and indent `total = 0`, `if v > 0`, `total += v`, `for v in values` to sum the positive values (learners must add colons too).

### §12.2 Tracing
- **Tracing execution order** is the inverse of a Parsons Problem: given code, the learner traces the order in which lines execute. It is an essential debugging skill, and it solidifies understanding of loops, conditionals, and evaluation order of function and method calls.
  - **Implement by having learners write a sequence of labelled steps.**
  - **Don't present it as an MCQ.** Choosing the correct sequence from a list adds cognitive load without value: learners do all the work of finding the sequence, then must search for it among options.
  - *Book example* (garbled in the EPUB; reconstructed): `vals = [-1, 0, 1]` (A); `inverse_sum = 0` / `try:` / `for v in vals:` (B); `inverse_sum += 1/v` with `except:` (C); `pass` (D). Learners give the execution order of the labelled lines.
- **Tracing values.** The learner lists the values one or more variables take as the program runs. It can be a list of values, or **a table with variable names as columns and line numbers as rows** for learners to fill in.
  - *Book example:* `left = 24; right = 6; while right: left, right = right, left % right`. What values do `left` and `right` take?
- **Reverse execution.** Trace backwards: what input must have produced this result? [Armo2008].
  - It requires search and deductive reasoning.
  - It is **particularly useful when the "output" is an error message**, because it builds debugging skills.
  - *Book example:* fill in the missing number in `values = [[1.0, -0.5], [3.0, 1.5], [2.5, ___]]` that made a `runningTotal += reading / scaling` loop crash.
- **Minimal fix.** Given buggy code, the learner makes or identifies the **smallest change** that produces correct output. *Making* the change is a C&R; *identifying* it can be an MCQ.
  - *Book example:* fix `inside(point, lower, higher)` with one small change. It returns false if `point <= lower`, false if `point <= higher`, else true.
- **Theme and variations.** Instead of fixing a bug, the learner makes a small alteration that **changes the output in a specified way**. Allowed changes include:
  - replacing one function call with another;
  - changing one variable's initial value;
  - swapping inner and outer loops;
  - reordering tests in a chain of conditionals;
  - changing the nesting of function calls or the order of chained methods.

  This is a real-world skill: "the fastest way to produce a working program is often to tweak one that already does something useful".
  - *Book example:* change the inner loop of a `fillTriangle(picture, color)` routine, which currently fills the whole image, so it fills only the upper-left triangle.
- **Refactoring.** The complement of theme and variations: change working code **without changing its output**, e.g. replace loops with vectorized expressions, or simplify a `while` condition.
  - The problem: there are often so many valid refactorings that **grading requires human intervention**. (The EPUB says "the exercise here is"; see caveats.)
  - *Book example:* write one list comprehension equivalent to a loop that appends `v` when `len(v) > threshold`.

### §12.3 Diagrams
- **Free-form diagrams** (concept maps etc., §3.1) give insight into thinking but need human time and judgment to assess.
- **Labelling diagrams** is "almost as useful" pedagogically and much easier to scale. Give a diagram and a set of labels; learners place the labels. The diagram can be:
  - a complex data structure ("which variables point to which parts?");
  - a program's output graph ("match each piece of code to the part of the graph it generated");
  - the code itself ("match each term to an example of that program element");
  - and more.

  The key: **constraining the set of solutions makes it usable in class and at scale.**
  - *Book example:* a tree showing how a small HTML fragment is held in memory. A root `<p>` has five children, in order: text, `<em>` (with one text child), text, `<em>` (with a text child and a nested `<em>` that has a text child), text. That is 10 nodes. Learners put labels 1–10 on the nodes to show depth-first traversal order.
- **Arranging diagram pieces.** Give learners the pieces and ask them to arrange them: a visual Parsons Problem. Provide as much or as little skeleton as they're ready for. Wilson's examples: placing resistors and capacitors to get the right voltage at a point; giving a fixed set of Scratch blocks to create a particular drawing.
- **Matching** is a special case of labelling where the "diagram" is a column of text.
  - **One-to-one:** two equal-length lists to pair (e.g. code ↔ output). *Book example:* match regex operators `?`, `*`, `+`, `$`, `^` with: start of line, zero or one occurrences, end of line, one or more occurrences, zero or more occurrences.
  - **Many-to-many:** unequal lists, so some items match several and some match none.
  - Both require higher-order thinking. Many-to-many is **harder** because learners can't do easy matches first to shrink the search space (higher cognitive load).
  - **Answer format:** submitting pairs as text ("A3, B1, C2") is clumsy and error-prone. Recognizing the correct set of pairs in an MCQ is **even worse**, because it is easy to misread.
- **Ranking** is a special case of matching, slightly more amenable to list answers because "our minds are pretty good at detecting errors or anomalies in sequences". Learners order items by a criterion:
  - *fastest to slowest* tends toward **recall**, e.g. knowing sorting algorithms' properties;
  - *most robust to most brittle* tends toward **reasoning and judgment**.
- **Summarization** requires higher-order thinking, and practises a skill useful for *reporting* bugs rather than fixing them. Example: "Which sentence best describes how the output of `f` changes as `x` varies from 0 to 10?", given as an MCQ.
- **Short free-form answers** in constrained domains, e.g. "What is the key feature of a stable sorting algorithm?". These still can't be fully auto-checked without frustrating false positives (wrong answers accepted) and false negatives (right answers rejected). They lend themselves well to **peer grading** (§5.3).

### §12.4 Automatic Grading
- Auto-graders are old: the first published mention is from 1960 [Holl1960], and surveys [Douc2005, Ihan2010] name many tools. Building one is harder than it looks:
  - how are assignments represented?
  - how are submissions tracked and reported?
  - can learners co-operate?
  - how are submissions executed safely?

  [Edwa2014a] is a whole paper on adaptively detecting infinite loops and other non-terminating submissions, just one of many issues.
- **Satisfaction ≠ outcomes.**
  - [Magu2018] replaced informal labs with a weekly machine-evaluated test (a competition auto-grader) in a second-year course. Learners disliked it, but **the failure rate halved and first-class honours tripled**.
  - [Rubi2014] also used a competition auto-grader but saw **no significant drop in dropout**. Negative comments were attributed to the tool's **feedback messages**, not to auto-grading itself.
- **Fuzz testing** [Srid2016]: random test cases compare learner code with a reference implementation. In the first project of a 1400-learner course, fuzzing caught errors missed by hand-written tests for **more than 48% of learners**.
- **Test unlocking** [Basu2015]. Learners had to answer a question about each test's expected behaviour before they could run it against their solution.
  - Example: "What does `largestPair(4, 3, -1, 5, 3, 3)` produce?" Answer: `(5, 3)`.
  - In a 1300-person course the vast majority chose to validate their understanding this way first, and then **asked fewer questions and expressed less confusion**.
- **Style checkers as graders.** [Nutb2016] initially found **no correlation** between human marks and style-checker violations, for two reasons:
  - one rule violated many times over-penalized learners;
  - near-unchanged starter code scored too well.
- **Reconsidering automated feedback** [Buff2015]. Auto-graders help learners find bugs but "may inadvertently discourage learners from thinking critically and testing thoroughly", encouraging dependence on the teacher's tests.
  - Key issue: a learner may test thoroughly yet still implement the feature differently from the spec. The failure is a **misunderstanding of requirements, not a lack of testing**, and more testing won't expose it. Without insightful, actionable feedback this only frustrates.
  - Their system maps failing tests to the learner's methods those tests execute, linking failures to features. It gives specific hints only when **earned**, i.e. when the learner has tested that feature enough, so learners can't substitute hints for testing.
- **Feedback message quality** [Keun2016a, Keun2016b]. They classified the messages from 69 auto-graders:
  - messages often don't say how to fix the problem or what to do next;
  - most teachers can't easily adapt the tools, which "tend to enforce their creators' unrecognized assumptions about how institutions work".

  Their classification is "a useful shopping list" for evaluating tools.
- **Sharing test feedback** [Srid2016], three strategies:
  1. **Give expected outputs.** Learners then hard-code outputs for those inputs ("anything that can be gamed, will be").
  2. **Report pass/fail only, revealing inputs and outputs after the deadline.** Frustrating: it tells learners they're wrong but not why.
  3. **Hashing.** Give a hash of the correct output. If the learner's output hashes the same, that unlocks the solution, but the hash can't be reversed to reveal the answer. It takes more setup and explanation, but "strikes a good balance" between revealing too early and withholding help.

### §12.5 Higher-Level Thinking
- Many valuable exercises are hard for teachers to assess beyond a few dozen learners, and hard for automated platforms to assess at all:
  - larger projects, and projects where learners set their own goals (which are "(hopefully) what classes are building toward");
  - free-form discussion and twitch coding (§8.4), which are valuable but don't scale.
- **Code review** is hard to auto-grade in general, but becomes tractable with a **rubric** (a list of faults to look for) and learners **matching comments to particular lines**.
  - *Novice version:* tell them how many of each fault exist, e.g. "two indentation errors and one bad variable name".
  - *Advanced version:* give half a dozen kinds of remark with no guidance on how many to find.
- Resources: [Steg2016b] for a code-style rubric; [Luxt2009] for peer review in programming classes. **If students do reviews, use calibrated peer review (§5.3)** so they have models of good feedback.
- *Book example:* mark each line of an 8-line `addem(f)` function using the rubric: (A) poor variable name, (B) unused variable, (C) use of undefined variable, (D) missing return value. The function reads lines into `x1`, filters non-blank lines into `x2`, sets `changes = 0`, loops printing `total` and accumulating `tot = tot + int(v)`, then prints `'total'`.

## Rules
- **EXR-1** — Keep a varied set of formative exercise types, and pick each one for what it assesses, not by habit. *Why:* different types check different skills and keep learners engaged (the "screwdrivers" analogy). *Check:* each exercise in a lesson names the skill or Bloom level it targets, and the set uses more than one type. (§12 intro)
- **EXR-2** — Make every MCQ distractor correspond to a specific misconception. *Why:* this is what gives MCQs diagnostic power (§2.1). *Check:* each wrong option has a written note of the misconception it detects. (§12.1)
- **EXR-3** — Keep in-class C&R exercises brief, with only one or two plausible correct answers. Name the function for novices; let advanced learners choose it. *Why:* open C&R is hard to assess; novices struggle with parameter placement. *Check:* count the plausible solutions; confirm that the function is named for novice audiences. (§12.1)
- **EXR-4** — For auto-graded C&R, give learners a small pre-submission test suite and grade against a fuller one, and never reject correct code just because it differs from the teacher's. *Why:* false rejections demoralize; early tests catch misread intent. *Check:* the grader is test- or output-based, not match-based; a public mini-suite exists. (§12.1)
- **EXR-5** — Use MCQ + C&R when you want learners to actually execute something and interpret the result. *Why:* it forces doing while staying auto-gradable. *Check:* the answer is unobtainable without running the command or code, and the environment state is controlled. (§12.1)
- **EXR-6** — Include test-writing exercises (inverted C&R) with seeded, distinct bugs. *Why:* testing is a skill in its own right. *Check:* the spec is precise, with a worked input→output example, and each listed bug is distinguishable by some test. (§12.1)
- **EXR-7** — For novices, prefer fill-in-the-blanks and Parsons Problems over blank-page coding. *Why:* less intimidating; Parsons separates control flow from vocabulary [Pars2006, Eric2015, Morr2016, Eric2017]; answers are predictable. *Check:* early exercises supply structure. (§12.1)
- **EXR-8** — Don't add distractor lines (or mix rearranging with writing new lines) in Parsons Problems unless you deliberately want them harder. *Why:* this significantly increases difficulty [Harm2016]; the bibliography adds that it increases solution time without improving learning. *Check:* the line count equals the solution's line count for novice exercises. (§12.1)
- **EXR-9** — Have learners write out tracing answers as labelled sequences or tables; never make tracing an MCQ of candidate sequences. *Why:* the MCQ form adds search load without value. *Check:* the answer format is free entry of labels or values. (§12.2)
- **EXR-10** — For value tracing, provide a variables × line-numbers table. *Why:* it structures the trace and standardizes notation. *Check:* columns are variables, rows are lines or steps. (§12.2)
- **EXR-11** — Use reverse-execution exercises, especially working back from an error message. *Why:* they build search, deduction, and debugging skill [Armo2008]. *Check:* the output or error is shown, and the space of valid inputs is small or all of it is accepted. (§12.2)
- **EXR-12** — In minimal-fix and theme-and-variation exercises, state what counts as "one small change" (and the allowed change kinds). *Why:* these practise real debugging and tweak-to-adapt skills, and need a constrained answer space. *Check:* the prompt says "one change" or lists the allowed changes; alternative valid fixes are anticipated. (§12.2)
- **EXR-13** — Budget human grading time for refactoring exercises, or narrow them to a single prescribed form (e.g. "a single list comprehension"). *Why:* too many valid refactorings to auto-grade. *Check:* the grading plan names a human or a constraint. (§12.2)
- **EXR-14** — Prefer labelling or arrangement over free-form diagrams when the class is large. *Why:* almost as useful pedagogically and far more scalable, because the solution set is constrained. *Check:* the diagram and label set are given; learners only place. (§12.3)
- **EXR-15** — Don't collect matching answers as typed pair lists or as MCQs of pair-sets; use a direct matching interface. Use one-to-one before many-to-many. *Why:* typed lists are error-prone; pair-set MCQs are easy to misread; many-to-many removes easy elimination (higher load). *Check:* the answer UI and matching cardinality fit the learner level. (§12.3)
- **EXR-16** — Choose ranking criteria deliberately: performance-type criteria test recall; robustness- or quality-type criteria test judgment. *Why:* the criterion sets the cognitive level. *Check:* the criterion matches the learning objective's Bloom level. (§12.3)
- **EXR-17** — Use summarization MCQs to exercise describing behaviour in words. *Why:* higher-order thinking; mirrors bug reporting. *Check:* the options differ in what behaviour they claim, not just in wording. (§12.3)
- **EXR-18** — Route short free-form answers to peer grading rather than auto-checking them. *Why:* auto-checks produce frustrating false positives and negatives. *Check:* the free-text items have a peer-grading rubric (§5.3). (§12.3)
- **EXR-19** — Judge auto-grading by learning outcomes, not learner satisfaction, and make its feedback messages actionable. *Why:* disliked graders can halve failure rates [Magu2018]; complaints often target feedback messages [Rubi2014]. *Check:* outcome data tracked; messages say what to do next. (§12.4)
- **EXR-20** — Add fuzz testing against a reference implementation to hand-written tests. *Why:* it caught missed errors for more than 48% of learners in a 1400-learner course [Srid2016]. *Check:* a reference implementation and random-input harness exist. (§12.4)
- **EXR-21** — Make learners demonstrate understanding of the spec (e.g. predict a test's result) before they can use the test. *Why:* most learners use it, and confusion and questions drop [Basu2015]. *Check:* each test has an unlock question. (§12.4)
- **EXR-22** — Don't grade by raw style-checker violation counts. *Why:* no correlation with human marks; repeated violations over-penalize and unchanged starter code over-scores [Nutb2016]. *Check:* style scoring is capped per rule and starter code is diffed out, or a human rubric is used. (§12.4)
- **EXR-23** — Design auto-feedback to separate "under-tested" from "misread the requirements", tie failures to features, and make hints earned by testing. *Why:* thorough testing can't expose a spec misunderstanding; free hints breed dependence [Buff2015]. *Check:* failures map to features; hints are gated on learner tests. (§12.4)
- **EXR-24** — Choose a test-feedback disclosure strategy consciously: don't reveal expected outputs (they get gamed); prefer hashed outputs over pass/fail-only. *Why:* "anything that can be gamed, will be"; pass/fail alone frustrates [Srid2016]. *Check:* the disclosure policy is written; hashing is used where feasible. (§12.4)
- **EXR-25** — Evaluate auto-grading tools for actionable feedback and adaptability, using [Keun2016a, Keun2016b]'s classification as a checklist. *Why:* most tools lack next-step feedback and embed their creators' institutional assumptions. *Check:* a tool comparison covers feedback types and customizability. (§12.4)
- **EXR-26** — Make code review gradeable with a rubric and line-matched comments; tell novices how many of each fault to find; calibrate reviewers first. *Why:* it turns an open task into a constrained one; calibration models good feedback (§5.3) [Steg2016b, Luxt2009]. *Check:* rubric present, fault counts given for novices, calibration step planned. (§12.5)
- **EXR-27** — Reserve human assessment for projects, self-set goals, and discussion, and plan for it. *Why:* these are what classes build toward but they don't scale. *Check:* the course has at least one such activity with grading capacity budgeted. (§12.5)
- **EXR-28** — When timing an exercise, budget for how often "simple" steps fail (e.g. finding the right directory) and how long recovery takes. *Why:* expert blind spot hides these costs (Ch. 3). *Check:* the time estimate includes a failure allowance. (§12.6 "Counting Failures")
- **EXR-29** — Pilot each new exercise on a peer before use, and fix ambiguities. *Why:* the §12.6 exercises show descriptions are often misunderstood and solutions vary widely. *Check:* someone else solved it, and the time and misunderstandings were recorded. (§12.6)

## Procedures

### P1. Choosing an exercise type (EXR-1, catalog)
1. State the learning objective and its Bloom level (§6.2).
2. Identify the learner level. For novices, prefer structure-supplying types: fill in the blanks, Parsons without distractors, C&R that names the function.
3. Identify the skill family:
   - *recall or misconceptions:* MCQ;
   - *writing code:* C&R or fill in the blanks;
   - *testing:* inverted C&R;
   - *control flow:* Parsons, execution tracing;
   - *state:* value tracing;
   - *debugging:* reverse execution, minimal fix;
   - *adapting:* theme and variations;
   - *code quality:* refactoring or code review;
   - *structure or relationships:* labelling, arrangement, matching, ranking;
   - *explaining behaviour:* summarization, short answer.
4. Check grading capacity. With large classes or auto-grading, choose constrained types; send free-form work to peer grading (calibrated) or reserve it for small groups.
5. Check the answer format against the pitfalls: no MCQ for tracing; no typed pair lists or pair-set MCQs for matching.
6. Pilot on a colleague and record the time taken and any misunderstandings.

### P2. Writing an exercise of each type
Each type below gives a "how to write" recipe; the matching templates are in T1.
- **MCQ.** Write the stem. Write the correct answer. For each distractor, name the misconception it detects. Consider "none of the above" only if it's diagnostic.
- **C&R.** Specify exact output and the variables to assign. Name the function for novices. Ensure only 1–2 plausible solutions. Write a public mini test suite and a hidden full suite.
- **MCQ + C&R.** Fix the environment state (files, directory). Write options that can only be discriminated by running the code.
- **Inverted C&R.** Write a precise spec with a worked input→output example. Implement a version with *one* seeded bug. List 3–4 candidate bugs, each distinguishable by a test.
- **Fill in the blanks.** Start from a working solution. Blank only the parts tied to the objective. Check every blank has a unique, or enumerable, fill.
- **Parsons.** Take a working solution, split it into lines, and shuffle. For novices, no extra lines. Decide whether indentation and punctuation are part of the task (the book's example makes learners add colons and indent).
- **Execution tracing.** Label lines A, B, C… Pick inputs that exercise interesting paths (exceptions, loop exits). The answer is a free-entry sequence of labels.
- **Value tracing.** Short code (10–15 lines in the §12.6 drill). Provide a variables × steps table.
- **Reverse execution.** Show output or an error. Leave one input unknown. Ensure the valid inputs form a small set, and accept all of them.
- **Minimal fix.** Inject one bug into working code. Ask for "one small change". As an MCQ, list candidate one-line changes.
- **Theme and variations.** Give working code plus a target output change. Name the allowed change kinds (swap a call, change an initial value, swap loops, reorder conditions, re-nest calls or method chains).
- **Refactoring.** Give working code and constrain the target form (e.g. "a single list comprehension"). Otherwise plan human grading.
- **Labelling.** Give a diagram and a label set. The diagram can be a data structure (which variable points where), an output graph (which code made which part), or code (which term names which element).
- **Arrangement.** Give the pieces and a skeleton sized to readiness.
- **Matching.** One-to-one for easier items, many-to-many for harder. Use a drag or select interface.
- **Ranking.** Choose the criterion by target level: performance for recall, robustness or quality for judgment.
- **Summarization.** Write behaviour-level options ("as x goes 0→10, output …").
- **Short free-form.** Keep the domain narrow; prepare a peer-grading rubric.
- **Code review.** Write code with known faults; give a rubric of fault kinds; for novices, state counts; calibrate reviewers on a sample first.

### P3. Setting up auto-grading (EXR-4, 19 to 25)
1. Decide representation, submission tracking, collaboration policy, and **safe execution**, including detecting non-terminating code [Edwa2014a].
2. Grade by tests or output, never by matching the instructor's code.
3. Publish a small pre-submission test suite; keep a fuller hidden suite; add fuzz tests against a reference implementation.
4. Gate test use behind spec-comprehension questions (test unlocking).
5. Map failing tests to features; distinguish under-testing from spec misunderstanding; give earned hints.
6. Choose a disclosure strategy: avoid revealing expected outputs; prefer hashed-output checks; otherwise give pass/fail now and reveal details after the deadline.
7. If style is graded, cap per-rule penalties and discount starter code, or use a human rubric.
8. Check message quality against [Keun2016a, Keun2016b] categories: does each message say what to do next?
9. Evaluate on learning outcomes (failure and honours rates), not satisfaction surveys.

### P4. Timing an exercise ("Counting Failures", EXR-28)
1. List every step, including "trivial" ones (opening the right file, navigating to the directory, saving in the right place).
2. For each, estimate how often it fails and the recovery time alone vs. with help.
3. Add that expected loss to the time budget; pre-empt common failures (e.g. put files where the editor saves by default).

## Diagnostics
| Symptom (in a lesson, class, or community) | Underlying problem | Fix (rule IDs) |
|---|---|---|
| MCQ results don't tell you *what* learners misunderstand | Distractors not tied to misconceptions | EXR-2 |
| Correct but unusual solutions rejected; learners demoralized | Grader matches the instructor's code | EXR-4 |
| Novices freeze at an empty editor | Blank-page task too early | EXR-7 |
| Parsons Problems take forever, learning no better | Distractor lines added | EXR-8 |
| Learners hunt through options on tracing questions | Tracing posed as an MCQ | EXR-9 |
| Every learner's trace is in a different format | No table structure | EXR-10 |
| Refactoring submissions impossible to grade at scale | Unconstrained target form | EXR-13 |
| Diagram assignments swamp TAs | Free-form diagrams at scale | EXR-14 |
| Learners mis-enter matching answers | Typed pair lists or pair-set MCQ | EXR-15 |
| Learners complain about the auto-grader, but outcomes improved | Satisfaction ≠ learning; maybe poor messages | EXR-19, EXR-25 |
| Hand-written tests miss many bugs | No fuzz testing | EXR-20 |
| Many "what is this assignment asking?" questions | Spec not understood before coding | EXR-21, EXR-23 |
| Learners hard-code expected outputs | Expected outputs revealed | EXR-24 |
| Style grades don't match human judgment | Raw violation counts; starter code rewarded | EXR-22 |
| Learners test thoroughly but still fail | Requirements misunderstanding, not under-testing | EXR-23 |
| Peer code reviews are shallow | No rubric or calibration | EXR-26 |
| Exercise overruns badly | "Simple" failures unbudgeted (expert blind spot) | EXR-28 |
| Learners misread the exercise prompt | Not piloted | EXR-29 |

## Templates and checklists

### T1. Exercise templates, one per type
The worked answers in brackets are the converter's own solutions to the book's examples (> **Skill note**); the book doesn't print answers.

```
MCQ
  Stem: <question about a concept or code>
  (a) <correct>
  (b) <distractor> -- misconception: <...>
  (c) <distractor> -- misconception: <...>
  (d) <distractor / "none of the above"> -- misconception: <...>
  Book: order of operations in price = addTaxes(cost - discount)  [answer: subtraction, function call, assignment]
```
```
Code & Run
  "The variable <name> contains <data>. Using <one function / named function>, produce <exact result>
   and assign it to a new variable called <target>."
  Novice: name the function. Advanced: let them find it.
  Grading: public mini-suite + hidden full suite; output- or test-based.
```
```
MCQ + Code & Run
  "You are in <controlled state>. Which of the following <is/is not> <property>?"  (only answerable by running <command>)
  Book: in /home/greg, which of autumn.csv / fall.csv / spring.csv / winter.csv is NOT present? (run ls)
```
```
Inverted Code & Run
  "The function <f> <precise spec>. For example, given <input>, the output is <output>.
   Write and run unit tests to determine which of the following bugs <f> contains:"
   - <bug 1>  - <bug 2>  - <bug 3>  - <bug 4>
  Book: monotonic_sum([1, 3, 3, 4, 5, 1]) == [4, 12, 1]; candidate bugs: negatives start a run;
        first value omitted; last value omitted; restarts only on decrease not on non-increase.
```
```
Fill in the Blanks
  "Fill in the blanks so that the code below <does X>."
  <starter code with ____ at the objective-relevant spots>
  Book: text = 'all that it is'; slice = text[____:____]; print(slice) -> 'hat'   [answer: 5, 8]
```
```
Parsons Problem
  "Rearrange (and indent) these lines to <goal>. (<any punctuation they must add>)"
  <shuffled lines; novices: exactly the needed lines, no distractors>
  Book: total = 0 / if v > 0 / total += v / for v in values  -> sum positives (add colons)
        [answer: total = 0; for v in values: ; if v > 0: ; total += v]
```
```
Tracing Execution Order
  "In what order are the labelled lines in this block of code executed?"
  A) ...  B) ...  C) ...  D) ...
  Answer format: free-entry label sequence (NOT an MCQ of sequences)
  Book: vals = [-1, 0, 1] with try/for/inverse_sum += 1/v/except: pass
        [answer: A B C (B) C D -- the B block contains the for line, so whether B repeats depends on the
         labelling convention; division by zero on the second element jumps to except/D. Label the
         loop header separately to avoid this ambiguity.]
```
```
Tracing Values
  "What values do <vars> take on as this program executes?"
  | step/line | var1 | var2 |
  |-----------|------|------|
  Book: left = 24; right = 6; while right: left, right = right, left % right
        [answer: (24, 6) -> (6, 0); loop ends]
```
```
Reverse Execution
  "Fill in the missing <value> in <input> that caused <this output / this error>."
  Book: values = [[1.0, -0.5], [3.0, 1.5], [2.5, ___]]; runningTotal += reading / scaling crashed
        [answer: 0 / 0.0 -- division by zero]
```
```
Minimal Fix
  "This <function> is supposed to <spec>. Make one small change so that it actually does so."
  (MCQ variant: "Which single change fixes it?")
  Book: inside(point, lower, higher)  [one fix: change the elif test to point >= higher]
```
```
Theme and Variations
  "Change <one specified part> of the <function> below so that it <new output>."
  Allowed changes: swap one call / change one initial value / swap inner-outer loops /
                   reorder conditionals / change call nesting or method-chain order
  Book: change fillTriangle's inner loop to fill only the upper-left triangle
```
```
Refactoring
  "Write <a single constrained form> that has the same effect as this <code>."
  Book: loop appending v when len(v) > threshold -> one list comprehension
        [answer: result = [v for v in values if len(v) > threshold]]
```
```
Labelling a Diagram
  "<Diagram> shows <structure>. Put the labels <set> on <elements> to show <relationship/order>."
  Book: HTML tree (<p> with text, <em>, text, <em>(text, <em>(text)), text; 10 nodes) -> label 1-10 in depth-first order
        [answer: p=1, text=2, em=3, its text=4, text=5, em=6, its text=7, nested em=8, its text=9, last text=10]
```
```
Arrange the Pieces (visual Parsons)
  "Using only <these pieces / these Scratch blocks>, build <target>." Provide skeleton: <none / partial / most>.
```
```
Matching (one-to-one or many-to-many)
  "Match each <item in column A> with <item in column B>."  [many-to-many: "Some items may match
   several others or none."]
  Book: regex ?, *, +, $, ^  <->  zero or one / zero or more / one or more / end of line / start of line
  Answer UI: direct pairing interface (not "A3, B1, C2" text, not an MCQ of pair-sets)
```
```
Ranking
  "Order these <items> from <most X> to <least X>."
  Recall: fastest -> slowest.  Judgment: most robust -> most brittle.
```
```
Summarization
  "Which sentence best describes how <output of f> changes as <x varies from a to b>?"  (MCQ)
```
```
Short Free-Form (peer graded)
  "<Narrow conceptual question>"  e.g., "What is the key feature of a stable sorting algorithm?"
  Rubric for peer graders: <key points; acceptable phrasings>
```
```
Test-Unlock Question (Basu2015)
  Before using test <t>: "What does <call with t's inputs> produce?"
  Book: largestPair(4, 3, -1, 5, 3, 3) -> (5, 3)
```
```
Code Review (rubric-based)
  "Using the rubric provided, mark each line of the code below."
  Rubric: A) poor variable name  B) unused variable  C) use of undefined variable  D) missing return value
  Novice: "There are <n> of A, <m> of B ..."; Advanced: no counts.
  Book: 8-line addem(f)  [likely marks: x1/x2/tot -> A; changes -> B; total/tot before assignment -> C; no return -> D]
  Before peer review: calibrate on a sample (§5.3).
```

### T2. Exercise review checklist
```
[ ] Objective and Bloom level stated; type fits it (catalog)
[ ] Novice level: structure supplied (blanks / Parsons without distractors / named function)
[ ] Only 1-2 plausible correct answers (C&R), or all valid answers accepted
[ ] MCQ distractors each tied to a named misconception
[ ] Tracing answers are free entry (no MCQ of sequences); values use a table
[ ] Matching uses a direct pairing UI; one-to-one before many-to-many
[ ] Ranking criterion matches recall vs. judgment goal
[ ] Free-form items routed to peer grading with rubric / calibration
[ ] No arbitrary content (foo/bar); relatable data (see MOT-8)
[ ] Piloted on a colleague; ambiguities fixed; time recorded
[ ] Time budget includes "simple" failure allowance
```

### T3. Auto-grader checklist (§12.4)
```
[ ] Safe execution; non-terminating code detected
[ ] Grades by tests/output, never by matching instructor code
[ ] Public pre-submission mini-suite + hidden comprehensive suite
[ ] Fuzz tests vs reference implementation
[ ] Test-unlock comprehension questions
[ ] Failures mapped to features; spec-misunderstanding distinguished from under-testing
[ ] Hints earned by learner's own testing
[ ] Disclosure: no expected outputs; hashed outputs preferred; else pass/fail + post-deadline reveal
[ ] Style scoring capped per rule; starter code discounted (or human rubric)
[ ] Messages say what to do next (Keuning classification as shopping list)
[ ] Tool adaptable to our institution's workflow
[ ] Evaluated on outcomes (failure/honours rates), not satisfaction
```

### T4. Test-feedback disclosure options ([Srid2016])
| Strategy | Pro | Con |
|---|---|---|
| Reveal expected outputs | Learners see exactly what's wanted | Gets gamed (hard-coding) |
| Pass/fail now, details after deadline | Not gameable | Tells them they're wrong but not why |
| Hash of expected output | Confirms an exact match and unlocks the solution, without revealing it | More setup and explanation |

## Examples
- **Auto-grader disliked but effective** [Magu2018]: weekly machine tests replaced labs; failure halved and first-class honours tripled, despite learner dislike. Lesson: measure outcomes.
- **Auto-grader with no effect** [Rubi2014]: no drop in dropout; complaints about feedback messages. Lesson: message quality matters.
- **Fuzzing at scale** [Srid2016]: in a 1400-learner course, fuzz tests caught errors missed by hand-written tests for more than 48% of learners.
- **Test unlocking** [Basu2015]: 1300-person course; most learners chose to answer the questions; less confusion afterwards.
- **Style checker mismatch** [Nutb2016]: repeated single-rule violations over-penalized; lightly edited starter code over-rewarded.
- **Circuit and Scratch-block arrangement** (§12.3): Wilson placing resistors and capacitors to hit a voltage; teachers giving fixed Scratch blocks to draw a target. Lesson: visual Parsons with adjustable skeleton.
- **Counting failures** (§12.6): GUI editors save to the desktop or home directory, so if course files live elsewhere, a "substantial fraction" of learners can't find them without help. Lesson: budget for trivial failures.

## Evidence and caveats
- **Parsons Problems:**
  - effective because they separate control flow from vocabulary [Pars2006, Eric2015, Morr2016, Eric2017];
  - learners attempt them more readily than nearby MCQs [Eric2015, bibliography];
  - labelled subgoals help [Morr2016];
  - 2D Parsons with distractors are faster than writing or fixing code with equivalent learning [Eric2017, bibliography];
  - **distractors** significantly harden them [Harm2016]; the bibliography adds that they don't improve learning but increase solution time.

  There is an apparent tension: [Eric2017] used distractors and found equivalent learning to writing code, while [Harm2016] found distractors lower efficiency for young novices. Both hold if distractors are seen as a cost, not a benefit.
- **2D Parsons tool** [Ihan2011]: the bibliography notes experts solve "outside-in" rather than line by line.
- **Auto-grading outcomes:** [Magu2018] positive; [Rubi2014] null. The contrast is Wilson's point that satisfaction and outcomes differ.
- **Fuzzing** [Srid2016]: strong single-course result ("clearly demonstrates its value").
- **Test unlocking** [Basu2015]: large course, self-selected use.
- **Style checkers** [Nutb2016]: the text reports the *initial* finding of no correlation. The bibliography annotation says the paper then modified rules and weighted grades to improve the correlation, so style checkers can be tuned.
- **[Buff2015]** is described as a "well-informed reflection" plus a system design.
- **[Keun2016a, Keun2016b]:** "work is ongoing".
- **Short free-form answers:** auto-checking still yields "a frustrating number" of false positives and negatives.
- **Text anomalies:**
  - "The exercise here is that there are often so many ways to refactor" means "the problem here is" (the same global "challenge/problem→exercise" substitution seen in Ch. 10).
  - The Tracing Execution Order example and the Code Review listing are malformed in the EPUB (nested list markup). Labels and line numbers above are reconstructed from the source markup.
  - In the Minimal Fix example, the code uses `false`/`true`, which are not Python booleans; treat it as pseudocode.
- **§12.6 "Inverting Code and Run"** describes the inversion as "figure out what input produces a particular output". That matches *reverse execution* (§12.2), not the §12.1 definition (write tests against a spec). Both are inversions; a skill should label them distinctly.

## Practice exercises
- **Code and Run** (pairs, 10 min). Write a short C&R exercise, swap, time each other, and note ambiguities or misunderstandings.
- **Inverting Code and Run** (small groups of 4–6, 15 min). Each person writes an exercise asking what input produces a given output; pick two at random; count how many different inputs the group can find.
- **Tracing Values** (pairs, 10 min). Write a 10–15-line program, swap, trace how variables change, and compare trace notations.
- **Refactoring** (small groups of 3–4, 15 min). Each brings 10–30 lines of untidy code; pick one; everyone tidies it independently; compare versions and discuss how auto- or large-class grading could cope with the variation.
- **Labelling a Diagram** (pairs, 10 min). Draw a diagram of something you explained recently (e.g. browser–server fetch, objects vs. classes, R data-frame indexing), put the labels on the side, and have your partner place them.
- **Pencil-and-Paper Puzzles** (whole class, 15 min). [Butl2017] turned pencil-and-paper puzzles into intro assignments that students enjoyed and that encouraged metacognition; describe how to turn a childhood puzzle or game into a programming exercise.
- **Counting Failures** (pairs, 15 min). List "simple" things that go wrong in exercises; estimate frequency, fix time alone or with help, and how much class time you currently budget for them.

## Cross-references
- `02-mental-models.md`: MCQ distractors as misconception probes (§2.1); formative assessment.
- `03-expertise-and-memory.md`: concept maps (§3.1); expert blind spot.
- `04-cognitive-load.md`: faded examples, fill in the blanks, Parsons Problems, the blank-screen problem.
- `05-individual-learning.md`: peer assessment, calibrated peer review, contributed problem sets (§5.3).
- `06-lesson-design.md`: Bloom's taxonomy (§6.2); writing assessments before content.
- `08-teaching-as-performance.md`: live coding and twitch coding (§8.4).
- `10-motivation-and-inclusion.md`: authentic tasks vs. drill exercises; no arbitrary content (MOT-8).
- `11-teaching-online.md`: automated assessment limits at scale; peer grading online; feedback tags.

## Source map
| Book section | Covered under |
|---|---|
| §12 objectives, intro, [Sand2013] | Concepts §12; EXR-1 |
| §12.1 MCQ | Catalog; EXR-2; T1 |
| §12.1 Code & Run, grading problem | EXR-3, EXR-4; T1 |
| §12.1 MCQ + C&R | EXR-5; T1 |
| §12.1 Inverting C&R | EXR-6; T1; Evidence (naming discrepancy) |
| §12.1 Fill in the blanks | EXR-7; T1 |
| §12.1 Parsons Problems | EXR-7, EXR-8; T1; Evidence |
| §12.2 Tracing execution, tracing values | EXR-9, EXR-10; T1 |
| §12.2 Reverse execution | EXR-11; T1 |
| §12.2 Minimal fix, theme and variations | EXR-12; T1 |
| §12.2 Refactoring | EXR-13; T1 |
| §12.3 Free-form vs labelling, arrangement | EXR-14; T1 |
| §12.3 Matching, ranking, summarization, short answer | EXR-15 to EXR-18; T1 |
| §12.4 Automatic Grading | EXR-19 to EXR-25; P3; T3; T4 |
| §12.5 Higher-Level Thinking, code review | EXR-26, EXR-27; T1 |
| §12.6 Exercises | Practice exercises; EXR-28, EXR-29; P4 |
