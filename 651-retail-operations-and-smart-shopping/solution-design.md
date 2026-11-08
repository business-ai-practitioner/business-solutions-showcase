# Solution Design — Project 651

## 1. Design objective

Demonstrate a simple digital journey in which a shopper discovers products, builds a visit list and sees how that request could be presented to retail staff. The current implementation is a front-end prototype using synthetic information.

## 2. Scope

### Implemented in the prototype

- Product catalogue with 46 illustrative products.
- Category navigation and filters.
- Search across English names, Hindi names and alternate spellings.
- Illustrative product prices and unit prices.
- Weight selection for selected loose products.
- Shopping-list creation, quantity changes and indicative total calculation.
- Visit-list form and in-session request reference.
- Staff-facing preview of requests created during the current page session.
- English/Hindi product-name toggle.
- Illustrative new-arrivals view.

### Simulated or preview-only

- Customer sign-in.
- Saved monthly pantry.
- Previous order retrieval.
- New-arrival feed.
- Retail staff request management beyond the in-session preview.

### Not included

- AI or machine-learning integration.
- Real customer accounts or authentication.
- Backend, database or cross-session persistence.
- Live product catalogue, stock or price feed.
- Payment, checkout or order creation.
- Email, SMS, messaging or external request transmission.
- Delivery booking, stock reservation or POS integration.
- Retailer analytics based on real transactions.

## 3. Customer journey

1. **Enter the demo:** The shopper sees a fictional store identity and a clear demonstration notice.
2. **Discover products:** Browse categories or search using English, Hindi or common alternate spellings.
3. **Refine results:** Apply a category or filter, including Food & groceries, Popular picks or Under $10.
4. **Select products:** Add items to the list; adjust quantity or choose an estimated weight where supported.
5. **Review list:** Inspect selected products and an indicative total.
6. **Prepare visit list:** Enter synthetic demonstration details and an optional planned visit preference.
7. **Receive local reference:** The page generates a demo reference and explains that no retailer receives the request.
8. **Review staff preview:** Switch to the retail operations preview and inspect the request generated in this browser session.

## 4. Staff-facing journey

1. Staff preview is opened from the customer view.
2. The current session's demo requests are listed.
3. Staff select a request to see customer-entered demo details, requested products, quantities and indicative total.
4. The interface labels the request as a demonstration and not sent.

A real service would need a secure intake channel, authentication and access controls, request status management, staff ownership, response workflow and audit trail. None is implemented here.

## 5. Business rules

| Rule | Current demonstration behaviour |
|---|---|
| Catalogue search | Matches product name, Hindi name, brand/sample label, pack description and configured aliases; includes a limited one-character fuzzy match |
| Food & groceries | Includes Grocery, Fresh & chilled, Frozen, Snacks, Tea & drinks and Sweets & festival; excludes Puja & home and Kitchenware |
| Under $10 | Filters products where the configured sample price is below AUD 10 |
| Quantity | List quantity is limited to 20 per product |
| Weight | Selected loose-product weight is used to estimate line value from the illustrative per-kilogram price |
| List total | Sum of selected quantities multiplied by the configured illustrative price |
| Visit preference | Date/time are preferences only; no booking is made |
| Request storage | Request remains in JavaScript memory for the current page session only |

## 6. Human control and exceptions

The prototype does not make purchase, stock, price or fulfilment decisions. A real retailer would need to confirm availability and current prices before accepting any customer commitment. Staff review would remain necessary for substitutions, out-of-stock items, ambiguous product requests and any customer-specific question.

## 7. Data and privacy design

The demonstration uses synthetic catalogue content and sample customer details. The request form operates locally in the page and does not transmit information to a server. Users must not enter real personal information. A production design would require a privacy assessment, secure transmission, purpose limitation, retention rules, access controls, incident handling and appropriate customer notices.

## 8. Future options — subject to validation

1. **Retailer catalogue integration:** controlled product, price and stock updates from a retailer's system.
2. **Secure customer identity and saved lists:** only if repeat-shopping research supports the need.
3. **Request status and staff workflow:** assignment, acknowledgement, confirmation and exception handling.
4. **Natural-language search:** assess AI against alias dictionaries and conventional search first.
5. **Substitution support:** only with explicit retailer rules, reliable product attributes and human confirmation.
6. **Operational reporting:** request volumes, popular products and unresolved requests, based on valid operational data.

## 9. Architecture overview

The current prototype is a single `index.html` file:

- HTML provides page structure and forms.
- CSS provides responsive layout and visual styling.
- Vanilla JavaScript holds the sample product catalogue, filter/search logic, shopping list and in-session request state.
- No network service, external library, database, AI model or third-party image source is called.

This architecture is appropriate for a low-cost portfolio demonstration, not a secure multi-user retail service.

## Author

**Project by Ketul Shah**  
LinkedIn: https://www.linkedin.com/in/ketulhshah/
