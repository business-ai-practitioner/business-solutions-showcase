# Solution design

## 1. Purpose

Demonstrate how a structured workflow can support financial crime investigators, independent quality reviewers and managers.

The design is deliberately business-led. It focuses on the work people need to complete and the evidence they need to consider. Technology should support that work, not replace professional judgement.

## 2. Business problem

Investigation teams may need to bring together customer information, payment activity, explanations, documents and internal records. Quality problems can arise when:

- Relevant transactions are overlooked or not explained.
- The relationship between payment parties is unclear.
- Source or purpose of funds is assumed rather than established.
- Customer explanations are repeated without independent assessment.
- The conclusion is stronger than the available evidence.
- Quality review identifies issues but does not explain the correction required.
- Management reporting counts errors without showing their underlying themes.

These are the problems the proposed workflow is designed to address. They are not claims about every bank or every investigation team.

## 3. Intended users

| User | What they need |
|---|---|
| AML investigator | A structured way to review payment activity, counterparties, source/purpose and unresolved questions |
| Fraud investigator | A structured way to reconstruct the scam, payment chronology, authorisation and movement of funds |
| Quality reviewer | A separate, evidence-led challenge of completeness and reasoning |
| Team manager | Clear themes showing where investigations and controls need improvement |

## 4. Design principles

1. **Evidence before conclusion:** do not state more than the information supports.
2. **Different investigation pathways:** AML and fraud have distinct investigative questions.
3. **Facts and explanations are different:** a customer statement is not independent verification.
4. **Traceability:** observations should point to the transaction or case information that prompted them.
5. **Independent review:** quality review challenges the investigation; it does not merely repeat it.
6. **Human accountability:** authorised people retain decisions and actions.
7. **Proportionate enquiries:** recommend relevant next steps, not an indiscriminate document request.
8. **Transparency:** users should be able to understand why a prompt or quality flag appeared.

## 5. End-to-end workflow

1. **Receive case information:** customer profile, transactions, case narrative and available evidence.
2. **Choose investigation pathway:** AML or fraud.
3. **Review activity:** calculate basic flows and identify relevant patterns or chronology.
4. **Assess evidence:** label what is recorded, what the customer says, what is inferred and what remains unknown.
5. **Identify enquiries:** explain what needs to be established and why.
6. **Record provisional position:** state whether evidence is sufficient, further enquiries are required or the case is ready for an authorised decision.
7. **Independent quality review:** assess the work against pathway-specific criteria.
8. **Correct and learn:** record actions and group recurring quality themes for management.

## 6. What is implemented

The current local prototype:
- Loads three predefined JSON cases.
- Calculates incoming, outgoing and net transaction totals.
- Displays case facts and customer statements as separate categories.
- Displays unresolved questions supplied in the case data.
- Shows predefined AML or fraud prompts.
- Applies a transparent checklist to identify incomplete case information.
- Summarises illustrative quality themes across the sample cases.
- Exports a JSON snapshot of the selected case.

The prototype does not infer facts from documents or generate free-text conclusions. Its prompts and checks are predefined.

## 7. What is designed but not implemented

- Upload and extraction of bank statements or supporting documents.
- Automated entity resolution or network analysis.
- AI-generated investigation narratives.
- AI assessment of evidence reliability.
- Workflow assignment, approvals or case-management integration.
- Production management dashboards and trend analysis.
- User access controls, audit logging and enterprise security.

## 8. Roles and decision rights

| Activity | System support | Human responsibility |
|---|---|---|
| Transaction calculations | Calculates totals from supplied data | Confirm data completeness and relevance |
| Investigation prompts | Displays predefined questions | Decide which enquiries are appropriate |
| Evidence classification | Displays labels supplied in case data | Verify the accuracy of classification |
| Quality checklist | Flags missing fields or evidence gaps | Reviewer determines the finding and severity |
| Case outcome | No automated decision | Authorised bank personnel decide |
| Regulatory reporting or customer action | Not performed | Remains with the bank's authorised process |

## 9. Success measures for a future pilot

No benefits have been measured in this demonstration. A future controlled pilot could assess:
- Percentage of sampled cases with clear source references for material observations.
- Frequency of unsupported conclusions found in independent review.
- Rework required after quality review.
- Time taken to identify key evidence gaps.
- Consistency of quality findings between reviewers.
- Investigator and reviewer usability feedback.

Measures should have agreed definitions, a baseline, a suitable sample and independent validation before benefits are claimed.
