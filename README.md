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
| [pyramid-deck](pyramid-deck/) | Builds a presentation end to end using Barbara Minto's Pyramid Principle — SCQA intro, tested pyramid, action-titled storyboard, speaker notes, then renders the deck. |
| [software-design](software-design/) | Design lens for [superpowers](https://github.com/obra/superpowers), based on John Ousterhout's *A Philosophy of Software Design* — adds deep-module, information-hiding, and red-flag judgment to brainstorming, planning, and code review, and runs architecture audits that hand off to brainstorming. Requires superpowers; see its [README](software-design/README.md). |
| [clean-python](clean-python/) | Python lens for [superpowers](https://github.com/obra/superpowers), based on Mariano Anaya's *Clean Code in Python* — adds Pythonic idioms, typing, error handling, pytest, and tooling checks to brainstorming, planning, TDD, verification, debugging, and code review, and reviews Python files outside a commit range. Requires superpowers; see its [README](clean-python/README.md). |
| [data-intensive](data-intensive/) | Designs, reviews, and debugs data-intensive systems using Martin Kleppmann's *Designing Data-Intensive Applications* — choosing databases and formats, replication, sharding, transactions and race conditions, distributed failures and consensus, batch/stream pipelines and CDC, incident diagnosis, and system-design interview practice. |
| [teaching-tech](teaching-tech/) | Designs, reviews, and delivers technical teaching using Greg Wilson's *Teaching Tech Together* (CC BY 4.0) — backward lesson design, personas, diagnostic MCQs, faded examples, live coding, workshops, online courses, tutoring, onboarding, inclusivity, and community building. Aligns intent by asking MCQs with recommended options. |
| [pragmatic-programmer](pragmatic-programmer/) | Reviews, debugs, tests, builds/refactors, designs, estimates, and coaches using Hunt & Thomas's *The Pragmatic Programmer* — routes to one of 8 modes, cites all 70 tips and 11 checklists, returns ranked findings with options and patches, and translates 1999-era tooling to modern equivalents. |

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

