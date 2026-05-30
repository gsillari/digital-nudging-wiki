---
title: "Corbett-Davies et al., 2017"
page_type: source
source_path: raw/papers/Corbett-Davies et al., 2017.pdf
source_type: paper
status: active
tags:
  - source
  - algorithmic-fairness
  - policy-alignment
  - criminal-justice
  - decision-thresholds
updated_on: 2026-05-26
related_pages:
  - [[Algorithmic Fairness]]
  - [[Algorithmic Fairness]]
  - [[Sam Corbett-Davies]]
  - [[Emma Pierson]]
  - [[Avi Feller]]
  - [[Sharad Goel]]
  - [[Aziz Huq]]
---

# Corbett-Davies et al., 2017: Algorithmic Decision Making and the Cost of Fairness

## Summary

Corbett-Davies, Pierson, Feller, Goel, and Huq argue that algorithmic fairness should be analyzed in relation to the policy objective a decision rule is supposed to serve. In pretrial release, they model the objective as maximizing public safety while accounting for the social and economic costs of detention. Formal fairness constraints can then be treated as constraints on that objective.

Their central result is that several common fairness definitions force a decision-maker to use group-specific thresholds. A rule satisfying statistical parity, conditional statistical parity, or predictive equality may detain one group at a different risk threshold than another. By contrast, the unconstrained utility-maximizing rule applies one uniform risk threshold to everyone.

## Key claims

- Fairness constraints should be evaluated as constraints on a concrete decision objective, not as isolated statistical ideals.
- In the pretrial setting, the authors define immediate utility as a balance between crimes prevented and the cost of detention.
- The unconstrained utility-maximizing decision rule detains people above a single risk threshold, regardless of race.
- Common fairness constraints, including statistical parity, conditional statistical parity, and predictive equality, generally require multiple group-specific thresholds.
- The paper treats this as a real trade-off: satisfying common fairness metrics can reduce public safety relative to the unconstrained rule, while optimizing public safety can produce racial disparities.
- In the Broward County data, enforcing the studied fairness constraints increased estimated violent crime among released defendants and detained some defendants the public-safety rule would classify as lower risk.
- Calibration alone is insufficient to assess discrimination because calibrated scores can be strategically uninformative or can fail to answer the decision question.
- The authors emphasize that algorithmic decision-making does not preclude other policy interventions, such as social services, non-custodial supervision, improved data, higher detention thresholds, or changing the consequences of classifications.

## Evidence and methods

The paper formalizes algorithmic decision-making as constrained optimization. It defines decision rules, group membership, target outcomes, and immediate utility. The formal result shows that threshold rules are optimal both without fairness constraints and under the studied constraints, but the constrained rules generally require group-specific thresholds.

Empirically, the authors use the Broward County COMPAS data compiled by ProPublica. They train a logistic risk model for two-year violent recidivism using available features other than race, then compare unconstrained public-safety optimization to rules satisfying statistical parity, conditional statistical parity, and predictive equality.

## Why it matters for Digital Nudging

This paper adds the policy-alignment layer to the algorithmic fairness module. Digital nudging systems usually optimize something: safety, revenue, retention, attention quality, welfare access, fraud reduction, learning, exposure diversity, or user well-being. A fairness metric is not automatically appropriate simply because it reduces a visible disparity. It must be assessed against the policy goal, the legal context, the costs of errors, and the decision threshold.

For the course, the key lesson is not "ignore fairness for efficiency." It is that fairness claims should be connected to the objective of the intervention and the available policy alternatives. A platform can change the score, the threshold, the decision consequence, the data, or the surrounding support system. The fairness question is which combination best serves the justified goal without imposing unjustified burdens.

## Links into the wiki

- fairness as policy alignment ([[Algorithmic Fairness]]): the concept extracted from the paper.
- fairness metrics ([[Algorithmic Fairness]]): formal metrics become constraints whose value depends on the policy context.
- error rate parity ([[Fairness Impossibility Results]]): the paper studies predictive equality, a false-positive-rate criterion, and shows its cost under a public-safety objective.
- risk assessment in criminal justice ([[Algorithmic Fairness]]): the main institutional setting.
- algorithmic fairness as political philosophy ([[Algorithmic Fairness]]): connects policy objectives to normative justification.

## Open questions

- How should this paper be paired with Hellman's claim that error-rate disparities raise legal and moral concerns even when they carry policy costs?
- When is a uniform threshold itself the relevant fairness ideal, and when does it merely preserve a problematic status quo?
- How should the course handle long-term welfare, historical injustice, and omitted payoffs that are not captured by immediate utility?

## Bibliographic reference

Corbett-Davies, S., Pierson, E., Feller, A., Goel, S., & Huq, A. (2017). Algorithmic decision making and the cost of fairness. In *Proceedings of the 23rd ACM SIGKDD International Conference on Knowledge Discovery and Data Mining* (pp. 797-806). Association for Computing Machinery. https://doi.org/10.1145/3097983.3098095
