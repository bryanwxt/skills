# Checklists

Part A paraphrases the book's 11 quick-reference checklists. Part B collects operational checklists derived from the body text. Page numbers refer to the 1st edition.

## Part A — Book checklists

### A1. Languages to Learn (p.17), Tip 8
Learn at least one new language a year, and pick one that makes you think differently. The book's 1999 list (CLOS, Dylan, Eiffel, Objective-C, Prolog, Smalltalk, TOM) is dated. ⟳ modern: choose by *paradigm gap* from your current stack. Candidates include functional (Haskell, OCaml, Elixir), systems/ownership (Rust), logic/relational (Prolog, Datalog, SQL done well), array (APL/J, NumPy thinking), and concurrency-first (Erlang/Elixir, Go). Do a small home project in it.

### A2. WISDOM acrostic (p.20), Tip 10
- **W**hat do you want the audience to learn?
- What is their **I**nterest in what you've got to say?
- How **S**ophisticated are they?
- How much **D**etail do they want?
- Whom do you want to **O**wn the information?
- How can you **M**otivate them to listen?

### A3. How to Maintain Orthogonality (p.34), Tip 13
- Design independent, well-defined components.
- Keep code decoupled (shy code, Law of Demeter).
- Avoid global data, including singletons and read-only globals.
- Refactor similar functions (for example, use the Strategy pattern for "same start and end, different middle").

### A4. Things to Prototype (p.53), Tip 16
Architecture · new functionality in an existing system · structure or contents of external data · third-party tools or components · performance issues · user interface design.
*You may ignore:* correctness (dummy data is fine), completeness, robustness (crashing off the happy path is fine), and style. Do document what you learned.

### A5. Architectural Questions (p.55)
- Are responsibilities well defined?
- Are the collaborations well defined?
- Is coupling minimized?
- Can you identify potential duplication?
- Are interface definitions and constraints acceptable?
- Can modules access the data they need, when they need it? (This one surprises people most often.)

### A6. Debugging Checklist (p.98), Tips 24–27
- Is the reported problem the underlying bug, or merely a symptom?
- Is the bug really in the compiler or OS, or is it in your code?
- If you explained this problem in detail to a coworker, what would you say?
- If the suspect code passes its unit tests, are the tests complete enough? What happens if you run them with *this* data?
- Do the conditions that caused this bug exist anywhere else in the system?

### A7. Law of Demeter for Functions (p.141), Tip 36
A method should call methods only on:
- itself
- its parameters
- objects it creates
- its directly held component objects

Chained calls through returned objects (`a.getB().getC().doIt()`) are the classic violation.

### A8. How to Program Deliberately (p.172), Tip 44
- Stay aware of what you're doing.
- Don't code blindfolded, meaning with an app or technology you don't understand.
- Proceed from a plan.
- Rely only on reliable (documented, guaranteed) things. If in doubt, assume the worst.
- Document your assumptions (contracts).
- Test assumptions as well as code, using assertions.
- Prioritize effort on the hard, important parts.
- Don't be a slave to history. Refactor when existing code no longer fits.

### A9. When to Refactor (p.185), Tip 47
- You discover a DRY violation.
- You find things that could be more orthogonal.
- Your knowledge improves.
- The requirements evolve.
- You need to improve performance.

### A10. Cutting the Gordian Knot (p.212), Tip 55
- Is there an easier way?
- Am I solving the right problem?
- Why is this a problem?
- What makes it hard?
- Do I have to do it this way?
- Does it have to be done at all?

### A11. Aspects of Testing (p.237), Tips 62–66
- Unit
- Integration
- Validation and verification
- Resource exhaustion, errors, and recovery
- Performance
- Usability
- Testing the tests themselves

## Part B — Derived operational checklists

