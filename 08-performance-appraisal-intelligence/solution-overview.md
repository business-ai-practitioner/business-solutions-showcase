# Solution Overview

## 1. Product proposition

**Performance Appraisal Intelligence** is an AI-assisted performance management concept designed to help managers produce clearer, more evidence-based appraisals.

Its distinctive proposition is not simply to rewrite manager notes. It is to place the appraisal in context, examine the support for proposed assessments, identify gaps and contradictions, and only then assist with drafting.

## 2. The business problem

Managers may have to assess employee delivery against individual objectives while also considering team projects, shared outcomes, behavioural expectations and leadership priorities. These inputs are often fragmented across notes, objectives and project updates.

A polished narrative can conceal weak evidence. Conversely, an employee's contribution may be overlooked when the manager cannot easily connect individual work to wider team outcomes.

The proposed tool aims to improve the quality and consistency of the appraisal process without taking accountability away from managers.

## 3. Optional context model

The tool should operate in two modes:

**Standalone mode:** Employee objectives, proposed ratings and manager evidence are sufficient to begin.

**Context-enriched mode:** The manager may additionally provide:
- team structure, roles and reporting relationships;
- Team Head annual objectives;
- team objectives and expected outcomes;
- expected team projects, milestones and ownership;
- individual employee objectives and their links to team priorities.

Context is optional because not every manager will have structured team data available.

## 4. Assessment sequence

1. **Establish expectations** — identify the employee's agreed objectives and applicable behavioural criteria.
2. **Understand context** — map relevant team deliverables and leadership priorities, where supplied.
3. **Organise evidence** — distinguish recorded facts, manager-reported claims, explanations, interpretations and unknowns.
4. **Assess alignment** — identify plausible links between individual contributions and team priorities without assuming causation.
5. **Challenge the proposed assessment** — flag missing support, contradictions, vague language and possible attribution problems.
6. **Seek clarification** — present questions to the manager where evidence is insufficient.
7. **Draft** — create a structured appraisal using the organisation's configured criteria and format.
8. **Review and approve** — the manager checks accuracy, fairness and completeness and remains accountable for the final assessment.

## 5. What the system must not do

- Convert a manager assertion into a verified fact.
- infer an employee's contribution from a team result without attribution evidence.
- treat an unmet team objective as an individual's failure without considering role, dependencies and control.
- invent strengths, weaknesses, development needs or strategic alignment.
- silently change a proposed rating.
- rank employees or impose a rating distribution.
- make promotion, remuneration, termination or other employment decisions.

## 6. Assessment dimensions

| Dimension | Example question |
|---|---|
| Objective delivery | What was agreed, and what evidence shows delivery? |
| Quality and impact | Is the claimed outcome supported and attributable? |
| Team contribution | What was the employee's identifiable contribution to shared work? |
| Strategic alignment | Which stated team or leadership priority does the work support? |
| Behaviour | What specific observed examples support the behavioural assessment? |
| Risk and conduct | Are there relevant concerns or contradictions requiring human review? |
| Evidence sufficiency | What remains unverified or unknown? |

The organisation must supply the applicable rating definitions and behavioural framework. The product must not assume that a rating of 1, 2 or 3 has the same meaning across organisations.

## 7. Intended outputs

- Evidence and context summary.
- Objective-to-priority alignment view.
- Evidence gaps and clarification questions.
- Contradiction and attribution flags.
- Draft appraisal in the required format.
- Manager review checklist and approval record.
- Optional team-level consistency review for authorised managers.

## 8. Human oversight and fairness

The system should support managers, not replace their judgement. It should make uncertainty visible, preserve the source of material statements and allow managers to correct context. Team calibration should compare like with like and should never become automated ranking or forced distribution.

## 9. Proposed maturity path

| Stage | Description | Status |
|---|---|---|
| Concept | Problem and product proposition defined | Current |
| Interactive demonstrator | Public walkthrough of intended experience | Available |
| Functional prototype | Implement configurable criteria, evidence register and draft workflow | Proposed |
| Tested prototype | Test with synthetic cases and documented evaluation | Not yet achieved |
| Controlled pilot | Approved environment, privacy, security and HR governance | Future possibility |
| Deployed solution | Integrated operating use | Not claimed |

## 10. Success measures for future testing

Potential evaluation measures include:
- proportion of material appraisal statements traceable to supplied evidence;
- number and relevance of evidence gaps identified;
- rate of unsupported claims remaining in drafts;
- manager time and editing effort, measured in a controlled test;
- consistency of outputs across comparable synthetic cases;
- usability and manager trust;
- false-positive and false-negative rates for issue flags.

No performance improvement or ROI is claimed at this stage.
