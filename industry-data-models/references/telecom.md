# Telecommunications (Chapter 3)

**Concerns:**
- the network (provisioning, engineering, construction, turn-up)
- service availability at order time
- feature-rich service products
- number inventory
- usage capture and billing, often through other carriers

**Reuse:** most party, contact, order, invoice, accounting and HR models. **Modify:** party roles, product (service subtypes and features), product associations, orders (service orders), invoicing (billing agents, usage billing). **New:** deployment, network components and assemblies, circuits, capabilities, communication identifiers, deployment usage, usage star schema.

## Parties
- New organization roles:
  - **TELECOMMUNICATIONS CARRIER**: other carriers you interconnect or resell with.
  - **BILLING AGENT**: a party that bills on another carrier's behalf, e.g. a local exchange carrier billing for long distance.
- Matching relationships: CARRIER RELATIONSHIP and BILLING AGENT RELATIONSHIP.
- CUSTOMER is split into **RESIDENTIAL CUSTOMER** and **ORGANIZATION CUSTOMER**.

## Products
- **SERVICE** subtypes:
  - **CONNECTIVITY SERVICE**: local, long distance, wireless, dedicated line, internet access
  - **CONNECTIVITY FEATURE**: call waiting, caller ID, vanity number…
  - **LISTING OFFERING**: directory listings
  - **CHANNEL SUBSCRIPTION**: content channels
  - **INSTALLATION AND REPAIR**
  - **SERVICE AGREEMENT OFFERING**: maintenance plans
  - **CREDIT CARD OFFERING**: calling cards
- **GOOD** subtypes: SYSTEM, DEVICE, ACCESSORY.
- PRODUCT FEATURE subtypes:
  - **BILLING FEATURE**: usage-based vs flat rate, bill monthly
  - **AVAILABILITY FEATURE**: e.g. 24×7
  - **PERFORMANCE CHARACTERISTIC**: bandwidth, noise rating
  - OTHER
- **PRODUCT FEATURE APPLICABILITY** is typed required / standard / optional / selectable.
- **PRODUCT FEATURE INTERACTION** has subtypes INCOMPATIBILITY and DEPENDENCY. It can be qualified by the product it applies within.
- **PRICE COMPONENT** has subtypes ONE-TIME CHARGE, RECURRING CHARGE and UTILIZATION CHARGE (per unit of usage).
- **TELECOM PRODUCT ASSOCIATION** adds a DEPENDENCY subtype to complement, incompatibility and substitute. An association can depend on the **network component type** the deployment runs on (e.g. a feature works only on certain switch types).

## Deployment (the installed service)
- **DEPLOYMENT** is a product installed for a customer (from/thru dates). It replaces "shipment" as the delivery concept.
  - **FACILITY DEPLOYMENT** records where it lives: central office, customer location.
  - **DEPLOYMENT FEATURE** records the features *selected and installed*. PRODUCT FEATURE APPLICABILITY records those *available*.
- Deployments can relate to agreements (service agreements) and to listings (**LISTING** for directory entries).

## Network (asset structure)
- **NETWORK COMPONENT** is a serializable physical instance, either installed or in inventory:
  - **SUPPORT STRUCTURE**: pole, manhole, tower
  - **SERVER**: SWITCH, ROUTER, COMMUNICATION APPEARANCE (a port or line appearance)
  - **DEVICE**: amplifier, filter, loading coil, frequency shifter
  - **CONNECTION COMPONENT**: cable, fiber, wire
- **NETWORK COMPONENT TYPE** is recursive, so types can be composed of types.
- Components sit at **GEOGRAPHIC LOCATION**s with subtypes **PATHWAY** (a route), **POINT** (coordinates) and **BOUNDARY** (an area). These support outside-plant mapping and GIS.
- **NETWORK ASSEMBLY** is a configured grouping of components (e.g. a switch frame). It's built from **NETWORK COMPONENT ASSEMBLY** (which component in which assembly, from/thru) and nested via **NETWORK ASSEMBLY STRUCTURE**. **CONFIGURATION SETTING**s hold parameters.

