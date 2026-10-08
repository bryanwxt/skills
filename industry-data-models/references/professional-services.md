# Professional services (Chapter 7)

The chapter covers law and accounting firms, consultancies, staffing and placement agencies, cleaning and administrative contractors, and any firm that bills for people's time or deliverables. It's also relevant to product firms that sell services alongside goods.

**Concerns:**
- client value
- margins and professionals' cost
- revenue and volume
- differentiation
- on-time, on-budget delivery

**Reuse:** contacts, facilities, product pricing and costing, suppliers of products, agreements, shipments (for physical deliverables), accounting, HR. **Modify:** party roles, product (service subtypes, skills), product associations, requirements, requests, quotes, orders (renamed engagements), time entry (generalized to service entries), invoicing. **Not used:** inventory item storage, usually.

## Parties
- **New roles:**
  - **PROFESSIONAL**: a person able to deliver services, whether employee or contractor
  - **CLIENT** (replaces CUSTOMER), subtyped **BILL TO CLIENT** and **DELIVERY CLIENT**
  - **PROFESSIONAL SERVICES PROVIDER**: an internal division *or* an outside firm (subcontractor, prime contractor, competitor)
- **Generic roles dropped:** FAMILY MEMBER, HOUSEHOLD, REGULATORY AGENCY, DISTRIBUTION CHANNEL, CUSTOMER.
- **Relationships:** **CLIENT RELATIONSHIP** (client ↔ internal organization) and **SUBCONTRACTOR RELATIONSHIP** (either direction), plus employment, organization contact, supplier and rollup.
- An outside professional is PROFESSIONAL + CONTRACTOR + a contact of their own firm.

## Products
- **PRODUCT** splits into GOOD (pamphlets, software licences) and SERVICE.
  - SERVICE subtypes: **DELIVERABLE BASED SERVICE** (a predefined work product: patent filing, audit report, enterprise data model) and **TIME AND MATERIALS SERVICE** (a standard offering billed by rate, e.g. an hourly audit).
  - The same service can exist in both forms as two product instances.
- **PRODUCT DELIVERY SKILL REQUIREMENT**: the skill types needed to deliver each product. It drives staffing.
- Classifications include **PRODUCT INDUSTRY CATEGORIZATION** and **TECHNICAL PRODUCT CLASSIFICATION**.
- Features: SERVICE FEATURE (one vs two trademarks), BILLING FEATURE (biweekly, monthly), SOFTWARE FEATURE (source code included).
- **Pricing:** add a **rate** to PRICE COMPONENT. **Costing:** relate ESTIMATED PRODUCT COST to SUPPLIER PRODUCT if you track other firms' costs, otherwise directly to PRODUCT.
- **Product associations:**
  - MARKETING PACKAGE replaces component (service bundles, without quantity or instructions)
  - obsolescence and complement kept
  - substitute dropped
  - incompatibility rarely needed

## Requirements, requests, quotes
- **REQUIREMENT** has two independent subtype sets:
  - **who needs it:** CLIENT REQUIREMENT vs INTERNAL REQUIREMENT (e.g. your subcontracting needs)
  - **what is needed:**
    - **RESOURCE REQUIREMENT** (placement). It has NEEDED SKILLs with years and level, number of positions, start and end dates, and duties.
    - **PROJECT REQUIREMENT** (outcomes). It has NEEDED DELIVERABLEs of a DELIVERABLE TYPE.
    - **PRODUCT REQUIREMENT** (a standard offering), with DESIRED FEATUREs.
  - It's recursive (an overall need broken into detailed ones), at a FACILITY.
  - It has REQUIREMENT ROLEs (needer, servicer, recruiter, applicant) and REQUIREMENT STATUS (active, pending client approval, cancelled, filled by another firm, closed).
- **REQUIREMENT COMMUNICATION** links COMMUNICATION EVENTs whose purpose is requirement activity (résumé submission, sales meeting, interview, proposal), optionally naming the PROFESSIONAL concerned. Light-weight proposals can live here rather than in QUOTE.
- **REQUEST** subtypes RFI, RFP, RFQ, with REQUEST ROLEs and **RESPONDING PARTY**s (competitors bidding).
  - REQUEST ITEMs point to a requirement, needed deliverable, needed skill, desired feature or product. The same need can be requested repeatedly across RFI → RFP.
