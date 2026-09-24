# Pythonic code: idioms, protocols, and gotchas

## Contents
1. Indexes, slices, and sequences
2. Context managers
3. Comprehensions and assignment expressions
4. Attributes, underscores, and properties
5. Dataclasses
6. Iterables, containers, dynamic attributes, callables
7. Magic methods quick reference
8. Gotchas
9. Decorators
10. Descriptors
11. Generators and iteration
12. Coroutines and async

---

## 1. Indexes, slices, and sequences
- Use negative indexes (`items[-1]`) and slices (`items[1:-1]`, `items[::2]`) instead of manual index arithmetic. A slice returns a new object of the same type.
- To make your own sequence, implement `__len__` and `__getitem__`. When `__getitem__` receives a slice, return an object of the same class (or at least behave like the built-in: same type, consistent semantics). The easiest route is to wrap a list and delegate to it.
- Results of your sequence's slicing and indexing should behave the way users of built-in sequences expect.

## 2. Context managers
- Use `with` for anything that needs setup and teardown: files, locks, connections, temporary state changes. The cleanup runs even if an exception is raised.
- Write your own as a class (`__enter__` / `__exit__`) or, more compactly, with `contextlib.contextmanager` on a generator (code before `yield` is setup, after is teardown).
- `contextlib.ContextDecorator` lets one object work as both a context manager and a decorator — useful when the whole function should run inside the context.
- `__exit__` should not return `True` (swallowing the exception) unless that is truly the intent. Default to letting exceptions propagate.
- Use `contextlib.suppress(SomeError)` for the rare case where ignoring a specific exception is the point — it's explicit, unlike an empty `except`.

## 3. Comprehensions and assignment expressions
- Prefer comprehensions to building lists/dicts/sets with loops and `append`. They're shorter and usually faster.
- Keep them simple. If a comprehension needs several conditions, nested loops, or side effects, write a loop or extract a function.
- The walrus operator (`:=`) avoids calling something twice (e.g. a regex match inside a comprehension) and can make code more compact. Use it where it improves readability, not to squeeze lines.

## 4. Attributes, underscores, and properties
- Python has no enforced privacy. A single leading underscore (`_name`) means "internal, don't use from outside"; respect it.
- Don't use double leading underscores (`__name`) to mean "private". They trigger name mangling, which exists to avoid clashes in subclasses, and they make code harder to extend and debug.
- Use plain public attributes by default. Switch to `@property` when you need validation, computation, or to control access — callers don't have to change.
- Don't write Java-style `get_x` / `set_x` methods.
- A property getter shouldn't have side effects or do expensive work unexpectedly. Keep command-query separation: a method either does something or answers something, not both.

## 5. Dataclasses
- Use `@dataclass` for classes that mainly hold data: it generates `__init__`, `__repr__`, and `__eq__`.
- Use `field(default_factory=list)` for mutable defaults. Use `__post_init__` for validation or derived fields. Consider `frozen=True` for value objects.

## 6. Iterables, containers, dynamic attributes, callables
- **Iterables:** implement `__iter__` returning an iterator (often by making `__iter__` a generator). An object that returns `self` from `__iter__` is an iterator and can only be consumed once — prefer making the container return a fresh iterator each time.
- A sequence (`__len__` + `__getitem__`) is also iterable, but `__iter__` is clearer and more memory-efficient for lazy data.
- **Containers:** implement `__contains__` so callers can write `if item in grid` instead of reaching into internal details. This hides the representation and reads naturally.
- **Dynamic attributes:** `__getattr__` is called only when normal lookup fails. Useful for proxies and delegation. Always raise `AttributeError` for names you don't handle, or the object will behave strangely (e.g. `hasattr` lies).
- **Callables:** implement `__call__` for objects that act like functions but keep state between calls (e.g. a counter, a configured validator).

## 7. Magic methods quick reference
| Statement | Magic method | Behaviour |
|---|---|---|
| `obj[key]`, `obj[i:j]` | `__getitem__` | subscriptable |
| `with obj:` | `__enter__` / `__exit__` | context manager |
| `for x in obj` | `__iter__` / `__next__`, or `__len__` + `__getitem__` | iterable |
| `obj.attr` (missing) | `__getattr__` | dynamic attributes |
| `obj(*args)` | `__call__` | callable |
| `x in obj` | `__contains__` | container |
| `async with obj:` | `__aenter__` / `__aexit__` | async context manager |
| `async for x in obj` | `__aiter__` / `__anext__` | async iterable |

