---
title: "Narayanan, 2026"
page_type: source
status: active
source_path: raw/papers/Narayanan, 2026.pdf
source_type: book_chapter
tags:
  - source
  - algorithmic-fairness
  - sociotechnical-systems
  - algorithmic-accountability
  - algorithmic-bureaucracy
updated_on: 2026-05-26
related_pages:
  - [[Algorithmic Fairness]]
  - [[Algorithmic Fairness]]
  - [[Digital Nudging]]
  - [[Arvind Narayanan]]
---

# Narayanan, 2026: What If Algorithmic Fairness Is a Category Error?

## Summary

[[Narayanan, 2026|What If Algorithmic Fairness Is a Category Error?]] is the course's system-level corrective to the fairness-metrics sequence. [[Arvind Narayanan]] argues that the central question is not whether a predictive algorithm satisfies a mathematical fairness property in isolation. The better question is how to design accountable algorithmic bureaucracies: sociotechnical decision systems made of models, data, institutional goals, human discretion, interfaces, thresholds, appeals, incentives, and political context.

The paper does not make fairness metrics useless. It demotes them. Calibration, predictive parity ([[Fairness Impossibility Results]]), error rate parity ([[Fairness Impossibility Results]]), and related metrics can be diagnostics that alert us to possible discrimination or harm, but they should not be treated as constraints whose satisfaction makes a system fair.

## Key claims

- Algorithmic decision-making systems do not exist in a vacuum. Their harms and benefits depend on the organizations, legal regimes, user interfaces, and political choices through which predictions become action.
- The algorithmic fairness movement has often been drawn to mathematically precise criteria because they make fairness tractable, legally legible, and apparently less political. That tractability is also a limitation.
- Fairness is too narrow as a proxy for justice. A system can satisfy a chosen group-fairness metric and still be unjust, invalid, demeaning, unaccountable, punitive, or built around the wrong social goal.
- The COMPAS controversy ([[Algorithmic Fairness]]) should not only be taught as a metric conflict. Even in a counterfactual world without racial error disparity, pretrial risk detention may still be objectionable as precrime, procedurally opaque, and damaging to already burdened communities.
- Fairness metrics should be used as diagnostics for possible sociotechnical discrimination, not as final engineering objectives.
- Bias audits can become a bandage for a deeper bandage. In hiring, social services, and criminal justice, checking group disparities in a model may distract from whether the tool is valid, whether the institution should use it, and whether the underlying policy is itself just.
- Algorithmic bureaucracies require explicit attention to values and goals, but public administration often works through situated judgment and successive limited comparisons rather than clean objective specification.
- Cost-benefit analysis can help compare otherwise hidden trade-offs, but it must account for distribution, nonmarket goods, liberty, dignity, and values smuggled into the analysis.
- Human discretion is not just noise to be replaced. Street-level decision makers often supply judgment, contextual knowledge, moral interpretation, and escalation for cases that rules and models do not anticipate.
- A future "third wave" of algorithmic accountability should sit between model-level fairness tweaks and very broad structural critique: technical enough to inspect systems, political enough to address institutions.

## Conceptual contribution

This paper clarifies the relation among the fairness readings already in the vault:

- [[Kleinberg et al., 2016|Inherent Trade-Offs in the Fair Determination of Risk Scores]] shows why plausible metrics conflict.
- [[Hedden, 2021|On Statistical Criteria of Algorithmic Fairness]] defends predictive parity as preserving the meaning of scores.
- [[Hellman, 2020|Measuring Algorithmic Fairness]] shifts attention from belief to action and error burdens.
- [[Binns, 2018|Fairness in Machine Learning: Lessons from Political Philosophy]] argues that metric choice depends on normative theory.
- [[Corbett-Davies et al., 2017|Algorithmic Decision Making and the Cost of Fairness]] argues that fairness criteria must be assessed against regulatory goals and decision costs.
- Narayanan then pushes one step further: even normatively justified, policy-aligned metrics are only partial diagnostics unless the whole sociotechnical decision system is evaluated.

## Why it matters for Digital Nudging

Digital nudging systems are not merely algorithms. They are choice architectures embedded in platforms, institutions, incentives, data pipelines, feedback loops, A/B tests, recommender systems, human review practices, and governance arrangements. This paper gives the course a vocabulary for saying why fairness in digital nudging cannot be reduced to a ranking metric, a recommender accuracy score, or an equalized error rate.

For [[Hypernudge]], the paper reinforces the concern that algorithmic steering operates through opaque systems rather than isolated decisions. For constructive Behavioral Economics 2.0 ([[Algorithmic Thought Partners]]), it adds a design challenge: algorithmic thought partners and personalized choice architectures should be assessed as sociotechnical systems, including what they optimize, what they explain, when they escalate, how users contest them, and whether they genuinely support agency.

## Bibliographic reference

Narayanan, A. (2026). What if algorithmic fairness is a category error? In S. Nyholm, A. Kasirzadeh, & J. Zerilli (Eds.), *Contemporary debates in the ethics of artificial intelligence* (pp. 77-96). Wiley-Blackwell.
