# Tips catalogue

This paraphrases each tip. Columns: **§** is the book section. **Related** lists tips that reinforce it; the book presents the tips as a pattern language, so cite related tips when they strengthen a finding. **Signal** is what to look for in the user's work. **⟳** is the modern translation, where one applies.

## Ch 1: A Pragmatic Philosophy
| # | Tip | § | Related | Signal / how to apply | ⟳ |
|---|---|---|---|---|---|
| 1 | Care About Your Craft | Pref | 70 | Is there visible care, or just "it compiles"? | |
| 2 | Think! About Your Work | Pref | 44 | Autopilot patterns: copy-paste, cargo-cult config | |
| 3 | Provide Options, Don't Make Lame Excuses | 1 | 24 | "Can't be done" or "not my fault" → list what *can* be done | |
| 4 | Don't Live with Broken Windows | 2 | 47, 6 | Tolerated TODOs, warnings, flaky tests, dead code. Fix it or board it up. | Treat lint/CI warnings and flaky tests as broken windows |
| 5 | Be a Catalyst for Change | 3 | 15 | Blocked on approval → build a small working slice first | |
| 6 | Remember the Big Picture | 3 | 4 | Gradual scope, performance, or quality drift nobody has flagged | Track trends with dashboards and SLOs |
| 7 | Make Quality a Requirements Issue | 4 | 69 | Gold-plating, or cutting engineering corners → agree "good enough" with users | |
| 8 | Invest Regularly in Your Knowledge Portfolio | 5 | 9 | Stagnant skills; learning with no plan | |
| 9 | Critically Analyze What You Read and Hear | 5 | 58, 59 | Hype-driven technology choices | |
| 10 | It's Both What You Say and the Way You Say It | 6 | 67 | Doc, PR, or status aimed at the wrong audience → WISDOM | |

## Ch 2: A Pragmatic Approach
| # | Tip | § | Related | Signal / how to apply | ⟳ |
|---|---|---|---|---|---|
| 11 | DRY | 7 | 29, 38, 68 | The same *knowledge* in two or more places (checklist B1) | Schema-first codegen (OpenAPI, protobuf); single source for config |
| 12 | Make It Easy to Reuse | 7 | 11 | People rewrite because finding or using the existing code is hard | Internal packages, discoverable docs |
| 13 | Eliminate Effects Between Unrelated Things | 8 | 36, 42, 60 | Changes ripple; big test footprint; globals (B2) | DI, hexagonal/ports-and-adapters |
| 14 | There Are No Final Decisions | 9 | 37, 53 | Vendor calls everywhere; topology baked into code | Adapters, feature flags, IaC |
| 15 | Use Tracer Bullets to Find the Target | 10 | 16, 19 | Big-bang integration; "95% done" for weeks | Walking skeleton / vertical slice with CI from day 1 |
| 16 | Prototype to Learn | 11 | 15, 56 | A risky unknown with no spike; or a prototype shipped as product | Spikes, notebooks, Figma |
| 17 | Program Close to the Problem Domain | 12 | 54 | Names or structures that don't match the domain; rules repeated in code | Internal DSLs, YAML rule files, embedded Lua/Python |
| 18 | Estimate to Avoid Surprises | 13 | 45 | Commitments made without a model | |
| 19 | Iterate the Schedule with the Code | 13 | 15 | A fixed schedule never revisited | Rolling-wave / per-sprint re-forecast |

