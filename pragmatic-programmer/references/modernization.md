# Modernization map (1st edition, 1999 → today)

**Rule:** keep the principle and translate the tool. Mark translated advice with `⟳ modern:`. Never recommend a deprecated API.

| Book mentions | Principle | Recommend today |
|---|---|---|
| RCS / CVS / SCCS, nightly builds | Tip 23, 61 | git, trunk-based development or short-lived branches, CI on every push, required checks |
| make, recursive make, Ant, CruiseControl, cron | Tip 61 | Make/just/Task, Gradle/Bazel/Nx, GitHub Actions/GitLab CI, scheduled pipelines |
| Perl / awk / sed as text tools | Tip 28 | Python, jq/yq, ripgrep, sed/awk still fine |
| emacs/vi/CRiSP/Brief | Tip 22 | Any configurable editor + LSP; learn its macros and extension API |
| Cygwin/UWIN on Windows | Tip 21 | WSL, Git Bash, PowerShell |
| CORBA, RMI, EJB deployment descriptors | Tips 13, 14, 37 | Service interfaces (gRPC/REST), adapters, DI containers, annotations, K8s manifests |
| JavaSpaces / T Spaces / Linda | Tip 43 | Event stores, Kafka, Redis streams, DB + triggers, workflow/rules engines |
| AWT event handling, Swing JTree MVC | Tip 42 | MVC/MVVM, reactive UIs, pub-sub buses |
| Eiffel DbC, iContract, Nana | Tip 31 | Type systems + boundary validation (pydantic, zod), icontract/deal, Kotlin `require`/`check`, C++26 contracts, Ada/SPARK, property tests |
| C `assert`, `NDEBUG` | Tip 33 | Same idea. Remember Python `-O` strips asserts, so required checks must be real code |
| `auto_ptr`, Java `finalize` | Tip 35 | `unique_ptr`/`shared_ptr`, try-with-resources, `with`, `using`, `defer`, Rust Drop |
| Purify, Insure++ | Tip 35 | ASan/LSan/Valgrind, heap profilers, FD counters |
| JUnit 3 `TestCase`, per-class `main()` tests | Tip 48 | pytest, JUnit 5, Jest/Vitest, Go test, cargo test |
| Hand-planted saboteur bugs | Tip 64 | Mutation testing tools |
| Code-coverage tools | Tip 65 | Coverage *plus* property-based and state-machine testing |
| Embedded diagnostics web server on port 8080 | §34 test window | Health/metrics endpoints, OpenTelemetry, structured logs, admin consoles |
| Wizards (MSVC AppWizard), CASE tools | Tip 50 | Framework scaffolders **and AI code assistants**. Same rule: understand every line |
| yacc/bison/javaCC | Tip 17 | Parser combinators, ANTLR, tree-sitter, or an internal DSL in the host language |
| .ini, Registry, X resources, Java properties | Tip 38 | TOML/YAML/JSON + schema validation, env vars, feature-flag services |
| DocBook, DSSSL, troff, Javadoc/DOC++ | Tips 67, 68 | Markdown/AsciiDoc, static site generators, OpenAPI/TypeDoc/Sphinx, doctests, ADRs |
| MD5 checksums for config tamper-detection | §14 | SHA-256 / HMAC signatures |
| Usenet, trade magazines | Tip 8 | Forums, Q&A sites, conference talks, OSS communities, meetups |
| 1999 language list (CLOS, Dylan, TOM, Sather…) | Tip 8 | Pick by paradigm gap: Rust, Haskell/OCaml, Elixir/Erlang, Prolog/Datalog, APL/array thinking, Zig, etc. |
| Y2K | Tips 11, 53 | Same lesson for time zones, currency, Unicode, 2038, ID formats |
| 56k modems, 64MB RAM, 4GB tapes | §13, §32 | Update magnitudes. The method still holds (e.g. "never underestimate the bandwidth of a truck of disks" → shipping drives to the cloud) |

## Ideas the 1999 text anticipates
When you use one of these connections, say it's your interpretation, not the book's text.
- *Dynamic contracts and agents* (§21) → contracts and schemas for autonomous software agents and LLM tool calls.
- *Test before code* (§34) → TDD.
- *Saboteurs* (§43) → mutation testing.
- *Tracer bullets* (§10) → walking skeleton / MVP.
- *Evil Wizards* (§35) → reviewing AI-generated code.
