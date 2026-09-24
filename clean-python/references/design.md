# Design principles for Python code

> When `software-design` is active, it decides how the system is split into modules and what each hides. Use this file for the Python side: contracts, errors, SOLID in Python, patterns, and keeping frameworks at the edges.

## Contents
1. Contracts and defensive programming
2. Error handling
3. Separation of concerns, cohesion, coupling
4. DRY, YAGNI, KIS, EAFP
5. Inheritance vs composition
6. Function arguments
7. Orthogonality and code structure
8. SOLID in Python
9. Design patterns in Python
10. Architecture

---

## 1. Contracts and defensive programming
**Design by contract.** Make each component's expectations explicit:
- **Preconditions** — what must be true of inputs before the function runs. Validate them at the boundary.
- **Postconditions** — what the function guarantees about its result or state afterwards.
- **Invariants** — what stays true throughout.
- Decide on one place for each check. Usually the called function validates its own preconditions (a "tolerant" caller, "demanding" callee), so validation isn't duplicated at every call site.
- When a contract breaks, it should fail loudly with a clear exception so you know which side broke it.

**Defensive programming** protects a component from bad input or unexpected states:
- **Value substitution** — return a safe default when appropriate (e.g. `dict.get(key, default)`, `os.getenv("X", "default")`). Use only where a default is truly correct; substituting a value can hide errors.
- **Exception handling** — raise when the function can't do its job.

**Assertions** are for conditions that should be impossible if the code is correct. Don't use them for input validation or control flow (they're removed with `python -O`), and don't catch `AssertionError`. Give them a helpful message.

## 2. Error handling
- Use exceptions for exceptional situations, not as normal control flow (no "go-to" via exceptions).
- **Raise at the right level of abstraction.** A function should raise and handle only errors that relate to what it does. Low-level errors (e.g. `ConnectionError` with retries) belong in the connection logic; decoding errors belong with decoding. Split the function if one `try` block mixes unrelated errors.
- **Translate** low-level exceptions into domain exceptions at module boundaries, with `raise DomainError(...) from e` to keep the original traceback.
- Create a small hierarchy of custom exceptions for your package, rooted in one base class, so callers can catch broadly or narrowly.
- **Never use a bare or empty `except`.** Catch specific exceptions, and do something real in the handler (log with context, clean up, retry, re-raise, or translate). If ignoring an error is truly intended, use `contextlib.suppress` so the intent is explicit.
- Don't expose tracebacks to end users — log them and show a safe message. Tracebacks can leak sensitive details.
- Handle errors in the place that knows what to do about them; let them propagate otherwise.

## 3. Separation of concerns, cohesion, coupling
- Each part of the program should handle one concern, so changes stay local and don't ripple.
- **High cohesion:** a module or class should have a small, well-defined purpose, and everything in it should serve that purpose.
- **Low coupling:** components should know as little about each other as possible. High coupling causes limited reuse, ripple effects, and components that leak each other's details.
- Aim for both: cohesive components with narrow, stable interfaces between them.

## 4. DRY, YAGNI, KIS, EAFP
- **DRY / OAOO (once and only once).** Each piece of knowledge should live in one place. Duplication causes inconsistency when one copy changes. Remove it with functions, classes, decorators, context managers, or iterators — whatever abstraction fits.
- **YAGNI.** Don't build for speculative future requirements. Design so that future changes are easy, but only implement today's needs.
- **KIS (keep it simple).** Choose the minimal solution that solves the problem. Avoid clever metaprogramming, needless layers, and generality you don't need. Plain objects and functions often beat elaborate frameworks.
- **EAFP over LBYL.** In Python it's usually clearer to try the operation and handle the exception (`try: open(...) except FileNotFoundError:`) than to check first (`if os.path.exists(...)`). It also avoids race conditions between the check and the use.

## 5. Inheritance vs composition
- Inheritance is right when the child is a genuine **specialization** of the parent and the parent's whole public interface makes sense for the child (e.g. a specific HTTP handler overriding `handle()`). It also suits defining interfaces with abstract base classes, and exception hierarchies.
- **Anti-pattern:** inheriting only to reuse code. If a domain class inherits from a data structure (e.g. `class Policies(collections.UserDict)`), it exposes irrelevant methods (`pop`, `clear`, …) as part of its interface. Instead, compose: hold the data structure as an attribute and expose only the domain operations, plus magic methods like `__getitem__` / `__len__` if they fit.
- **Multiple inheritance** works through the method resolution order (MRO, C3 linearization; inspect with `Class.mro()`). Keep it simple.
- **Mixins** are small classes providing one reusable behaviour, meant to be combined with other classes. They're the acceptable common use of multiple inheritance. Keep them stateless and focused.
- When in doubt, prefer composition.

