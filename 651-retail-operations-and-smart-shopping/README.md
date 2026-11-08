# Project 651 — Retail Operations & Smart Shopping

**An independent retail experience and store-workflow prototype using a fictional brand and synthetic catalogue data.**

> **Demonstration status:** Interactive front-end prototype. This is not a live retail service, is not affiliated with a real retailer and does not include AI integration, payment processing, live stock, real customer accounts or external order transmission.

## The business problem

Independent grocery retailers need to make product discovery and repeat shopping convenient while handling customer enquiries and shopping requests through practical store workflows. Customers may search using different product names or spellings, rebuild recurring baskets and prepare a list before visiting a store. Store teams may then need to interpret those requests and confirm availability and prices.

This project explores a lightweight digital journey connecting product discovery and customer list preparation with a simple in-store staff preview. It is a concept demonstration, not evidence that retailers have validated the problem or would purchase this solution.

## What the prototype demonstrates

- A sample catalogue of **46 synthetic products** across grocery, fresh and chilled, frozen, snacks, drinks, sweets, home and kitchen categories.
- Search using English product names, Hindi names and common alternate spellings (for example, `atta` / `aata`).
- Category navigation and product filters, including a corrected **Food & groceries** filter.
- Illustrative prices, unit prices and quantity/weight selection for selected loose products.
- A shopping list with quantity controls and an indicative total.
- A visit-list form that creates a local demonstration reference.
- A staff-facing preview of the request created during the current browser session.
- Preview screens for a future saved pantry and previous-order experience.
- A sample “New arrivals today” view, clearly identified as illustrative data.

## Try the demonstration

1. Open [`index.html`](index.html) in a modern browser, or publish this folder using GitHub Pages after completing the publication checks.
2. Search for `aata` or select **Food & groceries**.
3. Add one or more products to the shopping list and open **View list**.
4. Select **Prepare visit list**, use synthetic details such as `Demo Shopper` and `demo@example.test`, and submit.
5. Open the retail operations preview to see the request in the staff-facing view.

All request data remains in the current page session. Refreshing or closing the page clears it. Do not enter real personal or customer information.

## Business proposition and differentiation

The demonstration focuses on a joined-up customer-to-store visit-list journey rather than presenting a generic online checkout. It combines product discovery, repeat-shopping concepts, list preparation and a staff preview in one small prototype. This is a design hypothesis, not a proven market differentiator. Existing ecommerce, POS, retailer apps, messaging and shopping-list products may already cover parts or all of this journey. See [Business case](business-case.md) for the alternatives, buyer, value hypotheses and adoption considerations.

## Why no AI is used in this version

The current features are better handled by straightforward catalogue search, filters, calculations and browser-based workflow logic. Adding a language model would increase cost and error risk without a clear benefit for these functions. Possible future AI applications—such as natural-language product discovery or substitution suggestions—would need to be tested against simpler search and rules-based alternatives, and would require reliable catalogue data and human control.

## Solution design

See [Solution design](solution-design.md) for the customer and staff journeys, process steps, controls and proposed next-stage capabilities.

## Technology

The prototype is a single self-contained HTML file using HTML, CSS and vanilla JavaScript. It has no backend, database, third-party JavaScript library, API integration or external image dependency. See [Technology and limitations](technology-and-limitations.md).

## Testing and maturity

JavaScript syntax validation and focused business-logic checks were run. The Food & groceries filter, product count, alternate-spelling search and Under $10 logic passed those checks. Full browser click-through testing could not be completed in the build environment, so the full customer-to-staff journey remains to be manually verified before publication. See [Testing record](testing-record.md).

**Current maturity:** Working front-end prototype with partially validated business logic; not yet a fully browser-verified or deployed solution.

## Repository contents

| File | Purpose |
|---|---|
| `index.html` | Interactive prototype and GitHub Pages entry point |
| `README.md` | Project overview and demonstration instructions |
| `business-case.md` | Buyer, user, problem, alternatives and commercial hypotheses |
| `solution-design.md` | Workflow and capability design |
| `technology-and-limitations.md` | Implementation details, maturity and limitations |
| `testing-record.md` | Executed checks, results and outstanding verification |
| `publication-checklist.md` | Pre-publication actions and status |

## Identity, data and intellectual property

“Saffron Market” is a fictional placeholder identity for this demonstration and has not been cleared for commercial use or trademark availability. The project contains no real retailer name, phone number, address, website or store-specific branding. Product descriptions, prices, categories and new-arrival labels are illustrative. Product images from third-party websites were removed and replaced with emoji illustrations. The project is not endorsed by any retailer.

Do not enter real customer data. Do not describe the sample prices, availability, customer records or operational outcomes as real. Review the publication checklist before making the repository public or enabling GitHub Pages.

## Author

**Project by Ketul Shah**  
LinkedIn: https://www.linkedin.com/in/ketulhshah/