- **QUOTE / QUOTE ITEM** adds STATEMENT OF WORK as a subtype alongside PROPOSAL.
  - A statement of work assumes agreement exists and confirms it in writing.
  - Quote items can be for a skill type (contract labour), product feature, deliverable type, product or work effort.
  - Quote items lead to **ENGAGEMENT ITEM**s, not orders.

## Engagements (the "order")
- **ENGAGEMENT / ENGAGEMENT ITEM** subtypes:
  - **PROFESSIONAL PLACEMENT**: hiring a specific person for a period, via PROFESSIONAL ASSIGNMENT
  - **CUSTOM ENGAGEMENT ITEM**: bespoke work
  - **PRODUCT ORDER ITEM**: STANDARD SERVICE ORDER ITEM, DELIVERABLE ORDER ITEM, GOOD ORDER ITEM
  - OTHER
- **Why one structure for placements and deliverables:** a staffing firm can expand into projects, and a consultancy into placements, without redesign. Invoicing is unified.
- **ENGAGEMENT RATE** (RATE TYPE: regular, overtime, weekend; UNIT OF MEASURE: hour, day; from/thru) holds both the billing rate and the professional's cost, because rates change during long engagements.
- **ENGAGEMENT WORK FULFILLMENT** is the many-to-many between engagement items and WORK EFFORTs. Commitments can be stated differently from how projects are managed (one item → per-country projects; three items → one project).
- Use standard order roles and contact mechanisms. Keep regular purchase orders for the buy side.

## Agreements
- **PROFESSIONAL SERVICES AGREEMENT** has subtypes **CLIENT AGREEMENT** (master terms: payment, NDA, service terms) and **SUBCONTRACTOR AGREEMENT**.
- Agreements and their items carry terms and price components that **govern** engagements and engagement rates. It's the "master agreement → statements of work" pattern.

## Delivery: service entries
- **SERVICE ENTRY** subtypes:
  - **TIME ENTRY**: amount of time, unit of measure, billing rate (defaulted from the engagement rate, overridable), **cost** paid to the professional
  - **EXPENSE ENTRY**
  - **MATERIALS USAGE**
  - **DELIVERABLE TURNOVER**: completion handed to the client

  All have from/thru datetime, description and **billable indicator**.
- **SERVICE ENTRY HEADER** (a generalized timesheet) is submitted by a PROFESSIONAL. It's named for the concept, not the paper form.
- **Where entries attach:**
  - **Placement or contract firms:** professional → PROFESSIONAL ASSIGNMENT → engagement item, with entries against the **engagement item**.
  - **Deliverable or project firms:** professionals assigned to WORK EFFORTs (project, activity, task) that fulfil engagement items, with entries against the **work effort**.

  The combined model allows either per entry.
- Don't relate entries to PROFESSIONAL ASSIGNMENT directly. The header already identifies the professional.
- Physical deliverables (reports, media) use normal shipments.

## Invoicing
- **INVOICE ITEM** can bill PRODUCTs, PRODUCT FEATUREs, SERVICE ENTRYs (many entries → one item) or WORK EFFORTs (with a **percentage** for partial or milestone billing).

## Star schema: time entries
- **TIME_ENTRY_FACT** measures:
  - dollars billed (rate × time)
  - hours billed (converted via the unit-of-time conversion)
  - cost
  - gross margin

  The book defines gross margin as cost ÷ dollars billed. Conventionally it's (billed − cost) ÷ billed, so confirm which the business means.
- **Dimensions:**
  - PROFESSIONALS
  - CLIENTS (from the engagement "client" role)
  - PROJECTS (work efforts of subtype project, by project type)
  - RATE_TYPES
  - ENGAGEMENT_ITEM_TYPES (placement vs product order vs custom)
  - TIME_BY_DAY
- **Answers:** utilization and profitability per professional, client, project type and engagement style.

## Modelling decisions to raise
- Do service entries attach to the engagement item, the work effort, or both? Decide per firm type.
- Rate history vs per-entry override: keep both. The override is common.
- **Modern additions:** capacity and resource planning (bookings vs actuals), utilization targets, revenue recognition (ASC 606 / IFRS 15: percentage of completion, milestones), WIP and unbilled, and retainers and prepayments.
