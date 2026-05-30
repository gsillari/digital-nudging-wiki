---
title: "Hedden, 2021"
page_type: source
source_path: raw/papers/Hedden, 2021.pdf
source_type: paper
status: active
tags:
  - source
  - algorithmic-fairness
  - predictive-parity
  - calibration
  - fairness-metrics
updated_on: 2026-05-26
related_pages:
  - [[Algorithmic Fairness]]
  - [[Fairness Impossibility Results]]
  - [[Brian Hedden]]
---

# Hedden, 2021: On Statistical Criteria of Algorithmic Fairness

## Summary

Brian Hedden argues that most statistical criteria proposed for algorithmic fairness are not necessary conditions for fairness. The major exception is the calibration family: for risk scores, calibration within groups; for binary predictions, predictive values that preserve the evidential meaning of a prediction across groups.

The paper is useful after [[Angwin et al., 2016|Machine Bias]] and [[Kleinberg et al., 2016|Inherent Trade-Offs in the Fair Determination of Risk Scores]] because it gives a philosophical defense of the calibration side of the COMPAS debate. Hedden's central thought is that a risk score should have the same evidential import regardless of group membership. If a score of 0.7 indicates one probability for one group and another probability for another group, the score treats people differently in virtue of group membership.

## Key claims

- Statistical fairness criteria are attractive because they can often be evaluated from predictions and outcomes without inspecting an opaque or proprietary model.
- Hedden reviews eleven criteria: three for risk scores and eight for binary predictions.
- Calibration within groups is the key risk-score criterion: for each score, the expected share of people with the target outcome should be the same across groups and should match the score.
- Equal positive predictive value and equal negative predictive value are binary-prediction analogues of the same evidential idea.
- Other criteria, including error-rate parity, balance for positive and negative classes, statistical parity, and equal overall error rates, can be violated by a manifestly fair and uniquely optimal predictive algorithm.
- The violations can occur even when group base rates are equal, so unequal base rates are not the only source of metric conflict.
- Calibration may be necessary, but Hedden does not treat it as sufficient. Fairness may also depend on model features, proxies, the decision rule built on top of predictions, background injustice, and side effects such as stereotype reinforcement.

## Evidence and methods

The central argument uses a thought experiment involving people, coins, and rooms. Individuals receive coins with known chances of landing heads. A prediction algorithm reads the label on each coin, assigns the corresponding risk score, and predicts heads when the chance is above a threshold. The algorithm is fair because room membership is irrelevant to the prediction and the coin label is the uniquely optimal evidence.

Hedden then shows that this fair algorithm can violate every reviewed statistical criterion except calibration within groups. This is especially important because the example can be constructed with equal base rates across rooms. The point is not that real COMPAS-like cases are like coin flips, but that many statistical parity failures can reflect distributions of clear and marginal cases rather than unfair treatment by the predictor.

## Why it matters for Digital Nudging

Digital nudging systems often work with scores: relevance scores, risk scores, quality scores, trust scores, propensities to click, predicted churn, predicted need, or predicted vulnerability. Hedden supplies a strong reason to require that a score mean the same thing across groups before it is used to steer attention or action.

At the same time, the paper keeps the course from collapsing fairness into score calibration. A calibrated prediction can still be deployed through unfair thresholds, harmful institutional uses, background injustice, or stereotype-reinforcing presentation. For digital nudging, this distinction is crucial: the fairness of a predictive signal is not the same as the fairness of the choice architecture built around it.

## Links into the wiki

- predictive parity ([[Fairness Impossibility Results]]): the concept page for Hedden's central calibration/evidential-meaning claim.
- fairness metrics ([[Algorithmic Fairness]]): the broader taxonomy of parity, calibration, and error criteria.
- [[Fairness Impossibility Results]]: Hedden's response to pessimistic readings of metric incompatibility.
- COMPAS controversy ([[Algorithmic Fairness]]): the motivating case in which ProPublica and calibration-based defenses emphasized different fairness ideas.

## Open questions

- How should Hedden's defense of calibration be paired with Hellman's argument about the moral significance of different errors?
- Should the course treat calibration as a minimum condition for fair prediction, or as one important value among several institutional goals?
- How should the critique of fairness metrics handle downstream harms that Hedden says may not make the predictive algorithm itself unfair?

## Bibliographic reference

Hedden, B. (2021). On statistical criteria of algorithmic fairness. *Philosophy & Public Affairs, 49*(2), 209-231. https://doi.org/10.1111/papa.12189
