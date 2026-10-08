# Reusable cross-industry constructs

The book files its models by industry for convenience, but says they should be **reused freely across industries**. Chapter 10 regroups them as modular constructs. This file extends that table with the recurring patterns behind them.

## The book's modular constructs (Chapter 10, paraphrased)

| Construct | Source models | Reuse it for |
|---|---|---|
| **Engineering** (specifications, documents, engineering change) | Manufacturing | Any design process: design firms, systems integrators, software and system design, architects |
| **Bill of materials** (BOMs, substitutes, configurations) | Manufacturing | Distributors that bundle, telecom equipment, repair vendors, anything assembled from parts |
| **Deployed product usage** | Telecom (and manufacturing) | Utilities (gas, electric, water), metered equipment, SaaS usage, manufacturers tracking end-user usage |
| **Facilities management** (network components, assemblies, circuits, capabilities) | Telecom | Utilities, oil and gas pipelines, any physical infrastructure network |
| **Geographic location** (pathway, point, boundary) | Telecom | Utilities, oil and gas, government, research, field operations, GIS-linked assets |
| **Payment settlement** (claims, adjudicated settlement amounts) | Health care | Anything paid after evaluation: lawsuit or arbitration settlements, warranty claims, expense reimbursements |
| **Product rules** | Insurance | Products governed by complex rules or regulation: securities, oil-well shares, regulated offerings |
| **Renewal billing** (premium schedule) | Insurance | Subscriptions and recurring billing: SaaS, hosting, card fees, mortgages, leases, rentals |
| **Product regulation** (regulation → requirement → rule) | Financial services | Any regulated offering: hazardous materials, weapons, telecom, pharma |
| **Accounts and account transactions** | Financial services | Billing accounts (utilities, wholesalers, telecom), wallets, prepaid balances, loyalty points |
| **Risk and segment analysis** | Financial services | Insurers, venture capital, credit scoring, churn or propensity scoring in any industry |
| **Engagement, time and billing** | Professional services | Any firm billing time, expenses or deliverables. Product firms providing support or consulting |
| **Preferences, reservations, ticketing, experience** | Travel | Event and venue ticketing, sports, appointments, rentals, anything selling scheduled capacity |
| **Internet visits and hits** | E-commerce | Any digital channel analytics |
| **Electronic object tracking** | E-commerce | Digital asset management: documents, images, media reused across channels |

## Recurring structural patterns

### 1. Party / role / relationship
Use one PARTY (person, organization, sometimes automated agent), with many PARTY ROLEs and PARTY RELATIONSHIPs between roles. The industry-specific vocabulary goes **only in role and relationship subtypes**.
- The test: can the same person be a patient *and* an employee *and* a payer? Then they're roles, not tables.

### 2. Type / instance / occurrence
| Type | Instance | Occurrence or usage |
|---|---|---|
| PART | INVENTORY ITEM | INVENTORY ITEM CONFIGURATION |
| NETWORK COMPONENT TYPE | NETWORK COMPONENT | DEPLOYMENT IMPLEMENTATION |
| PASSENGER TRANSPORTATION OFFERING | SCHEDULED TRANSPORTATION | SCHEDULED TRANSPORTATION OFFERING, then RESERVATION ITEM |
| FINANCIAL PRODUCT | ACCOUNT (via ACCOUNT PRODUCT) | ACCOUNT TRANSACTION |
| HEALTH CARE OFFERING | HEALTH CARE DELIVERY | CLAIM ITEM |
| PRODUCT | DEPLOYMENT | DEPLOYMENT USAGE |

### 3. Marketing offering ≠ physical or functional thing
- PRODUCT vs PART (manufacturing)
- PRODUCT vs CIRCUIT vs NETWORK ASSEMBLY (telecom)
- FINANCIAL PRODUCT vs ACCOUNT

One physical or functional thing can be sold as several products: residential vs business, consumer vs corporate.

### 4. Applicability with a type
X APPLICABILITY (product × feature, product × coverage × level, category × feature × setting) is typed **required / standard / optional / selectable**. This is how to configure offerings without schema changes.

### 5. Interaction / dependency / incompatibility
A recursive association on features or coverages: FEATURE INTERACTION, COVERAGE INTERACTION, TELECOM PRODUCT ASSOCIATION (dependency).

### 6. Rules as data
A RULE entity links to whatever it constrains and records its **source**: a regulation requirement, an agreement term, or internal policy. Rules are effective-dated and have factors or parameters.
- Examples: PRODUCT RULE, FINANCIAL PRODUCT RULE, ADJUDICATION RULE and FACTOR, TRAVEL PROGRAM RULE and FACTOR, INSURANCE RATE and FACTOR.

### 7. Analysis as a work effort
RISK ANALYSIS / ACTUARIAL ANALYSIS / ANALYSIS TASK, with weighted **parameters**, producing dated **outcome scores** against a target (party, account, asset type, market segment). The same structure serves underwriting, credit scoring and campaign targeting.

### 8. Commitment → fulfilment → billing bridges
Use many-to-many associative entities between stages, because grouping differs at each stage:
- order item ↔ shipment item ↔ invoice item
- engagement item ↔ work effort ↔ service entry ↔ invoice item
- service order item → deployment → usage ↔ invoice item
- health care delivery ↔ claim item ↔ settlement ↔ payment
- policy item premium ↔ invoice item

### 9. Master agreement governs transactions
AGREEMENT (with items, terms and price components) **governs** orders, engagements, reservations and tickets. Effective dates let you trace which terms applied to a given transaction.

### 10. Status history, roles per transaction
Every important transaction gets `X STATUS` (dated, typed) and `X ROLE` (party, role type, from/thru). Don't add more foreign-key columns per participant.

### 11. Recursion for structure, association entities for history
BOMs, assemblies, configurations, requirement breakdowns, category rollups, account and transaction relationships, claim resubmission. Add from/thru dates when the structure changes over time. Add a **seq id** to the key when the same pair can recur.

### 12. Inventory of identifiers vs contact info
The pool of identifiers you *issue* (phone numbers, account numbers, ticket numbers) is not the same as how you *reach* a party (CONTACT MECHANISM). Model the inventory separately, with assignment history.

### 13. Events and touch points
Model the customer experience as events: TRAVEL EXPERIENCE EVENT, HEALTH CARE VISIT, SERVER HIT within a VISIT, COMMUNICATION EVENT. Give each event roles, status, satisfaction and feedback. This is the basis for experience analytics.

## Combining industries
For conglomerates or diversified firms:
1. List the Volume 1 generic constructs everyone shares (party, product, agreement, invoice, accounting).
2. Pick the industry chapters that supply the extra constructs.
3. Merge on the generic spine: one PARTY, one PRODUCT supertype with industry subtypes, one AGREEMENT supertype.
4. Resolve naming collisions explicitly. INCIDENT in health care and in insurance is the same concept. CLAIM in health care (provider side) and in insurance (payor side) is the same entity seen from two ends.

Examples: a bank selling insurance; a manufacturer with field services (manufacturing + professional services + telecom-style deployment usage); a travel company with a loyalty credit card (travel + financial services).
