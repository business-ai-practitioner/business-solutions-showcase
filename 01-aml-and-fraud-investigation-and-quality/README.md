# Intelligent AML & Fraud Investigation and Quality Assurance

**Improving investigation consistency, evidence assessment and operational intelligence through structured, AI-ready workflows.**

> **Project status:** Working rules-based demonstration prototype. The prototype demonstrates structured case intake, preliminary analysis, evidence-gap identification and quality checks. It does **not** connect to a bank, use a large language model, make suspicious activity determinations, or make customer, account or regulatory decisions.

## The business problem

AML and fraud investigation teams work with customer profiles, transaction records, payment information, explanations and supporting evidence. Common challenges include incomplete analysis, weakly supported conclusions, inconsistent documentation, missed evidence gaps and limited visibility of recurring quality weaknesses.

A generic document summariser does not address the full operational problem. This project demonstrates a connected workflow that supports investigation preparation, evidence assessment, independent quality review and management intelligence while retaining human accountability.

## The solution

The platform has two specialist investigation pathways with a shared assurance layer:

| AML investigation pathway | Fraud investigation pathway |
|---|---|
| Transaction patterns and flows | Fraud/scam typology indicators |
| Customer profile and expected activity | Victim, beneficiary and payment relationships |
| Counterparty relationships | Payment chronology and fund movement |
| Source and purpose of funds | Customer account of events and payment authorisation |
| Unresolved enquiries | Evidence required to establish what happened |

Both pathways feed a common set of capabilities:

1. **Structured case intake** — capture the customer, case context, transactions and evidence.
2. **Investigation support** — identify observable patterns and questions for an investigator.
3. **Evidence assessment** — distinguish recorded facts, customer explanations, inferences and unknowns.
4. **Independent quality review** — assess completeness and reasoning separately from the investigation narrative.
5. **Management intelligence** — group quality findings into themes for learning and process improvement.

## Demonstration

The included browser-based prototype runs locally using Python's standard library.

It can:
- Load the supplied synthetic AML or fraud case.
- Display case and transaction information.
- Calculate basic transaction totals and identify incoming/outgoing flows.
- Surface rule-based prompts and unresolved evidence questions.
- Run a separate checklist-based quality review.
- Export a JSON demonstration report.

The prototype is deliberately transparent and deterministic. It is **not an AI model**. It establishes the workflow and data structure that could later be connected to an approved AI service, subject to appropriate privacy, security, validation and governance controls.

## Run the prototype

Requirements: Python 3.9 or later. No third-party Python packages are required.

From this project folder, run:

```bash
python prototype/app.py
```

Then open `http://127.0.0.1:8000` in a browser.

To stop the server, press `Ctrl+C` in the terminal.

## Project contents

```text
01-aml-and-fraud-investigation-and-quality/
├── README.md
├── solution-design.md
├── demonstration-walkthrough.md
├── evidence-assessment-guide.md
├── independent-quality-checklist.md
├── management-intelligence.md
├── limitations-and-controls.md
├── sample-data/
│   ├── aml-case.json
│   ├── fraud-case.json
│   └── quality-failure-case.json
├── prototype/
│   ├── app.py
│   └── README.md
└── images/
    └── workflow.mmd
```

## How to interpret outputs

- Transaction calculations are arithmetic derived from the supplied synthetic records.
- Rule-based prompts are investigative questions, not findings of wrongdoing.
- Missing evidence means the supplied case file does not contain that evidence; it does not prove that the evidence does not exist.
- Quality flags identify checklist items requiring human review. They are not validated quality scores.
- A case position of "further enquiries required" is not a regulatory reporting decision.

## Data, privacy and intellectual property

All institution names, people, account references, transactions, explanations and events in this repository are fictional and synthetic. Do not add employer-confidential information, customer information, credentials, API keys or third-party proprietary material.

## Future development

Potential next steps include document extraction, source-linked evidence registers, configurable typology and quality criteria, role-based review, human approval steps, trend dashboards, evaluation datasets and integration with an approved AI model. These are future opportunities, not implemented capabilities.

## Portfolio context

This project is part of a seven-project business AI portfolio. It demonstrates business problem definition, workflow design, structured data, transparent automation, assurance thinking and responsible AI boundaries.
