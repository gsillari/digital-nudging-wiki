---
title: Omitted Payoff Bias
page_type: concept
status: active
tags:
  - concept
  - algorithmic-decision-support
  - decision-theory
  - policy-alignment
  - econometrics
updated_on: 2026-05-26
source_count: 3
related_pages:
  - [[Mullainathan, 2025|Economics in the Age of Algorithms]]
  - [[Kleinberg et al., 2018|Human Decisions and Machine Predictions]]
  - [[Ludwig and Mullainathan, 2021|Fragile Algorithms and Fallible Decision-Makers]]
  - [[Algorithmic Decision Support Efficiency]]
  - [[Fairness as Policy Alignment]]
  - [[Risk Assessment in Criminal Justice]]
  - [[Selective Labels]]
  - [[Override Problem]]
  - [[Algorithmic Fairness]]
---

# Omitted Payoff Bias

## Core idea

[[Omitted Payoff Bias]] arises when an algorithm predicts one outcome even though the real decision depends on a broader payoff function. A system may look better than human decision-making on the measured outcome while worsening values that were not measured.

In bail, the omitted-payoff problem is relatively narrow because the legal decision is closely tied to flight and public-safety risk. In sentencing, by contrast, recidivism prediction is only one input among deterrence, culpability, remorse, proportionality, and social meaning.

## Why it matters

Omitted payoff bias is the efficiency branch's version of the "wrong target" problem. A system that improves prediction is not necessarily a system that improves decisions. The outcome must match the legitimate objective, and the objective must include the values the institution is supposed to serve.

## Evidence and debate

[[Kleinberg et al., 2018|Human Decisions and Machine Predictions]] explicitly warns that outperforming judges on one predicted outcome does not prove that the algorithm improves welfare if judges or society care about other outcomes. The authors therefore examine other possible concerns, including violent crime and racial disparities.

[[Ludwig and Mullainathan, 2021|Fragile Algorithms and Fallible Decision-Makers]] makes omitted payoff bias one of the reasons algorithms are fragile. Poorly specified objectives can turn a useful predictor into a misleading recommendation system.

[[Mullainathan, 2025|Economics in the Age of Algorithms]] uses omitted payoff bias to explain why prediction policy problems still need economics. The core question is not simply what the algorithm predicts, but whether the prediction matches the decision-maker's legitimate objective function.

## Practical or policy relevance

For [[Digital Nudging]], omitted payoff bias is everywhere. Platforms may optimize engagement, conversion, watch time, click-through, churn, fraud loss, or short-term satisfaction while omitting autonomy, privacy, learning, well-being, exposure diversity, or long-term regret.

This concept links the efficiency branch to [[Fairness as Policy Alignment]]: the decision target has to be explicit, justified, and broad enough to include the relevant harms and benefits.

## Related pages

- [[Algorithmic Decision Support Efficiency]]
- [[Prediction Policy Problems]]
- [[Fairness as Policy Alignment]]
- [[Selective Labels]]
- [[Override Problem]]
- [[Risk Assessment in Criminal Justice]]
- [[Digital Nudging]]
