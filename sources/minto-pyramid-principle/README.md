# Minto Pyramid Principle: skill reference set

A complete, paraphrased reference of Barbara Minto's *The Minto Pyramid Principle: Logic in Writing, Thinking and Problem Solving* (expanded edition; preface dated London 1996), organized for building Claude skills. It covers all four parts and all three appendices. It is meant to be complete enough that a skill author never needs to reopen the book: every chapter's ideas, rules, procedures, diagnostics, patterns, and exhibits are here, with page citations.

This is source material, not a skill. Start with **`skill-blueprint.md`**.

## Layout

```
minto-pyramid-principle/
├── README.md
├── skill-blueprint.md          # how to turn this into skills: shapes, loading map, open decisions, evals
├── scripts/
│   ├── build_rule_index.py     # regenerate the rule index after editing chapter files
│   └── check_overlap.py        # flag verbatim runs against the book's text layer
└── references/
    ├── 00-book-map.md          # chapter → pages → file; exhibit locator; source-scan notes
    ├── 01-pyramid-fundamentals.md      PYR  Preface, Part One intro, Ch 1–2
    ├── 02-building-the-pyramid.md      BLD  Ch 3
    ├── 03-introductions.md             INT  Ch 4
    ├── 03b-introduction-patterns.md    PAT  Ch 4 patterns + Appendix B (28-pattern catalog)
    ├── 04-deduction-and-induction.md   DED  Ch 5
    ├── 05-logical-order.md             ORD  Part Two intro, Ch 6
    ├── 06-summarizing-grouped-ideas.md SUM  Ch 7
    ├── 07-defining-the-problem.md      DEF  Part Three intro, Ch 8
    ├── 08-structuring-the-analysis.md  ANL  Ch 9
    ├── 09-abduction.md                 ABD  Appendix A
    ├── 10-pyramid-on-the-page.md       PAG  Part Four intro, Ch 10
    ├── 11-pyramid-on-screen.md         SCR  Ch 11
    ├── 12-pyramid-in-prose.md          PRO  Ch 12
    ├── rules-and-checks.md     # core on one page, 10-pass review checklist, Appendix C paraphrase, all 295 rules
    ├── workflows.md            # router + end-to-end flows (WF1–WF8) stitched from the chapter procedures
    ├── diagnostics.md          # the most common faults by document region: symptom → problem → fix
    ├── glossary.md             # 120 terms
    └── eval-scenarios.md       # 16 baseline scenarios + trigger tests for RED-phase testing
```

Size: about 134k words in total. The chapter files run 4–16k words each, and the cross-cutting files 1.6–11k.

## How the files fit together

- **Chapter files** (`01`–`12`) are the source of truth. Each follows the same template: *When a skill needs this* → *Key terms* → *Concepts* (one subsection per book subsection) → *Rules* → *Procedures* → *Diagnostics* → *Templates and patterns* → *Worked examples* (exhibit skeletons) → *Nuances and exceptions* → *Cross-references* → *Source map*.
- **Rules** have stable IDs (`PFX-n`, 13 prefixes, 295 rules). Each states the rule, *Why* (the author's rationale), *Check* (how an agent tests a draft), and the page. Cite IDs in any skill built from this, so condensed text can be traced back.
- **Cross-cutting files** sequence and index the chapter files; they add no new book content. `workflows.md` is the operational spine, `rules-and-checks.md` the review spine.
- **`> Skill note:` blocks** in the chapter files mark interpretation or invented examples. Everything else reports what the book says.

## Source fidelity

- **Missing pages:** book pp. 34–35 (the opening of Ch. 4, "The Story Form", and the start of "Why a Story?", including Exhibit 9) are absent from the scanned PDF. `03-introductions.md` reconstructs them from the rest of the book only and labels them "reconstructed".
- **Out-of-order pages:** book pp. 164–167 (end of Ch. 9) are bound at the back of the PDF. They were read in their proper place.
- **OCR:** the text layer is noisy, so every exhibit and diagram was read from rendered page images.
- **Internal inconsistencies** in the book (group-size limits, rule numbering, question lists, exhibit mislabels, figures) are recorded in each chapter file's *Nuances* section. The ones a skill must resolve are collected in `skill-blueprint.md` §6.
- **Readings marked uncertain by the readers** (all minor):
  - Exhibit 4's step numbering (p. 22)
  - Exhibits 40, 41, 44, and 52 in Ch. 9 (rotated, dense, or cropped diagrams)
  - Exhibit 69's small chart drawings (p. 201)
  - the Roman-numeral numbering scheme on p. 179
  - the mapping of Exhibit 11's examples to question types

## Paraphrase and licensing

The book is copyrighted. Everything here is paraphrased:

- Book examples are reduced to their structure or replaced with invented examples of the same shape.
- Pronouns for the reader are neutral.
- `scripts/check_overlap.py` was run on every file against the book's text layer. No run of ten or more words matches, except chapter and subsection titles.

Rerun it on anything you condense from these files. Whether to commit these notes to a public repo is your call. Skills built from them should ship condensed references, as `crafting-presentations` does.

## Maintenance

```bash
python3 scripts/build_rule_index.py
```

Regenerates Part 4 of `rules-and-checks.md` after rule edits. Parts 1–3 are hand-written.

```bash
python3 scripts/check_overlap.py book.txt 10 references/*.md
```

Re-checks the paraphrase. The script's docstring shows how to extract `book.txt` with pypdf.
