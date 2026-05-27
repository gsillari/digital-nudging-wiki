---
title: Selective Labels
page_type: concept
status: active
tags:
  - concept
  - machine-learning
  - evaluation
  - algorithmic-decision-support
  - econometrics
updated_on: 2026-05-26
source_count: 3
related_pages:
  - [[Mullainathan, 2025|Economics in the Age of Algorithms]]
  - [[Kleinberg et al., 2018|Human Decisions and Machine Predictions]]
  - [[Ludwig and Mullainathan, 2021|Fragile Algorithms and Fallible Decision-Makers]]
  - [[Algorithmic Decision Support Efficiency]]
  - [[Risk Assessment in Criminal Justice]]
  - [[Omitted Payoff Bias]]
  - [[Override Problem]]
  - [[Algorithmic Fairness]]
---

# Selective Labels

## Core idea

[[Selective Labels]] are missing outcome labels caused by prior human decisions. In bail, we observe whether released defendants fail to appear or are rearrested, but we do not observe what detained defendants would have done if released. The label is selective because the human decision controls whether the outcome can be observed.

## Why it matters

Selective labels make it hard to compare human decisions with algorithmic predictions. If an algorithm recommends releasing someone whom judges detained, the relevant outcome is counterfactual. A naive evaluation can either overstate or understate the algorithm's value depending on how the missing labels are handled.

## Evidence and debate

[[Kleinberg et al., 2018|Human Decisions and Machine Predictions]] treats selective labels as a central evaluation problem. The authors use judge leniency and quasi-random assignment to construct comparisons that do not simply assume judges have no private information.

[[Ludwig and Mullainathan, 2021|Fragile Algorithms and Fallible Decision-Makers]] generalizes the point. Selective labels appear in hiring, predictive policing, parole, and other domains where past decisions determine which outcomes enter the training or evaluation data.

[[Mullainathan, 2025|Economics in the Age of Algorithms]] turns selective labels into a general warning for prediction policy problems: ignoring missing counterfactual labels can make algorithms look better than human decision-makers by assuming away the human's possible private information.

## Practical or policy relevance

For [[Digital Nudging]], selective labels appear whenever a platform only observes outcomes for options it showed, users it targeted, cases it escalated, or choices it allowed. Recommender systems, fraud tools, and personalized interventions can all inherit blind spots from earlier decisions.

## Related pages

- [[Algorithmic Decision Support Efficiency]]
- [[Prediction Policy Problems]]
- [[Omitted Payoff Bias]]
- [[Override Problem]]
- [[Risk Assessment in Criminal Justice]]
- [[Algorithmic Fairness]]
