# Star schemas

## Principles from the book
- **Model first, then dimensionalize.** A star schema built without understanding the normalized model produces wrong numbers. Two examples:
  - **Many-to-many classification:** if a product is in several categories, summing by category double-counts.
  - **Mismatched grain:** if shipment items and invoice items are many-to-many, a shipment-grain fact can't carry invoice amounts correctly.
- Star schemas are **physical** designs. Dimension tables are plural, and hierarchies are flattened into levels (product → category → rollup; facility → geo level 1/2/3).
- Each chapter's star is a **template**. Start from the enterprise's actual questions.
- Pick time granularity to match the question: TIME_BY_HOUR (usage, web hits), TIME_BY_DAY (transactions, production runs, travel), TIME_BY_WEEK (accounts, episodes). Add a finer level only if needed. Very fine grain (per second) belongs in a separate, narrow star.
- **Role-playing dimensions:** use the same dimension twice with different meanings (start and end hour; departure and arrival facility).
- **"Not applicable" member:** add a blank row (e.g. a blank product for hits not about a product) so the fact foreign keys stay mandatory.
- **Filter rather than dimensionalize** when only one state matters, e.g. only "posted" transactions.

## Catalogue

| Industry | Fact (grain) | Measures | Dimensions |
|---|---|---|---|
| Manufacturing | PRODUCTION_RUN_FACT (production run) | cost, cost variance, duration, duration variance, qty produced, qty rejected | manufactured parts, plant locations, responsible parties, production run types, time by day |
| Telecom | DEPLOYMENT_USAGE_FACT (usage record) | quantity, billing amount | customers, usage types, units of measure, products, facilities, time by hour (start), time by hour (end) |
| Health care | HEALTH_CARE_EPISODE_FACT (episode) | # episodes, # visits, # deliveries, avg episode length, total charges | **outcome types**, episode types, diagnosis types, incident types, practitioners, provider organizations, patient types, time by week |
| Insurance | CLAIM_FACT (settled claim item) | requested amount, payment amount, estimated processing cost | time by day, party types, geographic boundaries, risk level types, insured asset types, insurance products and categories, coverage types, coverage levels |
| Financial services | ACCOUNT_FACT (account snapshot) | # accounts, average balance, average return, # transactions | facilities (+ geo levels), internal organizations, financial products (+ category, rollup), owners, account managers, market segments, time by week |
| Financial services | ACCOUNT_TRANSACTION_FACT (transaction) | # transactions, total amount | as above + account transaction types; time by day |
| Professional services | TIME_ENTRY_FACT (time entry) | dollars billed, hours billed, cost, gross margin | professionals, clients, projects, rate types, engagement item types, time by day |
| Travel | TRANSPORTATION_OFFERING_FACT (travel experience) | # experiences, sales $, + comments, − comments, avg satisfaction, on-time arrivals, on-time departures, avg minutes late | travel providers, travel products, accommodation classes, departure facilities, arrival facilities, transportation vehicles, time by day |
| Travel | non-transportation fact (hotel or car experience) | the first five measures above | travel providers, travel products, accommodation classes, travel accommodation assets, time by day |
| E-commerce | SERVER_HIT_FACT (hit) | # hits, # bytes, # visits | visitors, ISPs, referrers, web contents, user agent types, user logins, products, time by hour |
| E-commerce | WEB_VISIT_FACT (visit) | # hits, # pages, # products inquired, # products ordered, # visits with orders, avg visit time | as the hit star, minus web contents |

The book also points to Volume 1's financial and HR stars for every industry, and reuses the insurance claim star for provider claims analysis.

## Checks before shipping a star
1. **State the grain** in one sentence. Every measure must be additive (or explicitly semi-additive, like balances) at that grain.
2. For each dimension, confirm the fact-to-dimension relationship is **many-to-one** at that grain. If it's many-to-many (categories, diagnoses per claim item, owners per account), use a bridge table, an allocation weight, or a "primary" designation, and document the choice.
3. **Derived measures** (average return, gross margin, on-time %) should be stored as additive components (sum of return, sum of billed, count on time, count total) and computed at query time. Averages of averages are wrong.
4. **Slowly changing dimensions:** products, rates, risk levels and segments change. Decide whether each dimension is type 1 or type 2. Volume 2 assumes the from/thru history exists in the source.
5. **Reconcile** fact totals to the operational system: billed amounts to invoices, claim payments to payments.
