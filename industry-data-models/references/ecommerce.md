# E-commerce and the web (Chapter 9)

The chapter is for businesses that sell or engage online, whether online-only or as a channel alongside traditional sales.

**Concerns:**
- building a quality web presence
- customer satisfaction
- revenue and cost
- branding without cannibalizing other channels
- the visitor's experience

**Reuse:** products, orders and agreements, shipments (add an electronic delivery method), invoicing, work efforts (site development), accounting, HR. **Modify:** party roles and relationships, contact mechanisms, product (electronic objects), needs. **New:** web content and logins, objects, subscriptions, visits and server hits, two star schemas.

## Parties
- **AUTOMATED AGENT** is a new PARTY subtype alongside PERSON and ORGANIZATION: web servers, FTP servers, spiders, bots.
  - **The debate:** legally, an agent isn't a party, because it can't be held accountable. Transactionally, agents are everywhere on the web.
  - **Alternative:** keep AUTOMATED AGENT outside PARTY, with its own role subtypes (HOSTING SERVER, VISITING SERVER), and relate visits to both parties and agents.
  - *Today this question also applies to AI agents acting for users. Model who the agent acts for (a delegation relationship to a party), not just the agent itself.*
- **New roles:**
  - **WEBMASTER** (person)
  - **ISP** (organization)
  - **HOSTING SERVER** (automated agent role)
  - **REFERRER** (search engine, referring site)
  - **CONSUMER**: anyone who may or did buy. It's a supertype of **VISITOR**, **SUBSCRIBER**, **CUSTOMER** and **PROSPECT** (an alternative to keeping customer and prospect elsewhere).
- **Relationships:** **WEBMASTER ASSIGNMENT** (webmaster ↔ server), **HOST SERVER VISITOR** (ongoing visitor ↔ server), **VISITOR ISP**. Together they show which ISPs reach which servers, useful for partnerships and mirrors.
- **A role always has a party, but the party can be anonymous.** Keep the role → party relationship mandatory and make the person and organization name attributes optional.
  - Assign a party ID to unknown visitors and merge later when they're identified, so the profile isn't lost.

## Contact mechanisms
- ELECTRONIC ADDRESS gains **WEB ADDRESS (URL)** and **IP ADDRESS** subtypes. An IP address is the contact mechanism of a server or automated agent.
- **CONTACT MECHANISM LINK** models gateways (email → fax, email or URL → pager) and URL ↔ URL links.
  - Store only significant site links, or link volume will swamp the database.

## Web content and logins
- **WEB CONTENT** sits at a WEB ADDRESS. It has:
  - a **WEB CONTENT TYPE** (article, product description, company info)
  - **WEB CONTENT STATUS** (live, pending, retired)
  - a file location
  - **WEB CONTENT ROLE**s (author, webmaster, updater)
- **WEB CONTENT ASSOCIATION** (content containing content) carries a placement coordinate and a **FUNCTION TYPE** (scrolling list, radio box) for database-driven pages.
- **USER LOGIN** is per party per web address. It has **WEB USER PREFERENCE**s (of a preference type: show top-5 cruises, blue background) and **LOGIN ACCOUNT HISTORY**.
  - *Store credential hashes and change events only, never past or current plaintext passwords.*

## Electronic objects (storefront and catalog)
- **OBJECT** subtypes: **ELECTRONIC TEXT** (HTML), **IMAGE OBJECT**, OTHER OBJECT (applet, sound, video). It has an OBJECT TYPE (JPEG, GIF, streaming video…) and **OBJECT PURPOSE**s (web image, brochure).
- An object is linked to what it depicts via **PRODUCT OBJECT**, **FEATURE OBJECT** (e.g. the red variant) and **PARTY OBJECT**, and to where it's used via **OBJECT USAGE** in WEB CONTENT (and in marketing material).
- **Stored once, reused everywhere.** It also enables interest inference: a click on content about a "red" object for product X suggests interest in X-red.

