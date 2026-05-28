---
title: Fairness Metrics
page_type: concept
status: active
tags:
  - concept
  - algorithmic-fairness
  - parity
  - calibration
  - risk-scores
updated_on: 2026-05-26
source_count: 7
related_pages:
  - [[Algorithmic Fairness]]
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
  - [[COMPAS Controversy]]
  - [[Fairness Impossibility Results]]
  - [[Risk Assessment in Criminal Justice]]
---

# Fairness Metrics

## Core idea

[[Fairness Metrics]] are formal criteria for evaluating whether an algorithmic score, ranking, classifier, or decision rule treats groups fairly. The crucial course lesson is that these metrics are not interchangeable. Different metrics identify different harms, and some cannot be satisfied together.

## Key distinctions

- Calibration within groups: among people assigned a given risk score, the observed outcome rate should match that score in each group. The score has the same empirical meaning across groups.
- [[Predictive Parity]]: for binary predictions, the positive predictive value of a positive prediction should be the same across groups. In the course sequence, this belongs to the same evidential-meaning family as calibration for risk scores.
- Balance for the negative class: among people who do not experience the target outcome, the average assigned score should be the same across groups. This tracks the burden of being scored too risky when one would not have reoffended.
- Balance for the positive class: among people who do experience the target outcome, the average assigned score should be the same across groups. This tracks the burden of being scored too low when one would have reoffended.
- [[Error Rate Parity]]: in binary classification, fairness can require equal false positive rates, equal false negative rates, equalized odds, or Hellman's error-ratio parity across groups.
- Statistical parity: groups receive the favorable or unfavorable classification at the same rate. This is distinct from calibration and can be inappropriate when the target outcome or legitimate qualification rates differ.
- Score versus threshold: a calibrated risk score and a binary high-risk classification can raise different fairness questions, especially when thresholds vary by context.

## Evidence and debate

The COMPAS debate is the motivating case. [[Angwin et al., 2016|Machine Bias]] centers unequal false high-risk and false low-risk labels. [[Kleinberg et al., 2016|Inherent Trade-Offs in the Fair Determination of Risk Scores]] shows that calibration, balance for the negative class, and balance for the positive class cannot generally coexist when base rates differ and prediction is imperfect.

[[Hedden, 2021|On Statistical Criteria of Algorithmic Fairness]] then gives calibration and predictive parity a stronger philosophical role. Hedden argues that the non-calibration criteria are not necessary conditions for fairness because a manifestly fair and uniquely optimal predictor can violate them, even when base rates are equal. Calibration is special because a violation means the same score has different evidential import across groups.

[[Hellman, 2020|Measuring Algorithmic Fairness]] pushes in the other direction from a legal point of view. Hellman argues that predictive parity is an epistemic criterion: it tells us what to believe about a scored person. Legal fairness usually concerns action, treatment, and the burdens of error. For that reason, error-rate and especially error-ratio criteria can be more relevant to fairness than predictive parity.

[[Binns, 2018|Fairness in Machine Learning: Lessons from Political Philosophy]] reframes this whole debate. Binns argues that each metric imports assumptions from political philosophy: what counts as discrimination, which inequalities matter, whether opportunity or outcome is the target, whether brute luck or desert matters, and whether the relevant harm is distributive or representational.

[[Corbett-Davies et al., 2017|Algorithmic Decision Making and the Cost of Fairness]] reframes metrics as constraints on policy optimization. A metric can reduce one disparity while worsening the decision system's stated goal. This makes metric choice a regulatory and policy question, not just a mathematical question.

[[Narayanan, 2026|What If Algorithmic Fairness Is a Category Error?]] then reframes metrics as diagnostics inside a sociotechnical system. A parity violation can be evidence of discrimination or institutional harm, but metric satisfaction does not show that the decision system is fair, valid, legitimate, or worth building.

## Practical or policy relevance

Fairness metrics are policy instruments and diagnostics, not self-standing moral verdicts. Selecting a metric decides whose errors count, what kind of equality is prioritized, and how much accuracy or efficiency may be traded for equal treatment.

For digital nudging, the same issue appears in recommendation systems, targeting, eligibility scoring, content moderation, search ranking, and personalized prompts. A system can be fair by one metric and troubling by another. Following Binns, the course should ask which philosophical account justifies the metric before treating it as an engineering objective. Following Corbett-Davies et al., it should also ask whether the metric is aligned with the legitimate policy goal. Following Narayanan, it should ask whether the metric is even evaluating the right object: the whole choice architecture and decision workflow rather than a model alone.

## Related pages

- [[Algorithmic Fairness]]
- [[Algorithmic Fairness as Political Philosophy]]
- [[Fairness as Policy Alignment]]
- [[Sociotechnical Fairness]]
- [[Predictive Parity]]
- [[Error Rate Parity]]
- [[COMPAS Controversy]]
- [[Fairness Impossibility Results]]
- [[Risk Assessment in Criminal Justice]]
- [[Algorithmic Accountability and Fairness]]

## Open questions

Which additional parity metrics should become separate pages once the Barocas et al. taxonomy is added, and which political theory or sociotechnical audit role best explains each?
