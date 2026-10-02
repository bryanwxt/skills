# Teaching Tech Together: skill reference set

A complete reference of Greg Wilson's *Teaching Tech Together* (Lulu.com, 2018, ISBN 978-0-9881137-0-1, http://teachtogether.tech/), organized for building Claude skills. It covers all 16 chapters and every appendix: every practice, rule of thumb, procedure, research finding (with its citation key), template, checklist, and end-of-chapter exercise. The goal is that a skill author never needs to reopen the book.

This is source material, not a skill. Start with **`skill-blueprint.md`**.

## License and attribution

*Teaching Tech Together* © Greg Wilson and contributors, licensed under **CC BY 4.0** (https://creativecommons.org/licenses/by/4.0/).

- **Condensed:** the chapter files are condensed and restructured for skill use, with quotations marked.
- **Verbatim:** the glossary entries marked "book glossary", the bibliography, and the templates labelled verbatim (Code of Conduct, rubrics, checklists, pre-assessment questionnaire, cold-email template) are reproduced word for word.
- **Not covered by the licence:** Figure 8.1 (© Deathbulge 2013) and Figure 7.3 (third-party Scratch screenshot) are described, not reproduced.

## Layout

```
teaching-tech-together/
├── README.md
├── skill-blueprint.md          # how to turn this into skills: candidates, loading map, open decisions, relation to existing skills
├── scripts/
│   └── build_rule_index.py     # regenerate the rule index after editing chapter files
└── references/
    ├── 00-book-map.md                          # chapters, appendices, figures → files
    ├── 01-introduction-and-motivation-to-teach.md   WHY  Ch 1, Ch 16
    ├── 02-mental-models.md                     MOD  Ch 2
    ├── 03-expertise-and-memory.md              MEM  Ch 3
    ├── 04-cognitive-load.md                    COG  Ch 4
    ├── 05-individual-learning.md               IND  Ch 5, App K Teamwork Rubric
    ├── 06-lesson-design.md                     LES  Ch 6, App H Template, App M Design Notes
    ├── 07-programming-pck.md                   PCK  Ch 7, App G Notional Machines
    ├── 08-teaching-as-performance.md           PRF  Ch 8, App J Presentation Rubric
    ├── 09-in-the-classroom.md                  CLS  Ch 9, App I Event Checklists, App L Pre-Assessment
    ├── 10-motivation-and-inclusion.md          MOT  Ch 10, App D Code of Conduct
    ├── 11-teaching-online.md                   ONL  Ch 11
    ├── 12-exercise-types.md                    EXR  Ch 12 (25-type catalog)
    ├── 13-building-community.md                COM  Ch 13, App C Joining, App F Meetings
    ├── 14-marketing.md                         MKT  Ch 14
    ├── 15-partnerships.md                      PTN  Ch 15
    ├── rules-and-checks.md     # core on one page, 4 review checklists, all 384 rules
    ├── workflows.md            # router + 10 end-to-end flows plus a programming overlay
    ├── diagnostics.md          # 265 symptom → problem → fix rows, grouped by area
    ├── glossary.md             # 110 book-glossary terms (verbatim) + 57 more
    ├── bibliography.md         # 343 annotated entries (verbatim) for resolving citation keys
    └── eval-scenarios.md       # 18 baseline scenarios + trigger tests
```

About 150k words in total. The chapter files are 4.5–12k words each.

## How the files fit together

- **Chapter files** (`01`–`15`) are the source of truth. They share one template: *When a skill needs this* → *Key terms* → *Concepts* (one subsection per book section) → *Rules* → *Procedures* → *Diagnostics* → *Templates and checklists* → *Examples* → *Evidence and caveats* → *Practice exercises* → *Cross-references* → *Source map*.
- **Rules** have stable IDs (`PFX-n`, 15 prefixes, 384 rules). Each states the rule, *Why* (the rationale or evidence), *Check* (how an agent tests a lesson, plan, or practice), and the section. Cite the IDs in derived skills.
- **Citations** use the book's own keys (e.g. `[Mill1956]`). `bibliography.md` resolves them; all 267 keys used resolve.
- **Practice exercises:** every end-of-chapter teacher-training exercise is summarized. They make good eval tasks and workshop activities.
- **`> Skill note:` blocks** mark the readers' interpretations. Everything else reports what the book says, including Wilson's hedges and the myths he debunks.

## Source notes

- **Edition and section numbers:** EPUB dated 2018-07-16. It has no page numbers, so files cite §chapter.section or appendix letter. Appendix letters follow the book: A License … M Design Notes.
- **Figures:** read from the image files. The data in Figures 7.4 and 10.2 is read off the image and approximate; Figures 7.1, 7.2 and 11.1 were reconstructed from their SVG sources.
- **Errors in the book itself:** a systematic "exercise"-for-"challenge" word swap, some mistyped citation keys, a few garbled sentences, and wrong section pointers. Each is flagged in the relevant file; the important ones are listed in `skill-blueprint.md` §6.

## Maintenance

```bash
python3 scripts/build_rule_index.py
```

Regenerates Part 3 of `rules-and-checks.md` after you edit rules. Parts 1–2 are hand-written.