## 8. Gotchas
- **Mutable default arguments.** `def f(items=[])` shares one list across all calls. Use `None` and create the object inside the function.
- **Extending built-ins.** Subclassing `list` or `dict` directly often doesn't work as expected, because built-in methods (implemented in C) don't call your overridden methods. Subclass `collections.UserList`, `UserDict`, or `UserString` instead, or use composition.
- **Class attributes that are mutable** are shared across all instances.
- **Late binding in closures:** lambdas created in a loop capture the variable, not its value at that iteration.
- **`is` vs `==`:** use `is` only for identity (`None`, sentinels).

## 9. Decorators
- A decorator is just a function (or class) that takes a callable and returns a replacement. They're good for reusable cross-cutting concerns: retries, logging, timing, caching, access checks, parameter transformation, registration.
- **Always use `functools.wraps`** on the inner function so the wrapped function keeps its name, docstring, and signature for debugging and tools.
- **Where to use them:** apply the rule of three — create a decorator when the logic is used in at least three places. Before that, the indirection costs more than the duplication.
- **Keep them focused:** one decorator, one concern. Stack several small decorators rather than one that does everything.
- **Decorators with arguments** need an extra level of nesting, or can be written as a class whose `__init__` takes the arguments and whose `__call__` takes the function. To support both `@retry` and `@retry(times=3)`, use keyword-only arguments with defaults and check whether the first argument is the function.
- **Side effects:** code in the decorator's outer body runs at import time, when the function is defined. Keep work that should happen per call inside the wrapper. Use import-time side effects only on purpose (e.g. registering handlers in a registry).
- **Works everywhere:** a decorator written as a plain function works on both functions and methods. A class-based decorator needs `__get__` (to become a descriptor) to work on methods.
- **Match signatures:** when a decorator adapts a function, prefer keeping the original signature visible rather than hiding everything behind `*args, **kwargs`.
- **Class decorators** can replace simple metaclass or inheritance tricks (e.g. adding methods or registering classes) with less magic.
- Decorators also work on generators and coroutines; for async functions, the wrapper must itself be `async` and `await` the call.

## 10. Descriptors
- A descriptor is an object that defines `__get__`, `__set__`, `__delete__`, and/or `__set_name__`, placed as a **class** attribute. It controls how that attribute behaves on instances. Properties, methods, `classmethod`, and `staticmethod` are all descriptors.
- **Data descriptors** (define `__set__` or `__delete__`) take precedence over the instance `__dict__`. **Non-data descriptors** (only `__get__`) can be overridden by instance attributes — useful for caching a computed value in the instance after the first access.
- Use `__set_name__` to learn the attribute name automatically instead of passing it in.
- **Shared-state trap:** the descriptor instance is shared by all instances of the owner class. Don't store per-instance values on the descriptor itself. Store them in the instance's `__dict__` (using the name from `__set_name__`) or in a `weakref.WeakKeyDictionary`.
- Use descriptors for generic, reusable technical behaviour — validation of typed fields, lazy attributes, tracing — typically in libraries, frameworks, or internal APIs. Don't put business logic in them, and don't reach for them when a property would do.
- Keep the descriptor's interface small and annotate it so type checkers understand the attribute type.

## 11. Generators and iteration
- Use generators to produce values lazily. They save memory on large or infinite data and let processing start before all data is ready.
- Generator expressions (`sum(x.price for x in items)`) are the lazy form of comprehensions.
- Use the iteration tools: `enumerate`, `zip`, `itertools` (`islice`, `chain`, `groupby`, `tee`, `product`, `accumulate`), and `next(iterator, default)` to get the first match.
- **Separate iteration from processing:** move complex iteration logic (filters, windows, nested loops) into a generator so the consumer's loop is simple.
- **Nested loops that need an early exit** are cleaner as a generator of combinations or a helper that returns, rather than flags and `break`s.
- An iterator can be consumed once. If you need to go over data twice, use a container, `itertools.tee`, or re-create the iterator.
- `yield from` delegates to a sub-generator, passes values through, and captures its return value.

## 12. Coroutines and async
- Generators and coroutines are related but mean different things: generators are for iteration, coroutines for suspending and resuming work (async I/O). Keep them separate in your mind and in your code.
- Generator methods `send()`, `throw()`, and `close()` exist but are rarely needed in application code — prefer `async`/`await`.
- Use `async with` (`__aenter__`/`__aexit__`, or `contextlib.asynccontextmanager`) for async resources, and `async for` with async generators for async streams.
- Don't block the event loop: no synchronous I/O or long CPU work inside coroutines. Offload it (`asyncio.to_thread`, executors).
