# Model types: settings, levels, mindsets (Chapters 3, 8–10)

## The four camera settings
Every model takes one value for each setting. Match the settings to the model's purpose and state them on the model.

| Setting (camera analogy) | Values | Notes |
|---|---|---|
| **Scope** (zoom) | Department/project · Organization/program · Industry | Most work is project-scope. Programs (data warehouse, ODS, CRM) need long-lived models. Industry models come from consortia and standards bodies |
| **Abstraction** (focus) | *Business clouds* (Person, Transaction, Document) · *Database clouds* (Entity, Object, Attribute) · *On the ground* (Student, Course, Instructor) | On the ground takes longest but adds the most understanding. Clouds suit cases with little business access or very broad coverage |
| **Time** (timer) | Today (as-is) · Tomorrow (to-be) | A to-be model usually needs an as-is model first |
| **Function** (filter) | Business view · Application view | The application view uses the application's terms (e.g. "Object" for Product) and its definitions |

**Format** sets the level of detail:
- **Conceptual:** the proof sheet, a one-page overview.
- **Logical:** the negative, the full business solution, independent of technology.
- **Physical:** the print, the version tuned for a technology.

Examples from the book's exercise answers:
- Explaining a legacy application to developers: department · business clouds · today · application.
- Onboarding a new hire to the business: organization · on the ground · today · business.
- A new data mart's requirements: department · on the ground · tomorrow · business.

## Five model types
| | Relational: *how the business works* (rules) | Dimensional: *how the business is monitored* (navigation) |
|---|---|---|
| **Conceptual (CDM)** | One page of key concepts and their rules: "Each Customer may place one or many Orders" | One page of measures and the levels needed to see them: "Gross Sales Amount by Customer" |
| **Logical (LDM)** | All attributes, normalized, technology-free: "each Customer ID returns at most one Customer Last Name" | All attributes for reporting, organized around measures: "…and show the customer's first and last name" |
| **Physical (PDM)** | The LDM compromised for a technology (indexes, denormalization, embedded documents) | Same: star or snowflake, aggregates, partitions |

The main difference is what a line means. **Relational:** a line is a business rule. **Dimensional:** a line is a navigation path along which you aggregate measures.

