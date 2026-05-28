---
title: Override Problem
page_type: concept
status: active
tags:
  - concept
  - human-ai-complementarity
  - algorithmic-decision-support
  - decision-aids
  - interpretability
updated_on: 2026-05-26
source_count: 3
related_pages:
  - [[Mullainathan, 2025|Economics in the Age of Algorithms]]
  - [[Ludwig and Mullainathan, 2021|Fragile Algorithms and Fallible Decision-Makers]]
  - [[Kleinberg et al., 2018|Human Decisions and Machine Predictions]]
  - [[Algorithmic Decision Support Efficiency]]
  - [[Algorithmic Accountability and Fairness]]
  - [[Sociotechnical Fairness]]
  - [[Selective Labels]]
  - [[Omitted Payoff Bias]]
  - [[Algorithmic Thought Partners]]
---

# Override Problem

## Core idea

The [[Override Problem]] is the design problem of deciding when a human decision-maker should follow an algorithmic recommendation and when they should override it. The point is not to maximize obedience to the algorithm. The point is to combine machine and human information so that the overall decision system improves.

## Key distinctions

- Longer data versus wider data: algorithms can use many administrative cases, while humans may observe contextual information absent from the dataset.
- Correct override versus harmful override: a human may add genuine private signal, or may add noise, bias, or overconfidence.
- Explanation versus performance: explanations matter because humans need to know when the model is likely reliable, not merely because transparency is intrinsically attractive.
- Decision aid versus decision maker: many algorithmic systems operate through human uptake, resistance, or reinterpretation.

## Evidence and debate

[[Ludwig and Mullainathan, 2021|Fragile Algorithms and Fallible Decision-Makers]] names the override problem as a central human-plus-machine challenge. It argues that successful deployment requires helping people learn where they have comparative advantage over the algorithm and where the algorithm has comparative advantage over them.

[[Kleinberg et al., 2018|Human Decisions and Machine Predictions]] focuses mainly on the welfare frontier, but it also treats algorithms in practice as decision aids rather than final decision-makers.

[[Mullainathan, 2025|Economics in the Age of Algorithms]] frames the problem as comparative advantage. Algorithms can extract signal from the data frame; humans may see what is missing from the data frame and may better understand the relevant payoff function. The design question is how to make those advantages complement each other.

## Practical or policy relevance

For [[Digital Nudging]], the override problem is central to AI assistants, recommender dashboards, clinical triage, moderation queues, fraud review, and personalized decision aids. A digital nudge can support agency only if users or human reviewers know when to accept, question, contest, or revise the system's guidance.

## Related pages

- [[Algorithmic Decision Support Efficiency]]
- [[Prediction Policy Problems]]
- [[Algorithmic Accountability and Fairness]]
- [[Sociotechnical Fairness]]
- [[Algorithmic Thought Partners]]
- [[Reflective Equilibrium]]
