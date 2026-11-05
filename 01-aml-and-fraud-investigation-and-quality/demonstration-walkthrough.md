# Demonstration Walkthrough

## Purpose

Show an end-to-end workflow using fictional case data. The demonstration is designed to make clear what is supplied, what the prototype calculates or flags, and what a human must decide.

## Demonstration A — AML case

1. Start the local prototype.
2. Select **AML — Harbourline Bank synthetic case**.
3. Review the customer profile and transactions.
4. Review incoming and outgoing totals and the net movement.
5. Read the investigation prompts. They identify questions such as counterparty relationships, source and purpose of funds, and consistency with the customer profile.
6. Review the evidence gaps. Do not treat a missing item as proof of suspicious activity.
7. Open the independent quality review.
8. Review each checklist result and the recommended follow-up.
9. Export the JSON report.

Expected interpretation: the available synthetic information is insufficient to establish the source, purpose or beneficiaries of all funds. Further enquiries are required.

## Demonstration B — Fraud case

1. Select **Fraud — synthetic authorised payment scam case**.
2. Review the reported event chronology and payment records.
3. Compare the customer's account of events with the available payment and beneficiary information.
4. Review missing evidence, including communication records and independent confirmation of the beneficiary.
5. Run the separate quality review.
6. Export the JSON report.

Expected interpretation: the scenario contains reported scam indicators, but the prototype does not determine fraud, liability, reimbursement or reporting outcomes.

## Demonstration C — Quality failure case

1. Select **Quality failure — synthetic incomplete investigation**.
2. Review the deliberately incomplete investigation notes.
3. Run the quality review.
4. Identify checklist items that require attention, such as unsupported conclusions, missing counterparty analysis or unaddressed evidence gaps.
5. Discuss what corrective action would be required before the case could be considered complete.

## What to explain to an audience

- The tool structures and surfaces information; it does not replace an investigator.
- AML and fraud use different investigative questions.
- Evidence status and source traceability matter.
- Quality review is a distinct activity.
- Management intelligence should be based on consistently recorded findings.
- The current prototype is deterministic and rules-based, not an AI model.
