# Demonstration walkthrough

## Before you start

The prototype runs locally on your computer. It uses synthetic examples and predefined checks. Allow around 5–10 minutes to explore it.

Start the application using the instructions in [Prototype README](prototype/README.md).

## Demonstration 1 — AML case

Select **AML — multiple unrelated incoming payments**.

Look at:
1. The customer profile and review period.
2. The incoming and outgoing transaction totals.
3. The list of payment parties and unresolved relationships.
4. The customer's explanation, which is recorded as a statement—not as verified fact.
5. The suggested questions about source, purpose and counterparties.

**What a practitioner should notice:** multiple incoming payments and onward transfers are relevant observations, but they do not prove wrongdoing. The investigator still needs to establish who the parties are, why the payments were made and whether the explanations are supported.

## Demonstration 2 — Fraud case

Select **Fraud — authorised payment scam**.

Look at:
1. The sequence of contact, deception and payments.
2. The payments made by the customer.
3. The beneficiary and onward movement information available.
4. What the customer authorised and what the customer says they were told.
5. The outstanding enquiries about the scammer, beneficiary and recovery actions.

**What a practitioner should notice:** payment authorisation and customer deception are separate questions. The chronology is central to understanding the event.

## Demonstration 3 — Incomplete case for quality review

Select **QA challenge — incomplete investigation**.

Look at:
1. Missing counterparty information.
2. An explanation that has not been independently supported.
3. An incomplete transaction rationale.
4. A conclusion that is not adequately supported by the recorded evidence.
5. The checklist flags and corrective actions.

**What a reviewer should notice:** the review should explain why the gap matters and what the investigator needs to do—not simply mark a field as incomplete.

## Management view

Open the management summary in the application. It groups the sample-case flags into themes. The sample is intentionally tiny and selected for demonstration; it is not representative and must not be interpreted as a quality rate or bank benchmark.

## Export

Use **Download case review (JSON)** to save a structured snapshot of the selected case. This is a technical demonstration output, not a bank record or regulatory report.

## Discussion questions for a banking practitioner

- Are the AML and fraud questions appropriate for the stated scenarios?
- Are any material investigative questions missing?
- Are the evidence labels clear enough for investigators and reviewers?
- Does each quality flag explain the issue and the required correction?
- Which checks should be mandatory, conditional or not applicable?
- What additional controls would be needed before any use with real customer data?
