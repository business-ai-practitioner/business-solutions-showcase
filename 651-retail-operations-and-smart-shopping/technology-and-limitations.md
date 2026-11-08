# Technology, Implementation and Limitations

## 1. Technology used

| Component | Implementation | Purpose |
|---|---|---|
| Page structure | HTML5 | Catalogue, navigation, forms, list and staff preview |
| Styling | Embedded CSS | Responsive layout and visual presentation |
| Application logic | Vanilla JavaScript | Product search, filters, list management, indicative calculations and in-session request preview |
| Data | Hard-coded synthetic JavaScript array | 46 illustrative catalogue records |
| Runtime | Modern web browser | Local demonstration without a server |

No third-party JavaScript packages, backend services, APIs, database, authentication provider or AI model are used.

## 2. Implementation status

| Capability | Status | Notes |
|---|---|---|
| Catalogue display | Implemented | 46 synthetic products |
| Category navigation | Implemented | Includes food and non-food categories |
| Food & groceries filter | Implemented and logic-tested | Includes six food categories; excludes Puja & home and Kitchenware |
| Product search | Implemented and logic-tested | English/Hindi names and configured aliases; fuzzy matching is limited |
| English/Hindi product-name toggle | Implemented in front end | Supporting interface remains predominantly English |
| Price and unit-price display | Implemented with illustrative values | Not connected to a retailer's price feed |
| Weight selection | Implemented for selected products | Estimates line amount using sample per-kilogram price |
| Shopping list and totals | Implemented in browser session | No checkout or order is created |
| Visit-list request | Implemented as local simulation | In-memory only; no external transmission |
| Staff preview | Implemented as local simulation | Displays requests created in the same page session |
| Pantry and previous order | Simulated preview | No account, saved list or order history exists |
| New arrivals | Simulated sample data | Not connected to live stock or product feed |
| AI features | Not implemented | No model or AI service is called |
| Payment and fulfilment | Not implemented | No payment, delivery, stock reservation or order creation |

## 3. Why this technology was selected

A single HTML file is sufficient to demonstrate the intended front-end journey with minimal setup and no hosting dependency. Deterministic JavaScript is appropriate for filtering structured products, calculating indicative totals and managing a temporary list. A backend or AI model would add complexity without improving the current demonstration objective.

## 4. Limitations and risks

- All catalogue data and prices are illustrative; they must not be used for actual purchasing decisions.
- The fictional name “Saffron Market” is a placeholder and has not been cleared for trademark or commercial use.
- The prototype has no retailer affiliation or endorsement.
- No live inventory, price, POS, ecommerce or order-management integration exists.
- No user authentication, persistent storage, secure server or multi-user functionality exists.
- Form details are held in page memory only and are lost on refresh/close; users must use synthetic details.
- No email, SMS, WhatsApp or other external communication is sent.
- No stock is reserved and no visit appointment is booked.
- No payment, checkout, delivery or fulfilment functionality exists.
- The staff preview is not a real staff application and has no access control.
- Product imagery has been removed; product cards use emoji illustrations. This avoids reliance on external image URLs but is not product photography.
- Search fuzzy matching is basic and may produce missed matches or irrelevant matches; it is not a semantic AI search.
- The Hindi toggle changes product names, not the entire interface.
- Browser click-through testing was blocked in the build environment. See the testing record for the exact verification boundary.

## 5. Security and privacy considerations for a real deployment

A production version would require, at minimum, secure identity and access management, server-side validation, encrypted transport, appropriate data retention, privacy notices and consent where applicable, protection against injection and abuse, logging and monitoring, backups, incident response, and a security review. Staff access to customer requests would need role-based permissions. None of these production controls is implemented by this static prototype.

## 6. Hosting

The file is structured as `index.html`, so it can be considered for GitHub Pages as a static demonstration after local browser testing and publication checks. It has not been deployed. A GitHub repository file view is not a live application URL; deployment must be configured and the resulting public page independently verified.

## Author

**Project by Ketul Shah**  
LinkedIn: https://www.linkedin.com/in/ketulhshah/
