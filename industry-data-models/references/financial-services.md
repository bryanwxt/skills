# Financial services (Chapter 6)

The chapter covers banks, lenders, credit unions, brokerages, securities and fund firms. Insurance is a specialized financial service with its own chapter.

**Concerns:**
- customer needs, objectives and plans
- highly configurable products
- regulation
- agreements and collateral
- accounts and transactions
- customer notifications
- risk and credit analysis

**Reuse:** contacts, communication events, invoicing (linked to statements), accounting, HR. **Modify:** party roles, product (features plus functional settings), agreements (financial agreements with assets). **Not used:** shipments (delivery is the account). **New:** needs, objectives and plans; product rules and regulations; account; account transaction; transaction tasks; account notification; analysis task; account and transaction star schemas.

## Parties
- **WORKER** is a supertype over EMPLOYEE and CONTRACTOR, so work can be assigned to either.
- **FINANCIAL INSTITUTION** can be internal or external. Subtype it (bank, broker, credit union…) if that adds clarity.
- **REGULATORY AGENCY** is central: frequent reporting and audits.
- **CUSTOMER** subtypes **INVESTOR** (provides money) and **LOAN CUSTOMER** (borrows). A party can be both.
- **PROSPECT** differs from a customer mainly in how much is kept and for how long. A party can be a customer of one internal organization and a prospect of another, which drives cross-selling.
- **Syndication:** a CONTROLLING SYNDICATOR leads a large deal and PARTICIPATING SYNDICATORs take shares of the risk.
- **Informal relationships** between person roles (business partners, influencers) matter for relationship banking, even when one party isn't a customer.

## Needs, objectives, plans
- **PARTY NEED** has a NEED TYPE and may be qualified by party type, financial product or product category ("interested in bond funds"). It's broader than Volume 1's REQUIREMENT.
- **PARTY OBJECTIVE** subtypes: **INVESTMENT OBJECTIVE** and **LENDING OBJECTIVE**. It has an objective type and from, thru and goal dates. State objectives in terms of risk tolerance.
- **PLAN** is a financial course of action:
  - PLAN TYPE (income, growth, venture…)
  - statuses (created, approved, shown to customer)
  - satisfies objectives and needs, with a **priority score** (1 = highest)
  - **PLAN ROLE** (planner, investor, beneficiary; from/thru)
  - **PLAN PRODUCT** (the products or categories proposed)

  Several alternative plans per customer are normal.

## Financial products
- A financial product is a **service defined by arrangements**, not a catalogued item. It may be predefined ("A+ Checking") or customized for one customer, and the same structure handles both.
- **PRODUCT CATEGORY**: INVESTMENT VEHICLE (mutual fund, security → fixed income, money market, equity; annuity), DEPOSIT (savings, checking, time deposit), LOAN, LEASE. Nested via **PRODUCT CATEGORY ROLLUP** for reporting.
- **PRODUCT FEATURE** is *what* the product has (monthly interest, ATM access, statements, per-check fee). **FUNCTIONAL SETTING** is *how it behaves* (interest compounded daily, fee charged per ATM transaction, statement sent yearly, renews annually).
- Applicability entities:
  - **PRODUCT FEATURE APPLICABILITY**: feature ↔ product
  - **FUNCTIONAL SETTING APPLICABILITY**: setting ↔ product or feature
  - **PRODUCT CATEGORY FEATURE APPLICABILITY**
  - **PRODUCT CAT FEAT FUNC APPLICABILITY**: which settings are valid for which feature within which category (a per-check fee only in CHECKING)
- Features and settings are the usual **negotiation points**. Customizing a product means choosing a different combination.

## Regulations and product rules
- **FINANCIAL REGULATION** subtypes **GOVERNMENT REGULATION** (federal, state, local) and **ORGANIZATION REGULATION** (internal policy). The text can be stored.
- A regulation is made up of **REGULATION REQUIREMENT**s.
- A **FINANCIAL PRODUCT RULE** comes from a regulation requirement *or* a customer **AGREEMENT TERM**. It affects any of: financial product, product category, product feature, functional setting.
  - Example: annual statements required, so no "send no statement" setting is allowed.
  - Example: fee disclosure applies to all checking and card categories.
  - Example: a negotiated "waive all ATM fees" overrides a standard setting.
- Rules constrain which applicabilities are allowed. Validate configurations against them.

## Agreements
- **FINANCIAL AGREEMENT** (subtype of AGREEMENT) splits into **LOAN AGREEMENT**, **INVESTMENT AGREEMENT** and **LEASING AGREEMENT**.
  - It starts with status "applied for", with items, terms and roles (owner, co-owner, co-signer, authorized user).
  - Use a separate APPLICATION entity only if there's substantial application data, as insurance does.
  - Acceptance results in an **ACCOUNT**. Rejection ends it, and closes the account if one was opened early.
- **ASSET** splits into FIXED ASSET (car, house, land) and INTANGIBLE ASSET (security, estimated income).
  - **ASSET ROLE**: a party's role in an asset (owner, part-owner) with **equity value**. It's an independent fact, reused across agreements.
  - **AGREEMENT ASSET USAGE** (of an ASSET USAGE TYPE): the asset used in an agreement or agreement item as collateral, and/or as the thing being purchased. One asset can have several usages in one loan.
  - **Business rules:** only an owner may pledge, and only up to available equity. Whether an asset is required depends on agreement type and risk.

