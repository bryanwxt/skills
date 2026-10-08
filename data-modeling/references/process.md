# Process, templates, and working with people (Chapters 8, 11, 13)

## The five-step conceptual approach
```
1 Ask the five strategic questions
2 Identify and define the concepts   ◄──┐ (loop back as new concepts appear)
3 Capture the relationships          ───┘
4 Determine the most useful form
5 Review and confirm                 ──► back to step 2 if changes are needed
```

### Step 1: the five strategic questions
1. **What will the application do?** A few precise sentences. Is it replacing, adding, or integrating systems? Begin with the end in mind; this sets the scope.
2. **As-is or to-be?**
3. **Is analytics a requirement?** If yes, at least part of the solution is dimensional. Relational answers business *rules*; dimensional answers business *questions*.
4. **Who's the audience?** Who **validates** the model and who **uses** it? Very different audiences may need different forms.
5. **Flexibility or simplicity?** Flexibility leads to generic terms (Event, Person). Simplicity uses the users' own words.

### Step 2: identify and define concepts
- **Relational:** fill a **concept template**, one column each for Who, What, When, Where, Why and How, with up to about 5 entries per column.
  - Example (bank account system): Customer · Account · Account Open Date · Branch · Check Debit / Deposit Credit / Interest Credit / Statement Fee / Withdrawal Debit · Check / Deposit Slip / Withdrawal Slip / Statement / Account Balance.
- **Definitions:** see "Writing definitions" below.
- **Dimensional:** collect the **business questions** with their sources. Example: "number of students on financial aid by department and semester for 5 years (Financial Aid Office)".

### Step 3: capture relationships (relational): the eight questions per relationship
| # | Question | Determines |
|---|---|---|
| 1 | Can an A relate to more than one B? | many at B's end |
| 2 | Can a B relate to more than one A? | many at A's end |
| 3 | Can an A exist without a B? | zero (optional) at B's end |
| 4 | Can a B exist without an A? | zero at A's end |
| 5–6 | Are there examples of A (B) worth showing? | subtyping to show examples |
| 7–8 | Does A (B) go through a lifecycle? | subtyping for lifecycle states |

Don't repeat questions 5–8 for an entity you've already asked about.

