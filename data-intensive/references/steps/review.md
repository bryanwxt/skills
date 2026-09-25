# Lens rules for requesting- / receiving-code-review

<!-- steps-review:start — identical in software-design, clean-python and data-intensive; check with scripts/check-coordination.sh in the lens repo -->
Read one copy, from any lens, when this superpowers step starts. It holds the shared rules for the step, then one section per lens: skip the sections of lenses that aren't installed. `references/coordination.md` has the rules for every step.


## Shared

- **Final whole-branch review** (either execution skill), **or a standalone requesting-code-review:** append a lens's `review-lens.md` to `PLAN_OR_REQUIREMENTS` only when the diff touches that lens's area.

## software-design

### requesting- / receiving-code-review
- **Requesting:** per-task reviews get design rules only through Global Constraints. For the final whole-branch review or a standalone requesting-code-review, and only when module boundaries or interfaces change, append `review-lens.md` and the touched module cards to `PLAN_OR_REQUIREMENTS`.
  - Important: red flags that spread change amplification in shared modules.
  - Minor: local issues.
- **Receiving:**
  - Push back on "split it smaller" when that makes pieces shallow, pass-through, or conjoined.
  - Push back on "add an option" when the module could decide itself.
  - Accept feedback that reveals leakage or special cases.


## clean-python

### requesting- / receiving-code-review
- **Requesting:** per-task reviews get Python rules only through Global Constraints. For the final whole-branch review or a standalone requesting-code-review, and only when Python files change, append `review-lens.md` and the spec's Python notes to `PLAN_OR_REQUIREMENTS`.
  - Critical: correctness hazards.
  - Important: idiom or design problems in shared code.
  - Minor: local issues.
- **Receiving:**
  - Accept fixes for hazards, typing of public APIs, and replacing hand-rolled code with protocols.
  - Push back on inheritance just to reuse code, getters and setters, `__private` names, broad `except` "to be safe", premature abstraction, and metaclass or descriptor tricks where a function would do.
  - Style feedback belongs in tool config.


## data-intensive

### requesting- / receiving-code-review
- **Requesting:** per-task reviews get data rules only through Global Constraints; the Review Focus lines are pinned by tests. For the final whole-branch review or a standalone requesting-code-review, and only when the diff touches schemas, migrations, transactions, queues, caches, or concurrency, append `review-lens.md` and the spec's guarantees to `PLAN_OR_REQUIREMENTS`.
  - Critical: loss, corruption, broken invariants.
  - Important: races or duplicates under load or failure.
  - Minor: everything else.
- **Receiving:**
  - Accept fixes that close races, add idempotency, or remove dual writes.
  - Push back on:
    - caches without an invalidation plan;
    - XA or 2PC across heterogeneous systems;
    - "just retry" without idempotency;
    - "move to NoSQL" without a named load parameter.
<!-- steps-review:end -->
