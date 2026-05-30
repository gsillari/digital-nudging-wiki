---
title: "Mullainathan, 2025"
page_type: source
status: active
source_path: raw/papers/Mullainathan, 2025.pdf
source_type: journal_article
tags:
  - source
  - algorithms
  - prediction-policy
  - economics
  - algorithmic-decision-support
updated_on: 2026-05-26
related_pages:
  - [[Algorithmic Fairness]]
  - [[Algorithmic Policy Efficiency]]
  - [[Prediction Policy Problems]]
  - [[Ludwig et al., 2024|The Unreasonable Effectiveness of Algorithms]]
  - [[Kleinberg et al., 2018|Human Decisions and Machine Predictions]]
  - [[Ludwig and Mullainathan, 2021|Fragile Algorithms and Fallible Decision-Makers]]
  - [[Algorithmic Thought Partners]]
  - [[Digital Nudging]]
  - [[Sendhil Mullainathan]]
---

# Mullainathan, 2025: Economics in the Age of Algorithms

## Summary

[[Mullainathan, 2025|Economics in the Age of Algorithms]] is a high-level summary and agenda-setting paper for the efficiency branch. [[Sendhil Mullainathan]] argues that algorithms are not merely another technology affecting the economy. They change how decisions are studied, modeled, and improved, so they should change economics itself.

For the course, the most important parts are the pretrial decision example, the general category of [[Prediction Policy Problems]], the argument that algorithmic interventions can be unusually cost-effective, and the open problem of designing human-plus-algorithm decision aids.

## Key claims for the efficiency branch

- Many important social decisions are prediction policy problems: the decision does not primarily ask "what is the causal effect of this intervention?" but "which case has the highest predicted risk, benefit, need, or fit?"
- The pretrial bail example remains the anchor. Algorithmic prediction can improve the crime/incarceration frontier: roughly 40 percent lower jailing at the same risk level, or 25 percent lower risk at the same jailing rate.
- These results are not an argument for automation. They show that algorithms can discover information that could improve decisions.
- The hardest work is econometric rather than computational. Building a supervised learner may be easier than evaluating whether it improves on the human decision-maker.
- selective labels ([[Algorithmic Policy Efficiency]]) and omitted payoff bias ([[Algorithmic Policy Efficiency]]) are the two central evaluation hazards. Ignoring them builds in a pro-algorithm bias.
- Algorithms expand the toolkit of behavioral intervention. Decision aids are presented as a category that extends the tradition of nudges and choice architecture.
- Human and algorithmic prediction have different comparative advantages: algorithms extract signal from the data frame, while humans may notice information missing from the data frame and may understand the broader payoff function.
- Algorithmic interventions can look unusually cost-effective because software scales cheaply, human decision-making leaves room for improvement, and ranking problems create large deadweight loss when cases are misordered.
- [[Ludwig et al., 2024|The Unreasonable Effectiveness of Algorithms]] is the companion effectiveness paper that quantifies this point with MVPF comparisons across several domains.
- Economists must treat algorithm design as part of policy design. Once algorithms mediate job search, health choice, school choice, consumer choice, or social programs, behavioral parameters are no longer external facts; they can depend on the algorithm.

## Selective coverage

This note does not try to ingest the whole paper at equal depth. It preserves the parts most useful for the second branch of the course:

- prediction policy problems as the general class behind bail, hiring, medical testing, tax audits, credit, job search, and recommender-assisted decisions;
- the welfare-frontier interpretation of algorithmic decision support;
- the evaluation framework around selective labels and omitted payoffs;
- the human-plus-machine framework behind the override problem ([[Algorithmic Policy Efficiency]]);
- the bridge from algorithmic prediction to digital nudging, behavioral interventions, and LLM-mediated decision support.

## Why it matters for Digital Nudging

Digital nudging increasingly uses algorithmic decision aids, recommenders, and AI assistants rather than static interface tweaks. Mullainathan gives the course a way to place those systems in a wider economic frame: they are interventions that change how people and institutions predict, rank, choose, and learn.

The paper also links the efficiency branch to the constructive side of Behavioral Economics 2.0 ([[Algorithmic Thought Partners]]). If algorithms can reveal decision mistakes and redesign choice environments at scale, then digital nudging is no longer only about salience, defaults, or friction. It becomes a question of how to build prediction-guided decision systems that improve welfare without collapsing into opaque automation.

## Bibliographic reference

Mullainathan, S. (2025). Economics in the age of algorithms. *AEA Papers and Proceedings, 115*, 1-23. https://doi.org/10.1257/pandp.20251118
