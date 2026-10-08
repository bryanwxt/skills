# Beyond the model: metadata, XML, agile, UML, unstructured data (Chapters 2, 14–16)

## Data model uses (Chapter 2)
- Designing **new applications**: analysis and design, before the database exists.
- **Understanding existing applications** by **reverse engineering** the database into a model, e.g. before a platform migration.
- **Managing risk:** impact analysis of changes, including customizations to purchased software, and of archiving.
- **Learning the business** before building for it. In William Kent's words, agree what "one book" means before designing a book database.
- **Educating team members:** walk new joiners through the models.
- **Forward engineering** runs from the conceptual model to the database. **Reverse engineering** runs from the database back up to the conceptual model.

## Metadata
- "Data about data" is correct but neither clear nor complete.
- **Better definition:** text, voice or image that describes what an audience (a person, group or program) wants or needs to see or experience. It helps clarify and find the actual data.
- **Data or metadata is a role,** not a fixed property. Search keywords are data that act as metadata.
- **Six types:**

| Type | Examples |
|---|---|
| Business (semantic) | definitions, tags, business names |
| Storage | column names, formats, volumetrics |
| Process | source-to-target mappings, load metrics, transformation logic |
| Display | display formats, colours, device type |
| Project | requirements, plans, status reports |
| Program | Zachman framework, DAMA-DMBOK, naming standards |

## Showing the value of a logical model
- It's hard to price a blueprint. Instead, **quantify the cost of not having one:** data quality failures.
- Tell concrete stories with figures. The book's example: a $125M Mars orbiter lost because two teams used different units.

## XML (and, by extension, JSON)
- An XML document plus its schema (DTD or XSD) is a **data model**: hierarchical, human-readable, separating content, format and rules.
- **Limitation:** hierarchies state cardinality from **one end only**. A Recipe contains Ingredients, but can an Ingredient belong to many Recipes? The document can't say.
- **To derive a logical model from a document,** ask the missing questions:
  - Is the title single-valued?
  - Is the short name really the natural key?
  - Do ingredients belong to many recipes?
  - Can a step use several ingredients?
  - Units of measure become a reference entity.
- **The book's example result:** Recipe, Ingredient, Unit Of Measure, Recipe Ingredient (with amount and unit), Recipe Step (with sequence), and Recipe Ingredient Step.
- **Industry XML standards** are good input for enterprise models (the book cites ePub for publishing). JSON Schema and OpenAPI payloads raise the same one-directional-cardinality caveat.

## Agile
- In practice, agile teams often skip data models because they focus on process and prototypes.
- **Hoberman's position:** modeling belongs wherever requirements are found. The business questions still have to be asked, whatever the methodology.
- **Practical approach (extension):**
  - Keep a living conceptual model and glossary across sprints.
  - Model just enough logical detail per story.
  - Score changes incrementally.
  - Watch the program-level view, which agile tends to neglect.

## Keeping skills sharp
- Play other roles. As a developer you meet the model's customers' questions: how to load it with ETL, how to make development simpler, how to extract fast for reporting.
- Model everyday forms (menus, prescription labels) to spot concatenated and multi-valued fields.
- Monthly design challenges, the Data Modeling Zone conference, DAMA.

## UML for data modelers (Michael Blaha, Chapter 15)
- **Why model at all:** better quality (conceptual integrity), lower cost and faster delivery (fix problems before code), easier tuning, better communication. Models also help evaluate packaged software.
- **UML** is OMG-standardized notation, not a process. Use only the diagrams that help.

| UML class model | Data modeling equivalent |
|---|---|
| Class (with attributes and **operations**) | Entity (with no behaviour) |
| Attribute with multiplicity [1], [0..1], [*] | Mandatory, optional, or multi-valued (a 1NF issue) attribute |
| `/attribute` (derived) | Derived attribute: removed from an LDM, but may be stored physically |
| Association with end multiplicities 1, 0..1, * | Relationship with cardinality |
| Association end names (origin, destination) | Role-named relationships (two FKs to Airport) |
| `{ordered}` on an end | A sequence-number attribute in the child |
| Association class | Associative entity |
| Qualified association (Airline + accountNumber) | Composite alternate key scoped by the parent |
| Aggregation (part-of; transitive, antisymmetric) / composition (a part belongs to at most one whole) | Recursive or BOM structures; identifying relationships |
| Generalization (hollow arrow to the superclass) | Subtyping |
| Operations (e.g. update total miles; check balance) | Stored procedures, triggers, constraints, views |

- **Other diagrams:** object, **use case**, state, activity, sequence. For databases, the class and use case models matter most.
- **Use case model:**
  - **Actors** are direct external users: people, devices, systems. Actors can be generalized (Agent → Human Agent, Computer Agent).
  - **Use cases** are units of externally visible functionality (open account, post activity, redeem miles, expire miles). They can *include* other use cases.
  - Use cases drive data needs. For example, "close account" revealed a missing close-date attribute.
- **Inputs:**
  - use cases (but don't fixate on them)
  - business documents (justifications, screen mock-ups, sample reports)
  - user interviews
  - technical reviews
  - related and legacy systems
  - standard models (e.g. OMG's Common Warehouse Metamodel)
- **Outputs:** diagrams, explanations or a data dictionary, the database structure, and converted seed data.
- **Modeling insight from the frequent-flyer example:** distinguish a published flight from its legs (a through-flight has several legs under one number), and keep award logic out of the structural model.

## Unstructured data (Bill Inmon, Chapter 14)
- **Structured data** is repetitive: the same event shape over and over (cashing a check). **Unstructured or textual data** (email, reports, notes) follows no pattern. There's about 4–5× as much of it, and it's mostly absent from decision making.
- **A data model abstracts structured data** and links systems to the real world. Structured data is **mutable**: change the model, change the system. Text is effectively **immutable**: you must keep what was written, even known-wrong values on a loan application.
- **Taxonomies are to text what data models are to structured data.**
  - A taxonomy is a categorized list of words or phrases (Cars: Porsche, Ford…).
  - Applying it tags raw text ("Porsche/car"), so queries find every car, and synonyms collapse (the ~20 ways of saying "broken bone").
- **Practical issues:**
  - **Cost:** n words × m taxonomy terms, across all taxonomies.
  - **Choose taxonomies that fit the corpus:** "President Ford drove a Ford" tags differently in a presidents corpus and a cars corpus.
  - **Each taxonomy classifies one aspect only** (sports vs family car; country of origin).
  - **Multi-level and recursive:** a term can appear in several categories (Porsche is both sports and off-road).
  - **Maintenance:** taxonomies change over time. Decide case by case whether to reprocess text already tagged.
  - **Phrases count too,** not just single words.
  - **Taxonomies translate across languages,** enabling unified multilingual categorization.
- **Ontology:** a taxonomy plus relationships between its terms. Gruber's phrase is "explicit specification of a conceptualization".
- **Today:** NLP, embeddings and knowledge graphs extend these ideas. Model the taxonomy itself (term, category, synonym, language, version) as reference data so tagging stays reproducible.
- **Semi-structured data** needs you to inspect the content to find its structure, e.g. JSON or XML payloads. It's one processing step from structured. **Unstructured** attributes use the class words Text or Object.
