# Python sections to add to a brainstorming spec

Add these inside the superpowers spec (`docs/superpowers/specs/YYYY-MM-DD-<topic>-design.md`), under a "Python implementation notes" heading, alongside brainstorming's own sections and any `software-design` sections. Omit what doesn't apply.

## Python implementation notes

**Runtime and tooling**
- Python version: <…>
- Packaging / dependency manager: <…>
- Checks that must pass: <formatter> · <linter> · <type checker + strictness> · pytest (+ coverage threshold if any)

**Package layout and public API**
```
src/<pkg>/
  __init__.py      # public API: <names in __all__>
  <module>.py      # <what it holds>
tests/
  <mirrors src>
```

**Extension points**
| Point | Mechanism (Protocol / ABC / registry) | Why |
|---|---|---|

**Value objects and data**
<dataclasses (frozen?) inside; validation library at I/O boundaries; key types>

**Errors**
- Base exception: `<Pkg>Error`
- Subclasses: <…>
- Translated at boundaries: <low-level error → domain error, with `raise … from e`>

**Dependencies and injection**
<What's injected where (constructor/function params); what's created only at the composition root>

**Concurrency**
<sync / async / threads / processes — and why>

**Testing approach**
<unit tests against public interfaces; fakes injected vs mocks at boundaries; properties for Hypothesis; integration tests and how they're isolated>
