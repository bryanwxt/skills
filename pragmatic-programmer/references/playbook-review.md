# REVIEW mode: code and design audit

**Goal:** find the highest-leverage broken windows, and hand back ranked findings, options, and patches.

## Inputs
- **Required:** the artifact (code, a diff, a design doc, config, or docs).
- **Helpful:** its purpose, the change intent (for PRs), criticality (prototype, internal, public API, life- or money-critical), and the test suite.
- If the purpose is unknown, infer it from the code, and state the inference as `ASSUMPTION:`.

## Pass order
Run these passes in order and stop early on large inputs once 7 strong findings exist. Each pass lists what to look for and the source tip.

1. **Correctness & paranoia** (Tips 30–35, 44)
   - Swallowed or ignored errors
   - Unchecked close, write, or commit calls
   - `switch`/`match` without a failing default
   - Asserts with side effects, or asserts doing input validation
   - Exceptions used for control flow (run the handler-removal test)
   - Resources acquired and released in different places, or through shared or global state
   - Inconsistent lock order
   - Reliance on undocumented behavior, the current working directory, locale, or an interactive stdin (accidents of context)
2. **Semantic invariants** (Tip 31, §21)
   - Money, time, identity, and idempotency: can anything be applied twice, lost, or reordered?
   - Is the "err in favor of the consumer" direction chosen explicitly?
3. **DRY** (Tip 11, checklist B1)
   - Classify each duplication as one of the four kinds.
   - Name *the knowledge* that is duplicated, and both locations.
   - Look for: stored derived fields, repeated literals, schemas mirrored by hand, comments restating code, docs or tests maintained in parallel.
4. **Orthogonality & coupling** (Tips 13, 36, checklists A3, A7, B2)
   - Law of Demeter train wrecks
   - Globals and singletons
   - Hidden static state between calls (temporal coupling, e.g. a `strtok`-style API)
   - A constructor plus a separate `init()` leaving half-built objects
   - A single handler for all events
   - Similar functions that differ only in the middle
   - Unit-test footprint: how much must be built to test this?
5. **Reversibility & metadata** (Tips 14, 37, 38)
   - Vendor SDK calls scattered everywhere instead of behind an interface
   - Business policy hard-coded (thresholds, roles, periods)
   - Deployment topology baked into code
   - Only flag what *plausibly varies*. Don't abstract stable things.
6. **Views & models** (Tip 42)
   - Business logic tangled with UI or transport, which also blocks headless testing (Tip 48).
7. **Performance sanity** (Tips 45, 46)
   - Loops over *unbounded external* n
   - Nested loops over the same collection
   - Hand-rolled sorts
   - Recommend measuring before optimizing.
8. **Testability & tests** (Tips 48, 62–66)
   - Missing tests for the changed behavior
   - Tests that assert nothing meaningful
   - Untested boundary states
9. **Readability & docs** (Tips 17, 67, 68, B14)
   - Misleading names (worst), meaningless names, comments that explain how instead of why
   - Hand-maintained metadata in headers
   - Domain vocabulary not reflected in names
10. **Generated & wizard code** (Tips 29, 50)
    - Generated files edited by hand
    - Generators not run in the build
    - Scaffolding or AI-generated code nobody can explain
11. **Automation** (Tips 23, 61)
    - Manual steps in README or deploy docs that should be scripts
    - Anything not under version control

## Design-doc variant
If the input is a design or architecture without code, run:
- Architectural Questions (A5)
- The reversibility probes (B3)
- The orthogonality team test (B2)
- The concurrency/workflow check (Tips 39–41): find actions that could run in parallel, and objects that are invalid at some call times.
- Requirements hygiene (B11) for any embedded requirements.

## Severity guidance
- 🔴 Critical: data corruption or loss, a double-apply, a leak on a hot path, a silent failure, deadlock-prone lock order.
- 🟠 Major: a knowledge duplication across modules, coupling that makes a likely change ripple, a missing contract at a public boundary, coincidental correctness.
- 🟡 Minor: a local Demeter chain, a missing assert, an unclear name, a manual step.

## Output
Use the default template (SKILL.md §5.1). For PRs, add one line: **"Leaves the codebase: better / same / worse"**, a nod to broken windows.

## Patch rules
- Top 1–3 findings only. Keep them minimal and idiomatic.
- Refactor-only patches must preserve behavior. Say so, and name the test that proves it.
- Behavior-changing patches include a failing-first test.
- Where a full fix is too big, give the **board-up**: a TODO with a ticket, a failing-loud guard, or a deprecation shim.
