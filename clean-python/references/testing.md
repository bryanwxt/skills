# Testing and refactoring in Python

## Contents
1. Why tests are part of clean code
2. What and how much to test
3. Tools: unittest and pytest
4. Mocks and patching
5. Coverage, property-based and mutation testing
6. Choosing test cases
7. Refactoring safely
8. TDD

---

## 1. Why tests are part of clean code
- Unit tests are the formal specification of what the code should do and the evidence that it does it. Without them, refactoring is guesswork.
- Testability mirrors design. Code that's hard to test is usually too coupled, does too much, or hides its dependencies. When a test is painful to write, fix the design, not just the test.
- Test code is production code: apply the same standards of naming, structure, and DRY. Neglected tests become a liability that people disable or ignore.

## 2. What and how much to test
- Unit tests check one unit (function, class) in isolation, run fast, and don't depend on external systems (network, databases, clocks). Integration and acceptance tests cover the rest — keep them separate.
- Test **your** code, not third-party libraries. At the boundary with external dependencies, replace them with test doubles.
- Test behaviour through public interfaces, not implementation details, so refactoring doesn't break tests needlessly.

## 3. Tools: unittest and pytest
- `unittest` is in the standard library (`TestCase`, `assertEqual`, `subTest` for parameterized cases).
- **Prefer pytest:** plain `assert` statements with rich failure output, less boilerplate, and it runs unittest tests too.
- `@pytest.mark.parametrize` for running the same test over many inputs — keeps each case visible without copy-paste.
- **Fixtures** for reusable setup (objects, temp files, fake services). Scope them appropriately and keep them small. Put shared ones in `conftest.py`.
- `pytest.raises(SomeError, match=...)` to test exceptions.

## 4. Mocks and patching
- `unittest.mock.Mock` / `MagicMock` stand in for dependencies; `MagicMock` also supports magic methods. Use `spec` / `autospec` so the mock fails if you call something the real object doesn't have.
- `mock.patch` replaces an object for the duration of a test. **Patch where the object is looked up** (the module that imports it), not where it's defined.
- Assert interactions (`assert_called_once_with`) only when the interaction *is* the behaviour you care about.
- **Warning sign:** if a test needs many patches, the code under test is too coupled. Prefer dependency injection — pass collaborators in, and hand the test a fake. Excessive mocking also makes tests brittle and can make them pass while the real integration is broken.
- Wrap third-party libraries in your own small adapter; mock the adapter rather than library internals.

## 5. Coverage, property-based and mutation testing
- **Coverage** (`pytest-cov` / `coverage.py`) shows which lines ran. Use it to find untested code, not as a goal in itself. High coverage doesn't mean good tests — a line can run without its behaviour being checked. Enable branch coverage.
- **Property-based testing** (Hypothesis) generates many inputs and checks properties that should always hold (e.g. round-trips, invariants). Great for finding edge cases you didn't think of.
- **Mutation testing** (e.g. mutmut) changes the code in small ways and checks that tests fail. Surviving mutants reveal tests that don't really verify behaviour.

## 6. Choosing test cases
- **Boundaries / limit values:** test at and around every limit (0, 1, max, max+1, empty, just-over-threshold).
- **Equivalence classes:** group inputs that should behave the same and test one representative from each class, rather than many from one.
- **Edge cases:** empty inputs, `None`, very large values, unicode, duplicates, unusual types, concurrency.
- Every bug fix gets a regression test that fails before the fix.

## 7. Refactoring safely
- Refactoring changes structure without changing behaviour. The tests prove behaviour didn't change, so get a safety net first (write characterization tests for legacy code if needed).
- Take small steps and run the tests after each one.
- Good tests target the public interface; if refactoring breaks many tests without changing behaviour, those tests were too tied to implementation.
- Tests evolve too: when production code changes shape, refactor the tests to match, and remove duplicated setup into fixtures.

## 8. TDD
- Test-driven development: write a failing test, write the minimum code to pass it, then refactor. It keeps code testable by construction and ensures every piece of code has a test.
- Even without strict TDD, writing the test before fixing a bug is a strong habit.