### B1. Four kinds of duplication (§7, Tip 11)
| Kind | Cause | Detect | Remedy |
|---|---|---|---|
| **Imposed** | The environment seems to require it (multiple languages or platforms, docs next to code, headers) | The same schema or message format lives in two languages. Docs or tests are hand-maintained next to code. Comments restate code. | An *active* code generator from one source, run in every build. Comments explain *why*, never *how*. |
| **Inadvertent** | Design mistake | Stored derived fields (e.g. `length` next to `start`/`end`). The same fact is held by two entities. | Normalize, and compute derived values. A cache is allowed only if it's private, local, and invalidated in the setters (uniform access). |
| **Impatient** | Time-pressure shortcuts | Copy-paste-modify, repeated literals, vendored copies of library code | Extract, name constants, depend on the library instead of copying it. "Shortcuts make for long delays." |
| **Interdeveloper** | Multiple people unknowingly build the same thing | The same validation or utility shows up in several modules (e.g. many independent ID validators) | A clear owner per concern, a central utilities location, a librarian or focal points, code reading and review. |

### B2. Orthogonality probes (§8)
- **Requirement test:** if one requirement changes dramatically, how many modules change? Aim for one.
- **Unit-test footprint:** what must be built or linked to test this module? If the answer is "half the system", it's coupled.
- **Bug-fix footprint:** does fixing a bug touch one module, or many? Track files touched per fix in version control.
- **Real-world coupling:** does it depend on things you don't control (phone number as ID, locale, filesystem layout)?
- **Library intrusion:** does a toolkit force changes into your code that don't belong there?
- **Team test:** how many people must be involved to discuss one change?

### B3. Reversibility probes (§9, Tip 14)
- Is each third-party product (DB, queue, cloud SDK, LLM API) behind an interface you own?
- Is the deployment topology (monolith, client-server, services) a config or deploy decision, or is it baked into code?
- Can you list the plausible futures, and roughly what each would cost to support?

### B4. Design by Contract authoring (§21, Tip 31)
- **Preconditions:** what the caller must guarantee. The *caller* is responsible, so never use them to validate user input.
- **Postconditions:** what the routine guarantees on return, including termination.
- **Class invariants:** true whenever the object is observable from outside. They may break mid-method but must be restored before return. Don't expose unrestricted write access to invariant fields.
- **Lazy code:** be strict in what you accept and promise as little as possible.
- **Inheritance (LSP):** a subclass may weaken preconditions and strengthen postconditions, never the reverse.
- Contract expressions must be **side-effect-free**. Reference entry values (`old`/`@pre`) when a parameter may be mutated.
- **Loop invariants:** the generalized goal holds before the loop, after each iteration, and at exit. Use them to kill off-by-one errors.
- **Semantic invariants:** state inviolable business laws explicitly and publish them (e.g. "never apply a transaction twice; when in doubt, err toward not processing"). Keep laws distinct from changeable policies.

### B5. Crash early / assertions (§22–23, Tips 32–33)
- Every `switch`/`match` has a default that fails loudly on the "impossible" case.
- Check return values of close, write, flush, and commit calls.
- Assertion conditions have **no side effects** (e.g. an iterator advanced inside an assert). No required logic lives in asserts, because they may be compiled out (`-O`, `NDEBUG`).
- Assertions are not error handling for user input.
- Leave assertions on in production. Disable only the specific ones that are measurably expensive.
- When you must die, release resources and log, but don't trust the data that triggered the failure.
- "Impossible" things that happen anyway: leap seconds, calendar reforms, integer overflow, a directory deleted while in use, operator overloading.

### B6. Exceptions (§24, Tip 34)
- **Handler-removal test:** would normal-path code still work if every handler were deleted? If not, exceptions are being used for control flow.
- **Expected vs. exceptional:** a file that *must* exist → throw. A user-supplied path that may not exist → check and return an error value or Result.
- Don't scatter catch blocks. Wrap noisy APIs (e.g. remote calls) behind an error-handler layer.

