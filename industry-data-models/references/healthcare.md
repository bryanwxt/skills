# Health care (Chapter 4), from the provider's point of view

**Concerns:** quality of care and outcomes; patient, practitioner, provider and payor relationships; the clinical record of incidents, episodes, visits and deliveries; claims and getting paid; referrals.

**Reuse:** contact mechanisms, facilities (with subtypes), communication events, accounting, HR. **Modify:** party roles and relationships, product (health care offerings), agreements (policies, provider agreements), invoices (as a parallel to claims), payments. **Not used:** orders (appointments are visit statuses) and shipments. **New:** incidents, episodes, visits, deliveries, diagnosis and outcomes, claims submission, claim settlement, referrals, episode outcome star schema.

## Parties
- **Person roles:**
  - **INDIVIDUAL HEALTH CARE PRACTITIONER** (physician, nurse, therapist…)
  - **PATIENT**
  - INSURED INDIVIDUAL, subtyped **INSURED CONTRACT HOLDER** and **INSURED DEPENDENT**
- **Organization roles:**
  - **HEALTH CARE PROVIDER ORGANIZATION** (subtypes INSTITUTION such as a hospital, and PRACTICE)
  - **HEALTH CARE NETWORK**, e.g. an HMO or PPO network
  - **GROUP** (recursive: employer groups, sub-groups)
  - **EMPLOYER**
  - **THIRD PARTY ADMINISTRATOR**
  - **INSURANCE PROVIDER**
  - **PAYOR** (whoever actually pays the claim: an insurer, a self-insured employer or a TPA)
  - **HEALTH CARE ASSOCIATION**
  - **INSURED ORGANIZATION**
- **Relationships:**
  - **PATIENT PRACTITIONER RELATIONSHIP**, flagging whether the practitioner is the patient's primary care provider (PCP)
  - **PATIENT PROVIDER RELATIONSHIP**
  - **PRACTICE AFFILIATION** (practitioner ↔ practice or institution)
  - **PROVIDER NETWORK RELATIONSHIP**
  - **FAMILY DEPENDENCY**
  - **PRACTITIONER REFERRING RELATIONSHIP**
- **Practitioner details:**
  - PARTY QUALIFICATION and PARTY SKILL (degrees, board certifications)
  - **LICENSE** held per GEOGRAPHIC BOUNDARY (state), with from/thru dates
- **Patient details:** **MEDICAL CONDITION** (allergies, chronic conditions) and **PHYSICAL CHARACTERISTIC** (height, weight, blood type) as dated histories.
- **FACILITY** subtypes: hospital, clinic, ward, room, operating room, and so on.

## Health care offerings (products)
- **HEALTH CARE OFFERING** splits into:
  - **SERVICE OFFERING**: PROCEDURE OFFERING, OTHER SERVICE
  - **GOOD OFFERING**: DME (durable medical equipment), PHARMACEUTICAL, NEUTRACEUTICAL, SUPPLY, AID
- **PROVIDER OFFERING** records which provider offers what (with pricing). **HEALTH CARE CATEGORY OFFERING** categorizes offerings.
- **A diagnosis is not an offering.** It's a clinical finding, modelled separately.
- **CERTIFICATION REQUIREMENT** (of a CERTIFICATION TYPE) records offerings that need prior approval from an insurer's medical management, or a prerequisite such as a specialist's prescription.

