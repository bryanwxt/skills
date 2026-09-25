# skills

A collection of Claude skills by Bryan.

Each skill lives in its own folder:

```
skill-name/
├── SKILL.md        # frontmatter (name, description) + instructions
├── scripts/        # optional helper scripts
└── references/     # optional reference docs
```

## Skills

| Skill | What it does |
|---|---|
| [crafting-presentations](crafting-presentations/) | Gated, superpowers-style process for any presentation — classifies it as Decide, Inform, Teach, or Talk, then runs brief → storyline → storyboard → build → fresh-eyes review → rehearsal, with the storyline as a hard approval gate. Uses Minto's *Pyramid Principle* for arguments and Wilson's *Teaching Tech Together* for lessons. |
| [software-design](software-design/) | Design lens for [superpowers](https://github.com/obra/superpowers), based on John Ousterhout's *A Philosophy of Software Design* — adds deep-module, information-hiding, and red-flag judgment to brainstorming, planning, and code review, and runs architecture audits that hand off to brainstorming. Requires superpowers; see its [README](software-design/README.md). |
| [clean-python](clean-python/) | Python lens for [superpowers](https://github.com/obra/superpowers), based on Mariano Anaya's *Clean Code in Python* — adds Pythonic idioms, typing, error handling, pytest, and tooling checks to brainstorming, planning, TDD, verification, debugging, and code review, and reviews Python files outside a commit range. Requires superpowers; see its [README](clean-python/README.md). |
| [data-intensive](data-intensive/) | Data-systems lens for [superpowers](https://github.com/obra/superpowers), based on Martin Kleppmann's *Designing Data-Intensive Applications* — a data track for designing architectures from scratch in brainstorming, brainstorming-style technology choices and data architecture/incident reviews, and data checks (races, idempotency, migrations, dual writes) in planning, TDD, verification, debugging, and code review. Requires superpowers; see its [README](data-intensive/README.md). |
| [pragmatic-programmer](pragmatic-programmer/) | Reviews, debugs, tests, builds/refactors, designs, estimates, and coaches using Hunt & Thomas's *The Pragmatic Programmer* — routes to one of 8 modes, cites all 70 tips and 11 checklists, returns ranked findings with options and patches, and translates 1999-era tooling to modern equivalents. |

## Using the superpowers lenses together

`software-design`, `clean-python` and `data-intensive` are lenses for [superpowers](https://github.com/obra/superpowers). Superpowers runs the process; each lens supplies judgment in its own lane (module design / Python / data systems). When several are active at once, a shared **`references/coordination.md`** (identical in each lens; read once per session) sets:

- one question budget and order for brainstorming;
- which lens sets the axis for comparing approaches;
- a merged spec outline;
- one plan order;
- the test-double rule (real database for correctness tests, fakes for external services);
- one combined check for small changes;
- joint reviews.

The three copies must stay identical. Check with:

```bash
scripts/check-coordination.sh
```

## References (third-party)

Not my skills — included as read-only references via git submodule.

| Reference | License | What it is |
|---|---|---|
| [obra/superpowers](https://github.com/obra/superpowers) → [`vendor/superpowers`](vendor/superpowers) | MIT © Jesse Vincent | An agentic skills framework for Claude Code: brainstorming, planning, TDD, systematic debugging, code review, subagent-driven development, and more. |

Clone with submodules:

```bash
git clone --recurse-submodules https://github.com/bryanwxt/skills.git
# or, in an existing clone:
git submodule update --init
```

Update the reference to its latest version:

```bash
git submodule update --remote vendor/superpowers && git commit -am "Update superpowers reference"
```

To *use* superpowers in Claude Code, install it as a plugin from [obra/superpowers-marketplace](https://github.com/obra/superpowers-marketplace) rather than from this folder.