### Product vs network vs circuit
| | Is | Example |
|---|---|---|
| PRODUCT | what's marketed | residential line, business line |
| NETWORK COMPONENT / ASSEMBLY | the physical parts that provide it | switch port, copper pair |
| CIRCUIT | the *functional* capability, a logical path | a voice-grade circuit, which both lines may share |

- **CIRCUIT PRESENCE** maps a circuit onto the assemblies it uses (many-to-many).
- **DEPLOYMENT IMPLEMENTATION** ties a deployment to the circuits and/or assemblies that implement it, and can use a number assignment (below).
- **CAPABILITY TYPE** links many-to-many to NETWORK ASSEMBLY TYPE, CIRCUIT TYPE and PRODUCT (via ...CAPABILITY intersections), answering "what can this kind of equipment, circuit or product do?". Move it to instance level if capabilities vary by instance.

## Communication identifiers (number inventory)
- **COMMUNICATION IDENTIFIER** is the carrier's *inventory* of numbers (phone, fax, cell…), with statuses (available, reserved, assigned, aging…).
  - It's deliberately **separate from CONTACT MECHANISM**, which is "how to reach a party". They serve different purposes.
  - An optional link between them helps data integrity, but many firms won't maintain it.
- **COMMUNICATION ID ASSIGNMENT** attaches a logical number to a physical COMMUNICATION APPEARANCE (port), with from/thru dates.
- Numbers can be **reserved by a SERVICE ORDER ITEM** before deployment.

## Orders and availability
- **SERVICE ORDER / SERVICE ORDER ITEM** is a subtype of order for provisioning. Each item is fulfilled by a DEPLOYMENT, and order items can link to deployment implementations.
- The **three "is it available?" questions**:
  1. Is the product available at the central office serving the customer's area? Answer from products, circuits and assemblies, deployments, and associations.
  2. Is it permitted by company or regulatory policy? Use a rules structure; the book defers this, pointing to the insurance and financial product-rule models.
  3. Is there network capacity under the current load? Answer from assemblies, circuits and their current utilization.

## Usage and billing
- **DEPLOYMENT USAGE** subtypes:
  - **CALL DETAIL**: from/to number, start/end datetime. Store the called-from number even though it can be derived, because deployments change.
  - **VOLUME USAGE**: e.g. megabytes.
  - **TIME PERIOD USAGE**: e.g. a monthly flat charge.

  Each has a USAGE TYPE and UNIT OF MEASURE.
- **BILLING AGENT ASSIGNMENT** designates who bills for a deployment (from/thru, changeable over its life) and drives invoicing.
- **DEPLOYMENT USAGE BILLING** is the many-to-many between usage records and INVOICE ITEMs. Recurring and one-time charges bill from the deployment and price components.

## Star schema: deployment usage
- **DEPLOYMENT_USAGE_FACT** measures: quantity (of usage) and billing amount.
- **Dimensions:**
  - CUSTOMERS
  - USAGE_TYPES
  - UNITS_OF_MEASURE
  - PRODUCTS
  - FACILITYS (central office / location)
  - TIME_BY_HOUR, used twice for start and end (a role-playing dimension)
- **Use:** traffic by hour for capacity, revenue by product and customer segment, usage patterns by office.

## Modelling decisions to raise
- Keep circuits (logical) and assemblies (physical) separate even if today they map one to one. Products change faster than the network.
- Decide how deep the asset model goes. Outside plant (poles, cable) vs inside plant (switch ports) often live in different systems; the model integrates them.
- **Modern extensions the book lacks:** mobile subscriptions (SIM/eSIM, IMSI/MSISDN as communication identifiers), number portability, VoIP/SIP endpoints, mediation-platform usage records (CDR/xDR/IPDR), bundles and plans with allowances, and rating vs billing separation.
