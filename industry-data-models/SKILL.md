---
name: industry-data-models
description: 'Use when designing, reviewing, or extending a logical data model, database schema, or data warehouse for a specific industry: manufacturing (parts, BOMs, engineering change, MRP), telecommunications (network, circuits, deployment, usage billing), health care (episodes, visits, claims, payors), insurance (coverage, policies, underwriting, premiums, claims), financial services (accounts, transactions, product rules, risk scoring), professional services (engagements, time and expense, deliverables), travel (reservations, ticketing, travel experience, loyalty programs), or e-commerce (visitors, web content, subscriptions, visits and server hits). Also use when adapting generic party/product/order/agreement/work-effort/invoice patterns to an industry, choosing star schema facts and dimensions for these domains, or reusing one industry''s constructs in another. Based on Len Silverston''s "The Data Model Resource Book, Volume 2" (Revised Edition, 2001).'
---

# Industry Data Models (Universal Data Models, Volume 2)

**The book's lens.** Most enterprises share eight subject areas:
1. parties (people and organizations) and their roles and relationships
2. products
3. commitments (orders, agreements)
4. shipments, or delivery
5. work efforts
6. invoices
7. accounting and budgeting
8. human resources

An industry model is **not a new model from scratch**. It's the generic ("universal") model plus a few changes: subtyped roles, renamed commitments, a tailored product structure, and a handful of genuinely new structures. Silverston's advice is to model **generically within the industry**: build "travel", not "airline"; "insurance", not "auto insurance". That keeps the design stable when the business expands, integrates departments, and can still be narrowed later. The overriding goal is **integration**: one shared definition of party, product and transaction across the enterprise, never a separate silo per department.

## How to use this skill

1. **Find what's actually new.** For each subject area, decide whether the generic pattern is used as is, modified, not used, or whether a new model is needed. (Each chapter of the book opens with this table.) Usually the result is 70–90% reuse.
2. **Load the industry reference** for the domain (list below) and adopt its role subtypes, renamed commitments and new structures.
3. **Borrow across industries** when the problem fits, even if the industry name doesn't: `patterns.md`. For example, a ticketing business borrows travel reservations, and a utility borrows telecom deployment and usage.
4. **Use the notation and naming in** `conventions.md`. That includes TYPE entities, from/thru dates, roles and statuses as separate entities, and recursion for hierarchies.
5. **For analytics, derive star schemas from the normalized model**, not instead of it (`star-schemas.md`). Many-to-many relationships you didn't model become double-counted facts.
6. **Paraphrase into the user's vocabulary.** These are templates. Rename entities to match the business, but keep the structure.

## Quick rules (no references needed)

- **PARTY plus PARTY ROLE plus PARTY RELATIONSHIP**, never separate CUSTOMER, SUPPLIER and EMPLOYEE tables. Industry-specific roles are subtypes of role: PATIENT, CLIENT, TRAVELER, VISITOR.
- **Separate the thing from its classification** (PRODUCT vs PRODUCT CATEGORY, joined many-to-many through a classification entity) and **the definition from its occurrence**. Examples: a flight offering vs a scheduled flight; a product vs an inventory item; a network component type vs a network component.
- **Status, roles and type are separate entities**, with from/thru dates for history. Don't use a single status column if the history matters.
- **Keep the commitment, the delivery and the billing distinct.** Each has its own name per industry:

  | Industry | Commitment | Delivery | Billing |
  |---|---|---|---|
  | Generic | order | shipment | invoice |
  | Professional services | engagement | time/expense service entries | invoice |
  | Telecom | service order | deployment and usage | invoice |
  | Travel | reservation | travel experience | ticket/sale (prepaid) |
  | Health care | (no order) | health care delivery within visit and episode | claim |
  | Insurance | policy | (no delivery) | premium billing, and claims flowing back |
  | Financial services | financial agreement | account and account transactions | statement/notification |

- **Link the stages with associative entities** (order item ↔ shipment item, engagement item ↔ work effort, delivery ↔ claim item), because they're usually many-to-many.
- **Rules belong in data, not structure.** Product rules, coverage interactions, travel program rules and factors, and adjudication rules are rows, so the business can change them without schema changes.
- **Anonymous is still a party.** A web visitor with no known name still gets a party ID; the name attributes become optional.
- **Logical isn't physical.** Denormalize for performance (reservation systems are a classic case), but do it knowingly, starting from the normalized model.

