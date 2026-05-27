---
title: Prediction Policy Problems
page_type: concept
status: active
tags:
  - concept
  - prediction-policy
  - algorithmic-decision-support
  - economics
  - digital-nudging
updated_on: 2026-05-26
source_count: 2
related_pages:
  - [[Ludwig et al., 2024|The Unreasonable Effectiveness of Algorithms]]
  - [[Mullainathan, 2025|Economics in the Age of Algorithms]]
  - [[Algorithmic Decision Support Efficiency]]
  - [[Kleinberg et al., 2018|Human Decisions and Machine Predictions]]
  - [[Ludwig and Mullainathan, 2021|Fragile Algorithms and Fallible Decision-Makers]]
  - [[Selective Labels]]
  - [[Omitted Payoff Bias]]
  - [[Override Problem]]
  - [[Fairness as Policy Alignment]]
  - [[Digital Nudging]]
---

# Prediction Policy Problems

## Core idea

[[Prediction Policy Problems]] are decisions that hinge on predicting an outcome rather than estimating the causal effect of an intervention. The policy question is not primarily "what does this treatment do?" but "which person, case, option, or situation is most likely to have the relevant outcome?"

In the course sequence, this concept generalizes the bail example. A judge deciding whom to release, a doctor deciding whom to test, a platform deciding what to recommend, a tax authority deciding which returns to audit, and a job seeker deciding which openings to apply to can all involve prediction policy problems.

## Key distinctions

- Prediction versus causation: if the decision changes the payoff conditional on a predicted outcome, prediction is central; if the decision changes the outcome itself, causal inference is central.
- Ranking versus treatment effect: many prediction policy problems are ranking problems in which welfare improves when high-risk, high-benefit, or high-need cases are prioritized correctly.
- Prediction accuracy versus policy value: accurate prediction matters only through the decision and payoff function it supports.
- Algorithmic aid versus automation: prediction policy problems often call for decision support rather than replacement of human judgment.
- Evaluation versus construction: building the predictor can be comparatively easy; evaluating whether it improves decisions can be difficult.

## Evidence and debate

[[Mullainathan, 2025|Economics in the Age of Algorithms]] presents prediction policy problems as one of the main reasons algorithms should matter to economics. [[Kleinberg et al., 2018|Human Decisions and Machine Predictions]] gives the canonical empirical example in bail, while [[Ludwig and Mullainathan, 2021|Fragile Algorithms and Fallible Decision-Makers]] explains why implementation is fragile.

[[Ludwig et al., 2024|The Unreasonable Effectiveness of Algorithms]] adds the public-policy effectiveness frame. Prediction policy problems often have a ranking structure, and better ranking can create large welfare gains without expanding the underlying policy. This is why algorithmic interventions can have high apparent returns when they are aimed at misranked decisions.

The concept is inseparable from [[Selective Labels]] and [[Omitted Payoff Bias]]. A prediction policy problem can look solved if one ignores missing counterfactual outcomes or evaluates only one narrow outcome. That is why Mullainathan treats the hard work as economic and econometric, not merely computational.

## Practical or policy relevance

For [[Digital Nudging]], prediction policy problems describe many algorithmic choice architectures: recommender systems, triage tools, fraud alerts, safety prompts, benefit targeting, consumer decision aids, and AI assistants. These systems decide what to show, when to intervene, whom to prioritize, and what explanation to provide.

The digital-nudging question is therefore not just whether a prediction is accurate. It is whether the prediction-guided workflow improves welfare, preserves agency, handles omitted values, and remains contestable.

## Related pages

- [[Mullainathan, 2025|Economics in the Age of Algorithms]]
- [[Ludwig et al., 2024|The Unreasonable Effectiveness of Algorithms]]
- [[Algorithmic Decision Support Efficiency]]
- [[Selective Labels]]
- [[Omitted Payoff Bias]]
- [[Override Problem]]
- [[Digital Nudging]]

## Open questions

Which digital nudging examples should become the course's non-criminal-justice cases for prediction policy problems: job search, consumer choice, health insurance, recommender systems, or tax/audit targeting?
