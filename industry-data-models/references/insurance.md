# Insurance (Chapter 5)

The chapter covers insurance providers (underwriters that carry the risk), agencies, brokers, administrators and TPAs, across property, casualty, life, disability and health.

**Concerns:** product and coverage definition, underwriting and rating, applications and quotes, policy administration, premium scheduling and billing, incidents, claims and settlement, regulatory rules.

**Reuse:** contacts, facilities, communication events, invoices and payments, work efforts, accounting, HR. **Modify:** party roles, product (insurance product and coverage), pricing (rate tables), quotes, agreements (policy). **New:** coverage structures, product rules, underwriting and actuarial analysis, insurance rates, applications, policy items and enrollment, premium schedules, incidents, insurance claims, adjudication and settlement, claim star schema.

## Parties
- **Roles:**
  - INSURANCE PROVIDER (underwriter)
  - **DISTRIBUTION CHANNEL** → INSURANCE AGENCY, INSURANCE BROKER
  - INSURANCE AGENT (person)
  - CLAIMS ADJUSTER
  - INSURANCE ADMINISTRATOR (services the product without underwriting, e.g. for self-insured employers)
  - PAYOR
  - REGULATORY AGENCY
  - INSURANCE PARTNER
  - INSURANCE ASSOCIATION (publishes standard forms, risk practices and language)
  - PROSPECT and SUSPECT (an unqualified lead)
  - TRUSTEE, BENEFICIARY
  - **INSURED PARTY**
  - **FINANCIALLY RESPONSIBLE PARTY** (responsible for premiums and the insured asset)
  - DEPENDENT
- **Relationships:** insured ↔ agent, agent ↔ provider, **insured ↔ provider** (the core one, tied to the policy), distribution channel relationship, partnership (risk-sharing between insurers).

## Products and coverage
- **INSURANCE PRODUCT** gets several independent classifications through PRODUCT CATEGORY CLASSIFICATION:
  - line: property, casualty, life, disability, health
  - individual vs group
  - target industry or market

  Categories roll up for reporting.
- **COVERAGE TYPE** (bodily injury, collision, hospitalization…) can be composed of other types (**COVERAGE TYPE COMPOSITION**) and categorized (**COVERAGE CATEGORY**).
- **COVERAGE LEVEL** subtypes: **amount** (a limit), **range** (from/thru, e.g. 100k/300k), **deductible**, **copay**, **coinsurance**. Levels can have a **COVERAGE LEVEL BASIS** (per person, per incident, per year…).
- **COVERAGE AVAILABILITY** = product × coverage type × coverage level, typed **required / standard / optional / selectable**. It's the same applicability pattern as product features.
- **COVERAGE INTERACTION**: coverages that require or exclude one another.
- **PRODUCT FEATURE** (non-coverage aspects, e.g. a policy loan or accidental-death rider) with categories. **PRODUCT FEATURE COVERAGE** links features to coverages.
- **PRODUCT RULE**:
  - Applies to a product, feature, coverage level, coverage type or insured asset type.
  - Originates from an internal organization or a regulator.
  - Examples: minimum liability limits by state; who is eligible.
  - Rules are data, so they can change without schema changes.

## Underwriting and rating
- **Two rating approaches:**
  - **Community-based rating**: a broad pool of similar risk, so standard **rate tables**.
  - **Experience-based rating**: a specialized or individual risk, rated case by case. It reuses the same analysis structures and feeds POLICY ITEM PREMIUM directly.
- **RISK ANALYSIS** is a WORK EFFORT made up of **ACTUARIAL ANALYSIS** efforts.
  - An actuarial analysis targets a product, feature, coverage type or level, and an **INSURED TARGET** (an asset type).
  - It weighs **ANALYSIS PARAMETER**s (region, driver age, mileage…) in order of importance and produces an actuarial score.
- **INSURANCE RATE ANALYSIS SOURCE** links an analysis to the rates or factors it created (many-to-many).
- **INSURANCE RATE** is the rate amount for a coverage type and level, qualified by:
  - geographic boundary
  - party type
  - **risk level** (high, medium, low)
  - insured asset type
  - **INSURANCE FACTOR**s
  - period type (per month…)

  Rates and factors are effective-dated. Expect frequent change and many factors, so keep the structure flexible.

## Applications and quotes
- **APPLICATION** has status, roles, **APPLICATION ITEM**s, and the **INSURED ASSET**s described.
- **QUOTE** has QUOTE ROLEs, QUOTE TERMs and QUOTE ITEMs (per insured asset, with a quoted premium), plus issue date and valid from/thru dates.
- The party's **INCIDENT** history feeds the quote. MOTOR VEHICLE INCIDENT has subtypes MOTOR VEHICLE TICKET and MOTOR VEHICLE ACCIDENT.