## References

- `references/conventions.md`: notation (entities, subtypes, keys, relationships, arcs, recursion), naming standards, and the Volume 1 generic patterns every chapter extends.
- `references/patterns.md`: reusable cross-industry constructs (the book's "modularized" view). Use it when the industry isn't covered, or when a problem in one domain matches a construct from another.
- Industry references, each covering party roles, products, commitments, delivery, billing, new structures, star schemas and modelling decisions:
  - `references/manufacturing.md`: parts vs products, specifications, engineering change, BOMs, substitutes, configurations, deployment and usage, process plans, production runs.
  - `references/telecom.md`: carriers and billing agents, service products and features, network components and assemblies, circuits, communication IDs, service orders, deployment and usage billing.
  - `references/healthcare.md`: practitioners, providers, payors and insured parties, offerings, episodes, visits, deliveries, claims, settlements, referrals.
  - `references/insurance.md`: coverage types and levels, product rules, underwriting, applications, quotes, policies, premiums, incidents, claims, adjudication.
  - `references/financial-services.md`: needs, objectives and plans, product features and functional settings, regulations and rules, financial agreements and collateral, accounts, transactions, notifications, risk analysis.
  - `references/professional-services.md`: requirements, RFx, quotes and statements of work, engagements, rates, service entries, work efforts, invoicing.
  - `references/travel.md`: travel products and schedules, accommodation maps, reservations, ticketing and coupons, travel experience events, programs and accounts.
  - `references/ecommerce.md`: automated agents, web and IP addresses, web content and logins, product objects, needs, subscriptions, visits, server hits, and the rules for defining a visit.
- `references/star-schemas.md`: every star schema in the book (fact grain, measures, dimensions) and the pitfalls of building dimensional models without the normalized one.
- `references/playbooks.md`: procedures for building an industry model, reviewing an existing schema, adapting to an uncovered industry, combining industries, and deriving a star schema.
- `references/glossary.md`: key entities and terms.

## Limits (say these when they apply)

- **Published in 2001.** Domain specifics have moved on, so check current standards before building:
  - **Health care:** UB-92 became UB-04, HCFA-1500 became CMS-1500, ICD-9 became ICD-10-CM/PCS (US, 2015), DRG became MS-DRG. HIPAA X12 837/835 transactions, NPI identifiers and FHIR-based interoperability are absent.
  - **Telecom:** circuit-switched and landline-centric. Mobile, VoIP/SIP, number portability, eSIM and usage via mediation platforms all need extension.
  - **E-commerce:** Web 1.0 (ISP tracking, browser types, cookie-only identity). Privacy law (GDPR/CCPA), consent records, the end of third-party cookies, and mobile apps change what you may and should store. Never store passwords in "login account history": store hashes only.
  - **Financial services:** predates modern KYC/AML, open banking/PSD2, real-time payments and card tokenization.
  - **Industry classification:** the book references SIC codes. NAICS (US) and ISIC are the current schemes.
- **Templates, not standards.** These are one practitioner's well-tested patterns. The heavy use of generic supertypes (PARTY, AGREEMENT, WORK EFFORT) trades readability and constraint enforcement for flexibility. Keep only what the business actually needs. Silverston's own rule is that an entity belongs in the model only if the enterprise needs to maintain that information.
- **No attribute-level schemas here.** The book's appendices and the companion SQL products list full attributes. This skill captures entities, relationships and design reasoning, paraphrased. Design attributes for the actual requirements.
- **Volume 1 is assumed.** Where a generic pattern is only referenced (e.g. order roles, shipment routing, accounting), `conventions.md` summarizes it from how Volume 2 uses it, not from Volume 1 itself.

Condensed and paraphrased from Len Silverston, *The Data Model Resource Book, Volume 2: A Library of Universal Data Models by Industry Types* (Revised Edition, Wiley, 2001). For the full models, diagrams and attribute lists, see the book.
