# Playbooks

Each one lists inputs → steps → output. Paraphrase entity names into the user's vocabulary, keep the structure, and say where you're deliberately departing from the template.

---

## A. Build a logical model for an enterprise in a covered industry
**Inputs:** industry, the business's scope (which lines and segments), the key business questions, the systems being replaced or integrated.
1. **Scope generically within the industry.** Model "travel" even if the client is only an airline today, unless they're certain never to diversify. Note the scope decision.
2. **Build the usage table.** For each subject area (parties, products, commitments, delivery, work effort, invoicing, accounting/budgeting, HR, plus industry-specific areas), mark it *use as is*, *modify*, *not used*, or *new*. Load the industry reference for the modify and new rows.
3. **Parties:** list the person roles, organization roles and relationships the business talks about. Map them to generic roles, and subtype only where the business needs different attributes or relationships.
4. **Products:** separate the offering from the physical or functional thing (part, circuit, account, scheduled occurrence). Decide the feature, applicability and rule structure.
5. **Commitment, delivery and billing:** name each in the industry's language and draw the bridge entities between them.
6. **Industry-specific structures:** add them from the reference (e.g. network, claims, travel experience, service entries).
7. **Statuses and roles:** give every key transaction a status history and a role entity.
8. **Validate with illustration tables.** Fill sample rows for the trickiest entities, using the business's own examples. That's how the book proves each model.
9. **Prune:** drop entities the enterprise won't maintain. The book says that real-world existence alone doesn't justify an entity.

**Output:** subject-area diagrams (or a text entity list with relationships in "Each A must/may be … one/many B" form), the usage table, the scope and pruning decisions, and sample data.

---

## B. Review an existing schema against the universal patterns
**Inputs:** the DDL, ERD or entity list; the domain.
1. **Party test:** are there separate CUSTOMER, SUPPLIER and EMPLOYEE tables with duplicated name and address? Can one real party play several roles? Flag duplication and integration risk.
2. **Classification test:** does anything have a single category FK where the business classifies many ways? Look for hard-coded type columns that should be TYPE entities.
3. **Definition, instance and occurrence:** are type and instance conflated (e.g. a flights table mixing the schedule and the dated departure; products holding serial numbers)?
4. **History:** do status, price, rate, role and product-on-account history exist where the business asks "what was true then?"
5. **Many-to-many reality:** order ↔ shipment ↔ invoice, delivery ↔ claim, engagement ↔ work effort. Are 1:N shortcuts losing information (partial shipments, split claims, milestone billing)?
6. **Rules:** are business rules hard-coded in columns or code that change often (product eligibility, adjudication, loyalty earning)? Consider rules as data.
7. **Identifier inventory:** are issued numbers (phone, account, card) managed separately from contact data?
8. **Over-generalization check:** is the schema *too* generic (everything in PARTY / AGREEMENT / attribute-value tables), so constraints can't be enforced and queries are unreadable? Recommend subtyping or physical splits where the generic form costs more than it saves.

**Output:** findings (issue → consequence → recommended change → effort), ranked by integration and data-quality risk.

---

## C. Model an industry the book doesn't cover
1. **Find analogues** using the table in `patterns.md`. Examples:
   - Utilities: telecom deployment, usage and network, plus financial accounts.
   - Event venues: travel reservations, ticketing and experience.
   - SaaS: deployment usage, renewal billing, professional services for onboarding, e-commerce visits.
   - Logistics: manufacturing BOM/configuration, plus shipments and facilities.
   - Education: professional services engagements, plus travel-style scheduled offerings and reservations (classes as scheduled occurrences with capacity).
   - Property management: agreements, renewal billing, accounts, and facilities with fixed assets.
2. **Write the industry's vocabulary list** and map each term to a generic entity or an analogue entity.
3. **Follow playbook A from step 2.**
4. **Note the analogues used**, so later modellers understand where the structures came from.

---

## D. Combine several industries (conglomerates, diversified firms)
1. Agree one generic spine: PARTY, PRODUCT, AGREEMENT, WORK EFFORT, INVOICE/PAYMENT, ACCOUNTING.
2. Add industry subtypes under that spine rather than parallel structures. Example: PRODUCT → TRAVEL PRODUCT, FINANCIAL PRODUCT, INSURANCE PRODUCT.
3. Unify shared concepts: INCIDENT and CLAIM (health and insurance); NEED (financial and e-commerce); RISK ANALYSIS (insurance and financial); DEPLOYMENT USAGE (telecom and manufacturing).
4. Check the role model: one person may be a traveller, a cardholder and a policyholder. That integrated view is the payoff.

---

## E. Derive a star schema from the normalized model
1. Write the business questions. Choose the **process** (production run, usage record, claim item, account snapshot, time entry, travel experience, hit or visit) and the **grain**.
2. Take the measures from the transaction entity's attributes. Store additive components.
3. Take dimensions from the entities the transaction is many-to-one with. Flatten hierarchies into levels. Handle many-to-many with a bridge or allocation (`star-schemas.md`).
4. Choose the time grain, and add role-playing dates or facilities.
5. Add "not applicable" members, decide SCD types, and define reconciliation queries back to source.

**Output:** a fact and dimension spec (table, grain, measures with formulas, dimensions with levels, source mapping).

---

## F. Answer a "how do I model X?" question quickly
1. Identify the industry and subject area, and open that reference section.
2. Give the core entities and relationships in a few lines, in "Each A … B" form.
3. Name the key design decision and the book's choice, with the reason. Examples:
   - Parts are separate from products because one finished good is sold as several products.
   - Claims are analogous to invoices.
   - The account is separate from the product, so history survives product changes.
4. Mention the modern gap if relevant (privacy, current code sets, standards).
