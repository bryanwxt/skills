# Teaching programming: what novices do and what helps

Pedagogical content knowledge for computing — "actionable approximations" of what research says. Most studies are of school and university students; treat findings as useful defaults.

## Contents
1. How novices program
2. Debugging and testing
3. Misconceptions
4. Common mistakes
5. Languages and tools
6. Feedback, error messages, visualization
7. Interventions that raise pass rates
8. Practical recommendations

---

## 1. How novices program
- Experts know *what* to write and *how* to build it (plans and patterns). Teaching usually covers only the what; many novice bugs come from having no strategy.
- **Show how to program, not just the result:** live coding with small steps and frequent feedback; stick to one plan rather than random changes; show the order experts write code (signature → control flow → details and edge cases), whereas novices write top to bottom.
- **Roles of variables** give novices a vocabulary for plans: fixed value, stepper, walker, most-recent holder, most-wanted holder (best so far), gatherer (accumulator), follower (previous value), one-way flag, temporary, organizer, container.
- Naming a few patterns (e.g. accumulator) helps; big pattern catalogues are too abstract for novices.

## 2. Debugging and testing
- Debugging is rarely taught explicitly. Teach it: stepping through with a debugger, tracing by hand, writing tests, re-reading the spec.
- Many novices can't predict the output of short code; gaps between tracing and writing skill predict poor results.
- Novice debugging habits to model and correct: the same print in both branches of an `if`; commenting out correct lines.
- Time spent debugging varies 2–3× between learners; teaching slower learners the faster ones' habits evens things out.
- **Reading code** is the most effective way to find bugs; teach a code-quality rubric in chunks.
- **Tracing variable values** while debugging is the most effective sketching strategy.
- **Testing:** strong students test a lot; novice tests have low coverage, test many things at once, and aim to confirm rather than break. Specify problems as tests to pass; model your own testing.

## 3. Misconceptions
- **The "superbug":** thinking the computer understands intent. Teach explicitly that naming a variable `cost` doesn't make it a cost.
- Common misconceptions:
  - variables behave like spreadsheet cells (after `grade=65; total=grade+10; grade=80`, novices expect `total` to be 90);
  - a variable remembers its past values;
  - two objects with the same name or ID are the same object;
  - functions run when defined, or in the order defined;
  - a `while` condition is checked continuously and exits the moment it's false; an `if` "watches" continuously;
  - assignment moves values, leaving the source empty;
  - assignment copies objects (rather than references);
  - forgetting to store a return value; calling a method without an instance;
  - returning `False` as soon as one condition fails in a check that should examine all items.
- In Python, `self` confuses novices (omitted in definitions or attribute access).
- People with prior CS centre their mental maps on classes and data structures; those without, on the processor and data.

## 4. Common mistakes
- Mismatched quotes and brackets are most common but quickly fixed.
- Some errors are made once (wrong bracket type for a condition); some recur (wrong argument types).
- Errors that produce compiler messages are fixed faster than silent ones.
- Unfinished code isn't an error (empty `if`, unused method).
- **Teachers can't predict which mistakes are common** — their rankings barely agree with data or with each other. (`=` vs `==` is rarer than teachers think.) Look at real learner data.
- HTML: basic tag syntax errors persist for weeks; "the rules are simple" is blind spot.

## 5. Languages and tools
- **Blocks first for children and teens** (Scratch, Blockly-style): no syntax errors, faster learning, fewer loop misconceptions. Adults may prefer grown-up-looking blocks or go straight to text. Dual block/text tools let learners browse what's possible.
- **Syntax matters:** C-style syntax is about as hard for novices as randomly designed syntax; Python and Ruby are easier; usability-tested languages easier still. `for`, `while`, `foreach` are among the least intuitive keywords to non-programmers.
- **Start procedural;** defer class definitions and higher-order functions until control flow and data types are solid — unless the goal requires them early (e.g. callbacks in JavaScript).
- **Types:** declared types add complexity but serve as documentation and catch some bugs; no firm recommendation for novices.
- **Naming:** full-word names help comprehension somewhat; conventional single letters (i, n, x) are fine in small scopes. Use a style checker so all examples are consistent.
- Notebooks and hybrid environments blur lines between tools; choose what minimizes setup and extraneous load.

## 6. Feedback, error messages, visualization
- Better error messages reduce errors and repeats (e.g. suggesting the likely fix).
- Learners do read error messages (13–25% of their time); reading them is as hard as reading code. **Give practice interpreting error messages.**
- **Visualizers** (e.g. Python Tutor) help; **building** a visualization teaches more than watching one.
- Flowcharts beat pseudocode when both are equally well structured.
- A **notional machine** — a simplified, accurate model of how programs execute (call stack, heap, references, frames, lookup) — is a concrete target for teaching. For Python: data lives on the heap with a type and a value; atomic values are immutable; collections hold references; calls push frames holding names and references; lookup checks the current frame then globals.

## 7. Interventions that raise pass rates
Reported improvements (with publication-bias caveats): collaboration and group work; content changes; contextualization (games, media computation); a preliminary CS0 course; grading schemes weighting programming work; peer support (pairing, mentors, tutors); more instructor availability. Cooperative learning also leaves fewer exam questions blank (more self-efficacy). **Unplugged / creativity exercises** (e.g. describe a nail clipper by inputs, outputs, functions) improve grades.

## 8. Practical recommendations
1. Show *how* to program (live coding, plans, expert order).
2. Teach debugging and testing explicitly.
3. Teach that computers don't understand intent.
4. Measure outcomes in a way you can compare over time.
5. Start younger learners with blocks.
6. Start procedural, then objects/functions as goals demand.
7. Use a style checker for consistent examples.
8. Give practice reading error messages; teach tracing variable values.
9. Base teaching on observed learner errors, not intuition.
10. Classic benchmarks: the Rainfall problem (average positive integers until a sentinel) reveals planning difficulties.

Typical outcomes for calibration: about two-thirds pass CS1; prior experience gives an early advantage that fades by the second course; teaching evaluations don't correlate with learning.