## Conceptual data model (CDM)
- A **concept** is **basic** (mentioned many times a day by this audience) and **critical** (the business would be very different without it). Both depend on the audience: a bank's CDM may need Checking and Savings Account, a manufacturer's needs GL Account and AR Account.
- **Limit it to one page, about 20 concepts.** If you have too many, group them (Order Line goes into Order).
- Many-to-many relationships are allowed. Show definitions on the diagram when they're short, or when they're contentious and need debate.
- **Why definitions matter:** decisions (does "product" include raw materials?), resolving perspectives (sales vs accounting on "customer"), and precision (no rule is precise if its terms aren't).
- **Benefits:** broad understanding on one page, scope and direction (scope projects out of a department model), early discovery of issues, and rapport between IT and the business.
- **A dimensional CDM** shows:
  - a **meter** (the business process being measured, e.g. Account Balance)
  - its **dimensions** (Region, Account, Month)
  - their higher levels, called **snowflakes** in the book's icon set (Country, Customer, Year)

  The audience can be shown it with the **axis technique** (below).

## Logical data model (LDM), relational
- **It's the business solution.** Record questions about technology (big data volume, security, two-second response) but don't act on them until the physical model.
- **Normalization is mandatory.** Abstraction is optional.

### Normalization: "a formal process of asking business questions"
**Rule:** every attribute is **single-valued** and provides a fact **completely** and **only** about its primary key. In practice "normalized" usually means 3NF. BCNF, 4NF and 5NF cover rarer cases.

| Level | Meaning | Question template | Fixes |
|---|---|---|---|
| **1NF** | single-valued | "Can a [entity] have more than one [attribute]?" and "Does [attribute] contain more than one piece of business information?" | Move repeating attributes (Phone 1/2/3) to their own entity, *or* discover they're really different facts. Split multi-valued attributes (Name → First Name, Last Name) |
| **2NF** | the whole key (completely) | "Are all the PK attributes needed to retrieve one [attribute]?" | Remove partial dependencies into their own entities. The answer depends on rules, e.g. "can an employee work in several departments at once?" decides whether you need an Employee Assignment associative entity |
| **3NF** | nothing but the key (only) | "Is [attribute] a fact about any other attribute in this entity?" | Remove hidden (transitive) dependencies and **derived attributes** (e.g. an On-Time Indicator derived from dates; a Vested Indicator derived from start date), or move them to the entity they describe |

- **Work through the book's example with sample data.** In the employee spreadsheet, the three phone columns turned out to be:
  - one value constant across all rows: the organization's number
  - one that varied by department: the department number
  - one per employee: the employee's own number

  Sample values reveal meaning that names hide.
- **With practice, apply all three checks at once per entity:** is the key right and minimal, and is every attribute about only that key?
- *Review note:* in the book's 3NF result, Organization Phone Number stays in Department, but it's constant across departments. A strict review would move it to an Organization entity (or reference data).

### Abstraction
- **What it is:** redefining and combining entities, attributes and relationships into generic terms. Examples: Employee becomes Party + Party Role (Role Type Code 03 = Employee); Customer Location becomes Location.
- **Gains:** new types (Contractor, Consumer) fit without changing the model or the application.
- **Costs:**
  1. **Lost communication:** concepts become rows, not boxes.
  2. **Lost rules:** "an Employee must have a Start Date" can no longer be enforced by structure, only by code.
  3. **Development complexity:** pivoting attributes to values and back in ETL.
- **When to use it:** only when new types are really expected. Common in data warehouses and integration hubs, where longevity matters. Less suited to analytic marts and simple applications.

## Logical data model, dimensional
- **Start from business questions** and build a grain matrix (`process.md`).
- **Meter** (called a *fact table* at the physical level) is a bucket of related **measures** for one business process. It's not a person, place or thing. It often names the application (the Sales mart).
- **Meter types:**
  - **Aggregate / summarization:** stored above transaction level, e.g. monthly account balance.
  - **Atomic:** the lowest level of detail, e.g. each deposit and withdrawal.
  - **Cumulative / accumulating:** the duration of a process, e.g. mortgage application to completion.
  - **Snapshot:** the timestamps of steps in a life cycle (created, confirmed, shipped, delivered, paid). The book's use of the term differs from the common Kimball usage, where "periodic snapshot" means a balance at period end, so state which you mean.
- **Grain** is the lowest level of detail in the meter. Declare it.
- **Dimension:** a subject that gives measures meaning (filter, sort, sum by it). It has attributes and often hierarchies.
- **Hierarchy:** each lower level belongs to at most one higher level (January 2016 → 2016). Higher levels are where you can roll measures up (Region → Country).
- **Dimension types:**
  - **Fixed (SCD Type 0):** values never change (e.g. a gender code list).
  - **Degenerate:** a lone attribute such as Order Number stored in the meter.
  - **Multi-valued:** e.g. several diagnoses on a bill line. Use a bridge with weights that sum to 1.
  - **Ragged:** a parent missing at some level, giving variable depth (org charts, parts explosions).
  - **Shrunken:** large text at the meter's grain, split off for space or speed. The book lists it among dimensions, but in common usage a shrunken dimension is a subset of another dimension's rows or columns.
  - **Junk:** combinations of small flags and codes.
  - **Conformed:** shared across marts (or drawn from one superset) so queries can drill across.
- **Slowly changing dimensions (SCD):**

  | Type | Keeps |
  |---|---|
  | 0 | the original only; never changes |
  | 1 | current only, overwriting history |
  | 2 | full history, with a new row per change ("the time machine") |
  | 3 | current plus limited history (previous or original) in columns |
  | 6 | a mix of 1, 2 and 3 in one dimension (1+2+3) |

- **Factless fact:** a meter with no measures. You count relationship occurrences, e.g. attendance or coverage.
- **Bridge table:** resolves a many-to-many between a meter and a dimension.
- **Trace every dimensional element back to the relational model that sources it.** Example: the dimensional model wants Region, but the source has Branch Code, so you need a branch → region derivation.

## Physical data model (PDM)
- **The LDM compromised for specific software or hardware:** speed, space, security, tool limits. As hardware improved, PDMs came to look more like LDMs. Big-data and NoSQL designs widened the gap again, and a single wide table or document may well be the right physical design.
- **Terms change:** entity → table (RDBMS) or collection (MongoDB); attribute → column or field; relationship → constraint or reference/embedding.

### Techniques
- **Denormalization:** deliberately reintroduce redundancy for retrieval speed or user-friendliness. Two forms:
  - **Rolldown:** the parent disappears and its columns and relationships move into the child. It's the most common form. It keeps the normalized flexibility but stops the database enforcing it, and it cuts joins and code.
  - **Rollup (repeating groups or arrays):** child rows become a fixed number of repeated columns in the parent (e.g. Category 1–3 on Offering). Use it only when the maximum is truly fixed and the parent is what's used.
- **Subtypes on the physical model**, three options:
  - **Rolldown:** drop the supertype and copy its attributes and relationships into each subtype table.
  - **Rollup:** drop the subtypes into the supertype table, with a **type code** and nullable subtype columns. Subtype NOT NULL rules are lost unless you add check constraints.
  - **Identity:** keep all the tables, with one-to-one relationships from the supertype to each subtype.
  - Choose by query patterns, rule enforcement and how often new subtypes appear.
- **Star schema:**
  - Each dimension's hierarchy is flattened into one table (Customer into Account, Country into Region, Year into Month).
  - The fact table sits in the centre, linked to each dimension at the lowest level.
  - It's simple for both IT and the business. "Denormalization" is a relational term; in dimensional design call it *flattening* or *collapsing*.
- **Snowflake (physical):** each hierarchy level is kept as its own table, so it resembles the logical dimensional model.
- **Views:** a stored query acting as a virtual table, for convenience or security. Unlike an ad-hoc query, it's saved in the database.
- **Indexes:**
  - PK and AK become unique indexes; IE (secondary keys) become non-unique indexes.
  - Indexes help most on attributes that are queried often and updated rarely.
- **Partitioning:**
  - **Vertical:** split columns, e.g. move volatile columns out.
  - **Horizontal:** split rows, e.g. orders by year.
  - The two are often combined, and partitioning can be added after go-live once performance is known.
- **Record every compromise** with its reason, so the logical model remains the source of meaning.

### NoSQL notes (light in the book; extended here)
- Entities can become collections or documents. Embedding replaces joins for data that's read together.
- Keep the logical model regardless of the physical store. Hoberman's position is that the analysis and the questions don't change with the technology.
- **Key-value stores** hold a key and an opaque value. The structure lives in the application.
- **Review physical NoSQL designs** for:
  - duplicated data without an owner
  - unbounded arrays
  - unclear identifiers
  - whether relationships are queried in both directions (embedding supports only one)
