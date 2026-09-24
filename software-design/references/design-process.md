# Design process for new systems

## Contents
1. Start from knowledge, not steps
2. Design it twice
3. Interface first, comments first
4. Sizing modules
5. Errors and defaults
6. Iterating strategically

## 1. Start from knowledge, not steps

List the design decisions and bodies of knowledge the system needs: data formats, storage and caching choices, external APIs and protocols, algorithms, business rules, policies, and platform specifics. For each, ask: "Which single module should own this, so nothing else has to know it?" The answers give you the first draft of your modules.

Resist the natural urge to decompose by the order things happen (request comes in → validate → process → store → respond). That produces modules that each need to know the same data shapes and formats. Order-of-operations belongs inside a module's implementation, not in the module structure.

Also note the likely directions of change (new data sources, new output formats, scaling, new user types). Put a module boundary around each decision that is likely to change.

## 2. Design it twice

Your first idea is rarely the best one. For anything important — the top-level decomposition, a core module's interface, a key data model — sketch at least two **radically different** approaches before committing. Rough sketches are enough: the interface signatures and a paragraph each.

Compare on:
- Which gives the simplest interface for the most common uses?
- Which is more general-purpose without being harder to use?
- Which hides more information from its users?
- Which has better performance characteristics where performance matters?
- What are the weaknesses of each? Would a hybrid take the best parts?

If none is attractive, use the weaknesses you found to generate a third. The time this takes is small compared to building on a weak design. Record the losers and why they lost; that rationale is valuable later.

Do this at every level where it matters: system decomposition, module interfaces, and occasionally even a tricky implementation.

## 3. Interface first, comments first

For each module, before implementing:

1. Write a one-line statement of the abstraction it provides.
2. Write the class/module comment: what it represents, what it hides, key invariants.
3. Write each public method's signature and interface comment: behaviour, arguments (with units and ranges), return value, side effects, errors.
4. Review: is every comment short and simple? Is the common case trivial for callers? Can any method be removed without losing capability? Does any comment leak implementation?
5. Only then implement, adding implementation comments for anything not obvious as you go.

If a comment is hard to write or keeps growing, stop and rethink the module. The comment is telling you the abstraction is unclear.

## 4. Sizing modules

- Aim for deep modules: prefer fewer, more capable modules with small interfaces over many small modules with lots of glue.
- Don't create a class per concept by reflex. Every module adds an interface to learn.
- Combine things that share knowledge, are always used together, or that together give a simpler interface.
- Separate general-purpose mechanisms from special-purpose uses. The general mechanism should never need to know which specific uses exist.
- Make each layer a different abstraction. If two adjacent layers have the same method list, one of them probably shouldn't exist.
- Make interfaces somewhat general-purpose (usable for many cases) while implementing only today's needs.

Test for a module: can you explain what it does, in one sentence, without mentioning how it does it? Would a caller need to read its implementation to use it correctly? If yes, it isn't hiding enough.

## 5. Errors and defaults

For each module, list the exceptional conditions it can encounter and decide, in this order of preference:

1. Can the semantics be defined so this isn't an error at all?
2. Can the module handle it internally (mask it) so callers never see it?
3. Can several conditions be aggregated into one handling point higher up?
4. Is it rare and unrecoverable enough to just crash with a clear message?
5. Only then: expose it in the interface, documented.

For each configuration choice: can the module work out a good value itself? If not, what default fits the common case?

## 6. Iterating strategically

- Build in increments of **abstractions, not features**: when a feature needs a new abstraction, build that abstraction properly rather than a piece of it.
- After each change, the system should look as if it had been designed with that change in mind.
- Keep a short design-notes file for decisions that span modules, and reference it from the code.
- When you are unsure what matters most, commit to a hypothesis, build on it, and review later why it was right or wrong.
