---
title: Fairness Impossibility Results
page_type: concept
status: active
tags:
  - concept
  - algorithmic-fairness
  - impossibility
  - calibration
  - parity
updated_on: 2026-05-26
source_count: 4
related_pages:
  - [[Kleinberg et al., 2016|Inherent Trade-Offs in the Fair Determination of Risk Scores]]
  - [[Hedden, 2021|On Statistical Criteria of Algorithmic Fairness]]
  - [[Hellman, 2020|Measuring Algorithmic Fairness]]
  - [[Binns, 2018|Fairness in Machine Learning: Lessons from Political Philosophy]]
  - [[Predictive Parity]]
  - [[Error Rate Parity]]
  - [[Algorithmic Fairness as Political Philosophy]]
  - [[Fairness Metrics]]
  - [[COMPAS Controversy]]
  - [[Algorithmic Fairness]]
  - [[Risk Assessment in Criminal Justice]]
---

# Fairness Impossibility Results

## Core idea

[[Fairness Impossibility Results]] show that multiple plausible fairness conditions for algorithmic prediction cannot generally be satisfied at once. The foundational result currently in the vault is Kleinberg, Mullainathan, and Raghavan's theorem for risk scores: with unequal base rates and imperfect prediction, calibration within groups cannot be combined with balance for both the negative and positive classes.

## Key distinctions

- Structural impossibility is not the same as practical difficulty. The theorem says that some combinations of fairness demands are mathematically incompatible outside special cases.
- The special cases are narrow: perfect prediction or equal base rates across groups.
- The impossibility concerns fairness conditions for scores, not only binary decisions.
- Impossibility does not imply ethical paralysis. It implies that institutions must choose and justify which fairness demand matters most in context.

## Evidence and debate

[[Kleinberg et al., 2016|Inherent Trade-Offs in the Fair Determination of Risk Scores]] formalizes the result after the COMPAS debate. It helps explain why ProPublica and Northpointe-like defenses could each appeal to a plausible fairness idea while talking past each other.

[[Hedden, 2021|On Statistical Criteria of Algorithmic Fairness]] responds to pessimistic readings of these results by arguing that most non-calibration criteria are not necessary for fair prediction. Hedden's coin-and-rooms example is meant to show that a fair and uniquely optimal predictor can violate error-rate and statistical-parity criteria even when base rates are equal. On this view, [[Predictive Parity]] or calibration has a special role because it preserves the evidential meaning of a score across groups.

[[Hellman, 2020|Measuring Algorithmic Fairness]] argues that the impossibility result should not lead us to privilege predictive parity simply because it preserves meaning. Hellman treats predictive parity as epistemic and [[Error Rate Parity]] as pragmatic: fairness turns on action, error costs, and treatment.

[[Binns, 2018|Fairness in Machine Learning: Lessons from Political Philosophy]] adds that impossibility results create philosophical work rather than merely technical work. If metrics conflict, the appropriate response is to ask which egalitarian, anti-discrimination, or representational ideal should govern the domain.

The result also sets up later normative readings. Once the metrics conflict, the next question is not only "which metric is mathematically correct?" but "which error, burden, right, or institutional goal should govern this setting, and is the unfairness in the prediction, the decision rule, or the surrounding institution?"

## Practical or policy relevance

For digital nudging, impossibility results are a warning against treating fairness as a post-hoc technical patch. If recommender systems, targeting engines, predictive models, or eligibility scores optimize one fairness criterion, they may worsen another. Designers and regulators need an explicit account of the decision context, the affected parties, and the cost of different errors.

## Related pages

- [[Kleinberg et al., 2016|Inherent Trade-Offs in the Fair Determination of Risk Scores]]
- [[Hedden, 2021|On Statistical Criteria of Algorithmic Fairness]]
- [[Hellman, 2020|Measuring Algorithmic Fairness]]
- [[Binns, 2018|Fairness in Machine Learning: Lessons from Political Philosophy]]
- [[Algorithmic Fairness as Political Philosophy]]
- [[Predictive Parity]]
- [[Error Rate Parity]]
- [[Fairness Metrics]]
- [[COMPAS Controversy]]
- [[Algorithmic Fairness]]
- [[Algorithmic Accountability and Fairness]]

## Open questions

How should this page incorporate later impossibility results and critiques without turning into a purely technical taxonomy?