## Ch 3: The Basic Tools
| # | Tip | § | Related | Signal / how to apply | ⟳ |
|---|---|---|---|---|---|
| 20 | Keep Knowledge in Plain Text | 14 | 11, 23 | Opaque binary config; meaningless keys (`field19`) | JSON, YAML, TOML, CSV; golden-file tests. Use a secure hash (SHA-256/HMAC), not MD5, for tamper checks |
| 21 | Use the Power of Command Shells | 15 | 61 | "Click here, then there" instructions | bash/zsh, PowerShell, WSL |
| 22 | Use a Single Editor Well | 16 | | Slow, repetitive manual editing | VS Code, JetBrains, Vim/Neovim, Emacs with LSP; macros; multi-cursor |
| 23 | Always Use Source Code Control | 17 | 61 | Anything not versioned: scripts, docs, infrastructure, prompts | git; `git blame`/`log`/`bisect`; IaC in the repo |
| 24 | Fix the Problem, Not the Blame | 18 | 3 | Blame in a postmortem or review | Blameless postmortems |
| 25 | Don't Panic When Debugging | 18 | 27 | "That's impossible" | |
| 26 | "select" Isn't Broken | 18 | 27 | Blaming the compiler, OS, or library first | Minimal repro before filing upstream |
| 27 | Don't Assume It — Prove It | 18 | 33, 44 | Untested "known good" code | |
| 28 | Learn a Text Manipulation Language | 19 | 21, 29 | Manual bulk edits or data wrangling | Python, jq, ripgrep, sed/awk |
| 29 | Write Code That Writes Code | 20 | 11, 50 | Hand-mirrored structures; generated files edited by hand | Codegen in the build (protobuf, OpenAPI, sqlc, ORMs); scaffolding (passive) |

## Ch 4: Pragmatic Paranoia
| # | Tip | § | Related | Signal / how to apply | ⟳ |
|---|---|---|---|---|---|
| 30 | You Can't Write Perfect Software | 4 intro | 31–35 | Code that trusts every input and every call | |
| 31 | Design with Contracts | 21 | 33, 48 | Unstated pre/postconditions; subclasses weakening contracts (B4) | Type hints plus runtime checks (icontract/deal, zod/pydantic at boundaries), Kotlin `require`/`check`, Ada/SPARK, property tests |
| 32 | Crash Early | 22 | 33 | Swallowed errors; continuing after corruption | Fail-fast; supervisors ("let it crash"); `set -euo pipefail` |
| 33 | Use Assertions to Prevent the Impossible | 23 | 27, 31 | "Can't happen" comments; asserts with side effects (B5) | |
| 34 | Use Exceptions for Exceptional Problems | 24 | 32 | Exceptions used as control flow (handler-removal test) | Result/Option types, Go error values |
| 35 | Finish What You Start | 25 | 36 | Leaks; open and close in different functions; inconsistent lock order (B7) | RAII, `with`, `using`, `defer`, try-with-resources, Rust Drop; ASan/Valgrind. Not `finalize`/`auto_ptr` |

## Ch 5: Bend, or Break
| # | Tip | § | Related | Signal / how to apply | ⟳ |
|---|---|---|---|---|---|
| 36 | Minimize Coupling Between Modules | 26 | 13 | Train wrecks; fear of change; huge test builds (A7). Deliberate, documented coupling for performance is acceptable. | Also applies to service call chains |
| 37 | Configure, Don't Integrate | 27 | 14, 38 | Technology choice hard-wired | Config-selected adapters, env-driven DI |
| 38 | Put Abstractions in Code, Details in Metadata | 27 | 11, 17 | Business policies hard-coded (periods, thresholds, roles) | Feature flags, rules files, hot-reloadable config (validated and versioned) |
| 39 | Analyze Workflow to Improve Concurrency | 28 | 41 | Needlessly serial steps | DAG/workflow engines, async pipelines |
| 40 | Design Using Services | 28 | 13, 41 | Monolith where independent units would be simpler | Queues plus workers, actors (not necessarily microservices) |
| 41 | Always Design for Concurrency | 28 | 40 | Hidden static state; constructor + `init()`; call-order dependencies | Immutable data, per-instance state |
| 42 | Separate Views from Models | 29 | 13, 48 | Logic in UI or controllers; one handler for every event | MVC/MVVM, pub-sub, event buses, Kafka |
| 43 | Use Blackboards to Coordinate Workflow | 30 | 38, 42 | Out-of-order multi-source facts wired point-to-point | Event store, shared DB + triggers, Redis, rules engines |

