# Limitations, Risks and Controls

## Current prototype limitations

- Uses synthetic sample data only.
- Uses deterministic rules and checklist logic; no AI/LLM integration.
- Does not ingest PDFs, emails, bank statements or images.
- Does not authenticate users or provide role-based access.
- Does not connect to core banking, case management, payment or screening systems.
- Does not determine whether activity is criminal, fraudulent or reportable.
- Does not make customer, account, reimbursement or regulatory decisions.
- Does not provide a validated risk score or quality score.
- Does not implement multi-case trend analytics.
- Has not been independently validated for operational use.

## Key risks and proposed controls

| Risk | Proposed control |
|---|---|
| Unsupported AI-generated assertion | Source-linked evidence, explicit classification and human review |
| False positive or misleading prompt | Treat prompts as questions, not findings; record rationale |
| Missed evidence or incomplete input | Input completeness checks and visible limitations |
| Automation bias | Independent reviewer and human decision points |
| Inappropriate disclosure | Approved environment, access controls and data minimisation |
| Inconsistent quality decisions | Defined criteria, reviewer guidance and calibration |
| Misleading management metrics | Defined denominators, sampling context and validation |
| Model or prompt change | Versioning, testing, monitoring and change approval if AI is introduced |

## Safe-use boundary

This is a portfolio demonstration, not an operational banking system. Never upload real customer data, employer-confidential information, credentials or sensitive records. Any future use with real information would require formal legal, privacy, security, model-risk, operational-risk and compliance review.
