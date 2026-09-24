# Red flags: how to detect and fix them

Each red flag is a symptom of a design problem. Its presence doesn't prove a problem, but it demands an explanation. For each: what it is, how to find it in real code, and the usual fix.

## Contents
- Structure: shallow module, information leakage, temporal decomposition, overexposure, pass-through method, pass-through variable, repetition, special-general mixture, conjoined methods, too many exceptions, config parameter sprawl
- Documentation and naming: comment repeats code, implementation contaminates interface, vague name, hard-to-pick name, hard to describe, nonobvious code
- Process: tactical drift

---

## Structure

### Shallow module
The interface isn't much simpler than the implementation.
- **Detect:** classes whose methods are mostly one-liners delegating elsewhere; many tiny classes each needing to be learned; wrappers that only rename; APIs that need several calls in a fixed sequence to do one ordinary thing. Compare the number of public methods, parameters, and exceptions against lines of real logic.
- **Fix:** merge shallow pieces into a module with a smaller, intent-level interface. Hide the sequencing. Give it defaults.

### Information leakage
One design decision is reflected in more than one module.
- **Detect:** the same file format, schema, protocol detail, magic constant, or data-structure assumption appearing in several modules; a change history where two files always change together (`git log` co-change); modules that must "agree" on something no interface expresses.
- **Fix:** move the knowledge into a single module that owns it — either merge the modules or extract a new one that encapsulates the decision.

### Temporal decomposition
Modules are split by when things happen, not by what they know.
- **Detect:** modules named after phases (`Reader`, `Parser`, `Processor`, `Writer`, `Step1Handler`) that each need to understand the same format or data; pipeline stages that pass rich intermediate structures around.
- **Fix:** regroup by knowledge. E.g. one module that both reads and writes a file format, rather than a reader and a writer that each understand it.

### Overexposure
An API forces users to learn about rarely used features to use common ones.
- **Detect:** constructors or functions with many parameters most callers leave at the same value; required setup for options almost nobody changes; "you must also create X and pass it to Y" for the common path.
- **Fix:** defaults for the common case; separate advanced methods or options objects for the rare case.

### Pass-through method
A method does little except call another method with a similar signature.
- **Detect:** chains like `Controller.save(x)` → `Service.save(x)` → `Repository.save(x)` where each layer adds nothing; interface methods that mirror a lower layer one-for-one.
- **Fix:** let callers use the lower layer directly, move functionality so each layer does real work, or merge the layers.

### Pass-through variable
A value threaded through many methods that don't use it, just to reach one deep method.
- **Detect:** a parameter that appears in a long call chain but is only read at the bottom.
- **Fix:** a context object (created once, reachable from where it's needed), or restructure so the consumer can obtain the value directly. Keep the context disciplined — it's not a dumping ground.

### Repetition
A nontrivial piece of code appears again and again.
- **Detect:** copy-pasted blocks, the same validation or error-handling pattern at many call sites, near-identical functions differing by a constant.
- **Fix:** find the right abstraction that removes the need — often a deeper helper, or a change in a lower module's semantics so callers don't need the repeated code at all.

### Special-general mixture
General-purpose mechanisms contain code specific to one use.
- **Detect:** a generic library or core class that checks for particular feature flags, UI concepts, customer names, or one caller's special case; `if (type == ...)` branches inside shared utilities.
- **Fix:** keep the general mechanism general and move specialization up into the caller, or down into a plug-in implementation behind a general interface.

### Conjoined methods
Two methods (or classes) can't be understood without reading each other.
- **Detect:** you keep jumping between two functions to understand either one; a function that only makes sense given state set up by another; one method split into "part 1" and "part 2".
- **Fix:** merge them, or re-cut the split so each piece is a complete, independently understandable abstraction.

### Too many exceptions / special cases
- **Detect:** many custom exception types in a public interface; callers wrapping every call in try/catch; defensive checks for conditions that could have been defined as normal behaviour; `if` statements for edge cases scattered across callers.
- **Fix:** define errors out of existence by changing semantics; mask at a low level; aggregate handling in one place; or crash for rare unrecoverable errors. See principles.md §9.

### Configuration parameter sprawl
- **Detect:** many config knobs, especially ones that need expert tuning or that no one knows how to set; config passed through many layers.
- **Fix:** have the module compute sensible values itself (measure, adapt), provide good defaults, and remove knobs nobody uses.

## Documentation and naming

### Comment repeats code
All the information in the comment is obvious from the code next to it.
- **Detect:** `// increment i` style comments; comments that restate the method name in sentence form; generated docstrings with no added information.
- **Fix:** replace with what the code can't say — units, invariants, rationale, the abstraction.

### Implementation contaminates interface
An interface comment describes how something works instead of what callers need.
- **Detect:** public docs that mention internal data structures, helper classes, or algorithm steps.
- **Fix:** move implementation notes inside the implementation; keep the interface comment to behaviour, arguments, results, side effects, and preconditions.

### Vague name
- **Detect:** names like `data`, `info`, `obj`, `result`, `tmp`, `manager`, `handler`, `process()`, `doWork()`, `flag`, `status` used beyond a tiny scope; the same name meaning different things in different places; different names for the same concept.
- **Fix:** rename to something precise that creates an image of the thing; enforce one name per concept.

### Hard to pick a name
- **Detect:** you (or the code's author) struggled to name something; names with "And" or "Or"; names that need a long qualifier.
- **Fix:** treat as a design signal. The entity probably does too much or isn't a coherent concept — re-cut it.

### Hard to describe
The documentation for a method or variable must be long to be complete.
- **Detect:** interface comments with many caveats and exceptions; parameters whose meaning depends on other parameters.
- **Fix:** simplify the abstraction until a short description is complete.

### Nonobvious code
Behaviour or meaning can't be understood quickly.
- **Detect:** readers' first guesses are wrong; event handlers with no indication of what triggers them; tuples/pairs with meaning encoded in position; declared types that hide the real type; surprising side effects.
- **Fix:** better names, named structs over generic containers, comments that fill the gap, and code that follows reader expectations.

## Process

### Tactical drift
- **Detect:** workarounds commented "temporary" or "hack" that became permanent; each new feature adding another flag to a shared function; a codebase where nobody refactors because "it works".
- **Fix:** adopt a continual-investment rule: when touching code, leave its design better; budget roughly 10–20% of effort for design improvement.
