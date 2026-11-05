# Solution Design

## 1. Objective

Demonstrate how an integrated solution can support AML and fraud investigation teams through two specialist investigation pathways and a shared evidence, quality and management-intelligence layer.

## 2. Users

- Investigator: reviews case information, records observations and determines further enquiries.
- Quality reviewer: independently assesses the completed investigation against defined criteria.
- Team manager: reviews aggregated quality themes and considers training or process changes.
- Governance and control stakeholders: consider whether the workflow has appropriate accountability, traceability and safeguards.

## 3. Logical workflow

1. Case intake and validation.
2. Select AML or fraud pathway.
3. Review customer, event and transaction information.
4. Identify observable patterns and investigative questions.
5. Record evidence, source, status and limitations.
6. Prepare an investigation assessment and provisional position.
7. Conduct a separate quality review.
8. Record findings and corrective actions.
9. Aggregate quality themes for management review.

## 4. Separation of pathways

### AML pathway

Focuses on whether activity is understood in the context of the customer profile, counterparties, source and purpose of funds, transaction flows and available supporting evidence.

### Fraud pathway

Focuses on the alleged fraud or scam event, chronology, customer/victim account, payment authorisation, beneficiary information, transaction movement and evidence supporting or contradicting the reported events.

The two pathways share data-handling and assurance principles, but must not use identical investigative criteria.

## 5. Shared evidence model

Each material assertion should be recorded with:
- Assertion or issue.
- Classification: verified fact, customer explanation, inference, assumption or unknown.
- Source reference.
- What the source actually establishes.
- Reliability or verification status.
- Contradictory information.
- Further evidence required.
- Investigator rationale.

## 6. Independent quality review

The reviewer should assess the underlying case information and investigation record, not simply approve the investigator's AI-generated narrative. The quality review should identify omissions, unsupported reasoning, inconsistent chronology and unresolved questions.

## 7. Prototype implementation

The included prototype is a local, rules-based demonstration. It uses Python's standard library, synthetic JSON case files, transparent calculations and checklist rules. No LLM or external service is called.

## 8. Human decision points

Humans remain responsible for:
- Determining investigative scope.
- Assessing source reliability and context.
- Deciding whether enquiries are proportionate.
- Resolving conflicting evidence.
- Determining case outcomes.
- Making any reporting, customer or account decisions.
- Approving corrective actions and management responses.
