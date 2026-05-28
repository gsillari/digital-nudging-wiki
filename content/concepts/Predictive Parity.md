---
title: Predictive Parity
page_type: concept
status: active
tags:
  - concept
  - algorithmic-fairness
  - predictive-parity
  - calibration
  - fairness-metrics
updated_on: 2026-05-26
source_count: 4
related_pages:
  - [[Hellman, 2020|Measuring Algorithmic Fairness]]
  - [[Hedden, 2021|On Statistical Criteria of Algorithmic Fairness]]
  - [[Error Rate Parity]]
  - [[Fairness Metrics]]
  - [[COMPAS Controversy]]
  - [[Fairness Impossibility Results]]
  - [[Risk Assessment in Criminal Justice]]
  - [[Algorithmic Fairness]]
---

# Predictive Parity

## Core idea

[[Predictive Parity]] is the fairness idea that a prediction should have the same evidential meaning across groups. For binary predictions, this is usually stated as equal positive predictive value: among people predicted positive, the share who are actually positive should be the same across groups. For risk scores, the closely related criterion is calibration within groups: a given score should correspond to the same outcome probability across groups.

For the course, this is the "same meaning" criterion. If two people receive the same risk score, the score should not mean one level of risk for one group and a different level of risk for another.

## Key distinctions

- Risk-score calibration: a score such as 0.7 should indicate the same probability of the target outcome in every relevant group.
- Binary predictive parity: a positive classification should have the same positive predictive value across groups.
- Negative predictive value parity: a negative classification should have the same evidential meaning across groups.
- Error-rate parity: predictive parity differs from equal false positive or false negative rates. A system can satisfy one and violate the other.
- Epistemic versus pragmatic criteria: Hellman treats predictive parity as a criterion for what to believe, while [[Error Rate Parity]] concerns what to do and who bears mistakes.
- Fair prediction versus fair use: a prediction may preserve evidential meaning while the threshold, action, institution, or social effect built on it remains unfair.

## Evidence and debate

In the [[COMPAS Controversy]], ProPublica emphasized unequal false positive and false negative burdens, while calibration-based responses emphasized that risk scores had roughly the same meaning across racial groups. [[Kleinberg et al., 2016|Inherent Trade-Offs in the Fair Determination of Risk Scores]] shows why calibration and error-balance conditions cannot generally be combined when base rates differ and prediction is imperfect.

[[Hedden, 2021|On Statistical Criteria of Algorithmic Fairness]] gives the calibration side a philosophical defense. Hedden argues that most statistical criteria are not necessary for fairness, while calibration within groups is special because its violation means the same score carries different evidential import depending on group membership.

[[Hellman, 2020|Measuring Algorithmic Fairness]] gives the legal counterweight. Hellman agrees that predictive parity preserves meaning, but argues that this makes it primarily epistemic. Because fairness usually concerns treatment and action, she argues that error-rate and error-ratio measures are more directly relevant to legal fairness.

## Practical or policy relevance

Predictive parity is especially important for decision support. Judges, loan officers, clinicians, moderators, and digital platforms need to know what a score means. If the meaning varies by group, the score becomes misleading or discriminatory even before one asks what action should follow.

For digital nudging, predictive parity is a constraint on personalization and scoring. But it is not a complete governance framework. A platform could use well-calibrated scores to target harmful nudges, allocate burdens unfairly, or intensify surveillance. Predictive parity secures the meaning of the signal, not the justice of the action rule.

## Related pages

- [[Hellman, 2020|Measuring Algorithmic Fairness]]
- [[Hedden, 2021|On Statistical Criteria of Algorithmic Fairness]]
- [[Error Rate Parity]]
- [[Fairness Metrics]]
- [[Fairness Impossibility Results]]
- [[COMPAS Controversy]]
- [[Algorithmic Fairness]]
- [[Algorithmic Accountability and Fairness]]

## Open questions

How should predictive parity be preserved while also addressing morally asymmetric error costs in legal, financial, medical, and platform settings?
