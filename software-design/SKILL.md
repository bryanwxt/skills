---
name: software-design
description: Evaluates the design of an existing codebase, or designs a new application from scratch, using the complexity-reduction principles from John Ousterhout's "A Philosophy of Software Design" (deep modules, information hiding, pulling complexity down, defining errors out of existence, design it twice). Use whenever the user asks to review, audit, critique, or refactor an app's architecture or module design, asks "is this well designed?", wants to reduce complexity or tech debt, or wants to plan, architect, or design a new app, service, library, or API — even if they don't mention the book.
---

# Software Design

This skill applies one idea relentlessly: **the goal of design is to reduce complexity**, and complexity is anything about a system's structure that makes it hard to understand or change. Everything else here is a tool for spotting complexity or for keeping it out.

It has two modes:

- **Evaluate** an existing application and produce a prioritized design review.
- **Design** a new application (or a major new subsystem) and produce a design doc.

Pick the mode from the request. If the user has code and wants a verdict or improvements, use Evaluate. If they have an idea, requirements, or a blank repo, use Design. A redesign of an existing subsystem uses Evaluate first, then Design for the replacement.

Reference files (read them when the step calls for them):

- `references/principles.md` — the core principles, condensed. Read before either mode.
- `references/red-flags.md` — the red-flag catalogue with how to detect each one in real code and how to fix it. Read in Evaluate mode.
- `references/design-process.md` — design-it-twice, interface-first, comments-first, and how to size modules. Read in Design mode.
- `assets/review-template.md` and `assets/design-doc-template.md` — the output formats.

## The lens

Complexity shows up as three symptoms. Keep them in mind for every finding:

1. **Change amplification** — a simple change needs edits in many places.
2. **Cognitive load** — a developer must hold a lot in their head to make a change safely.
3. **Unknown unknowns** — it isn't clear what must change or what knowledge is needed. This is the worst of the three.

Complexity has two causes: **dependencies** (code that can't be understood or changed in isolation) and **obscurity** (important information that isn't obvious). Every finding should name which symptom it produces and which cause it comes from. A finding that produces none of the three symptoms isn't a design problem — drop it or mark it as style.

Weigh complexity by where developers spend time. A messy module nobody touches matters less than a mildly confusing one that every feature passes through.

## Mode 1: Evaluate an existing application

### Step 1 — Map the system

Before judging anything, build a picture:

- Read the README, entry points, build config, and top-level directory layout.
- Identify the major modules (packages, services, classes, layers) and write one line per module saying what it hides from the rest of the system. If you can't say what a module hides, that is already a finding.
- Sketch the dependency direction between modules. Note cycles.
- Ask the user (or infer from git history if available: `git log --stat`, most-changed files) which areas change most often and which ones people are afraid to touch. Hot spots get reviewed first and weighted highest.

For large codebases, don't read everything. Sample: the most-changed files, the most-imported modules, the public APIs, and one representative end-to-end feature path.

### Step 2 — Walk a change

Pick one or two realistic changes the team is likely to make (ask, or infer from recent commits/issues). Trace what files and concepts each change would touch. This is the most reliable way to find change amplification and unknown unknowns, and it grounds the review in the team's actual work rather than abstract taste.

### Step 3 — Scan for red flags

Read `references/red-flags.md`. For each module in scope, check the red flags. Record each hit with:

- location (file/class/function),
- the red flag name,
- a two-to-three line explanation with evidence from the code,
- the symptom and cause it produces,
- the suggested fix, stated concretely (what moves where, what the new interface looks like),
- effort (S/M/L) and impact (low/med/high).

Be specific. "Module X is shallow" is not a finding. "`UserRepository` exposes 14 methods that each wrap one SQL query; callers must know the table schema to use them — collapse into 4 intent-level methods and hide the schema" is.

### Step 4 — Check module depth and layering

For each major module, estimate interface size (methods, parameters, exceptions, config, ordering rules callers must know) against the functionality it provides. Classify it as deep, reasonable, or shallow. For each layer boundary, check that the layers provide *different* abstractions — adjacent layers with the same vocabulary and signatures are a smell.

### Step 5 — Prioritize and report

Write the review with `assets/review-template.md`. Order by impact on the hot spots, not by the order you found things. Lead with the 3–5 changes that would remove the most complexity. Separate strategic fixes (restructuring) from tactical ones (naming, comments). Credit what is well designed — a review that only lists faults hides which patterns the team should copy.

Principles for the report:

- Every recommendation must make the system simpler for the *users of a module*, even if the module's own implementation gets harder. Don't recommend splitting things just to make them smaller.
- Prefer a few deep fixes over many cosmetic ones.
- Propose incremental steps. The book's stance is continual small investment, not big-bang rewrites. If a rewrite really is warranted, say why the incremental path fails.
- If you propose a new interface, write out its signatures.

## Mode 2: Design a new application

### Step 1 — Understand the problem

Establish, asking only what isn't clear from the request: what the system must do, who uses it (humans, other services, developers calling a library), scale and performance constraints, the likely directions of future change, and the team's size and experience. Future change directions matter most: good module boundaries are drawn around the decisions most likely to change.

### Step 2 — Identify the knowledge to hide

List the design decisions and bodies of knowledge in the system — data formats, storage choices, protocols, external APIs, algorithms, business rules, policies. Each significant one is a candidate to be hidden inside exactly one module. This list, not the order of operations or the UI screens, is what drives the decomposition. (Structuring modules by execution order — "read, then parse, then process, then write" — is the most common way to leak knowledge across modules.)

### Step 3 — Design it twice

Read `references/design-process.md`. For the top-level decomposition and for each important module interface, sketch at least two substantially different designs — not variations on one idea. Compare them on: interface simplicity for the common case, generality, information hiding, and performance. Pick one (or a hybrid) and record why the others lost. Show the user the alternatives briefly; they often know the constraint that decides it.

### Step 4 — Define the modules

For each module:

- one sentence stating the abstraction it provides,
- what it hides,
- its interface (signatures, with a one-line comment each), designed to make the common case trivial,
- which errors it defines out of existence, masks, or aggregates, and which it must expose,
- which defaults it picks so callers don't have to.

Write the interface comments **before** any implementation (the comments-first practice). If a module is hard to name or hard to describe briefly, the decomposition is probably wrong — revisit it before moving on.

### Step 5 — Check the design against the red flags

Run the red-flag list from `references/red-flags.md` against the proposed design, especially: shallow modules, information leakage, temporal decomposition, pass-through layers, overexposure, and special-general mixture. Fix what you find.

### Step 6 — Write the design doc

Use `assets/design-doc-template.md`. Include the rejected alternatives. Then, if the user wants code, scaffold the modules with their interface comments first and implementations second.

## Tone and judgment

- Name the principle behind each recommendation so the user learns it and can disagree.
- Every principle can be taken too far: too-general interfaces, over-hidden information that callers actually need, "defining away" errors that callers must know about, or consistency enforced where it doesn't pay. When you apply a principle, ask whether you've crossed that line.
- Distinguish design problems from style preferences. Don't pad the review with lint.
- Be honest about uncertainty. If the code sample was partial, say which conclusions depend on parts you didn't read.

## Credit

The principles and red flags are condensed and paraphrased from John Ousterhout, *A Philosophy of Software Design* (2nd ed.). The book is worth reading in full.
