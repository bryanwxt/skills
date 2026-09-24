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
| [software-design](software-design/) | Evaluates an existing app's design or designs a new one from scratch, using the complexity-reduction principles of John Ousterhout's *A Philosophy of Software Design* — deep modules, information hiding, red-flag review, design it twice. |
| [clean-python](clean-python/) | Designs, writes, reviews, and refactors Python code using the practices from Mariano Anaya's *Clean Code in Python* — Pythonic idioms, contracts and error handling, SOLID, decorators, descriptors, generators, pytest, and clean architecture. |