## 6. Function arguments
- Python passes references to objects. Mutating a mutable argument inside a function changes the caller's object — avoid mutating arguments unless that's the documented purpose.
- `*args` / `**kwargs` give flexible signatures but hide what a function expects. Use them sparingly (e.g. in wrappers that forward), and prefer explicit parameters.
- Use **keyword-only** parameters (after `*`) for options, flags, and anything that could be confused positionally. Use **positional-only** (before `/`) when the name is irrelevant or may change.
- **Too many arguments** is a smell that suggests a missing abstraction, or a function doing too much. Remedies:
  - **Reify** related arguments into an object (a dataclass or domain object) — this is often the abstraction you were missing.
  - Pass an existing object instead of several of its attributes.
  - If the function branches heavily on its arguments, split it into several functions.
- More parameters mean tighter coupling between caller and callee, because the caller must gather more information.

## 7. Orthogonality and code structure
- **Orthogonality:** changing one component shouldn't affect others. Build components that can be combined independently (e.g. a decorator that adds behaviour without touching the function it wraps). Orthogonal code is easier to test in isolation.
- **Structure:** avoid very large files. Group definitions by similarity into modules and packages. When a module grows too big, turn it into a package whose `__init__.py` re-exports the old names (and lists them in `__all__`) so existing imports keep working. Keep conventions for where things live (e.g. one module for constants).

## 8. SOLID in Python
- **Single responsibility (SRP):** a class should have one reason to change. If a class mixes unrelated operations (e.g. loading from a source, parsing, and sending), split it into classes that each handle one concern and are composed together. Watch for methods that don't use the same attributes — they probably belong elsewhere.
- **Open/closed (OCP):** open to extension, closed to modification. When a function uses an `if/elif` chain on type to handle cases, adding a case means editing it. Instead, give each case its own class implementing a common interface, and iterate over them (e.g. auto-discover subclasses via `__subclasses__()` or a registry). New behaviour = new class.
- **Liskov substitution (LSP):** any subclass must be usable wherever its parent is. Subclass methods must accept at least the same inputs, return compatible outputs, not strengthen preconditions, and not weaken postconditions. mypy and pylint (`arguments-differ`) catch signature mismatches; semantic violations need tests and review.
- **Interface segregation (ISP):** prefer several small interfaces to one large one. A class shouldn't be forced to implement methods it doesn't need. In Python, use small abstract base classes or `typing.Protocol`s, often one method each, and combine them.
- **Dependency inversion (DIP):** high-level logic should depend on abstractions, not on concrete low-level details. Pass dependencies in (dependency injection through `__init__` or function parameters) rather than instantiating them inside. This makes the code testable and lets implementations change. DI libraries (e.g. `pinject`) exist, but plain constructor injection is usually enough.

## 9. Design patterns in Python
Patterns are useful as shared vocabulary and as solutions to recurring problems. Python's features make many of them simpler or unnecessary — don't force a pattern where a function or a module suffices.
- **Creational:** Python functions and classes are already factories. Modules are natural singletons — prefer a module-level object to a Singleton class. If instances must share state, a shared-state design (Borg/monostate, or a descriptor holding class-level state) beats a forced singleton. Builders help only when object construction is truly complex.
- **Structural:** Adapter (via composition, or `__getattr__` delegation) makes an incompatible interface fit. Composite lets clients treat a single item and a group the same way. Decorator (the pattern) adds behaviour dynamically, often via composition or Python decorators. Facade gives one simple entry point to a complex subsystem — a package's `__init__.py` is a natural facade.
- **Behavioral:** Chain of responsibility (each handler handles or passes on), Template method (the base class defines the algorithm, subclasses fill in steps), Command (separate preparing an action from executing it), State (represent each state as a class instead of branching on a state flag). The **null object** pattern returns an object with the expected interface that does nothing, instead of `None`, so callers don't need `if x is not None` everywhere.
- Name classes after domain concepts, not pattern names (`EventDispatcher` rather than `EventStrategyFactory`), unless the pattern name genuinely communicates.

## 10. Architecture
- The same principles apply at the system level: separation of concerns, cohesion, low coupling, abstraction, and intention-revealing names.
- **Keep the domain independent of details.** Business logic shouldn't import the web framework, ORM, or cloud SDK. Put those in adapters at the edges, with dependencies pointing inward to the domain (clean architecture / ports and adapters).
- The top-level structure should reveal what the system does (its use cases), not which framework it uses.
- **Packages** are the unit of reuse. Create one for a cohesive set of functionality with a single responsibility. Package properly (`pyproject.toml`), pin and manage dependencies, and version artifacts.
- **Services and containers:** a service built from a packaged Python application can be deployed in a Docker image. Microservices follow the same cohesion/SRP logic — but they add operational cost, so a well-structured monolith is often the right start.
- Perfect isolation isn't always possible or worth it. If abstracting away a framework costs more than it saves, don't. Principles, not laws.
