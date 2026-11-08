# Testing Record — Project 651

## 1. Test environment

- Source file: `index.html`
- JavaScript runtime used for syntax and focused logic checks: Node.js v22.16.0
- Browser automation attempted: Playwright with local Chromium
- Test data: synthetic catalogue records and synthetic request details only

## 2. Executed checks

| ID | Check | Expected result | Actual result | Status |
|---|---|---|---|---|
| T01 | JavaScript syntax validation using `node --check` | No syntax errors | No syntax errors reported | Pass |
| T02 | Catalogue record count | 46 sample products | 46 records found | Pass |
| T03 | Food & groceries filter | Includes food categories and excludes Puja & home / Kitchenware | 43 records returned across Grocery, Fresh & chilled, Frozen, Snacks, Tea & drinks and Sweets & festival; no non-food category returned | Pass |
| T04 | Alternate spelling search for `aata` | Finds Whole Wheat Atta | Whole Wheat Atta returned | Pass |
| T05 | Under $10 filter | Every returned record has configured sample price below AUD 10 | Logic check returned true | Pass |
| T06 | External store identity and contact scan | No real store name, phone, address or domain remains in the HTML | Static scan performed after sanitisation; no known identifiers or external URLs found | Pass |
| T07 | External image dependency scan | No remote product or store image URLs | No HTTP(S) URLs remain in `index.html` | Pass |
| T08 | Browser load and end-to-end click-through | Page loads and core customer-to-staff journey completes | Attempted but Chromium navigation was blocked by the execution environment (`ERR_BLOCKED_BY_ADMINISTRATOR`) | Not verified |

## 3. Test interpretation

The food filter defect identified in the source prototype was corrected. The filter now includes the six food/drink categories and excludes the Puja & home and Kitchenware categories. Focused JavaScript checks passed for this rule, alternate spelling search and the Under $10 filter.

The JavaScript syntax check does not prove that all page interactions work in a browser. The end-to-end customer journey, responsive layout, dialog behaviour, form validation, staff preview, language toggle and browser-session reset still require manual browser testing.

## 4. Outstanding manual checks

Before publication, open `index.html` in a current desktop browser and complete these steps using synthetic details only:

1. Confirm the page loads with 46 sample products and no missing visual assets.
2. Select Food & groceries; confirm home and kitchen items are excluded.
3. Search `aata`, `tuvar`, `bhindi` and a Hindi product name.
4. Test category navigation, Popular picks and Under $10.
5. Add products, change quantities and verify the indicative total.
6. Change the weight for a loose product and verify the estimate updates.
7. Prepare a visit list using `Demo Shopper` and `demo@example.test`.
8. Open the retail operations preview and confirm the request appears as not sent.
9. Refresh the page and confirm the in-session request is cleared.
10. Test English/Hindi toggle, pantry preview, last-order preview, new arrivals and responsive layout on a narrow screen.

Record the actual results before describing the project as a tested prototype.

## 5. Defects and limitations

- **Corrected:** Food & groceries filter did not have a corresponding rule in the original filter logic. It now filters the intended food categories. Focused logic test passed.
- **Outstanding verification:** Full browser click-through could not be completed because the browser launch/navigation was blocked by the build environment. This is an evidence gap, not a claim that the user journey fails.
- No known Critical or High defect was identified by the checks completed, but the incomplete browser testing means overall functionality is not fully validated.

## 6. Current maturity

**Working front-end prototype; focused business logic validated; full browser journey not yet verified; not deployed.**

## Author

**Project by Ketul Shah**  
LinkedIn: https://www.linkedin.com/in/ketulhshah/
