# Core principles (condensed from *A Philosophy of Software Design*, 2nd ed.)

## Contents
1. Complexity: what it is, how to spot it
2. Strategic vs tactical programming
3. Deep modules
4. Information hiding and leakage
5. Somewhat general-purpose modules
6. Different layer, different abstraction
7. Pull complexity downward
8. Together or apart?
9. Define errors out of existence
10. Comments, names, and obviousness
11. Consistency
12. Performance
13. Decide what matters
14. Views on popular practices

---

## 1. Complexity

Complexity is whatever in the structure of a system makes it hard to understand and modify. A rough way to weigh it: the complexity of each part multiplied by how much time developers spend in that part. Complexity is judged by readers more than writers — if others find your code complicated, it is.

**Symptoms:** change amplification, cognitive load, unknown unknowns (see SKILL.md). Fewer lines is not automatically simpler; a longer approach that lowers cognitive load can be better.

**Causes:** dependencies and obscurity. Dependencies can't be eliminated, but they can be made fewer, simpler, and more obvious. Obscurity comes from vague names, missing documentation, and inconsistency; it is often a sign that the design itself is unclear.

**It accumulates.** No single shortcut ruins a system. Hundreds of small ones do, and once it's accumulated it is hard to remove. So small things matter — a "zero tolerance" attitude toward small complexity is the only thing that works.

## 2. Strategic vs tactical programming

- **Tactical:** get the feature working as fast as possible. Each shortcut seems harmless; together they produce a mess. The extreme is the "tactical tornado" who ships fast and leaves others to clean up.
- **Strategic:** working code isn't enough. The primary goal is a good long-term structure; working code is a byproduct. Invest continuously — roughly 10–20% of development time on design improvements — rather than in rare big cleanups.
- When you find a design problem while making a change, fix it rather than working around it. After each change, the system should look as if it had been designed with that change in mind from the start.
- The payoff comes within months, not years. Startups are not exempt: a messy codebase slows hiring and features.

## 3. Deep modules

A module (class, function, service, package, subsystem) has an **interface** (what users must know) and an **implementation** (what it does internally). The interface includes informal parts: side effects, ordering rules, performance characteristics, and any assumption callers must respect.

- The best modules are **deep**: a lot of functionality behind a simple interface. Think of the benefit as functionality and the cost as interface size.
- **Shallow** modules have interfaces nearly as complex as what they do. They add a concept for readers to learn without hiding much. A method that only wraps one line, or a class for every tiny idea, is shallow.
- **Classitis:** the belief that classes should be small at any cost. It yields many shallow classes, lots of boilerplate, and complexity spread across interfaces.
- **Make the common case simple.** An interface should make the most frequent usage easy, even if rare uses need more effort. Forcing everyone to request something (like buffering) that almost everyone wants is a design failure.
- A simple interface matters more than a simple implementation.

## 4. Information hiding and leakage

- Each module should encapsulate a few design decisions — data structures, formats, algorithms, protocols, low-level mechanisms — that the rest of the system doesn't need to know. Hidden information can change without affecting anything else.
- Private fields and getters/setters are not information hiding if the representation still shows through the methods.
- **Information leakage** is when one design decision shows up in more than one module. A change to it then touches all of them. Leakage can be through interfaces or "back doors" (two modules both know a file format without either one saying so). Fix by merging the modules that share the knowledge, or by pulling the knowledge into a new module that owns it.
- **Temporal decomposition:** structuring modules by the order operations happen (read file → parse → modify → write) usually spreads the same knowledge across several modules. Structure around knowledge instead, not around timing.
- **Defaults** are a form of information hiding: callers shouldn't need to know about things they don't care about.
- Hide information within a module too: keep each variable or piece of knowledge used in as few places as possible.
- Don't hide things callers genuinely need (e.g. a performance-critical setting). Hiding needed information creates unknown unknowns.

## 5. Somewhat general-purpose modules

