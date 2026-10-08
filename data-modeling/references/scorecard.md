# Data Model Scorecard® (Chapter 12)

> Data Model Scorecard® is from Steve Hoberman & Associates, LLC, www.stevehoberman.com. It's licensed royalty-free for internal data model improvement only, and that name and website must appear on every document that references the Scorecard. Copy that line into any Scorecard report. Hoberman's separate book *Data Model Scorecard* covers it in depth. The checks below combine this book's summary with general good practice.

## Why use it
- It highlights **strengths as well as fixes**, so give specific examples of both.
- It provides an **external perspective**: "the Scorecard recommends…" rather than "I hate what you did". That takes the emotion out of reviews.
- It's **straightforward**: even people new to modeling can review with it, and experienced reviewers can use it to organize their thinking.
- It works for **conceptual, logical and physical** models, whether **relational, dimensional or NoSQL**.
- **Score early.** Fixing problems is cheaper, and comments are more likely to be acted on.
- **Grade strictly.** A low score gets a fast response and a request to rescore. Hoberman's highest score ever given was 91.

## Template
| # | Category | Weight | Score | % | Comments (strengths, fixes) |
|---|---|---|---|---|---|
| 1 | How well does the model capture the requirements? | 15 | | | |
| 2 | How complete is the model? | 15 | | | |
| 3 | How well does the model match its scheme? | 10 | | | |
| 4 | How structurally sound is the model? | 15 | | | |
| 5 | How well does the model leverage generic structures? | 10 | | | |
| 6 | How well does the model follow naming standards? | 5 | | | |
| 7 | How well has the model been arranged for readability? | 5 | | | |
| 8 | How good are the definitions? | 10 | | | |
| 9 | How consistent is the model with the enterprise? | 5 | | | |
| 10 | How well does the metadata match the data? | 10 | | | |
| | **Total** | **100** | | | |

- Weights reflect what the organization values. Adjust them, but keep the total at 100.
- **% = score ÷ weight.** Always write at least a summary comment per category, even if it's perfect.
- Attach a detailed findings list that cites the specific entities or attributes behind each score.

## Category checks

**1. Requirements (correctness)**: does the model actually support each requirement?
- Trace each requirement or business question to structures. For example, check the model can answer "Student Count by Semester and Major".
- Read the relationships aloud to an SME. Does each rule match reality, e.g. can an account have several owners?
- This is the hardest category to grade: requirements are vague, differ from what was said, or keep growing.

**2. Completeness**: are all requirements present, and nothing extra?
- **Requirements:** every requested item appears. Flag **unrequested or "future" structures** too: they cost effort and risk if never used.
- **Metadata:** what the level needs is present. Examples: definitions everywhere; logical keys; physical formats, lengths and nullability; dimensional grain and SCD types.

**3. Scheme**: does it match its declared type?
- **A conceptual model** is about scope and the business need. It shouldn't contain attributes or physical detail.
- **A logical model** is technology-free. Flag processing or technical attributes (load timestamps, batch IDs, flags for an application's convenience).
- **A physical model** is tuned for performance, security and tooling.
- **Relational** captures rules; **dimensional** captures questions (meters, dimensions, grain); **NoSQL** reflects how the store holds data (documents, graphs).

**4. Structural soundness**: is it technically correct?
- every entity has a primary key, with no nullable PK columns
- every surrogate key has a natural or business alternate key, and alternate keys aren't nullable
- the model is normalized to 3NF (logical relational): no repeating groups, multi-valued attributes, partial or transitive dependencies, or **derived attributes**
- many-to-many relationships are resolved (logical and physical)
- foreign keys are consistent with relationships and match the parent's key datatype
- no orphan entities, circular mandatory relationships or impossible cardinalities (mandatory both ways with no way to insert first)
- subtypes are exclusive or inclusive deliberately; subtype attributes are mandatory where the rule says so
- recursion is validated with sample hierarchies or networks
- dimensional: one grain per meter, measures additive at that grain (or documented as semi- or non-additive), dimensions joined at the lowest level, bridges for many-to-many

**5. Generic structures (abstraction)**: is abstraction used appropriately?
- Is abstraction used where flexibility truly matters (data warehouse, integration hub, expected new types) and avoided where usability matters (marts, simple applications)?
- **Over-abstraction:** EAV-style "attribute/value" tables, "Thing/Thing Type", rules lost to code.
- **Under-abstraction:** near-duplicate entities that should be one (Customer Address, Supplier Address, Employee Address).
- Perfect balance earns full marks.

**6. Naming standards**
- **Structure:** the right building blocks, e.g. subject + modifier + **class word** (Customer Last Name; Order Entry Date).
- **Term:** the correct, approved word, spelled and abbreviated per the standard.
- **Style:** consistent case and format (snake_case, CamelCase, upper case).
- Entities are singular nouns. Relationship labels are meaningful verbs.

**7. Readability**
- parents above children
- related entities grouped together, e.g. subject areas
- short relationship lines with few crossings
- a conceptual model included or referenced for orientation
- large models split into subject-area views

This matters less than the other categories, but a hard-to-read model hides errors in categories 1–4.

**8. Definitions**: clear, complete and correct.
- Read each definition once. Is it understood? Does it say what's in and out, with examples, synonyms, derivations and exceptions? Does it match the business?
- Flag missing, circular ("Customer Id is the unique identifier of a customer") or copied-from-the-name definitions.

**9. Consistency with the enterprise**
- Compare against the enterprise data model, conformed dimensions and shared reference data: same names and meanings for the same concepts, and no conflicting rules.
- A local deviation must be deliberate and documented.

**10. Metadata matches data**
- **Profile the actual data:** does the Customer_Last_Name column really hold last names? Are "mandatory" fields full of placeholders (dummy data such as "N/A", 99, "ZZ")? Do codes stay within their list domains?
- **Check volatility:** do natural keys change? The book's top-scoring model handled changing natural account numbers. Look for duplicate natural keys and nulls in candidate keys.

## Review procedure
1. Get the model, its declared settings (scope, abstraction, time, function, level, mindset), the requirements, and sample or profiled data.
2. Read the whole model aloud as sentences. Note anything ambiguous.
3. Go through categories 3 → 4 → 6 → 7 → 8 first (you can judge these from the model alone), then 1, 2, 5 and 9 (these need the requirements and enterprise context), and finally 10 (needs data).
4. Score each category with comments. List **strengths** (specific) and **areas for improvement**, numbered and pointing to entities or attributes, each with a recommended fix.
5. Present it as "the Scorecard shows…". Agree the fixes, then rescore.

## Red flags that cost points quickly
- surrogate key with no alternate key; nullable alternate key
- no definitions, or definitions that repeat the name
- labels like "has" or "relates to", or unlabelled relationships
- repeating columns (Phone1/Phone2/Phone3) or concatenated fields on a "normalized" model
- derived or processing columns on a logical model
- dummy values hiding optional data (ZZ, 9999-12-31 misused, "Unknown" customer)
- one conceptual box per process ("Manufacturing", "Billing")
- a model that answers none of the stated business questions, or has no grain declared
- abstraction everywhere ("Entity", "Object", "Attribute" tables) for a simple application
