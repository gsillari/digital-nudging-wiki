---
title: "Kleinberg et al., 2016"
page_type: source
source_path: raw/papers/Kleinberg et al., 2016.pdf
source_type: paper
status: active
tags:
  - source
  - algorithmic-fairness
  - fairness-impossibility
  - risk-scores
  - calibration
updated_on: 2026-05-26
related_pages:
  - [[Algorithmic Fairness]]
  - [[Fairness Impossibility Results]]
  - [[Fairness Metrics]]
  - [[COMPAS Controversy]]
  - [[Risk Assessment in Criminal Justice]]
  - [[Algorithmic Accountability and Fairness]]
  - [[Jon Kleinberg]]
  - [[Sendhil Mullainathan]]
  - [[Manish Raghavan]]
---

# Kleinberg et al., 2016: Inherent Trade-Offs in the Fair Determination of Risk Scores

## Summary

Kleinberg, Mullainathan, and Raghavan formalize a central lesson of the [[COMPAS Controversy]]: different intuitive definitions of fairness for risk scores cannot generally be satisfied at the same time. If groups have different base rates and prediction is imperfect, a risk score cannot simultaneously satisfy calibration within groups, balance for the negative class, and balance for the positive class.

The paper is not a defense of any particular criminal justice tool. Its value for the course is conceptual. It shows that fairness disputes are not just caused by bad data, bad intentions, or bad engineering. Some conflicts are structural, so choosing a fairness criterion is partly a normative and institutional choice.

## Key claims

- Calibration within groups means that a score has the same empirical meaning in each group. Among people assigned a given risk score, the same fraction should experience the target outcome in each group.
- Balance for the negative class means that people who do not experience the target outcome receive the same average score across groups. In binary classification, this is closely related to equal false positive burdens.
- Balance for the positive class means that people who do experience the target outcome receive the same average score across groups. In binary classification, this is closely related to equal false negative burdens.
- Except in special cases, these three conditions cannot all hold simultaneously.
- The special cases are substantively narrow: prediction is perfect, or the groups have equal base rates for the target outcome.
- Approximate versions of the fairness conditions still require approximate versions of those special cases.
- Statistical parity is a different condition, and the paper treats it separately from the calibration and balance conditions at stake in the COMPAS debate.

## Evidence and methods

The paper develops a formal model of risk assignments over feature vectors and group membership. It proves a characterization theorem for risk scores satisfying the three fairness conditions and extends the result to approximate satisfaction.

The discussion uses risk assessment, lending, health care allocation, and school admissions as examples of domains where people may reasonably demand fairness but face incompatible statistical desiderata.

## Why it matters for Digital Nudging

Digital nudging increasingly uses scores, rankings, recommendations, and personalized predictions. This paper supplies the fairness grammar for those systems. Once an interface or institution scores users, products, citizens, defendants, patients, or consumers, fairness cannot be reduced to "remove protected attributes" or "make the model accurate."

For the course, the paper marks the transition from the COMPAS case to two later branches. The first branch asks how to define algorithmic bias when mathematical parity criteria conflict. The second branch asks whether algorithmic prediction can still improve institutional decisions, even when fairness constraints, selective labels, and omitted payoffs complicate the efficiency case.

## Links into the wiki

- [[Fairness Impossibility Results]]: the durable concept page for the trade-off theorem.
- [[Fairness Metrics]]: defines calibration, error-rate balance, and statistical parity.
- [[COMPAS Controversy]]: the public debate that motivates the formal distinction.
- [[Algorithmic Fairness]]: the sub-hub that will organize later bias/parity and efficiency/prediction readings.

## Open questions

- Which later source should be used as the main teaching reference for parity measures beyond the three conditions in this paper?
- How should the course teach the move from mathematical impossibility to political, legal, and institutional choice?
- Where should the omitted payoff problem enter the efficiency branch?

## Bibliographic reference

Kleinberg, J., Mullainathan, S., & Raghavan, M. (2016). *Inherent trade-offs in the fair determination of risk scores*. arXiv. https://arxiv.org/abs/1609.05807