## Accounts (the delivery mechanism)
- **Keep three things distinct:**
  - **product**: how the service works
  - **agreement**: what was promised, on what terms
  - **account**: the record of activity

  Not every product has an account; bill-pay can ride on an existing one.
- **ACCOUNT** subtypes follow the product category (CHECKING ACCOUNT…).
  - **ACCOUNT PRODUCT** (from/thru) lets the product behind an account change (standard → enhanced checking) while account history stays intact.
- **ACCOUNT ROLE**: owner (tax liability), joint owner, approved user, power of attorney, guarantor, account manager, portfolio manager.
- **ACCOUNT RELATIONSHIP**: ATM or debit card ↔ checking; credit line as overdraft backup; replaced account ↔ old account (stolen card), preserving credit history.
- **PARTY ACCOUNT MEDIA** (of a MEDIA TYPE: card, checks, software) is per account role, so each holder has their own card, with **PARTY ACCOUNT MEDIA STATUS** (active, inactive, lost).
- **ACCOUNT STATUS** history: new → active → review → closed.

## Account transactions
- **ACCOUNT TRANSACTION** splits into:
  - **FINANCIAL TRANSACTION**: DEPOSIT, WITHDRAWAL, ACCOUNT FEE, INTEREST, DIVIDEND, ACCOUNT PAYMENT, ADJUSTMENT/REVERSAL; **SECURITY TRANSACTION** (BUY, SELL); **MUTUAL FUND TRANSACTION** (PURCHASE, REDEMPTION, EXCHANGE)
  - **ACCOUNT REQUEST TRANSACTION** (non-monetary): SPECIAL REQUEST, CHANGE REQUEST, INQUIRY REQUEST
- It may come via a party account media item (debit card, ATM).
- **ACCOUNT TRANSACTION STATUS**: posted, on hold, completed, rejected (NSF).
- **ACCOUNT TRANSACTION RELATIONSHIP**: a reversal ↔ the original; an ATM withdrawal → account debit → overdraft draw on the card → transfer deposit; cross-provider sweeps (checking withdrawal ↔ brokerage deposit).
- **ACCOUNT TRANSACTION TASK** subtypes POST, AUTHORIZE and **PRE-DETERMINED** (scheduled) transaction tasks, with a **TIME FREQUENCY** (monthly transfer, a standing investment instruction). It records creation date, requested date, and the actual run and status.

## Notifications and analysis (work efforts)
- **ACCOUNT NOTIFICATION** (a WORK EFFORT) subtypes:
  - **INVOICING TASK**: produces an INVOICE
  - **STATEMENT TASK**: produces a STATEMENT, driven by a STATEMENT FEATURE and its settings
  - **MARKETING TASK**: cross-sell, often triggered by life events
  - **ALERT TASK**: posting errors, suspected fraud
  - **OTHER NOTIFICATION TASK**: past due, skip-payment, fee changes
- INVOICE becomes a subtype of notification output alongside STATEMENT. They're separate even when sent together.
- **ANALYSIS TASK / RISK ANALYSIS** is a variant of insurance underwriting:
  - **ANALYSIS PARAMETER**s are weighted (income, debt level, amount borrowed, time in job, payment history).
  - The result is **ANALYSIS OUTCOME** scores per parameter, rolled up.
  - Targets: **PARTY TARGET** (behavior score), **ACCOUNT TARGET** (account score), or a **MARKET SEGMENT** of accounts or parties (MARKET SEGMENT ACCOUNT, MARKET SEGMENT PARTY), e.g. a credit-limit increase for a whole segment.
  - Scores are dated by assessment date and re-run over time.

## Star schemas
**ACCOUNT_FACT** (account profitability and activity):
- **Measures:** number of accounts, average balance, average return (derived from interest, dividends, sell − buy, redemption − purchase), number of transactions.
- **Dimensions:**
  - FACILITYS (branch, ATM, call center, web), with geo levels 1–3
  - INTERNAL_ORGANIZATIONS
  - FINANCIAL_PRODUCTS (product → category → rollup)
  - OWNERS (from the "owner" account role; with industry/SIC)
  - ACCOUNT_MANAGERS (from the account or portfolio manager role)
  - MARKET_SEGMENTS
  - TIME_BY_WEEK

**ACCOUNT_TRANSACTION_FACT:**
- **Measures:** number of transactions, total transaction amount.
- **Dimensions:** same as above plus **ACCOUNT_TRANSACTION_TYPES**, with **TIME_BY_DAY**. Filter to "posted" transactions rather than adding a status dimension.
- **Answers:** interest earned by product over time; volumes by branch or ATM by day, for capacity; dividends by owner; activity by segment.

## Modelling decisions to raise
- **Product configurability vs complexity.** Features × settings × categories × rules is powerful but hard to govern. Model only the levels the business actually varies.
- **Ledger integrity.** Account transactions here are logical. A real core banking ledger needs immutable postings, double entry, value vs booking dates and running balances.
- **Missing today:** KYC/AML (customer due diligence, sanctions screening, beneficial ownership), consent and open-banking access, card tokenization, real-time payments, IFRS 9 / CECL credit-loss staging, and positions and holdings for securities.
