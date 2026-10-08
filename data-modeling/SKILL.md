---
name: data-modeling
description: 'Use when creating, reading, or reviewing a data model: conceptual, logical or physical; relational or dimensional (star schema); or a NoSQL/document design derived from one. Covers eliciting concepts and business rules, writing definitions, entities, attributes, domains, relationships and cardinality, keys (candidate, primary, alternate, surrogate, foreign), normalization to 3NF, abstraction trade-offs, dimensional modeling (grain matrix, meters/facts, dimension types, SCDs), physical design (denormalization, subtype rolldown/rollup, indexes, partitioning, views), requirements templates, and scoring model quality with the 10-category Data Model Scorecard. Based on Steve Hoberman''s "Data Modeling Made Simple" (2nd ed.).'
---

# Data Modeling Made Simple

**The book's lens.** A data model is a **wayfinding tool**: a set of symbols and text that precisely explains a slice of the information landscape. It has two jobs:
- **communication**, both while building it (the debates teach everyone) and after (a reusable map)
- **precision**: every symbol and term has exactly one reading

Data modeling is mostly **asking business questions**. The diagram is the record of the answers. There's no good model independent of its purpose. Quality means fitness for purpose, judged by how much the model contributes to the project.

## Pick the mode

**Create a model**
1. **Set the four "camera settings"** and the level (`levels.md`):
   - **scope:** department or project, organization or program, industry
   - **abstraction:** business clouds, database clouds, on the ground
   - **time:** as-is or to-be
   - **function:** business view or application view
   - **level:** conceptual, logical or physical
   - **mindset:** relational (business rules) or dimensional (business questions)
2. **Build the conceptual model** with the five-step approach (`process.md`):
   1. the five strategic questions
   2. identify and define concepts (who, what, when, where, why, how)
   3. capture relationships (the eight questions), or build a grain matrix for analytics
   4. choose the most useful form for the audience
   5. review and confirm
3. **Build the logical model:** add attributes, normalize to 3NF by asking the business, abstract only where flexibility is really needed, and define everything. For analytics, build meters, dimensions and hierarchies at a stated grain.
4. **Build the physical model:** apply the minimum compromises the technology needs (denormalize, collapse subtypes, index, partition, views) and record why.
5. **Score it** with the Scorecard before handing it over (`scorecard.md`).

**Review a model.** Use `scorecard.md`. Score all ten categories, list strengths as well as fixes, and be a strict grader. Read every relationship aloud as a sentence; it's the fastest way to find errors.

## Quick rules (no references needed)

- **Read every relationship in both directions:** "Each A {may/must} *verb* {one / one or many} B." *May* means zero is allowed; *must* means at least one. Start from the parent (the "one" side).
- **Labels are verbs that carry meaning:** contain, own, place, work for, categorize. Never use *has, have, associate, relate, participate, be* on their own.
- **Precision dies three ways:** weak definitions, dummy data (e.g. "ZZ = unknown country", fake phone numbers that sidestep a mandatory rule), and vague or missing labels.
- **Entities are nouns, not processes.** "Manufacturing" isn't an entity; Raw Material, Finished Good, Machine and Production Schedule are.
- **Candidate keys must be unique, mandatory, non-volatile (stable) and minimal.** When choosing the primary key, prefer the more succinct one with no sensitive data, because primary keys spread as foreign keys.
- **Surrogate key ⇒ always declare the natural (business) key as an alternate key.**
- **Normalization in one sentence:** every attribute is single-valued (1NF) and provides a fact about the key, completely (2NF) and only (3NF). Remove derived attributes from the logical model.
- **Abstraction has a price:** you lose communication (concepts become rows), business rules (now enforced in code), and simplicity of development. Use it only when new types are really expected.
- **Data rules go on the model; action rules don't.** Cardinality and referential integrity belong on the model. "Freshmen may take at most 18 credits" belongs in code or rules.
- **Conceptual model = one page, ~20 concepts, each basic and critical to *this* audience.** Many-to-many relationships are fine at this level.
- **Get definitions agreed at the conceptual level.** "Does Customer include prospects?" has to be settled before any attribute work.
- **Dimensional ≠ relational:** in a dimensional model, relationship lines are *navigation paths*, not rules. Never mix the two mindsets in one model without saying so.
- **The physical model is the logical model compromised for a technology.** Every compromise needs a reason (speed, space, security, tool limits).

## References

- `references/components.md`: entities (six categories, strong vs weak), attributes and domains (format, list, range), relationships (cardinality, labels, recursion, subtyping), keys, and how to read a model.
- `references/levels.md`: the camera settings; conceptual, logical and physical × relational and dimensional; normalization worked through 1NF–3NF with question templates; abstraction; meter and dimension types; SCDs; physical techniques; star vs snowflake; NoSQL notes.
- `references/process.md`: the five-step conceptual approach, the eight relationship questions, grain matrix and axis technique, logical and physical steps, requirements templates (In-The-Know, Concept List, Family Tree), definition writing, and working with stakeholders (setting expectations, staying on track, achieving closure).
- `references/scorecard.md`: the 10 categories with weights and detailed checks, a report template, and red flags.
- `references/beyond.md`: metadata types, XML/JSON to a logical model, agile, UML class and use case models mapped to data modeling, unstructured data, taxonomies and ontologies.
- `references/glossary.md`: terms.
- For **industry-specific templates** (party/role, product, order, claims…), see the `industry-data-models` skill if it's installed.

## Limits (say these when they apply)

- **An introductory book (2nd ed., 2009 text with 2016 updates).** It stops at 3NF and only names BCNF, 4NF and 5NF. NoSQL coverage is brief (MongoDB collections, key-value). Data vault, lakehouse/medallion layers, graph modeling, event streams and data contracts aren't covered.
- **Notation:** the book uses Information Engineering (crow's foot) notation and ER/Studio's dimensional icons. Translate to the team's tool or notation (IDEF1X, UML, Chen, dbt docs) as needed.
- **Inconsistencies in the book** (fixed or flagged in these references):
  - The glossary defines "aggregate" and "snowflake" differently from the chapters. The chapter meanings are used here.
  - The answer to exercise 12 calls requirements capture "Category 2". It's Category 1.
  - The keys chapter is mis-cited as "Chapter 5" in the physical chapter.
  - In the normalization example, the 3NF result still puts the organization-wide phone number in Department. That's a fact about the organization, so a strict 3NF review would move it.
- **Data Model Scorecard® attribution:** the Scorecard is Steve Hoberman & Associates, LLC's (www.stevehoberman.com). It's licensed royalty-free for internal model improvement only, and that name and website must appear on any document that references it. Include that line in any Scorecard report you produce.

Condensed and paraphrased from Steve Hoberman, *Data Modeling Made Simple: A Practical Guide for Business and IT Professionals*, 2nd edition (Technics Publications), with chapters by Graeme Simsion (working with others), Bill Inmon (unstructured data) and Michael Blaha (UML).
