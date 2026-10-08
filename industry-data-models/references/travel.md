# Travel (Chapter 8)

The chapter covers airlines, rail, bus, cruise, hotels, car rental and travel agencies: carrying passengers and accommodating travellers. The book treats them as one industry, because carriers, passengers, reservations and tickets are common to all.

**Concerns:**
- the traveller relationship
- convenient booking
- an enjoyable experience before, during and after the trip
- loyalty incentives
- cost control

**Reuse:** most party models, contacts, facilities, supplier products, pricing, costing, associations, agreements (with new subtypes), payments, work efforts (maintenance), accounting, HR. **Modify:** party roles, product definition (replaced), orders (renamed reservations), agreements to orders (replaced with agreements to reservations and tickets). **Not mainstream:** inventory storage, invoicing (payment is usually in advance; invoicing is mostly supply side or agency billing). **New:** travel preferences, travel products and scheduling, accommodation maps, reservations, ticketing, travel experience, travel programs and accounts, two star schemas.

## Parties
- **Person roles:**
  - **INDIVIDUAL CUSTOMER** → **TRAVELER/PASSENGER**, **INDIVIDUAL PAYER**, **TRAVEL ACCOUNT MEMBER**. These are independent: someone may pay without travelling, or travel only on an employer's account.
  - **TRAVEL STAFF** (flight attendant, purser)
  - **OPERATIONS CREW** (mechanics, ground crew)
  - plus PROSPECT, CONTACT, EMPLOYEE, DEPENDENT (for family travel demographics)
- **Organization roles:**
  - **TRAVEL PROVIDER**:
    - **TRAVEL CARRIER**: AIRLINE, CRUISE LINE, train, bus
    - **HOTEL PROVIDER**
    - **CAR RENTAL PROVIDER**
  - **TRAVEL PORT AUTHORITY**: the organization running an airport or port; the facility itself is separate
  - **DISTRIBUTION CHANNEL** → TRAVEL AGENCY
  - **TRAVEL PARTNER**, **TRAVEL ASSOCIATION**, REGULATORY AGENCY
  - ORGANIZATION CUSTOMER (corporate accounts), HOUSEHOLD, SUPPLIER
- **Relationships:** INDIVIDUAL CUSTOMER RELATIONSHIP, ORGANIZATION CUSTOMER RELATIONSHIP, DISTRIBUTION CHANNEL RELATIONSHIP, **TRAVEL PARTNERSHIP** (alliances), and carrier presence at a port (e.g. "major hub").

## Travel preferences
- **PARTY TRAVEL PREFERENCE** (from/thru) applies to individuals *and* organizations (e.g. "all employees fly coach").
- It can point at a **TRAVEL PREFERENCE TYPE** (seat, meal, smoking, bed, car type), an **ACCOMMODATION CLASS**, a **TRAVEL PRODUCT** (e.g. a particular flight), a **PRODUCT CATEGORY** or a **FACILITY**.
- History matters: an aisle preference replacing window, effective on a date.

## Travel products: you sell availability, not items
- **TRAVEL PRODUCT** subtypes:
  - **PASSENGER TRANSPORTATION OFFERING**: FLIGHT, BUS, TRAIN, SHIP, OTHER
  - **HOTEL OFFERING**: a room type, at specific HOTELs (FIXED ASSETs)
  - **RENTAL CAR OFFERING**: a car class, fulfilled by RENTAL VEHICLEs
  - **AMENITIES OFFERING**: meals, drinks, headsets
  - **ITEM OFFERING**: souvenirs
  - OTHER

  This covers your own, partners' and competitors' offerings.
- **TRAVEL PRODUCT REFERENCE NUMBER** (from/thru): the public number (flight 1234) can change while the offering stays the same.
- **Three levels** for transport:

  | Level | Is | Example |
  |---|---|---|
  | PASSENGER TRANSPORTATION OFFERING | a route between origin and destination FACILITYs, with **REGULARLY SCHEDULED TIME**s (departure and arrival time and day; changeable) | Monday 10:30 NY → Philadelphia train |
  | **SCHEDULED TRANSPORTATION** | a dated occurrence, with actual dates and times, using a **TRANSPORTATION VEHICLE** | the 2 Oct run, on aircraft #2545 |
  | **SCHEDULED TRANSPORTATION OFFERING** | what's *sellable* on that occurrence per **ACCOMMODATION CLASS**, with quantity and from/thru | 20 first, 200 coach seats |

- **ACCOMMODATION MAP** gives a vehicle's (or hotel's) physical capacity per class. Sellable quantity can exceed it, because of **overbooking**.
- **TRAVEL PRODUCT COMPLEMENT**: amenities with flights, hotel + cruise packages.
- The model records which provider offers which scheduled transportation and owns which fixed assets.

## Reservations (orders)
- **RESERVATION** (header, with created and completed timestamps for agent efficiency) has **RESERVATION ROLE**s: agent, requester (who may not travel), supervisor.
- **RESERVATION ITEM** is for a SCHEDULED TRANSPORTATION OFFERING, a HOTEL OFFERING (+ the specific HOTEL) or a RENTAL CAR OFFERING (+ the pickup facility).
  - It may reserve an **ACCOMMODATION SPOT** (SEAT NUMBER or ROOM NUMBER) from the map.
  - It has **RESERVED TRAVELER**s: several per item, e.g. a lap child or a shared room.
  - It has **RESERVATION PREFERENCE** overrides (only preference *types* apply at this point) and **RESERVATION ITEM STATUS** (reserved, booked, cancelled).
