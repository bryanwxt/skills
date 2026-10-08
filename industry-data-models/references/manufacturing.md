# Manufacturing (Chapter 2)

**Concerns:** design engineering, part management, bills of materials, MRP and just-in-time, distribution channels, tracking deployed products, and production runs.

**Reuse:** most party, contact, facility, order, shipment, invoice, accounting and HR models are used as is. **Modify:** party roles, product (add PART), inventory item status, and work effort (process plans). **New:** part specifications and documents, engineering change, part BOMs and substitutes, inventory item configurations, deployment and usage, production run star schema.

## Parties
- **Emphasis:** distribution channel, customer, supplier, contractor, employee.
- **DISTRIBUTION CHANNEL** (subtypes DISTRIBUTOR, AGENT) is related to an internal organization through DISTRIBUTION CHANNEL RELATIONSHIP.
  - A distributor buys and resells; an agent sells without taking ownership.
  - Distributors are deliberately **not** called customers, because their role is broader.
- **CUSTOMER** is the party that pays for, is shipped, or uses the product. Subtypes: **BILL TO**, **SHIP TO**, **END USER** customer. A party can play several at once.

## Products, parts, and inventory: three levels
| Level | Meaning | Example |
|---|---|---|
| PRODUCT | The *marketing offering*. It carries pricing, support plans and the name | "Super" consumer PC vs "Business" PC |
| PART | The *type of physical item* made or used | the one finished-good PC both products ship as |
| INVENTORY ITEM | A *physical instance* (serial or lot) | PC serial #123 |

- PART subtypes: **FINISHED GOOD** (ready to ship), **SUBASSEMBLY** (partly built, rarely bought or sold), **RAW MATERIAL** (the lowest level from this enterprise's point of view, bought whole).
  - The same item can be a raw material to one firm and a finished good to its maker.
- A finished good can be marketed as several products (one to many), so specifications attach to the **part**, and the product inherits them.

## Design engineering
- **PART SPECIFICATION** has a SPECIFICATION TYPE, so specifications are reusable across parts ("1500 MHz processing").
  - Subtypes: performance, constraint, testing requirement, tolerance, operating condition, other.
  - Has **PART SPECIFICATION STATUS** history (required → designed → tested → approved, each dated) and **PART SPECIFICATION ROLE**s (party responsible for design, testing, approval).
- **DOCUMENT** (PRODUCT DOCUMENT → drawing, model, engineering document, MARKETING MATERIAL; OTHER DOCUMENT) links to parts or products through **DOCUMENT APPLICABILITY**, because one brochure can cover a whole product line.
  - Stores a location pointer, and optionally the text or image.
- **ENGINEERING CHANGE**: request, notice and release are **statuses of one change**, not three entities.
  - It affects specifications or BOM lines through **ENGINEERING CHANGE IMPACT** (many-to-many), with its own status history and party roles (requested by, approved by…).

## Bills of materials
- Different functions see different breakdowns of the same item:
  - **engineering:** generic specified components
  - **manufacturing:** the actual parts chosen for cost, quality and availability
  - **marketing:** bundles such as PC + printer + T-shirt
  - **service:** what's actually installed
- **PART BOM** is a recursive part-to-part association, subtyped **ENGINEERING BOM** and **MANUFACTURING BOM**.
  - Key = parent part + child part + **seq ID**. The seq ID lets the same pair appear in both views, and reappear over time after being invalid. It carries quantity, instructions and from/thru dates.
- **MARKETING PACKAGE** is a subtype of PRODUCT ASSOCIATION for product bundles. Product-level BOMs stay in the product area.
- **PART SUBSTITUTE**: context-free substitution with a preference rank and quantity ("two 6-ft cords for one 12-ft").
- **PART BOM SUBSTITUTE**: substitution valid only within one assembly.
- **PART REVISION**: obsolescence and supersession. A revision is **not** a substitution.
- *Alternative:* one PART ASSOCIATION supertype over BOM, substitute and revision, mirroring PRODUCT ASSOCIATION.

## Inventory item configurations (as-built and as-maintained)
- **INVENTORY ITEM CONFIGURATION** is a recursive many-to-many between inventory items, with from/thru dates.
  - A child sits in only one parent at a time, but can move over time.
  - Subtypes: **MANUFACTURING CONFIGURATION** (what really went in, for defect tracing and legal exposure) and **SERVICE CONFIGURATION** (current configuration at the customer site, updated by technicians).
- **INVENTORY ITEM STATUS** becomes a history (good to deliver, defective, pending repair…), instead of Volume 1's single status.
- **INVENTORY ITEM** can be owned by a PARTY, for example consigned or customer-owned.

## Orders and MRP
- **PURCHASE ORDER ITEM** may be for a PART *or* a PRODUCT (exclusive). SALES ORDER ITEM is for PRODUCTs. Order items can be releases against agreements.
- **MRP needs no new structures.** It reads:
  - REQUIREMENTs, sales order items and sales agreements (demand)
  - purchase order items and purchase agreements (supply)
  - the manufacturing BOM and part substitutes (explosion)
  - inventory items by facility (on hand)
  - shipments (in transit)
  - product associations such as complements and substitutes (forecasting)

  The algorithms are out of scope, but the data is already modelled.

## Deployment and usage (installed base)
- **DEPLOYMENT** is an installation of a product, optionally a specific inventory item, at a FACILITY, with from/thru dates.
- **DEPLOYMENT USAGE** subtypes:
  - **ACTIVITY USAGE** (an event, e.g. an engine start)
  - **VOLUME USAGE** (a quantity in a UNIT OF MEASURE, e.g. copies made)
  - **TIME PERIOD USAGE** (per STANDARD TIME PERIOD)
- Supports warranty, service, usage-based billing and product-quality feedback. Telecom reuses the same structure.

## Process plans and production runs
- WORK EFFORT TYPE subtypes: **PRODUCTION RUN TYPE**, **PROCESS TYPE**, **PROCESS STEP TYPE**. They're recursive, defining the standard routing to make a part.
  - Standards per type: **SKILL STANDARD**, **GOOD (PART) STANDARD**, **FIXED ASSET STANDARD** (machines). These give estimated people, materials and equipment.
- Actual **production runs** are WORK EFFORTs of those types, using Volume 1's work effort structures (assignments, inventory issued, fixed asset assignments, time entries) and producing inventory items.

## Star schema: production runs
- **PRODUCTION_RUN_FACT** measures: cost, cost variance, duration, duration variance, quantity produced, quantity rejected.
- **Dimensions:** MANUFACTURED_PARTS, PLANT_LOCATIONS, RESPONSIBLE_PARTYS, PRODUCTION_RUN_TYPES, TIME_BY_DAY.
- **Use:** which plants, parts or run types overrun on cost or time, and where reject rates are highest.

## Modelling decisions to raise
- Do you need PART separate from PRODUCT? Yes when you design, build or assemble. A pure reseller can keep products only.
- Which BOM views does the business actually maintain? Don't build a marketing package if marketing never bundles.
- Is configuration tracking (serialized as-built and as-maintained) worth the data entry? Service technicians often won't update it, so plan the process, not just the table.
