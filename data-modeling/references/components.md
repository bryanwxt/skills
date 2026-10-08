# Model components (Chapters 4–7)

A data model differs from a spreadsheet in three ways: it shows **types** rather than values (Ice Cream Flavor, not "Chocolate"), it shows **interactions** between types, and it's a **concise** one-page medium.

## Entities
- **Definition:** a collection of information about something the business considers important enough to capture. It's named with a **noun or noun phrase**.
- **Six categories** are a checklist for finding entities:

| Category | Question | Examples |
|---|---|---|
| **Who** | Who matters to the business? (often a role) | Customer, Employee, Patient, Vendor, Student |
| **What** | What does it make or provide? | Product, Service, Raw Material, Course, Song |
| **When** | When does it operate? | Date, Month, Fiscal Period, Semester |
| **Where** | Where is business done (physical or electronic)? | Mailing Address, Distribution Point, URL, IP Address |
| **Why** | Which events keep it in business? | Order, Return, Complaint, Deposit, Claim, Trade |
| **How** | Which documents record the events? | Invoice, Contract, Purchase Order, Packing Slip |

- **Entity instance:** one occurrence, like a row in a spreadsheet (Bob, Bob's checking account).
- **Strong (independent or kernel) entity:** identified on its own, e.g. Customer by Customer ID. Drawn with square corners.
- **Weak (dependent) entity:** needs another entity's key to be identified, e.g. an order line or ice cream order identified via its flavor plus a sequence number. Drawn with rounded corners.
  - This tells developers that the parent must exist first (the flavor must exist before an order for it).
- **Processes are not entities.** If someone draws "Manufacturing" as a box, break it into the things the process uses: raw material, finished good, machine, schedule.
- **By level:**
  - **conceptual:** basic and critical concepts
  - **logical:** detailed business entities with attributes
  - **physical:** tables (RDBMS), collections (MongoDB) or other structures, including technology compromises, formats and nullability

## Attributes
- **Definition:** a single piece of information whose values **identify, describe or measure** an entity instance (Claim Number, Student Last Name, Gross Sales Amount).
- **Use the audience's word:** property, label or field for business; column or field for DBAs.
- **By level:**
  - **conceptual:** rare; only if the attribute itself is basic and critical (a phone number at a telco)
  - **logical:** a technology-independent business property
  - **physical:** the container (`ICE_CRM_FLVR_NAM` column, `IceCreamFlavorName` field)
- **Name attributes with a class word at the end** (Amount, Code, Name, Date, Indicator, Text…). The class word implies a standard domain.

### Domains
- **Domain:** the complete set of allowed values. It's reusable across attributes (the Date domain serves Hire Date, Order Entry Date…). An attribute must never hold values outside its domain.
- **Format domain:** a datatype and length, e.g. Integer, Character(30), Decimal(15,4).
- **List domain:** an enumerated set refining a format, e.g. Order Status Code ∈ {Open, Shipped, Closed, Returned}; ISO country codes.
- **Range domain:** min/max refining a format, e.g. delivery date between today and +3 months.
- **Domains can tighten for one attribute:** hire date must be ≤ today and on a weekday.
- **Benefits:** data quality (validate before insert), more communication on the model, and faster modeling through standard domains.
- **Probe vague domains with examples.** Is "Contact Name" first + last, first only, or company names too? Can it contain digits? Symbols?

## Relationships and rules
- A **rule** is captured as a **relationship**: a line between two entities that represents a rule or a navigation path.
- **Data rules** belong on the model:
  - **Structural (cardinality) rules:** how many instances participate, e.g. "each order line must contain one product".
  - **Referential integrity rules:** "an order line can't exist without a valid product". These come free with the structural rule.
- **Action rules** ("10% off orders with more than 5 products"; "a policy with 3+ claims is high-risk") can't be enforced by the model. Capture the data they need; enforce them in code or a rules engine.
- **Cardinality symbols** (crow's foot / IE notation):

  | Symbol | Meaning |
  |---|---|
  | bar | one |
  | circle | zero (optional) |
  | crow's foot | many (more than one) |

  Exact numbers ("a car has 4 tires") need documentation, or UML multiplicity.
- **Reading:**
  - Parent = the "one" side, child = the "many" side. Read from the parent first, starting with "Each".
  - Zero becomes **may**; no zero becomes **must**.
    - Each Ice Cream Flavor *may be the selection for* one or many Ice Cream Scoops.
    - Each Ice Cream Scoop *must contain* one Ice Cream Flavor.
  - Two entities can have several relationships, e.g. Department *contains* Employees and is *managed by* an Employee.
- **Labels:** use precise verbs (contain, own, work for, initiate, categorize, apply to). Avoid *has, have, associate, participate, relate, be* on their own. Hoberman labels one side and infers the reverse reading; labelling both sides is also acceptable.
- **Many-to-many** is allowed on conceptual models. Logical and physical models resolve it with an **associative entity** (e.g. Attendance between Student and Class).

### Recursion
- **One-to-many recursion = a hierarchy** (each employee has at most one manager).
- **Many-to-many recursion = a network** (an employee can have several managers).
- **Validate with sample values:** sketch Bob, Jill and Jane in a tree or network.
- **Trade-off:**
  - *For:* flexible to any depth, and covers rules nobody has stated yet.
  - *Against:* it hides rules, e.g. "where's the regional management level?".
  - Decide case by case: obscurity vs flexibility.

### Subtyping
- **Subtyping** groups the common attributes and relationships of similar entities into a **supertype**. Subtypes inherit everything, which reduces repeated relationships (Cone and Cup → Ice Cream Container holds Scoops).
- **Readings:**
  - "Each Container may be either a Cone or a Cup."
  - "Each Cone is a Container."
- **Exclusive vs inclusive (overlapping):**
  - An "X" in the subtype symbol means **exclusive**: an instance is exactly one subtype.
  - No X means **inclusive**: e.g. a Person can be both a Provider and a Patient.
- **Use subtypes to show examples** and **to show a lifecycle** (prospect → active → former customer).
- **Subtypes carry subtype-specific rules.** Example: only managers have an office, and Office First Occupied Date is mandatory for them. Put the date and the relationship on a Manager subtype (or Manager role), where they can be NOT NULL.

## Keys
- **Purpose:** enforce rules, retrieve data efficiently, and navigate between entities.
- **Candidate key:** one or more attributes that uniquely identify an instance. Four tests:

  | Test | Meaning | Failure example |
  |---|---|---|
  | **Unique** | one value means one instance | Student Name (two Eddie Murphys) |
  | **Mandatory** | never empty | Class Short Name (Juggling has none) |
  | **Non-volatile** | never changes | Class Description Text (descriptions get rewritten) |
  | **Minimal** | no unnecessary attributes | a 4-part key where 3 parts suffice |

- **Composite key:** more than one attribute (e.g. Promotion Type Code + Start Date).
- **Primary key:** the chosen candidate. Prefer **succinct** and **non-sensitive**, because PKs spread as FKs (Student Number beats first name + last name + birth date).
- **Alternate key (AK):** the other candidates. They become unique indexes. Notation like `AK1.2` means alternate key group 1, position 2.
- **Surrogate key:**
  - A meaningless, system-generated, usually fixed-size counter, hidden from the business.
  - It's efficient (one column instead of many) and helps integration across sources.
  - **Always pair it with the natural key as an AK.** A missing AK behind a surrogate is a classic review finding.
- **Foreign key (FK):** the parent's primary key copied into the child. It lets the database navigate parent↔child. Recursive FKs point to the same entity. Modeling tools create FKs when you draw the relationship.
- **Secondary key / inversion entry (IE):** a frequently searched attribute that gets a non-unique index (e.g. Student Last Name). It needn't be unique, stable or populated.
- **Defining an identifier properly** (not just "the unique ID for a customer"):
  - scope of uniqueness
  - whether values are ever reused
  - how it's validated
  - purpose (e.g. integration across sources)
  - natural or surrogate
  - who assigns new values and how
  - a reference to the entity's own definition

## Reading a whole model
1. Find the independent (strong) entities. They're usually the who, what, where and when.
2. Read each relationship as two sentences, parent first.
3. Read subtype clusters: "each X may be either A or B; each A is an X".
4. Check the keys: is there a PK in every entity? Does every surrogate have an AK? Are FKs consistent with the relationships?
5. Sample-value test: invent three or four realistic instances and walk them through the rules. Contradictions surface quickly.
