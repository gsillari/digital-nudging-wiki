---
title: Algorithmic Fairness as Political Philosophy
page_type: concept
status: active
tags:
  - concept
  - algorithmic-fairness
  - political-philosophy
  - egalitarianism
  - normative-theory
updated_on: 2026-05-26
source_count: 4
related_pages:
  - [[Binns, 2018|Fairness in Machine Learning: Lessons from Political Philosophy]]
  - [[Hellman, 2020|Measuring Algorithmic Fairness]]
  - [[Corbett-Davies et al., 2017|Algorithmic Decision Making and the Cost of Fairness]]
  - [[Narayanan, 2026|What If Algorithmic Fairness Is a Category Error?]]
  - [[Algorithmic Fairness]]
  - [[Fairness Metrics]]
  - [[Error Rate Parity]]
  - [[Fairness as Policy Alignment]]
  - [[Sociotechnical Fairness]]
  - [[Fairness Impossibility Results]]
  - [[COMPAS Controversy]]
  - [[Risk Assessment in Criminal Justice]]
  - [[Algorithmic Accountability and Fairness]]
---

# Algorithmic Fairness as Political Philosophy

## Core idea

[[Algorithmic Fairness as Political Philosophy]] is the view that fairness and bias in algorithmic systems cannot be defined by statistical metrics alone. A metric operationalizes a prior normative theory about discrimination, equality, justice, responsibility, harm, opportunity, representation, or legitimate differential treatment.

In the course sequence, this page marks the turn from metrics to normative theory. [[Fairness Metrics]] describe possible mathematical criteria; political philosophy helps decide which criterion, if any, fits the moral problem.

## Key distinctions

- Metric versus ideal: a fairness metric is a technical proxy for a normative ideal, not the ideal itself.
- Discrimination versus fairness: a system may be unfair without being discriminatory in the classic sense, and a discrimination account may not cover every algorithmic harm.
- Mental-state accounts: if discrimination requires animus, contempt, or disrespect, algorithmic systems raise attribution problems.
- Individual treatment accounts: if discrimination is wrong because it fails to treat people as individuals, predictive systems are challenging because all prediction generalizes.
- Egalitarian currencies: fairness may concern welfare, resources, capabilities, democratic status, opportunity, or recognition.
- Spheres of justice: the right fairness criterion can differ across domains such as credit, voting, employment, criminal justice, search ranking, and platform moderation.
- Deontic justice: whether a disparity is unfair depends partly on how it was produced historically and institutionally, not only on the disparity itself.
- Representational harms: some algorithmic harms concern cultural representation, identity, language, visibility, or stereotypes rather than direct allocation of benefits and burdens.

## Evidence and debate

[[Binns, 2018|Fairness in Machine Learning: Lessons from Political Philosophy]] maps fair ML definitions onto political-philosophical debates. Binns argues that statistical criteria such as demographic parity, equality of opportunity, disparate mistreatment, and counterfactual fairness make different assumptions about what discrimination and fairness mean.

This complicates the post-COMPAS sequence. [[Kleinberg et al., 2016|Inherent Trade-Offs in the Fair Determination of Risk Scores]] shows that some fairness metrics are mutually incompatible. [[Hedden, 2021|On Statistical Criteria of Algorithmic Fairness]] gives calibration and [[Predictive Parity]] a privileged role for fair prediction. [[Hellman, 2020|Measuring Algorithmic Fairness]] then argues from a legal perspective that fair treatment is more directly connected to [[Error Rate Parity]] because fairness usually concerns action rather than belief. [[Corbett-Davies et al., 2017|Algorithmic Decision Making and the Cost of Fairness]] adds that a metric's value depends on how it aligns with regulatory or policy goals. Binns widens the frame: the choice among metrics and interventions depends on the philosophical account of justice appropriate to the domain. [[Narayanan, 2026|What If Algorithmic Fairness Is a Category Error?]] widens it again: a philosophically justified metric may still be aimed at the wrong object if the full sociotechnical decision system is ignored.

## Practical or policy relevance

For digital nudging, the key implication is that platform fairness cannot be solved by choosing a metric from a menu. A recommender system, content moderation tool, search engine, targeting model, or personalized interface may distribute different goods: attention, visibility, speech, opportunity, risk, protection, or persuasion. The moral stakes differ across those goods.

This means governance should require a normative justification for metric choice. Designers and regulators should ask: What is being distributed? Which groups are affected? Are disparities caused by legitimate differences, background injustice, historical exclusion, or harmful representation? Is the target equal outcome, equal opportunity, priority for the worse off, equal civic standing, or something else?

Policy alignment adds a second governance question: What is the decision system legitimately trying to accomplish, and does the metric improve that goal or obscure it?

Sociotechnical fairness adds a third question: Is the algorithm the right unit of moral analysis, or should the course evaluate the entire institution, interface, appeal structure, and decision workflow?

## Related pages

- [[Binns, 2018|Fairness in Machine Learning: Lessons from Political Philosophy]]
- [[Hellman, 2020|Measuring Algorithmic Fairness]]
- [[Corbett-Davies et al., 2017|Algorithmic Decision Making and the Cost of Fairness]]
- [[Fairness Metrics]]
- [[Error Rate Parity]]
- [[Fairness as Policy Alignment]]
- [[Sociotechnical Fairness]]
- [[Fairness Impossibility Results]]
- [[Predictive Parity]]
- [[COMPAS Controversy]]
- [[Algorithmic Fairness]]
- [[Algorithmic Accountability and Fairness]]

## Open questions

How should the course map specific digital nudging cases to distinct philosophical theories of fairness rather than treating "fairness" as one undifferentiated value?
