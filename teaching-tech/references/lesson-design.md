# Lesson design

## Contents
1. Backward design
2. Learner personas
3. Learning objectives (Bloom and Fink)
4. Sequencing and sizing
5. Design techniques
6. Maintainability and sharing

---

## 1. Backward design
The usual process — write slides about what you know, invent assignments as you go, cram an exam at the end — produces lessons that drift from their goals. **Backward design** works like test-driven development: decide what "done" looks like first.

1. **Brainstorm** what to cover, how, the misconceptions you expect, and what's deliberately excluded. A concept map helps.
2. **Personas:** decide who it's for (can come before step 1).
3. **Write the assessments** — summative first (the final exercise), then formative ones that lead up to it.
4. **Order the formative assessments** by dependency and complexity. That order is the outline.
5. **Write just enough material** to get learners from one assessment to the next. An hour of teaching is typically 3–4 such episodes.

Why: every piece of content serves an objective, and no exam asks something the course didn't prepare learners for. This is **not teaching to the test** — that's when an outside authority imposes uniform tests tied to rewards; here the teacher uses assessments to guide design.

Design is iterative (writing an MCQ may change scope), but **document it in the canonical order** so future maintainers understand the reasoning ("faking a rational design process").

## 2. Learner personas
Borrowed from UX. Write 2–3. Five parts each:
1. General background.
2. What they already know.
3. What *they* think they want (not what an expert thinks they need).
4. How the course will help them.
5. Special needs (language, accessibility, time, equipment).

Rules:
- **You are not your learners.** Ask them; listen.
- Keep a shared set of personas across courses; names become shorthand ("would Jorge follow this?").
- Start from audience or from topic — either order works.
- Letting learners pick domain-specific versions of assignments (music, biology, finance) improves outcomes and satisfaction, if projects are open-ended and grading is shared.

## 3. Learning objectives
A **learning objective** is what the lesson aims for; a **learning outcome** is what learners actually get. Summative assessment compares them.

An objective is **one sentence describing how the learner will demonstrate learning**, with a **measurable verb** and **criteria for acceptable performance**.

Improving an objective:
- ✗ "Will be given opportunities to learn good practices." (describes the lesson, not the learner)
- ✗ "Will have a better appreciation for good practices." (no active verb, vague)
- ✗ "Will understand how to program in R." (not assessable)
- ✓ "Will write one-page data analysis scripts in R to read, filter, summarize, and print results for tabular data."

"Understand Git" could mean describing when version control beats file sync, committing with a GUI, or recovering from a detached HEAD — three different lessons. Be specific.

**Bloom's taxonomy (revised)** — hierarchical:
| Level | Learners can… | Verbs |
|---|---|---|
| Remembering | recall facts and terms | recognize, list, describe, name, find |
| Understanding | explain and interpret | interpret, summarize, paraphrase, classify, explain |
| Applying | use knowledge on new problems | build, identify, use, plan, select |
| Analyzing | break down, find causes and evidence | compare, contrast, simplify |
| Evaluating | judge against criteria | check, choose, critique, prove, rate |
| Creating | combine into something new | design, construct, improve, adapt, solve |

Intro programming mostly lives in the first four levels; the top two need the basics first. Experts disagree about classifying individual questions, so use it as a guide, not a law.

**Fink's taxonomy** — complementary categories, not a hierarchy; learning defined by the change in the learner:
| Category | Verbs |
|---|---|
| Foundational knowledge | remember, understand, identify |
| Application | use, solve, calculate, create |
| Integration | connect, relate, compare |
| Human dimension | come to see themselves as, understand others in terms of |
| Caring | get excited about, be ready to, value |
| Learning how to learn | identify sources for, frame useful questions about |
Fink lets you write objectives about attitudes and self-direction (e.g. "want to learn more about JavaScript") alongside skills.

## 4. Sequencing and sizing
- Outline at the level of **one major bullet per hour, 3–4 episodes per hour**, each episode ending in a formative assessment.
- Respect concept dependencies (operators before precedence; variables before operators).
- Put **quick-to-learn, immediately useful** things first for early wins; defer "useful but hard" fundamentals.
- Choose between **one extended example** (shows integration) and **independent exercises** (easy to catch up and rearrange), or mix.
- **Never start novices from a blank page:** extend the live-coded example or give starter code — but keep starter code free of confusing boilerplate.
- Plan for **mixed abilities:** extra self-paced exercises, pairing, and clear advertising of the level beforehand.
- **Limit innovation:** each new classroom technique adds load. Introduce one at a time with repeat groups; be conservative for one-off workshops.

## 5. Design techniques
- **Subtracting complexity:** write the finished program; remove the hardest part you want learners to write — that's the last exercise; remove the next hardest — that's the second to last; what remains (imports, data loading) is starter code.
- **PRIMM:** Predict output → Run → Investigate (trace, debugger) → Modify → Make something similar.
- **Concrete → Representational → Abstract** (especially for younger learners): manipulate objects, then draw the process, then write code.
- **Inessential weirdness:** list the in-group habits that alienate newcomers (cryptic names, sneering at tools) and remove what you can.
- **Evaluate a lesson on eight dimensions:** closed vs open; cultural relevance; recognition (can learners show others what they made?); space to play; driver shift (how often learners control the action); risk and reward; grouping; session shape (seating and space).
- **Authentic tasks and tangible artifacts** (see learning-science.md §7).
- **Choral explanations:** several explanations of the same thing, each suited to a different learner; prepare alternatives for the hardest points.

## 6. Maintainability and sharing
A lesson is maintainable when updating it is cheaper than replacing it. It depends on:
1. **Documented design** (backward design notes say why things are where they are).
2. **Collaboration tooling:** emailed slide files < shared docs/wikis < version control (best for merging, but hard for non-programmers and office formats).
3. **Willingness to collaborate** — the biggest factor. Teachers rarely share whole lessons but often **remix** pieces, so design in small, reusable parts.
Teachers want shared resources organized by role and level, shown in context, with low-risk ways to ask questions.
