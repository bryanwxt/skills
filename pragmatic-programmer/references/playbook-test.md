# TEST mode: test strategy and test design

**Goal:** make the tests catch bugs before users do (Tip 49), automatically and on every build (Tip 62), with coverage of meaningful *states* (Tip 65) and proof that the tests work (Tip 64).

## Inputs
- **Required:** the code or component under test, or its contract or spec.
- **Helpful:** the existing tests, the CI setup, the test framework, known bug history, and production incidents.

## Procedure
1. **Extract the contract** (Tips 31, 48). Write down preconditions, postconditions, and invariants, even informally. Each clause generates tests:
   - Precondition violated → rejected loudly.
   - Boundary of the precondition → accepted.
   - Postcondition holds across the valid domain, including the extremes.
   - Invariant holds after every public operation.
2. **Map the state space** (Tip 65).
   - Identify the significant states: empty, one, many, max, boundary ±1, invalid, concurrent, partially failed, retried.
   - Look for singular points, e.g. `a/(a+b)` fails only when `a+b==0`, and line coverage will never reveal it.
   - ⟳ modern: property-based testing (Hypothesis, fast-check, QuickCheck, jqwik) for broad state exploration.
3. **Layer the tests** (checklist A11), from fine nets to coarse ones:
   - **Unit:** each module against its contract, in isolation. Test the parts bottom-up before the composite, so a composite failure points at the composite.
   - **Integration:** subsystems honoring each other's contracts. This is often the biggest source of bugs.
   - **Validation:** does it solve the *user's* problem? Use real usage patterns and real data.
   - **Resource exhaustion, errors, and recovery:** memory, disk, file handles, connection pools, rate limits, timeouts, time budgets. Does it fail gracefully and preserve work?
   - **Performance and load:** expected users, connections, throughput, and scaling behavior.
   - **Usability:** real users as early as possible. A usability failure is as real a bug as divide-by-zero.
4. **Choose data** (B10): real samples for typical behavior, synthetic data for volume, boundaries, and statistical properties.
5. **Decouple for testability** (Tips 42, 48):
   - If logic can't be tested without the UI, database, or network, recommend separating the model from the view, or putting an interface at the boundary. This is a design finding, not just a test finding.
   - A big unit-test footprint is an orthogonality smell.
6. **Test the tests** (Tip 64):
   - For each critical test, say which injected bug it catches.
   - Recommend a saboteur or mutation run (⟳ modern: mutmut, Stryker, PIT, cargo-mutants).
   - For a bug-fix test, confirm it fails on the pre-fix code.
7. **Automate and gate** (Tips 61–63):
   - One command runs all tests, from the root or from a subdirectory for one module.
   - CI runs them on every push.
   - Code isn't done until all tests pass.
   - Scheduled heavy suites (stress, soak) run on a cadence, with resources actually allocated.
8. **Find bugs once** (Tip 66): every bug a human finds gets an automated test, with no exceptions for "trivial" bugs.
9. **Production test window:** structured, parseable logs, plus health and diagnostic endpoints, because some bugs only appear in production.

## Anti-patterns to flag
- Chasing a coverage percentage as the goal.
- Tests without meaningful assertions.
- Tests that mirror the implementation instead of the contract.
- Hand-maintained test registries.
- Ad hoc debug prints never promoted into tests.
- Flaky tests that nobody treats as a broken window.
- Only happy-path data.
- Test plans that exist only in a document.

## Output
Use the default template. The Findings table becomes **Gaps (ranked)**, followed by:

```
### Test plan
| Layer | Test | State / boundary covered | Contract clause | Catches injected bug |
### Test code   (top 3–6 tests, in the user's framework)
### Automation  (command + CI gate)
```