### Step 3: dimensional: the grain matrix
- A spreadsheet with **measures as columns** and **dimension levels as rows**. Each cell holds the numbers of the business questions that need that combination.
- Overlapping questions from different departments become visible, so you can **consolidate them into one scoped mart**.
- Example (the book's student matrix):
  - measure: Student Count
  - levels: semester, year, department, plus financial aid, scholarship, graduation and application indicators
  - source: four departments' questions

### Step 4: choose the most useful form
- **Audience fluent in data models:** traditional notation.
- **Audience not fluent:** a **business sketch**. Use pictures or icons for things (a branch building), nest subtypes inside supertypes, and use document shapes for "how" entities and buttons for transactions.
- **Dimensional:** traditional notation, or the **axis technique**:
  - the business process (meter) sits in the centre
  - each axis is a dimension
  - notches mark the levels (Calendar: Semester, Year)
  - it suits non-modelers best

### Step 5: review and confirm
- Validators confirm the model, which often sends you back to step 2.
- If validators took part throughout, this step is a formality.

## Logical model steps (relational)
1. Start from the agreed CDM and definitions. Each concept expands into several logical entities.
2. List attributes per entity, with sample values. Use forms, reports, screens and legacy data.
3. Assign domains, using class words and standard domains.
4. Normalize to 3NF with the question templates (`levels.md`). Keep a log of each question and its answer; that log becomes your business rules documentation.
5. Choose keys: candidates → primary → alternates. Add a surrogate only with the natural key kept as an AK.
6. Resolve many-to-many relationships with associative entities. Add subtypes where rules differ.
7. Decide on abstraction deliberately and record the trade-off.
8. Define every entity and attribute. Score the model (`scorecard.md`).

## Physical model steps
1. Record the non-functional requirements captured during the logical work: volume, latency, security, tooling, and NoSQL vs RDBMS.
2. Choose subtype implementations (rolldown, rollup, identity) and any denormalization, each with a reason.
3. Add formats, nullability, indexes (PK and AK unique; IE non-unique), partitions and views.
4. For dimensional models, decide star vs snowflake, SCD types, aggregates and bridges.
5. Check every physical structure traces back to the logical model, and that the metadata matches the actual data (Scorecard category 10).

## Requirements templates (Chapter 11)
Use whichever ones help; none are mandatory.

**In-The-Know template** records who and what to consult.

| Term | Resource | Type | Role / how used | Location / contact |
|---|---|---|---|---|
| Customer | (name of SME) | Subject matter expert | Customer reference data administrator | phone or email |
| Customer | Customer classification list | Reference document | Validate or create classifications | file path |
| Item | Current Item Report | Report | Identify current item information | URL |

- **Benefits:** a durable reference list; exposes gaps (no expert for Item) and redundancy; works as a sign-off, so managers allocate the experts' time.

**Concept List** records concepts before any notation is introduced.

| Name | Synonyms | Definition | Questions |
|---|---|---|---|
| Carrier | Trucking company, transporter | A company that physically moves our products between sites | Own and external carriers, or just ours? |

- Synonyms also hold narrower, industry-specific terms (Order under Contract).
- The Questions column records what the concept does and doesn't include.
- **Benefits:** high-level understanding; gets the team "out of the weeds" of attributes; gives a base for naming and defining entities and attributes; a quick win that builds rapport.

**Family Tree** records lineage and history for each concept or attribute.

| From here: Name | Source | Definition | History (yrs) | To arrive here: Name | Definition | History needed |
|---|---|---|---|---|---|---|
| Item | Item reference DB | Anything we buy, sell, stock, move or make | 10 | Product | Anything we sell | 3 |

- **Trace upstream** until you reach a reliable, accurate source, then stop.
- **Flag name or definition mismatches** between source and target (Item vs Product; Party vs Associate).
- **Compare history available with history required.** A shortfall is caught early; for BI this column is mandatory.
- Attribute-level trees can add length and domain.
- It's owned by the functional analyst (business analyst or modeler) and built in parallel with the LDM.
- **Benefits:** source capture, effort estimation, early detection of sourcing problems.

## Writing definitions (clear, complete, correct)
- **Clear:** understood on one reading, in business language.
- **Complete:** says what's included and excluded, with examples, synonyms, derivations, exceptions and lifecycle. Example: "a customer must have obtained at least one product; prospects aren't customers; once a customer, always a customer; a customer differs from a consumer."
- **Correct:** matches what the term really means and is consistent with the rest of the business.
- **Stand-alone:** don't rely on the entity name. "A Customer Id is the unique identifier for a Customer" fails, because it says nothing about scope, reuse, assignment or purpose.
- **Avoid circular and empty definitions** ("data about data"; "an employee is a carbon-based life form").

## Working with others (Graeme Simsion, Chapter 13)
The hardest modeling problems are usually *people* problems. Handle them through process rather than vague "people skills".

### Set expectations (most important)
- **Ask the next-higher question:** why is this being done, and what will the deliverable be used for? Most failed modeling assignments misread the context.
- **Quality is fitness for purpose.** Avoid the perfection trap: a model can always be improved. Time-critical projects may need "good enough".
- **For enterprise models,** establish exactly how and by whom the detail will be used before investing in it.
- **Stakeholders and what they expect:**
  - DBA or database designer: agree evaluation criteria up front, or arguments about "too generic" or "won't perform" come at handover
  - process developers and testers
  - affected users
  - project manager and sponsor: why and how it will be used; how fixed budget and time are
  - subject matter experts: their time
  - technical standards owners; procurement (for consultants)
  - your own manager or central team: standards, repository, relationships
  - Involve people early. They support what they help design.
- **Key questions:**
  - What does the final product look like? Show a sample.
  - What does success look like to each stakeholder?
  - Who directs the day-to-day work?
  - Who formally accepts the deliverable?
  - How will disputes be resolved?
  - Whose name goes on the deliverable? Prefer the client's.
  - What follow-up is planned?
- **Package it** as a written plan, integrated with the project plan, that overrides earlier informal promises. Include a **schedule of interviews**.

### Stay on track
- **Meet expectations rather than exceed them.** Extra scope gets raised and agreed, not done for free.
- **Seven habits:**
  1. work close to the client
  2. keep in touch with *all* stakeholders, including the sponsor
  3. support the relationship between your boss and the client's boss
  4. hold real progress meetings that **sign off work so far**
  5. listen
  6. take time out for perspective
  7. keep a daily diary
- **Problems:**
  - establish whose problem it is
  - step back before reacting
  - keep perspective
  - get help early
  - **assume people are acting rationally** ("under what circumstances would a rational person do this?")
  - know your own triggers (e.g. preferences for detail vs big picture, closure vs open options)
  - focus on the path forward; leave blame for later, if at all
  - keep team disputes "in the kitchen", out of the client's sight
  - hold a lessons-learned review

### Achieve closure
- **Frame the end as a handover** ("can you take it from here?") rather than a sign-off ("is it right?").
- **Use staged reviews**, with agreed costs for later changes of mind.
- **Bring stakeholders along** with unfamiliar concepts as they emerge, not in one final leap.
- **Reports should inform, not impress.** Start with a one-page summary, cut material the reader already knows, and write plainly.
- **Follow up:** post-implementation reviews, fixing misunderstandings (modify the model, don't fudge it), and checking whether the work delivered value.