## Agreements
- **PATIENT PROVIDER AGREEMENT**: consent and financial responsibility.
- **PROVIDER NETWORK AGREEMENT**: contracted rates with a network.
- **INSURANCE POLICY**: a subtype of AGREEMENT, though a designer may physically store it separately.
  - Subtyped **GROUP INSURANCE POLICY** (covers an insured organization's GROUP) and **INDIVIDUAL INSURANCE POLICY**.
  - Both cover insured individuals through **COVERED INDIVIDUAL**.
  - Coverage levels are left to the insurance chapter. Providers usually phone the insurer for benefits.
- **Patient ≠ insured.** Link them through PARTY: the same party plays both roles. Don't add a direct patient-to-policy relationship.

## Clinical delivery (replaces orders and shipments)
- **No orders.** You can't predetermine the services before the visit. An appointment is a **visit status** (scheduled, confirmed, arrived, cancelled, no-show).
- **INCIDENT** is an event that may cause care (car accident, epidemic), with an employment-related indicator.
- **HEALTH CARE EPISODE** is an injury or illness, possibly arising from an incident. It has an EPISODE TYPE.
- **HEALTH CARE VISIT** is for a PATIENT, at a FACILITY or at home, with VISIT STATUS history and VISIT ROLEs.
  - **VISIT REASON** links it to episodes, **SYMPTOM**s (which may later be tied to an episode), or free text.
- **HEALTH CARE DELIVERY** subtypes: **EXAMINATION**, **PROCEDURE DELIVERY**, **DRUG ADMINISTRATION**, **SUPPLY ADMINISTRATION**, **DME DELIVERY**.
  - Each is of a HEALTH CARE OFFERING, within a visit, optionally for an episode.
  - It has **DELIVERY ROLE**s (performing, assisting, ordering practitioner), status, and a **DELIVERY ASSOCIATION** (e.g. a drug given as part of a procedure).
- **DIAGNOSIS** (of a DIAGNOSIS TYPE) has **PRACTITIONER DIAGNOSIS** (several practitioners may diagnose) and **DIAGNOSIS TREATMENT** (which deliveries treated which diagnosis).
- **DELIVERY OUTCOME** and **EPISODE OUTCOME** are typed by OUTCOME TYPE. They make outcome analysis possible.

## Claims: the "invoice" of health care
- The book models claims by **analogy to invoices**:

  | Invoice | Claim |
  |---|---|
  | INVOICE / INVOICE ITEM | CLAIM / CLAIM ITEM |
  | resubmission, status | CLAIM RESUBMISSION, CLAIM STATUS (submitted, pending, denied, returned for correction, settled) |
  | shipment billing | HEALTH CARE DELIVERY CLAIM SUBMISSION (delivery ↔ claim item, many-to-many) |
  | payment application | CLAIM SETTLEMENT ↔ PAYMENT, many-to-many |

  Building one model from the other is a useful quality check.
- **CLAIM** subtypes follow the standard forms: **INSTITUTIONAL** (UB-92 then, UB-04 now), **MEDICAL / professional** (HCFA-1500 then, CMS-1500 now), **DENTAL** (ADA), **HOME CARE**.
- It has **CLAIM ROLE**s: enterer, submitter, claim manager. The patient is derivable through delivery → visit, but is usually stored as a role for practicality.
- **One claim is under exactly one INSURANCE POLICY**, but one delivery can go on several claim items. That handles coordination of benefits and resubmission after an unsatisfactory settlement.
  - Coordination-of-benefits *rules* stay in business logic, not the model.
- **Codes:**
  - **CLAIM SERVICE CODE** is a supertype over CPT, HCPCS and revenue (REV) codes.
  - **DIAGNOSIS TYPE** has an ICD subtype, linked many-to-many through **CLAIM ITEM DIAGNOSIS CODE**.
  - **DRG CLASSIFICATION** groups diagnosis and service codes for payment.
  - The supertypes keep the model **neutral to code-set changes**. That design held up when ICD-9 became ICD-10.
- **Standards:** the book says to follow HIPAA and HL7 for interchange and security; the model expresses requirements, not an interchange format. Today that also means X12 837/835/270/271, NPI, and FHIR resources such as Encounter, Condition, Procedure, Claim and ExplanationOfBenefit, which map closely onto these entities.

## Payments and settlement
- **PAYMENT** (from party → to party) subtypes: **INSURANCE RECEIPT**, **PATIENT RECEIPT**, **SUPPLIER DISBURSEMENT**. PAYMENT TYPE covers refunds and others; PAYMENT METHOD TYPE covers cash, card and so on.
- **CLAIM SETTLEMENT** is made up of **CLAIM SETTLEMENT AMOUNT**s. Subtypes:
  - **DEDUCTIBLE**
  - **USUAL AND CUSTOMARY** (may vary by geography)
  - **DISALLOWED**, with an **EXPLANATION OF BENEFIT TYPE**
  - **CLAIM PAYMENT**

  These could instead be attributes.
- **PAYMENT APPLICATION** applies patient payments to HEALTH CARE DELIVERYs directly (co-pays, uncovered services) or to INVOICEs. **HEALTH CARE DELIVERY BILLING** links deliveries to invoice items, including corrections.

## Referrals
- **PRACTITIONER REFERRING RELATIONSHIP** records habitual referral patterns by diagnosis or episode type ("for heart attack, Dr. James refers to Dr. Smith").
- **HEALTH CARE REFERRAL** records an actual referral for a patient, by date, about an episode or diagnosis.
- "Referral must come from the PCP" is enforced through the PCP flag on PATIENT PRACTITIONER RELATIONSHIP.

## Star schema: episode outcomes
- **HEALTH_CARE_EPISODE_FACT** measures: number of episodes, number of visits, number of deliveries, average episode length, total charges.
- **Dimensions:**
  - **OUTCOME_TYPES**, the key dimension
  - EPISODE_TYPES, DIAGNOSIS_TYPES, INCIDENT_TYPES
  - INDIVIDUAL_HEALTH_CARE_PRACTITIONERS, HEALTH_CARE_PROVIDER_ORGANIZATIONS
  - PATIENT_TYPES
  - TIME_BY_WEEK
- **Other analyses named:** financial, HR (from Volume 1), claims (reuse the insurance claim star), and delivery-level outcomes.

## Modelling decisions to raise
- **Provider vs payor perspective.** This chapter is the provider's. Payors need the insurance chapter's coverage and adjudication models.
- **Privacy and security.** PHI requires access control, audit and minimum-necessary design. These are absent from a 2001 logical model.
- **Map to FHIR or HL7 early** if interoperability is a goal. Keep the episode/visit/delivery separation, because it maps cleanly to them.
