# Limitations, safeguards and future controls

## Current limitations

The current prototype:
- Uses three fixed synthetic cases.
- Uses predefined rules and checklist conditions.
- Does not use an AI model or machine learning.
- Does not read uploaded documents or images.
- Does not connect to a bank, payment network, customer system or case-management platform.
- Does not verify customer, payer or beneficiary identities.
- Does not determine whether activity is criminal, fraudulent or reportable.
- Does not make account, customer, reimbursement or regulatory reporting decisions.
- Has no enterprise user access management, audit trail or production security controls.
- Has not been validated with bank investigators or reviewers.

## Safe interpretation

- An unusual pattern is a prompt for examination, not proof of wrongdoing.
- A customer explanation is a statement until appropriately corroborated.
- A missing item is an information gap, not evidence of guilt.
- A checklist flag is a prompt for human review, not a final quality finding.
- Sample-case results are illustrative and cannot be used as performance statistics.

## Controls required before real-world use

Any future implementation handling bank or customer information would require, at minimum:
- Formal business ownership and approved purpose.
- Privacy assessment and data minimisation.
- Security architecture, access controls and encryption.
- Approved data sources and records management.
- Clear human decision rights and escalation routes.
- Testing with representative, appropriately governed data.
- Validation of rules or AI model outputs, including limitations and failure modes.
- Monitoring, incident handling and change management.
- Independent risk and assurance review.
- Compliance with applicable legal, regulatory and institutional requirements.

These are design considerations, not a statement that this prototype meets those requirements.

## Potential future AI integration

An approved AI service could potentially help organise case material, draft structured summaries or suggest questions. Before such functions are considered, the bank would need to define permitted data, model use, human review, output validation, record retention and controls against unsupported statements.

The system should never silently convert an unverified statement into a fact or make a consequential decision without the required authorised human process.
