# BUILD mode: write defensive code and refactor

Two sub-modes. Pick **WRITE** for new code, or **REFACTOR** to change the structure of existing code.

## WRITE: new code, pragmatically paranoid

### Inputs
- **Required:** what the code must do.
- **Helpful:** the language, framework, callers, error-handling conventions, and criticality.

### Procedure
1. **Contract first** (Tip 31).
   - Write the preconditions, postconditions, and invariants as a docstring or comment, and as checks where the language allows.
   - Be **lazy**: strict about what you accept, minimal about what you promise.
   - State what is *not* promised.
2. **Design to test** (Tip 48): sketch 3–5 tests from the contract before or alongside the implementation, covering the boundaries and the invalid inputs.
3. **Shy structure** (Tips 13, 36):
   - Single responsibility.
   - Pass dependencies in, rather than reaching through globals or singletons.
   - Obey the Law of Demeter.
   - No hidden state between calls. An object is valid whenever it can be called (Tip 41).
4. **Details in metadata** (Tip 38): values that plausibly vary (thresholds, periods, endpoints, feature choices) go in config. Stable facts stay in code.
5. **Paranoia:**
   - Validate *external* input with real error handling.
   - Assert internal "impossible" states. Assertions are side-effect-free and stay on (Tip 33).
   - Every `switch` gets a failing default.
   - Crash early rather than continue with corrupt state (Tip 32).
   - Use exceptions only for the exceptional, and error values or Result types for expected failures (Tip 34).
6. **Balance resources** (Tip 35):
   - Scope-bound acquire and release (RAII, `with`, `using`, `defer`, try-with-resources).
   - Release in reverse order, and lock in a consistent order.
7. **Domain vocabulary** (Tips 17, 54): name things in the user's domain terms, and use the glossary if one exists.
8. **Program deliberately** (Tip 44): use only documented APIs. If you depend on an assumption, document it and assert it.
9. **Don't over-build** (Tip 7, "know when to stop"): no speculative abstraction, and no configurability nobody needs.

### Output
```
**Mode:** BUILD/WRITE
### Contract          (pre / post / invariants / not promised)
### Implementation    (code, in the user's stack)
### Tests             (from the contract; boundaries + invalid)
### Design notes      (≤5 bullets: each decision → Tip #)
### Assumptions / VERIFY
```

## REFACTOR: change the structure, keep the behavior

### Inputs
- **Required:** the code.
- **Helpful:** the reason (the pain point), the tests, and the constraints (public API frozen? schedule?).

### Procedure
1. **Justify it** with the When to Refactor checklist (A9): DRY violation, non-orthogonality, outdated knowledge, evolved requirements, performance. Name the trigger. If there isn't one, say so, and don't refactor just to match taste (Tip 44: don't overdo it).
2. **Safety net first:**
   - Confirm tests exist. If they don't, write *characterization tests* that pin down the current behavior before touching anything.
   - Never refactor and add functionality in the same step.
3. **Plan small steps:**
   - A sequence of 1–N behavior-preserving moves: extract, move, rename, inline, introduce parameter, replace conditional with polymorphism or a lookup table, pull up.
   - Each step leaves the tests green.
4. **Make breaking interface changes loud:** a drastic signature or semantic change should break the build or fail type checks, so every old caller is found. Never silently change meaning.
5. **Execute:** show the steps as successive diffs, or as a final diff plus the step list. Run or specify the tests after each step.
6. **If you can't refactor now:** add it to the schedule as a tracked item, board up the worst part, and tell the owners of dependent code what's coming. Explain the cost with the "growth" analogy: it gets more expensive and riskier the longer it waits.

### Output
```
**Mode:** BUILD/REFACTOR · **Trigger:** <A9 item> · **Behavior change:** none
### Safety net        (existing tests / characterization tests added)
### Steps             (numbered; each ≤1 line, each green)
### Result            (final code or diff)
### What got better   (DRY / coupling / clarity — with evidence)
### Deferred          (tracked items + board-ups)
```