- **Physical note:** production reservation systems use one big denormalized record for speed. The logical model still shows items, to capture the true requirements.

## Ticketing (unique to travel)
- **COUPON** is per reservation item and per segment (NY → SF, SF → Tokyo), with a seat number. Coupons are grouped into a **TICKET** (e.g. a round trip).
- A ticket also links directly to the TRAVELER and SCHEDULED TRANSPORTATION OFFERING, because tickets can be issued **without** a reservation.
- **COUPON COMPONENT / TICKET COMPONENT** (of a COMPONENT TYPE) is the price breakdown: fare, taxes, port charges, fees.
- **SALE** groups tickets and other items. It's paid via PAYMENT APPLICATION directly, or via an INVOICE.
- Some items (car rental) produce no coupon, because they're paid at pickup.

## Agreements and pricing
- **AGREEMENT** subtypes:
  - **CORPORATE TRAVEL AGREEMENT**: volume discounts
  - **DISTRIBUTION CHANNEL AGREEMENT**: agency terms
  - **PARTNERSHIP AGREEMENT**: alliances
  - **TRAVELER AGREEMENT**: ticket terms and conditions, with history
  - EMPLOYMENT, OTHER
- **PRICE COMPONENT**s come from travel products *and* agreements and affect RESERVATION ITEMs and TICKETs. Agreement dates trace which terms applied to a ticket.

## Delivery: the travel experience
- **TRAVEL EXPERIENCE** is for exactly **one traveller**. It optionally links to a reservation item, ticket, coupon or sale (walk-ups have no reservation), or directly to the offering if no reservation or ticket describes it.
- **TRAVEL EXPERIENCE EVENT** records the "touch points":
  - BAGGAGE HANDLING, TICKETING, CHECK IN, SEAT ASSIGNMENT, BOARDING, MEAL DELIVERY, AMENITIES DELIVERY, CUSTOMER SERVICE EVENT
  - HOTEL CHECKOUT, RENTAL CAR CHECKOUT, OTHER (via an event type)
- Each event has **EVENT ROLE**s (who served), **STATUS** history (e.g. baggage location progression), the ACCOMMODATION SPOT used, an optional **SATISFACTION RATING**, and linked COMMUNICATION EVENTs of purpose **TRAVELER FEEDBACK** (complaints, compliments, surveys).
- WORK EFFORTs (repairs, damaged-bag claims) can link back to the event that caused them.

## Travel programs and accounts (loyalty)
- **TRAVEL PROGRAM** has **TRAVEL PROGRAM RULE**s (of a rule type, with a rule value, e.g. "1 point per mile", "25,000 points = free ticket") and **TRAVEL PROGRAM FACTOR**s (exclusions such as "paid trips only", "no holiday travel"). Both are effective-dated, so programs change as data.
- **TRAVEL ACCOUNT** has **TRAVEL ACCOUNT ROLE**s (shared holders), **TRAVEL ACCOUNT STATUS** (gold member…) and **TRAVEL ACCOUNT ACTIVITY** (points or amount).
- Activity is triggered by a TRAVEL EXPERIENCE, SALE or PAYMENT (e.g. co-branded card spend), and governed by the rules in force at that time.

## Star schemas
**TRANSPORTATION_OFFERING_FACT** (service levels):
- **Measures:**
  - number of travel experiences, sales dollars
  - positive and negative comment counts, average satisfaction
  - on-time arrivals, on-time departures, average minutes late
- **Dimensions:** TRAVEL_PROVIDERS (including competitors), TRAVEL_PRODUCTS, ACCOMMODATION_CLASSES, DEPARTURE_FACILITYS and ARRIVAL_FACILITYS (role-playing), TRANSPORTATION_VEHICLES, TIME_BY_DAY.

**Non-transportation fact** (hotel, car):
- **Measures:** the first five measures above (punctuality doesn't apply).
- **Dimensions:** TRAVEL_PROVIDERS, TRAVEL_PRODUCTS, ACCOMMODATION_CLASSES, **TRAVEL_ACCOMMODATION_ASSETS** (the specific hotel or car), TIME_BY_DAY.

## Reuse beyond travel
Reservations, ticketing, preferences and experience fit **event and entertainment** businesses (venues, sports, concerts), clinics with appointment slots, and any business that sells capacity on scheduled occurrences.

## Modelling decisions to raise
- **Inventory control.** Sellable quantity per class is the simplest form. Real revenue management uses fare classes or buckets, nesting, and dynamic pricing.
- **Modern standards:** PNR and ticket structures follow IATA (NDC/ONE Order is replacing coupons with orders and offers). GDS integration, dynamic packaging, ancillaries, and API-sourced content all extend the product model.
- **Privacy:** preferences, meal choices (which can reveal religion or health) and passenger data (APIS/PNR) are regulated personal data.
