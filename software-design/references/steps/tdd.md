# Lens rules for test-driven-development

<!-- steps-tdd:start — identical in software-design, clean-python and data-intensive; check with scripts/check-coordination.sh in the lens repo -->
Read one copy, from any lens, when this superpowers step starts. It holds the shared rules for the step, then one section per lens: skip the sections of lenses that aren't installed. `references/coordination.md` has the rules for every step.


## software-design

### test-driven-development
- Test through the public interface and its documented behaviour, not helpers.
- Heavy setup or many mocks is a design signal: note it for review.


## clean-python

### test-driven-development
- **Red:**
  - Use `@pytest.mark.parametrize` for tables of cases, `pytest.raises(…, match=…)` for errors, and small fixtures in `conftest.py`.
  - Cover boundaries, equivalence classes, and edge cases: empty, `None`, huge, unicode, duplicates.
  - Use Hypothesis for invariants.
  - The test must fail for the expected reason, not with a `NameError` or `ImportError`.
- **Doubles:** follow the Tests rule in `coordination.md`. Use `create_autospec` or `spec=`. Many patches is a design signal: inject a fake instead.
- **Green / refactor:** write the simplest Pythonic code, then apply idioms: comprehensions, `enumerate`/`zip`, `with`, dataclasses, `@property`. Rerun the tests and tools.


## data-intensive

### test-driven-development
Add failing-first tests where relevant, run against the real engine:
- **Race:** two connections with explicit interleaving, then assert the invariant.
- **Idempotency:** the same request or message twice, and out of order, gives one effect.
- **Migration:** old code on the new schema, new code on the old schema, and unknown fields preserved.
- **Rerun:** running a job twice gives the same output.
- **Failure injection:** a timeout followed by a retry, and a crash before commit.
- **Property tests** for invariants.
<!-- steps-tdd:end -->
