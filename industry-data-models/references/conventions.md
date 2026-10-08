# Conventions and the generic (Volume 1) foundation

## Notation (how to read and draw the models)

| Element | Convention |
|---|---|
| Entity | Rounded box, singular noun, UPPER CASE in prose (ORDER). Include it only if the enterprise needs to maintain that information. Real-world existence alone isn't enough |
| TYPE entity | Suffix TYPE for a classification (ORDER TYPE) as opposed to an instance (order #23987). Shown on the diagrams even though it's usually just an ID and a description, because it marks where the allowed values live |
| Subtype | Box inside the supertype box. It inherits the supertype's attributes and relationships, to any depth. A subtype set should be **complete and mutually exclusive**. Add an OTHER… subtype to keep it complete. Finer classifications go in the TYPE entity rather than as more subtypes |
| Non-mutually-exclusive subtype sets | Each independent set sits in its own unnamed box inside the supertype. Example: REQUIREMENT is CUSTOMER vs INTERNAL, *and also* PRODUCT vs WORK requirement |
| Attribute markers | `#` primary key, `*` mandatory, `o` optional |
| Relationship line | Solid half = mandatory from that side; dotted half = optional. Crow's foot = many. Read it as "Each A {must be/may be} *name* {one and only one / one or more} B, *over time*" |
| "Over time" | Add it to test cardinality. Something that looks one-to-one (an order's status) becomes one-to-many once you need history |
| Many-to-many | Never drawn directly. Always resolved by an intersection (associative) entity that may carry its own attributes, typically from/thru dates |
| Foreign keys | Not drawn as attributes, because the relationship implies them. A **tilde (~)** across a relationship means the parent key is part of the child's primary key (e.g. ORDER ITEM = order ID + order item seq ID). Associative entities always inherit both keys this way, usually plus a from date |
| Exclusive arc | A curve across two or more relationships: exactly one of them applies (an inventory item is at a FACILITY *or* in a CONTAINER) |
| Recursion | One-to-many: an entity points to itself (a work effort redone via another). Many-to-many: an association entity, often subtyped (WORK EFFORT ASSOCIATION → DEPENDENCY, BREAKDOWN) |
| Few one-to-ones | Normalization usually merges them |
| Star schemas | Physical tables. Dimension tables are named in the **plural** (PRODUCTS) and may denormalize hierarchies (product category becomes a level in PRODUCTS) |

### Attribute naming suffixes
- **ID**: system-generated surrogate key.
- **seq id**: sequence within a parent (order item seq ID).
- **code**: a user-defined meaningful key (geo code "CO").
- **name**: a proper noun.
- **description**: the text for a code or ID.
- **flag / ind**: a binary value.
- **from date / thru date**: both **inclusive**. "Thru" is used rather than "to" precisely to signal the inclusive end.

## The generic patterns every industry chapter extends

These are summarized from how Volume 2 uses them. Volume 1 has the full models.

### Parties
- **PARTY** is the supertype of **PERSON** and **ORGANIZATION**. Organization splits into LEGAL ORGANIZATION (corporation, government agency) and INFORMAL ORGANIZATION (team, family, other).
- **PARTY ROLE** is subtyped into person roles (EMPLOYEE, CONTRACTOR, CONTACT, FAMILY MEMBER…), organization roles (INTERNAL ORGANIZATION, SUPPLIER, COMPETITOR, ASSOCIATION, HOUSEHOLD, REGULATORY AGENCY, DISTRIBUTION CHANNEL, ORGANIZATION UNIT → PARENT, SUBSIDIARY, DIVISION, DEPARTMENT…), and roles either can play (CUSTOMER, PROSPECT, SHAREHOLDER…).
- **PARTY RELATIONSHIP** connects two roles: EMPLOYMENT, ORGANIZATION CONTACT, SUPPLIER RELATIONSHIP, CUSTOMER RELATIONSHIP, ORGANIZATION ROLLUP, PARTNERSHIP, and so on. It has its own type, status, priority and from/thru dates.
- **CONTACT MECHANISM** (POSTAL ADDRESS, TELECOMMUNICATIONS NUMBER, ELECTRONIC ADDRESS) links to parties through **PARTY CONTACT MECHANISM** (from/thru) and its **PURPOSE**s. **CONTACT MECHANISM LINK** relates one mechanism to another.
- **COMMUNICATION EVENT** records interactions between parties, with a purpose, roles and status.
- **FACILITY** is a physical place (warehouse, plant, office, room). Geographic boundaries are separate.
- **PARTY QUALIFICATION / PARTY SKILL** come from the human resources area.

### Products
- **PRODUCT** splits into GOOD and SERVICE. PRODUCT CATEGORY joins it many-to-many via PRODUCT CATEGORY CLASSIFICATION, and categories nest via a rollup.
- **PRODUCT FEATURE** (color, size, billing option…) is attached through **PRODUCT FEATURE APPLICABILITY**, typed *required / standard / optional / selectable*.
- **PRODUCT ASSOCIATION**: component (bill of materials for products), substitute, obsolescence, complement, incompatibility.
- Further areas: SUPPLIER PRODUCT, INVENTORY ITEM (a specific instance or lot, at a facility or container), PRICE COMPONENT (base, discount, surcharge; by geography, party type, quantity, agreement…), ESTIMATED PRODUCT COST.

### Commitments
- **REQUIREMENT** (need) → **REQUEST** (RFI/RFQ/RFP) → **QUOTE** → **ORDER**. Each has items, roles and statuses.
- **ORDER / ORDER ITEM** are subtyped SALES vs PURCHASE, with ORDER ROLEs and contact mechanisms.
- **AGREEMENT** is the longer-term governing contract. It has AGREEMENT ITEMs, AGREEMENT TERMs, AGREEMENT ROLEs and pricing, and governs orders ("agreement to orders").

### Delivery, work, money
- **SHIPMENT / SHIPMENT ITEM** links to ORDER ITEM (order shipment) and to INVOICE ITEM (shipment billing). It also covers route segments, packages, receipts and issuances.
- **WORK EFFORT** (project, activity, task, production run, maintenance…): has associations (breakdown and dependency), party assignments, fixed-asset and inventory assignments, TIME ENTRY / TIMESHEET, rates, statuses and requirements.
- **INVOICE / INVOICE ITEM** for products, features, work efforts and time entries. It has roles, statuses and terms. PAYMENT links to invoices through **PAYMENT APPLICATION**, with a payment method.
- **Accounting and budgeting** (GL accounts, transactions, budgets) and **human resources** (positions, fulfilment, pay, benefits, skills). These rarely need industry changes.

## Recurring modelling moves in Volume 2

1. **Subtype the roles and relationships.** Every chapter does this first: new person roles, organization roles and relationship subtypes. Drop generic ones that don't apply (e.g. professional services drops CUSTOMER in favour of CLIENT).
2. **Rename the commitment** to the industry's word (engagement, reservation, policy, financial agreement, service order) but keep the order/item/role/status skeleton.
3. **Split the definition from the instance, and the instance from the occurrence:**
   - PART vs INVENTORY ITEM
   - NETWORK COMPONENT TYPE vs NETWORK COMPONENT
   - PASSENGER TRANSPORTATION OFFERING vs SCHEDULED TRANSPORTATION
   - FINANCIAL PRODUCT vs ACCOUNT
4. **Use applicability entities** (feature × product × category, with an applicability type) rather than hard-coding which options go with which offerings.
5. **Use a rule entity linked to whatever it constrains** (product, category, feature, coverage, setting), sourced from a regulation, an agreement term or internal policy.
6. **Use a "bridge" associative entity between stages** (DEPLOYMENT USAGE BILLING, HEALTH CARE DELIVERY CLAIM SUBMISSION, ENGAGEMENT WORK FULFILLMENT, POLICY ITEM PREMIUM BILLING).
7. **Keep statuses as history entities with dates** (claim, account, transaction, reservation item, travel experience event, inventory item).
8. **Use recursion for structure:** BOMs, configurations, network assemblies, requirement breakdowns, product category rollups, account and transaction relationships, group hierarchies.
9. **Finish each chapter with star schemas** whose facts come from the transaction entities just modelled.
