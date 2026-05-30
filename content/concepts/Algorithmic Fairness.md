---
title: Algorithmic Fairness
page_type: concept
status: active
tags:
  - concept
  - algorithmic-fairness
  - algorithmic-accountability
  - bias
  - digital-governance
updated_on: 2026-05-30
source_count: 20
aliases:
  - Algorithmic Accountability and Fairness
  - Fairness Metrics
  - Algorithmic Fairness as Political Philosophy
  - Fairness as Policy Alignment
  - Sociotechnical Fairness
  - COMPAS Controversy
  - Risk Assessment in Criminal Justice
related_pages:
  - [[Digital Nudging]]
  - [[Predictive Algorithms, Bias, and Fairness]]
  - [[Fairness Impossibility Results]]
  - [[Algorithmic Policy Efficiency]]
  - [[Prediction Policy Problems]]
  - [[Transparency and Disclosure]]
  - [[Algorithmic Governance]]
  - [[Angwin et al., 2016|Machine Bias]]
  - [[Kleinberg et al., 2016|Inherent Trade-Offs in the Fair Determination of Risk Scores]]
  - [[Hedden, 2021|On Statistical Criteria of Algorithmic Fairness]]
  - [[Hellman, 2020|Measuring Algorithmic Fairness]]
  - [[Binns, 2018|Fairness in Machine Learning: Lessons from Political Philosophy]]
  - [[Corbett-Davies et al., 2017|Algorithmic Decision Making and the Cost of Fairness]]
  - [[Narayanan, 2026|What If Algorithmic Fairness Is a Category Error?]]
---

# Algorithmic Fairness

## Core idea

[[Algorithmic Fairness]] asks how algorithmic systems that rank, recommend, predict, score, filter, or guide decisions distribute benefits, burdens, errors, opportunities, and reasons across people and groups. In [[Digital Nudging]], the issue is broader than automated decisions: ranking, recommendation, targeting, consent flows, adaptive prompts, and AI assistants can all shape opportunity before a formal decision is ever made.

This page now absorbs the older pages on algorithmic accountability, fairness metrics, political philosophy, policy alignment, sociotechnical fairness, COMPAS, and criminal-justice risk assessment. Those terms remain useful, but they belong as parts of one course-level concept rather than as separate concept pages.

## Canonical case

The entry case is the COMPAS controversy. [[Angwin et al., 2016|Machine Bias]] showed how a criminal-justice risk score could shape pretrial and sentencing decisions while producing racially asymmetric errors. Black defendants were more likely to be falsely labeled high risk; white defendants were more likely to be falsely labeled low risk.

The case matters because it makes three points visible at once. First, a score can influence liberty even when it is formally only decision support. Second, proprietary and technical opacity make contestation difficult. Third, different fairness objections can point in different directions.

## Metrics and impossibility

Fairness metrics are diagnostics, not final verdicts. They ask whether scores or decisions satisfy formal criteria such as calibration, predictive parity, error-rate balance, statistical parity, or equality of opportunity. The course keeps the detailed tradeoff in [[Fairness Impossibility Results]], where predictive parity and error-rate parity are treated as the central pair.

The important lesson is not that metrics are useless. It is that metrics answer different questions. Predictive parity asks whether a score has the same evidential meaning across groups. Error-rate parity asks whether false positives and false negatives impose comparable burdens across groups. When base rates differ and prediction is imperfect, these demands generally conflict, so the choice among them requires justification.

The formal conflict is anchored in Kleinberg, Mullainathan, and Raghavan's [[Kleinberg et al., 2016|Inherent Trade-Offs in the Fair Determination of Risk Scores]]. Hedden's [[Hedden, 2021|On Statistical Criteria of Algorithmic Fairness]] gives the strongest calibration-centered response, while Hellman, Binns, Corbett-Davies and coauthors, and Narayanan push the analysis toward burdens, philosophy, policy goals, and sociotechnical systems.

## Normative justification

Metric choice is never merely technical because each metric operationalizes an ideal of equality, discrimination, opportunity, desert, or representation. Binns makes that political-philosophy point in [[Binns, 2018|Fairness in Machine Learning: Lessons from Political Philosophy]].

Legal fairness often cares about the consequences of errors, not only the epistemic meaning of scores. Hellman's [[Hellman, 2020|Measuring Algorithmic Fairness]] is the anchor for that action-and-burden view. Policy alignment adds a further constraint: a fairness rule should be evaluated against the legitimate objective of the decision system and the costs of changing the decision rule, as Corbett-Davies and coauthors argue in [[Corbett-Davies et al., 2017|Algorithmic Decision Making and the Cost of Fairness]].

The practical question is therefore: what harm matters in this setting? Is it unequal evidential meaning, unequal error burdens, denial of opportunity, disparate impact, procedural opacity, historical injustice, or the legitimacy of the institution itself?

## Sociotechnical system

The system-level corrective is that fairness is not a mathematical property of a predictive algorithm by itself. It is a property of a decision system: data, model, threshold, interface, human discretion, organizational incentives, legal context, appeal procedures, and downstream effects. Narayanan's [[Narayanan, 2026|What If Algorithmic Fairness Is a Category Error?]] makes this correction explicit.

For the course, this means that model audits are necessary but incomplete. A system can satisfy a parity criterion and still be unfair if it optimizes the wrong target, hides its role, lacks contestation, reinforces punitive institutions, or steers different groups through unequal choice environments.

## Digital relevance

Digital nudging systems can be unfair without issuing a denial. A recommender may hide opportunities, a feed may allocate attention unequally, a fraud screen may impose more friction on some users, a consent flow may pressure vulnerable groups differently, and an AI assistant may explain or withhold options in patterned ways.

The core audit questions are:

- What outcome is being optimized?
- Who receives exposure, friction, warning, opportunity, or exclusion?
- Do scores or rankings have the same meaning across groups?
- Who bears false positives and false negatives?
- What policy goal justifies the metric or threshold?
- Can affected people understand, contest, or escape the system?
- Does the whole sociotechnical system deserve this decision role?

## Related pages

- [[Predictive Algorithms, Bias, and Fairness]]
- [[Fairness Impossibility Results]]
- [[Algorithmic Policy Efficiency]]
- [[Prediction Policy Problems]]
- [[Algorithmic Governance]]
- [[Transparency and Disclosure]]
- [[Digital Nudging]]

## Open questions

How should the course teach formal fairness metrics as indispensable tools without letting them become substitutes for legal, political, and sociotechnical judgment?