## Ch 6: While You Are Coding
| # | Tip | § | Related | Signal / how to apply | ⟳ |
|---|---|---|---|---|---|
| 44 | Don't Program by Coincidence | 31 | 27, 50 | "Works, not sure why"; shotgun calls; reliance on undocumented behavior or context (A8) | |
| 45 | Estimate the Order of Your Algorithms | 32 | 46 | Unbounded n in nested loops | |
| 46 | Test Your Estimates | 32 | 45 | Optimizing without measurement | Profilers, benchmarks (pytest-benchmark, JMH, criterion) |
| 47 | Refactor Early, Refactor Often | 33 | 4, 48 | Growing smells; refactor mixed with features (A9) | IDE automated refactoring |
| 48 | Design to Test | 34 | 31, 42 | Untestable without the UI or DB | TDD, contract tests |
| 49 | Test Your Software, or Your Users Will | 34 | 62 | Users find the bugs | |
| 50 | Don't Use Wizard Code You Don't Understand | 35 | 44 | Unread scaffolding, **AI-generated code** | Applies to LLM output: understand every line before committing |

## Ch 7: Before the Project
| # | Tip | § | Related | Signal / how to apply | ⟳ |
|---|---|---|---|---|---|
| 51 | Don't Gather Requirements — Dig for Them | 36 | 52, 53 | Requirements that are really policy, UI, or architecture (B11) | |
| 52 | Work with a User to Think Like a User | 36 | 51 | Developers never see real usage | User shadowing, support rotations |
| 53 | Abstractions Live Longer than Details | 36 | 14 | Raw dates, currency, or IDs scattered through the code | Value objects, `java.time`, Money types |
| 54 | Use a Project Glossary | 36 | 17 | Synonyms and homonyms in docs and code | Ubiquitous language (DDD) |
| 55 | Don't Think Outside the Box — Find the Box | 37 | 3 | Stuck; assumed constraints (A10) | |
| 56 | Start When You're Ready | 38 | 16 | Nagging doubt → spike the hardest part | |
| 57 | Some Things Are Better Done than Described | 39 | 15 | Spec spiral | |
| 58 | Don't Be a Slave to Formal Methods | 40 | 9 | Process adopted wholesale | |
| 59 | Costly Tools Don't Produce Better Designs | 40 | 9 | "The diagram is the app" | |

## Ch 8: Pragmatic Projects
| # | Tip | § | Related | Signal / how to apply | ⟳ |
|---|---|---|---|---|---|
| 60 | Organize Teams Around Functionality | 41 | 13 | Role silos; two teams in one module | Stream-aligned teams |
| 61 | Don't Use Manual Procedures | 42 | 21, 23 | Manual build, deploy, or release steps (B13) | CI/CD (GitHub Actions etc.), Makefile/justfile, IaC |
| 62 | Test Early. Test Often. Test Automatically. | 43 | 48 | Tests not in CI | |
| 63 | Coding Ain't Done 'Til All the Tests Run | 43 | 62 | Merging with red or skipped tests | Required status checks |
| 64 | Use Saboteurs to Test Your Testing | 43 | 65 | Tests never proven to fail | Mutation testing (mutmut, Stryker, PIT, cargo-mutants) |
| 65 | Test State Coverage, Not Code Coverage | 43 | 31 | Coverage percentage used as the goal | Property-based testing |
| 66 | Find Bugs Once | 43 | 62 | Fixed bugs with no regression test | |
| 67 | English Is Just a Programming Language | 44 | 11, 10 | Docs duplicated, drifting, or hand-formatted | Docs-as-code, Markdown/AsciiDoc + static site generators |
| 68 | Build Documentation In, Don't Bolt It On | 44 | 29 | Docs written separately that go stale | Generated API docs, doctests, ADRs in the repo |
| 69 | Gently Exceed Your Users' Expectations | 45 | 7 | Meets the spec but disappoints users | |
| 70 | Sign Your Work | 46 | 1 | Anonymous sloppiness, or territorial fiefdoms | CODEOWNERS plus shared review |
