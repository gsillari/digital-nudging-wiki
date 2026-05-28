---
title: Error Rate Parity
page_type: concept
status: active
tags:
  - concept
  - algorithmic-fairness
  - error-rate-parity
  - false-positives
  - false-negatives
updated_on: 2026-05-26
source_count: 6
related_pages:
  - [[Hellman, 2020|Measuring Algorithmic Fairness]]
  - [[Narayanan, 2026|What If Algorithmic Fairness Is a Category Error?]]
  - [[Corbett-Davies et al., 2017|Algorithmic Decision Making and the Cost of Fairness]]
  - [[Angwin et al., 2016|Machine Bias]]
  - [[Kleinberg et al., 2016|Inherent Trade-Offs in the Fair Determination of Risk Scores]]
  - [[Fairness Metrics]]
  - [[Predictive Parity]]
  - [[COMPAS Controversy]]
  - [[Risk Assessment in Criminal Justice]]
  - [[Fairness as Policy Alignment]]
  - [[Sociotechnical Fairness]]
  - [[Algorithmic Fairness]]
---

# Error Rate Parity

## Core idea

[[Error Rate Parity]] is the fairness idea that the practical burdens of algorithmic mistakes should not fall differently across protected groups. The simplest versions ask whether false positive rates or false negative rates are equal across groups. Hellman's more precise version, error ratio parity, asks whether the ratio between false positives and false negatives is the same across groups.

For the course, this is the pragmatic or error-burden family of fairness criteria. It asks how a system's mistakes translate into action, burden, risk, or protection.

## Key distinctions

- False positive rate parity: among people who do not have the target trait or outcome, groups should be equally likely to be mistakenly classified positive.
- False negative rate parity: among people who do have the target trait or outcome, groups should be equally likely to be mistakenly classified negative.
- Equalized odds: a combined requirement that both false positive and false negative rates are equal across groups.
- Error ratio parity: Hellman's preferred legal-philosophical criterion, focused on whether the balance between false positives and false negatives is the same across groups.
- Error rates versus predictive parity: [[Predictive Parity]] asks whether a score or positive prediction has the same evidential meaning across groups; error-rate criteria ask who bears which kind of mistake.
- Aggregate error rates versus marginal treatment: aggregate error disparities can reflect base rates and distributions of easy or hard cases, so they need interpretation rather than automatic condemnation.

## Evidence and debate

[[Angwin et al., 2016|Machine Bias]] made error-rate disparity vivid in the COMPAS case: Black defendants were more likely to be falsely labeled high risk, while white defendants were more likely to be falsely labeled low risk. [[Kleinberg et al., 2016|Inherent Trade-Offs in the Fair Determination of Risk Scores]] shows why calibration and error-balance conditions cannot generally coexist when base rates differ and prediction is imperfect.

[[Hellman, 2020|Measuring Algorithmic Fairness]] gives the legal argument for taking error rates seriously. Hellman argues that predictive parity concerns belief, while fairness usually concerns action. Because false positives and false negatives often have different moral costs, an algorithm can be practically unfair if it effectively applies a different error-cost balance to different protected groups.

[[Corbett-Davies et al., 2017|Algorithmic Decision Making and the Cost of Fairness]] gives the policy-cost counterpoint. Corbett-Davies et al. analyze predictive equality, a false-positive-rate parity criterion, as a constraint on public-safety optimization. They show that satisfying it can require group-specific thresholds and can reduce the modeled policy objective.

[[Narayanan, 2026|What If Algorithmic Fairness Is a Category Error?]] keeps error-rate parity in view but demotes it from a final fairness test to a diagnostic. Unequal error burdens can reveal serious harm, but equalized errors do not prove that a system is just, valid, procedurally fair, or legitimate.

## Practical or policy relevance

Error rate parity is central whenever the consequence of a mistaken classification is serious: detention, denial, exclusion, intensified surveillance, loss of opportunity, or exposure to harm. In digital nudging, false positives can wrongly target users as vulnerable, risky, fraudulent, low-value, or persuadable; false negatives can fail to protect or support users who need help.

Hellman's caution is important: error-rate disparity is not always proof of unfairness. It is a reason to investigate measurement error, biased inputs, base-rate histories, and compounding injustice, especially when the affected groups have been legally or socially disadvantaged.

Corbett-Davies et al.'s caution is complementary: error-rate parity can be costly relative to a policy goal, and the cost should be made explicit. The hard question is whether the cost is justified by the legal and moral importance of reducing the disparity.

Narayanan's caution is broader: after asking who bears mistakes, the course must still ask whether the institution should use the predictive system, what alternatives exist, whether people can contest outputs, and whether the system shifts attention away from deeper reform.

## Related pages

- [[Hellman, 2020|Measuring Algorithmic Fairness]]
- [[Corbett-Davies et al., 2017|Algorithmic Decision Making and the Cost of Fairness]]
- [[Fairness as Policy Alignment]]
- [[Sociotechnical Fairness]]
- [[Predictive Parity]]
- [[Fairness Metrics]]
- [[Fairness Impossibility Results]]
- [[COMPAS Controversy]]
- [[Algorithmic Fairness]]
- [[Algorithmic Accountability and Fairness]]

## Open questions

How should course examples distinguish equal false positive rates, equal false negative rates, equalized odds, and Hellman's error ratio parity without making the module too technical?