### B7. Resource balancing (§25, Tip 35)
- The routine or object that allocates also deallocates, and pairs them visibly in one scope.
- Nested resources: deallocate in *reverse* order of allocation.
- Acquire the same set of resources (locks) in the *same order* everywhere, to prevent deadlock.
- Use scope-bound cleanup (RAII, `with`, `try-with-resources`, `using`, `defer`, `finally`) instead of duplicating cleanup on each path.
- Where balance is impossible (aggregates), pick an explicit ownership policy: free recursively, orphan, or refuse to free while children exist. Apply it consistently, and consider reference counting.
- **Check the balance:** assert that resource counts are stable at a loop checkpoint (e.g. the top of a request loop). Use leak tools.
- Null out references and pointers after release.

### B8. Post-fix checklist (§18)
- Why wasn't it caught earlier? Add or strengthen the test that would have caught it.
- Did bad data travel several layers? Add checks and assertions nearer the source.
- Does the same bug pattern exist elsewhere? Fix those now.
- Will you know if it happens again? Add a test, alerting, or tracing.
- Did it take long to find? Add hooks, log analyzers, or better tracing.
- Was it a wrong assumption? Tell the team, because others probably share it.

### B9. Test harness must-haves (§34, Tip 48)
Standard setup and teardown · run one test or all tests · automatic pass/fail analysis · standardized failure reporting · composable suites · tests discovered by convention (DRY: no hand-maintained test list) · tests live near the code · ad hoc debug probes promoted into permanent tests.

### B10. Test data (§43)
- **Real data:** reveals what "typical" actually means and exposes misunderstood requirements.
- **Synthetic data:** volume (seeded from real data, with unique fields tweaked), boundaries (invalid dates, huge records, foreign formats, empty, max), and statistical properties (every Nth fails, presorted input).

### B11. Requirements hygiene (§36, Tips 51–54)
- Is it a need, or a **policy**? Policies belong in metadata or config, linked from the requirement.
- Is it a need, or a **UI detail** ("a list box")? Or **architecture** ("front end plus back end")? Restate it as the need.
- Is the **why** captured?
- Is every domain term in the **glossary**? Watch for one thing with two names, and worse, two things with one name.
- Is scope creep **tracked**, with the requester, the approver, and the schedule impact of each addition?
- Are volatile representations (dates, currency, IDs, time zones) wrapped behind an abstraction?

### B12. Estimation (§13, Tip 18)
1. Understand what's being asked: the accuracy needed, and the scope assumptions (state them in the answer).
2. Build a model of the system or process.
3. Break it into components and find how they combine: additive, multiplicative, or queueing.
4. Give each parameter a value. Focus on the multiplicative or dividing ones, because they dominate.
5. Calculate several scenarios, and express the answer in terms of the critical parameters.
6. Track your record. When you're off by more than 50%, find out whether the parameters or the model were wrong.

**Units follow precision:**

| Duration | Quote in |
|---|---|
| 1–15 days | days |
| 3–8 weeks | weeks |
| 8–30 weeks | months |
| 30+ weeks | think hard before giving any single number |

### B13. Automation / one-command build (§42, Tip 61)
1. Check out from source control.
2. Build from scratch in a clean environment, stamping the version.
3. Produce the distributable in its exact ship format.
4. Run *all* tests.

Also:
- A separate release build that tags, sets flags, and is retested if its compile differs.
- Generated files are derived by the build and never hand-edited.
- Reports, docs, and dashboards are regenerated automatically. Stale info is worse than none.

### B14. Documentation (§44, Tips 67–68)
- Comments say *why* (purpose, trade-offs, rejected alternatives), never restate *how*.
- Names are meaningful and spelled out. **Misleading names are worse than meaningless ones.**
- No hand-maintained lists in comments (exported functions, revision history, file lists), because version control and tools do these.
- Keep one authoritative source and generate the rest (schema → DDL, structs, docs; source → API docs).
- Version or date-stamp published docs, and separate content from presentation.
