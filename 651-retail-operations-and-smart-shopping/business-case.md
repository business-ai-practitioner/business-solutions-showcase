# Business Case — Project 651

## 1. Opportunity

Explore whether a lightweight digital shopping journey can reduce friction for customers of independent grocery retailers and make customer-prepared shopping lists easier for store teams to interpret.

The concept addresses three related tasks:

1. Customers find products using familiar names, local-language names or alternate spellings.
2. Customers assemble a basket or visit list, including repeat-shopping concepts.
3. Store staff view a structured request and can use it as a starting point for availability and price confirmation.

This is an opportunity hypothesis. No customer research, retailer interviews, market sizing or willingness-to-pay validation has been completed for this project.

## 2. Target market, buyer and users

| Role | Potential audience | Need |
|---|---|---|
| Economic buyer | Owner/operator of an independent grocery store or small specialist grocery chain | Improve customer convenience and manage enquiries without committing immediately to a full ecommerce platform |
| Operational sponsor | Store manager or operations lead | View customer-prepared lists in a consistent format |
| Primary user | Grocery shopper, including customers who use alternate product names or spellings | Find products and prepare a shopping list before visiting |
| Secondary user | Store staff | Review a structured list and confirm availability and current prices |

The initial concept is most relevant to stores with a meaningful repeat-shopping customer base and a catalogue that is not already well served by an existing digital channel. This segment requires validation.

## 3. Problem and urgency

Potential customer frictions include product search, remembering repeat purchases, and preparing a list before a store visit. Potential store frictions include interpreting unstructured enquiries and responding to requests where item availability or price may need confirmation.

The urgency is not established. Retailers may already manage these tasks adequately through POS systems, ecommerce platforms, messaging, phone calls or paper lists. Discovery interviews should establish whether the problem is frequent and costly enough to justify another tool.

## 4. Alternatives and competitive context

| Alternative | Strengths | Potential gap this concept explores |
|---|---|---|
| Existing ecommerce / click-and-collect platform | Product catalogue, checkout, payment and fulfilment capabilities | May be too costly or extensive for a small store that only wants a simple visit-list workflow; this assumption must be tested |
| POS or inventory software | Product, pricing and stock management | Customer-facing discovery and list preparation may require additional configuration or a separate channel |
| Messaging, phone or social channels | Familiar, low setup effort and already used by many small businesses | Requests can be unstructured and may require manual interpretation |
| Generic shopping-list app | Convenient personal list creation | May not connect a customer's list to a retailer's staff workflow |
| Paper lists / in-person shopping | Simple and reliable | Less convenient for planning and repeat list preparation |

This prototype does not establish that the market lacks these capabilities. Competitor and vendor research is a separate validation task before any commercial positioning.

## 5. Proposed proposition

A lightweight customer-facing catalogue and visit-list experience, paired with a basic staff-facing request preview. The current prototype demonstrates the front-end interaction only. A production implementation would need secure customer handling, a retailer-maintained catalogue, availability and price confirmation, operational ownership and integrations or a controlled manual process.

## 6. Potential value hypotheses

| Stakeholder | Potential benefit | Evidence required |
|---|---|---|
| Customer | Faster product discovery and easier preparation for repeat shopping | Usability tests; task completion time; search success; repeat-use rate |
| Store staff | More structured requests and less time interpreting messages | Baseline and pilot measurement of request handling time, completeness and follow-up rate |
| Store owner | Better visibility of customer demand and a possible digital engagement channel | Adoption, active users, conversion to in-store visits and incremental sales analysis |

No savings, productivity improvement, revenue uplift or customer outcome has been measured. All benefits above are hypotheses.

## 7. Differentiation assessment

The strongest design angle is the end-to-end connection between alternate-name product discovery, a customer-created visit list and a staff-facing request preview. The concept avoids the complexity of online payment and delivery in its initial scope.

However, these functions are not inherently unique. Existing retailer apps, ecommerce tools and messaging-based processes may provide comparable capabilities. The differentiator would need to be demonstrated through a specific underserved retailer segment, lower implementation burden, improved customer experience or measurable workflow improvement.

## 8. Why AI is not included

The current catalogue is structured. Exact and alias-based search, category filters, price calculations and list creation are deterministic tasks. Conventional JavaScript is simpler, faster, cheaper and easier to validate than an AI model for these functions.

AI may be worth testing later for natural-language product discovery, interpreting ambiguous customer requests or suggesting substitutions. It should not be introduced until user research shows a material need and a controlled catalogue-based approach can be evaluated. Substitution or dietary suggestions would require careful product, allergen and suitability controls.

## 9. Feasibility, complexity and adoption barriers

| Area | Assessment |
|---|---|
| Front-end feasibility | Low complexity for a demonstration; the current single-file prototype proves basic interactions |
| Production data | Requires retailer-owned catalogue, product identifiers, pricing and stock information |
| Integration | Potentially moderate to high depending on POS, inventory and order-management systems |
| Privacy and security | Customer identity/contact details would require secure collection, retention, access and privacy controls; current demo avoids server-side collection |
| Operational model | Staff need clear responsibility for reviewing requests, confirming prices/availability and responding through an agreed channel |
| Adoption | Customer awareness, staff capacity, catalogue maintenance and retailer willingness to pay are untested |
| Commercial model | Could be subscription, setup fee or part of a broader retail digital service; pricing is not assessed |

## 10. Validation plan

Before expanding the prototype, conduct a small discovery exercise with independent grocery retailers and shoppers:

1. Interview store owners/managers about request volumes, current channels, handling time and existing systems.
2. Observe a small number of customer shopping-list tasks and product-search behaviours.
3. Compare the concept with existing POS/ecommerce tools used by target stores.
4. Test the prototype with synthetic data and ask users to complete defined tasks.
5. Measure task completion, errors, user comprehension and staff usefulness.
6. Estimate implementation and support costs only after integration requirements are known.

**Decision:** Continue as a portfolio demonstration. Do not position it as a validated commercial product or claim market differentiation until this research is completed.

## Author

**Project by Ketul Shah**  
LinkedIn: https://www.linkedin.com/in/ketulhshah/