## Needs and subscriptions
- **PARTY NEED** is for a CONSUMER, about a PRODUCT or PRODUCT CATEGORY, with a NEED TYPE (specific product, category interest, general need such as "high-powered engine"). It has a date identified and a description.
  - **Discovered via** a SERVER HIT (by business rule: an image click creates a need) or a COMMUNICATION EVENT (a web form submission is a WEB SITE COMMUNICATION; a phone call is another subtype).
  - Tell consumers how the data will be used.
- **SUBSCRIPTION** means formal **permission** (opt-in), unlike a need:
  - Subtypes: **NEWSGROUP**, **PRODUCT INFORMATION**, **USER GROUP**, OTHER.
  - For a SUBSCRIBER, about products, categories or need types, delivered to a chosen CONTACT MECHANISM.
  - Originates from an ORDER ITEM (paid), a COMMUNICATION EVENT, or a PARTY NEED.
- **SUBSCRIPTION ACTIVITY** (e.g. a newsletter edition) is made up of **SUBSCRIPTION FULFILLMENT PIECE**s sent per subscription. Anonymous subscribers work too: a party ID plus an email address.

## Visits and server hits
- A **web log** records per hit:
  1. IP address (possibly NATed)
  2. authuser
  3. datetime
  4. request (URL, method, protocol and version)
  5. status code
  6. bytes
  7. referrer
  8. user agent
  9. cookies

  "-" means unknown and is stored as null.
- **VISIT** is a session: from/thru datetime, cookie string, the hosting WEB ADDRESS, the VISITOR (role → party). It may result in ORDERs, which measures conversion.
- **SERVER HIT** has a datetime and number of bytes, plus:
  - USER LOGIN (authuser)
  - SERVER HIT STATUS TYPE
  - the visitor's IP ADDRESS
  - the **referring WEB ADDRESS** (held per hit for flexibility)
  - **USER AGENT**: of a USER AGENT TYPE (browser, spider, crawler), with PLATFORM TYPE, BROWSER TYPE, PROTOCOL TYPE and METHOD TYPE
  - the WEB CONTENT requested
- **Rules for defining a visit (business rules, not fixed):**
  1. **Every visitor maps to a party**, perhaps anonymous. Re-point visits to the real party when identified.
  2. **Visit boundary:** an inactivity timeout (30 minutes is common, but adjust for long videos and similar), optionally combined with an external referrer marking a new visit.
  3. **Visitor identity strength:** authuser > cookie > IP address. IPs are reassigned dynamically and shared behind NAT. Cookies can be shared across people on one machine and are refused by some users. The same IP on different days with different cookie behaviour is probably a different party, but you can't know.

## Star schemas
**SERVER_HIT_FACT:**
- **Measures:** number of hits, number of bytes, number of visits.
- **Dimensions:**
  - VISITORS
  - ISPS
  - REFERRERS (campaign effectiveness; search keywords from the referrer URL)
  - WEB_CONTENTS (page and object popularity, for advertisers)
  - USER_AGENT_TYPES (browser support; bot share)
  - USER_LOGINS
  - PRODUCTS, with a **blank "not applicable" product** member for non-product hits; browse-to-buy rates
  - TIME_BY_HOUR (capacity planning)
- For per-second volume, build a separate, narrower star (content, agent type, time).

**WEB_VISIT_FACT:**
- **Measures:** hits, pages visited, products inquired, products ordered, visits resulting in orders, average visit time.
- **Dimensions:** the same, minus WEB_CONTENTS, because there are many per visit.

## Modelling decisions to raise (much has changed since 2001)
- **Consent and privacy law** (GDPR, CCPA/CPRA, ePrivacy):
  - IP addresses and cookie IDs are personal data.
  - Model consent records (purpose, basis, timestamp, withdrawal), retention and deletion, and data-subject requests.
  - Subscriptions need provable opt-in.
- **Identity:** third-party cookies are largely gone. Use first-party IDs, logged-in identity, device and app IDs, and consented identity resolution with a probabilistic match confidence.
- **Analytics** usually live in event pipelines (clickstream) and warehouses rather than OLTP. The hit/visit/visitor/content dimensional design still holds.
- **ISP and browser-type** dimensions matter less today. Add channel, campaign (UTM), device and app, and experiment variant.