## Policies
- **INSURANCE POLICY** is a subtype of AGREEMENT:
  - Lines: HEALTH, LIFE, CASUALTY, PROPERTY, DISABILITY.
  - Crossed with **INDIVIDUAL vs GROUP POLICY**.
  - Parties attach through AGREEMENT ROLEs (insured, owner, beneficiary, payor, agent, administrator).
  - **One insurance product per policy.**
- **POLICY ITEM** has per-line subtypes. Each item is for a coverage type and level (or a product feature), and optionally an **INSURED ASSET** (vehicle, building, person).
- Special or "rider" risks (flood, scheduled valuables) are additional items with their own premiums.
- **Group health enrollment:**
  - GROUP (the employer's eligible population)
  - **ENROLLMENT** (an individual joining)
  - **ENROLLMENT ELECTION** (chosen coverages and levels, including dependents)
  - **CARE PROVIDER SELECTION** (chosen PCP or network)
- Group administration can involve an underwriter and a separate administrator. Self-insured employers use an administrator.

## Premiums and billing
- **PREMIUM SCHEDULE** per policy, with a PERIOD TYPE (monthly, quarterly…).
  - It carries valid from/thru, **insured from/thru** (the coverage period paid for), due date and amount. It may originate from INSURANCE RATE.
- **POLICY ITEM PREMIUM** is the premium per policy item. It needs no dates, because they're inherited from the schedule.
- **POLICY PREMIUM ADJUSTMENT** applies after re-underwriting, e.g. +20% after a speeding ticket.
- **POLICY ITEM PREMIUM BILLING** is the many-to-many from premium to INVOICE ITEM. It records what was actually billed vs what was due. The invoice goes to the financially responsible party, and coverage lapses if it's unpaid.

## Incidents and claims
- **INCIDENT** is an event causing or related to loss, with **INCIDENT ROLE**s (cause, victim, witness, reporter) and an INCIDENT TYPE.
  - **INCIDENT PROPERTY DAMAGE** holds the damage per insured asset (description, restore cost).
  - Incidents are tracked **even without a claim**, because they affect risk.
- **CLAIM** is a report of loss **under one policy**:
  - Subtypes HEALTH CARE, PROPERTY, DISABILITY, LIFE (plus CLAIM TYPE).
  - Has CLAIM RESUBMISSION, CLAIM STATUS and CLAIM ROLE.
- **CLAIM ITEM** relates to incidents through **INCIDENT CLAIM ITEM** (many-to-many). It's for an insured asset or a specific damage. Health items link to deliveries via HEALTH CARE DELIVERY CLAIM SUBMISSION, reusing the health care model.
- **CLAIM ITEM DOCUMENT**: appraisals, photos, proof of death, medical records.

## Settlement
- The **CLAIMS ADJUSTER** performs an **APPRAISAL** (valuation of the insured asset).
- **CLAIM SETTLEMENT** is per claim item. **ADJUDICATION RULE**s apply:
  - **ELIGIBILITY**: is it covered?
  - **AUDIT**: are the codes and data correct?
  - **PRICING**: how much is paid?

  Rules have **ADJUDICATION FACTOR**s, e.g. "jewelry not itemized → cap $2,000".
- **CLAIM SETTLEMENT AMOUNT**s (deductible, usual and customary, disallowed, payment) carry an **EXPLANATION OF BENEFIT TYPE**. An appeal produces another settlement.
- **PAYMENT** with **REMITTANCE NOTICE**s, sent to several parties through **REMITTANCE NOTICE PARTY** (the insured, the provider).

## Star schema: claims
- **CLAIM_FACT** (settled claim items) measures:
  - claim_item_requested_amount
  - claim_payment_amount
  - estimated_cost (the cost to process the claim)
- **Dimensions:**
  - TIME_BY_DAY
  - PARTY_TYPES (e.g. the insured's industry)
  - GEOGRAPHIC_BOUNDARYS
  - **RISK_LEVEL_TYPES**
  - INSURED_ASSET_TYPES
  - INSURANCE_PRODUCTS and PRODUCT_CATEGORYS
  - COVERAGE_TYPES and COVERAGE_LEVELS
- **Purpose:** feedback into underwriting. Are rates per region and risk level in line with losses? Which coverages or asset types need exclusions? Is a $50 collision deductible worth offering?

## Modelling decisions to raise
- **Policy as an AGREEMENT subtype** (integration) vs its own table (clarity, performance). The logical model says subtype. The physical design may split it.
- **Rules-as-data granularity.** Adjudication and product rules can become a rules engine. Model rule identity, scope and effective dates; let an engine hold the logic.
- **Missing today:** reinsurance and treaties, reserves (case and IBNR) by claim, subrogation, endorsements as policy versions, IFRS 17 / LDTI measurement, and ACORD data standards.
