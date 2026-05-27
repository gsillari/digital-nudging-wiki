---
title: COMPAS Controversy
page_type: concept
status: active
tags:
  - concept
  - algorithmic-fairness
  - compas
  - criminal-justice
  - risk-assessment
updated_on: 2026-05-26
source_count: 7
related_pages:
  - [[Angwin et al., 2016|Machine Bias]]
  - [[Kleinberg et al., 2016|Inherent Trade-Offs in the Fair Determination of Risk Scores]]
  - [[Hedden, 2021|On Statistical Criteria of Algorithmic Fairness]]
  - [[Hellman, 2020|Measuring Algorithmic Fairness]]
  - [[Binns, 2018|Fairness in Machine Learning: Lessons from Political Philosophy]]
  - [[Corbett-Davies et al., 2017|Algorithmic Decision Making and the Cost of Fairness]]
  - [[Narayanan, 2026|What If Algorithmic Fairness Is a Category Error?]]
  - [[Predictive Parity]]
  - [[Error Rate Parity]]
  - [[Algorithmic Fairness as Political Philosophy]]
  - [[Fairness as Policy Alignment]]
  - [[Sociotechnical Fairness]]
  - [[Algorithmic Fairness]]
  - [[Fairness Metrics]]
  - [[Fairness Impossibility Results]]
  - [[Risk Assessment in Criminal Justice]]
  - [[Algorithmic Accountability and Fairness]]
---

# COMPAS Controversy

## Core idea

The [[COMPAS Controversy]] is the debate over whether the COMPAS criminal justice risk score was racially biased and how such bias should be measured. [[Angwin et al., 2016|Machine Bias]] made the case famous by showing asymmetric error burdens across racial groups. [[Kleinberg et al., 2016|Inherent Trade-Offs in the Fair Determination of Risk Scores]] then clarified that the debate involved incompatible fairness criteria, not just competing empirical claims. [[Hedden, 2021|On Statistical Criteria of Algorithmic Fairness]] adds the argument that calibration or [[Predictive Parity]] has a privileged role because it keeps scores evidentially meaningful across groups. [[Narayanan, 2026|What If Algorithmic Fairness Is a Category Error?]] reframes the case as a warning that even a metric-satisfying risk system can be unjust if the surrounding criminal justice decision system is unjust.

## Key distinctions

- Error burden: ProPublica emphasized that Black defendants were more likely to be falsely labeled high risk, while white defendants were more likely to be falsely labeled low risk.
- Calibration: defenders of the score emphasized whether a given score meant the same empirical probability of recidivism across groups.
- Predictive parity: in Hedden's framing, a prediction or score should carry the same evidential meaning regardless of group membership.
- Error-rate parity: in Hellman's framing, the legal fairness concern is practical: whether false positive and false negative burdens are balanced similarly across protected groups.
- Policy alignment: in Corbett-Davies et al.'s framing, fairness constraints should be evaluated by their effect on the policy objective and by whether group-specific thresholds are legally and normatively acceptable.
- Sociotechnical fairness: in Narayanan's framing, the fairness of COMPAS cannot be settled by the score alone; it depends on pretrial detention, judicial workflow, procedural opacity, community effects, and reform alternatives.
- Overall accuracy: similar aggregate error rates can hide different kinds of mistakes across groups.
- Proprietary opacity: even if a score is calibrated, defendants and the public may lack access to the full model, inputs, or validation evidence.
- Decision support versus decision-making: COMPAS did not formally sentence defendants, but it entered institutional decisions through salience, framing, and authority.

## Evidence and debate

The controversy begins with Broward County data and a public investigation of more than 7,000 defendants. It then becomes a general fairness debate because risk scores can be evaluated by multiple plausible criteria. If base rates differ and prediction is imperfect, calibration and equalized error rates cannot generally be achieved together.

For the course, the dispute should be presented as a bridge between journalism, statistics, law, political philosophy, policy design, and sociotechnical critique. The data show a harm pattern; the impossibility result shows that no single metric removes normative choice; Hedden shows why the calibration family still has special force for fair prediction; Hellman argues that legal fairness focuses on action and error burdens; Corbett-Davies et al. show that fairness constraints can have policy costs; Binns explains why deciding between fairness ideals requires political philosophy rather than statistical analysis alone; Narayanan asks whether metric-centered analysis misses the larger decision system.

## Practical or policy relevance

COMPAS is a clean example of algorithmic choice architecture in a coercive institution. Scores can shape bail, sentencing, supervision, treatment eligibility, and parole while being framed as neutral evidence. That makes transparency, contestability, validation, and the distribution of errors central to governance.

Narayanan makes the digital-nudging analogy sharper: the score is only one part of an institutional interface that makes some futures salient, shifts responsibility, and can legitimate preemptive restriction. That is why COMPAS should now be taught as both a metrics case and a sociotechnical systems case.

## Related pages

- [[Angwin et al., 2016|Machine Bias]]
- [[Kleinberg et al., 2016|Inherent Trade-Offs in the Fair Determination of Risk Scores]]
- [[Hedden, 2021|On Statistical Criteria of Algorithmic Fairness]]
- [[Hellman, 2020|Measuring Algorithmic Fairness]]
- [[Binns, 2018|Fairness in Machine Learning: Lessons from Political Philosophy]]
- [[Corbett-Davies et al., 2017|Algorithmic Decision Making and the Cost of Fairness]]
- [[Algorithmic Fairness as Political Philosophy]]
- [[Fairness as Policy Alignment]]
- [[Sociotechnical Fairness]]
- [[Predictive Parity]]
- [[Error Rate Parity]]
- [[Fairness Metrics]]
- [[Fairness Impossibility Results]]
- [[Risk Assessment in Criminal Justice]]
- [[Algorithmic Fairness]]

## Open questions

How should the class sequence balance the clean metric conflict with the broader sociotechnical critique without losing the force of either?
