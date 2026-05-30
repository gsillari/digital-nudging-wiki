---
title: "Ludwig and Mullainathan, 2021"
page_type: source
status: active
source_path: raw/papers/Ludwig and Mullainathan, 2021.pdf
source_type: journal_article
tags:
  - source
  - algorithmic-decision-support
  - criminal-justice
  - human-ai-complementarity
  - efficiency
updated_on: 2026-05-26
related_pages:
  - [[Algorithmic Fairness]]
  - [[Algorithmic Policy Efficiency]]
  - [[Algorithmic Fairness]]
  - [[Jens Ludwig]]
  - [[Sendhil Mullainathan]]
---

# Ludwig and Mullainathan, 2021: Fragile Algorithms and Fallible Decision-Makers

## Summary

[[Ludwig and Mullainathan, 2021|Fragile Algorithms and Fallible Decision-Makers]] is the bridge between the optimistic efficiency result and the sociotechnical caution. Ludwig and Mullainathan argue that algorithms in criminal justice are not doomed to fail, but they are fragile: small design, procurement, evaluation, and deployment choices can make them useless or harmful. The baseline is also not innocent. Human decision-makers are fallible, noisy, inconsistent, and often biased.

The paper's central posture is neither algorithmic triumphalism nor algorithmic rejection. Well-designed algorithms can improve on human decisions and can sometimes be easier to audit and repair than human judgment. But that requires social science, econometrics, regulation, and behavioral design around the full human-plus-machine system.

## Key claims

- Criminal justice decisions suffer from misprediction, inconsistency, and discrimination. Judges can release high-risk defendants while jailing low-risk defendants.
- Algorithms have often disappointed because they were poorly built, poorly regulated, or poorly integrated into human workflows, not because machine learning is inherently unusable.
- omitted payoff bias ([[Algorithmic Policy Efficiency]]) arises when an algorithm predicts only one outcome even though the real decision depends on a richer objective function.
- selective labels ([[Algorithmic Policy Efficiency]]) arise because data are filtered by past human decisions; we observe outcomes for people released by judges but not the counterfactual outcomes for people detained.
- The override problem ([[Algorithmic Policy Efficiency]]) arises because the algorithm is usually not the final decider. Humans may have useful private information, but they may also misuse that information.
- The right goal is not blind adherence to an algorithm. The right goal is understanding when the human has comparative advantage, when the algorithm has comparative advantage, and how the interface should support that division of labor.
- Algorithmic bias can be easier to discover and fix than human bias when transparency, data access, and regulatory incentives are properly designed.
- The discussion of algorithms should not happen in a vacuum. Humans set the benchmark, generate the data, build the systems, procure them, deploy them, and respond to their outputs.

## Conceptual contribution

This paper keeps the efficiency branch honest. [[Kleinberg et al., 2018|Human Decisions and Machine Predictions]] shows that an algorithmic release rule can dominate judicial decisions on the crime/incarceration frontier. Ludwig and Mullainathan explain why such gains do not automatically follow from any algorithm. The relevant object is the whole decision system: data generation, objective specification, prediction, recommendation, interpretation, override, procurement, regulation, and evaluation.

This makes the paper a natural complement to [[Narayanan, 2026|What If Algorithmic Fairness Is a Category Error?]]. Narayanan warns that fairness is a property of sociotechnical decision systems. Ludwig and Mullainathan add that efficiency is also a property of the whole human-plus-machine system, not just the predictive model.

## Why it matters for Digital Nudging

Digital nudging often uses algorithms as decision aids rather than final decision-makers: recommenders prioritize content, dashboards flag risk, platforms suggest actions, and AI assistants offer plans. This paper gives the course the right design problem: the question is not whether humans should always follow the model, but how the system helps humans use algorithmic information without ignoring context, hidden payoffs, due process, or the user's own agency.

For constructive digital nudging, the paper is especially useful because it connects efficiency, accountability, and behavioral design. A user-serving decision aid must be evaluated by what the combined human-machine workflow actually does.

## Bibliographic reference

Ludwig, J., & Mullainathan, S. (2021). Fragile algorithms and fallible decision-makers: Lessons from the justice system. *Journal of Economic Perspectives, 35*(4), 71-96. https://doi.org/10.1257/jep.35.4.71
