# Python review lens (append to `PLAN_OR_REQUIREMENTS` for the final whole-branch review or a standalone requesting-code-review; never to per-task reviews)

Also review the Python-specific quality of the change, based on *Clean Code in Python*. Skip anything the project's formatter, linter, or type checker would catch; if a whole class of issue should be automated, say so once instead of listing instances. For each finding give file:line, the problem, why it matters, and a short fix.

**Critical**
- Mutable default arguments; mutable class attributes shared by accident.
- Bare `except`, `except Exception: pass`, or re-raising without `from e`.
- Resources opened without `with`; blocking I/O inside `async def`.
- `assert` used for validation or control flow.
- Subclassing `dict`/`list`/`str` with overrides that built-ins bypass; `__getattr__` not raising `AttributeError`.
- Per-instance state stored on a descriptor.

**Important**
- A function or class doing several jobs; `if/elif` chains on type that must grow per case.
- Inheritance used only to reuse code (use composition).
- Dependencies created inside business logic instead of injected; tests needing many patches.
- Long argument lists or boolean flag parameters (parameter object, or separate functions).
- Exceptions handled at the wrong level; no package exception hierarchy.
- Duplicated logic that a function, decorator (3+ uses), context manager, or generator would remove.
- Public functions missing type hints or docstrings (args, returns, raises).
- Tests coupled to internals, over-mocked, missing boundaries or edge cases, or copy-pasted instead of parametrized.

**Minor**
- Manual index loops, loop-plus-append instead of a comprehension, over-complex comprehensions.
- Getters/setters instead of attributes or `@property`; double-underscore "private" names.
- Hand-written `__init__`/`__repr__`/`__eq__` where `@dataclass` fits.
- Look-before-you-leap where EAFP is clearer.
- Vague names; comments restating code; commented-out code.
