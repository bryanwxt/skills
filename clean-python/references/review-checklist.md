# Python review checklist

Work top to bottom — earlier sections matter more. For each hit, give location, problem, why it matters, and a before/after snippet.

## 1. Correctness hazards
- [ ] Mutable default arguments (`def f(x=[])`, `={}`, `=set()`) → use `None` and create inside, or `field(default_factory=...)` in dataclasses.
- [ ] Bare `except:` or `except Exception: pass` → catch specific exceptions and actually handle them; `contextlib.suppress` if ignoring is intended.
- [ ] Re-raised exceptions that lose the original → `raise NewError(...) from e`.
- [ ] `assert` used for input validation or control flow → raise a proper exception.
- [ ] Arguments mutated in place without the caller expecting it.
- [ ] Mutable class attributes shared across instances by accident.
- [ ] Descriptors storing per-instance state on the descriptor itself.
- [ ] Subclasses of `list` / `dict` / `str` overriding methods that built-in methods won't call → `UserList` / `UserDict` / composition.
- [ ] `__getattr__` that doesn't raise `AttributeError` for unknown names.
- [ ] Iterator reused after being exhausted.
- [ ] Resources opened without `with` (files, locks, connections).
- [ ] Blocking calls inside `async` functions.
- [ ] Tracebacks or internal errors shown to end users.

## 2. Design
- [ ] Class or function with more than one reason to change (SRP) → split by concern.
- [ ] `if/elif` chains on type or kind that must be edited for each new case (OCP) → polymorphism, registry, or dispatch dict.
- [ ] Subclass that changes the parent's signature or contract (LSP).
- [ ] Large interface forcing implementers to stub methods (ISP) → smaller ABCs / Protocols.
- [ ] High-level code instantiating its own concrete dependencies (DIP) → inject them.
- [ ] Inheritance used only to reuse code, exposing irrelevant parent methods → composition.
- [ ] Exceptions handled at the wrong level of abstraction; one `try` mixing unrelated errors.
- [ ] Duplicated logic (DRY) → extract function, decorator, context manager, or generator.
- [ ] Speculative generality nobody uses yet (YAGNI) / clever metaprogramming where plain code works (KIS).
- [ ] Functions with many parameters → parameter object / dataclass, or split the function.
- [ ] Boolean flag parameters that switch behaviour → two functions, or keyword-only with a clear name.
- [ ] Domain logic importing frameworks, ORMs, or SDKs directly → adapters at the edges.
- [ ] Very large modules → package with re-exports in `__init__.py`.
- [ ] Hard-to-test code that needs many patches → reduce coupling, inject dependencies.

## 3. Idioms
- [ ] Manual index loops (`for i in range(len(x))`) → direct iteration, `enumerate`, `zip`.
- [ ] Loop + `append` building a collection → comprehension (if it stays simple).
- [ ] Over-complex comprehension → loop or helper function.
- [ ] Repeated computation that `:=` would remove cleanly.
- [ ] Look-before-you-leap checks where EAFP is clearer and race-free.
- [ ] `get_x()` / `set_x()` methods → attribute or `@property`.
- [ ] Double-underscore "private" names → single underscore.
- [ ] Hand-written `__init__` / `__repr__` / `__eq__` for data holders → `@dataclass`.
- [ ] Reaching into internals (`if x in obj.items.keys()`) → `__contains__` on the object.
- [ ] Building a full list just to iterate once → generator.
- [ ] Complex iteration mixed with processing → extract a generator; use `itertools`.
- [ ] Flags and `break`s for nested-loop exits → generator or helper that returns.
- [ ] Setup/teardown pairs → context manager.
- [ ] Repeated cross-cutting code (retry, log, timing) in 3+ places → decorator with `functools.wraps`.
- [ ] Decorator doing work at import time that should happen per call.
- [ ] `None` returned where callers must always check → null object or exception.

## 4. Documentation and typing
- [ ] Public functions/classes missing type hints or docstrings.
- [ ] Docstrings that don't mention raised exceptions or non-obvious return values.
- [ ] Comments restating the code; commented-out code.
- [ ] Names that don't reveal intent (`data`, `tmp`, `do_it`, single letters outside tiny scopes).

## 5. Tests
- [ ] New or changed behaviour without tests.
- [ ] Tests coupled to implementation details or mocking everything.
- [ ] Missing boundary, equivalence-class, and edge-case tests.
- [ ] Copy-pasted test cases → `pytest.mark.parametrize`, fixtures.
- [ ] Bug fix without a regression test.

## 6. Tooling (recommend a tool rather than listing individual issues)
- [ ] No autoformatter, linter, or type checker in CI → see `assets/pyproject-tooling.toml`.