- Design interfaces to be general enough to serve many uses, while implementing only what is needed today. General-purpose interfaces tend to be simpler and deeper, and they hide more (the lower module doesn't learn about UI concepts like "backspace" — it just deletes a range).
- Questions to ask:
  - What is the simplest interface that covers all my current needs? Fewer methods with no loss of capability usually means more general.
  - In how many situations will this method be used? A method designed for one call site is a red flag.
  - Can today's callers use this API easily? If they need lots of extra code, it's gone too general.
- **Push specialization up or down.** Keep special-purpose logic at the top (the UI or application layer) or at the bottom (device-specific drivers behind a general interface), not tangled into general mechanisms.
- **Eliminate special cases.** Design the normal case so it automatically covers edge cases (e.g. an empty selection that behaves like any other selection instead of a "no selection" flag checked everywhere).

## 6. Different layer, different abstraction

- In a well-layered system, each layer offers an abstraction different from the ones above and below it.
- **Pass-through methods** (a method that only calls another method with a similar signature) signal that responsibilities are split badly. Fix by exposing the lower layer, redistributing functionality, or merging the classes.
- Duplicate signatures are fine when each implementation does something substantially different (e.g. a dispatcher, or several implementations of one interface).
- **Decorators** tend to be shallow and full of pass-throughs. Before writing one, consider adding the feature to the underlying class, merging it into the use case, or building it as a standalone feature.
- An interface should usually differ from its implementation. If a class stores data as lines but callers think in characters, the interface should talk in characters.
- **Pass-through variables** (threaded through a long chain of methods that don't use them) add complexity. Consider a shared context object that holds global-ish state, and keep what goes into it disciplined.

## 7. Pull complexity downward

- When complexity is unavoidable, it is better for the module's implementer to deal with it than for every user. A module has few developers and many users.
- **Configuration parameters** often push decisions up to users who are less able to make them. Before adding one, ask whether the module could compute a good value itself. When a parameter is unavoidable, give it a good default.
- Taken too far: pulling complexity down only helps if it is closely related to the module's existing job, lowers complexity elsewhere, and simplifies the interface. Don't dump unrelated features into a module.

## 8. Together or apart?

Combine two pieces of code when:
- they share information,
- they are always used together (in both directions),
- they overlap conceptually,
- it's hard to understand one without reading the other,
- combining would simplify the interface, or
- combining eliminates duplication.

Separate them when one is general-purpose and the other special-purpose. General mechanisms shouldn't know about specific uses.

**Methods:** length alone is not a reason to split. Split a method only when it produces a cleaner abstraction — either an extractable subtask that is independently understandable, or a method doing two genuinely separate things that callers invoke separately. Fragments that can only be understood together ("conjoined methods") should stay merged. Every method should be understandable on its own, do one thing, and do it completely.

## 9. Define errors out of existence

Exceptions and special cases are among the worst sources of complexity: handling code is rarely exercised, hard to test, and often wrong.

- **Throw fewer exceptions.** Don't throw just to avoid deciding what to do. Every exception in an interface makes the interface more complex.
- **Define the error away:** change the semantics so the condition isn't an error. (Deleting a file that's in use can still succeed from the caller's view; a substring call with out-of-range indices can clip to the string; unsetting a variable that doesn't exist can simply mean "ensure it doesn't exist".)
- **Mask exceptions:** handle the condition at a low level so higher levels never see it (e.g. retransmitting lost packets inside the transport).
- **Aggregate exceptions:** handle many exceptions in one place with one handler rather than many specialized ones.
- **Just crash:** for errors that are rare and hard to recover from (out of memory), crashing with a clear diagnostic can be simpler than pretending to handle them.
- Don't take it too far: if callers genuinely need to know about a condition, it must be exposed.

## 10. Comments, names, and obviousness

**Why comments matter.** Code can't express everything: the abstraction, rationale, constraints, and units live in the designer's head. Comments capture that. "Self-documenting code" helps but isn't enough; the four excuses (no time, they go stale, they're worthless, good code doesn't need them) don't hold up.

**What to write.** Comments should describe what isn't obvious from the code.
- Don't repeat the code. If the comment uses the same words as the name it describes, it adds nothing.
- **Lower-level comments** add precision: units, ranges, whether bounds are inclusive, what null means, invariants, ownership.
- **Higher-level comments** give intuition: what a block of code is doing overall and why.
- **Interface comments** describe the abstraction for users — behaviour, arguments, return values, side effects, preconditions — without implementation details. **Implementation comments** explain what and why, not how.
- Document **cross-module decisions** in one central place (e.g. a design notes file) and reference it.
- Keep comments next to the code they describe; put design explanations in the code, not only in commit messages. Avoid duplicating documentation; check diffs to keep comments current.

**Write comments first.** Write the class and method interface comments before the implementation. Comments written late are worse and tend not to get written. Early comments are a design tool: if a method or variable is hard to describe simply, the design is probably wrong.

**Names.**
- A name should create an image of what the thing is. Pick names that are precise and not generic (`count`, `data`, `result`, `status` are vague).
- Use the same name for the same concept everywhere, never use one name for different things, and keep the purpose of a name narrow enough that everything with that name really is the same.
- Avoid extra words that carry no information.
- Short names are fine when the scope is tiny and the meaning obvious; the further a name travels, the more precise it must be.
- If a name is hard to pick, the thing it names probably isn't a clean concept.

**Obvious code.** Code is obvious when a reader's first guess about it is correct. It is written for readers, not writers.
- Helps: good names, consistency, judicious whitespace, and comments that fill gaps.
- Hurts: event-driven programming without documentation of what triggers handlers, generic containers (pairs/tuples) that hide meaning, a declared type that differs from the allocated type, and code that violates reader expectations.

## 11. Consistency

Doing similar things in similar ways lets developers learn once and apply everywhere. It covers names, coding style, interfaces with multiple implementations, design patterns, and invariants. Ensure it with documentation, automated checkers, and "when in Rome" (follow existing conventions). Don't change an existing convention unless the new one is significantly better *and* you'll update all the old code. Taken too far, consistency forces unlike things into the same shape.

## 12. Performance

- Keep a rough sense of what is expensive (network, I/O, allocation, cache misses) and choose naturally efficient designs when they're just as clean.
- Measure before optimizing, and after, to confirm it helped.
- For real hot paths, design around the critical path: identify the minimum work the common case must do, build the design around that path, and push special cases off it (ideally to a single check).
- Clean, simple designs are usually fast. Complexity tends to slow code down.

## 13. Decide what matters

- Structure the system around the things that matter and minimize the rest. Look for **leverage**: solutions that solve many problems, or pieces of knowledge (like invariants) that explain many behaviours.
- **Minimize what matters:** fewer required parameters, good defaults, errors handled low, configuration computed automatically.
- **Emphasize what matters** through prominence (names, interface docs, parameters to widely used methods), repetition, and centrality (core ideas at the heart of the structure).
- Two mistakes: treating too many things as important (clutter, shallow classes) or failing to recognize something important (hidden functionality, unknown unknowns). When unsure, commit to a hypothesis about what matters and learn from the result.

## 14. Views on popular practices

- **Inheritance:** interface inheritance gives leverage; implementation inheritance creates dependencies between parent and child. Prefer composition where it's reasonable.
- **Agile:** fine, but develop in increments of **abstractions, not features**. When you need an abstraction, build it fully rather than piecemeal.
- **Unit tests:** very valuable, especially because they make refactoring safe.
- **TDD:** risks tactical programming, since it focuses on making a test pass rather than finding the best design. Good for bug fixes (write the failing test first).
- **Design patterns:** useful when they fit; the danger is forcing a pattern where a simpler custom approach works better.
- **Getters/setters:** they're shallow and expose representation. Avoid exposing instance variables in the first place.
