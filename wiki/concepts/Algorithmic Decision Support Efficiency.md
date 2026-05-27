---
title: Algorithmic Decision Support Efficiency
page_type: concept
status: active
tags:
  - concept
  - algorithmic-decision-support
  - efficiency
  - prediction-policy
  - criminal-justice
updated_on: 2026-05-26
source_count: 4
related_pages:
  - [[Ludwig et al., 2024|The Unreasonable Effectiveness of Algorithms]]
  - [[Mullainathan, 2025|Economics in the Age of Algorithms]]
  - [[Kleinberg et al., 2018|Human Decisions and Machine Predictions]]
  - [[Ludwig and Mullainathan, 2021|Fragile Algorithms and Fallible Decision-Makers]]
  - [[Prediction Policy Problems]]
  - [[Algorithmic Fairness]]
  - [[Risk Assessment in Criminal Justice]]
  - [[Selective Labels]]
  - [[Omitted Payoff Bias]]
  - [[Override Problem]]
  - [[Fairness as Policy Alignment]]
  - [[Sociotechnical Fairness]]
  - [[Digital Nudging]]
---

# Algorithmic Decision Support Efficiency

## Core idea

[[Algorithmic Decision Support Efficiency]] is the claim that algorithmic decision aids should be evaluated by whether they improve the decision frontier, not merely by whether they predict accurately. In judicial bail, the frontier is between crime and incarceration: can a system reduce crime without increasing jail, or reduce jail without increasing crime?

The central course example is [[Kleinberg et al., 2018|Human Decisions and Machine Predictions]]. Kleinberg et al. estimate that an algorithmic release rule could reduce crime by up to 24.7 percent at the same jailing rate, or reduce jailing by up to 41.9 percent with no increase in crime. Those numbers make efficiency a moral metric because both crime and incarceration are serious harms.

## Key distinctions

- Prediction accuracy versus decision quality: a model can predict well without improving the decision rule.
- Efficiency versus cost-cutting: the relevant gains are not merely administrative; they concern avoided crime, avoided detention, and better allocation of coercive burdens.
- Human-only baseline versus algorithmic aid: the benchmark is not an ideal judge but the observed pattern of human decisions.
- Automation versus decision support: the same prediction can be used as an automated rule, an advisory score, or a structured prompt for human judgment.
- Efficiency versus fairness: efficiency gains do not erase fairness concerns, but fairness concerns do not erase the moral importance of avoidable harm.
- Local frontier versus full welfare: a crime/incarceration frontier can omit due process, dignity, racial meaning, long-term effects, and broader institutional reform.

## Evidence and debate

[[Kleinberg et al., 2018|Human Decisions and Machine Predictions]] supplies the empirical anchor. The authors use New York City bail data and judge leniency variation to compare existing judge decisions with algorithmic release rules. The main result is not simply that the algorithm predicts risk; it is that algorithmic ranking could improve the crime/incarceration trade-off.

[[Ludwig and Mullainathan, 2021|Fragile Algorithms and Fallible Decision-Makers]] supplies the implementation theory. Algorithms can remedy human fallibility, but they are fragile. Efficiency only materializes when builders handle [[Selective Labels]], [[Omitted Payoff Bias]], and the [[Override Problem]].

[[Mullainathan, 2025|Economics in the Age of Algorithms]] supplies the summary frame. Mullainathan treats the bail result as one instance of a broader class: [[Prediction Policy Problems]]. Algorithmic decision aids can be unusually cost-effective because they scale cheaply, improve misranked cases, and operate against human decision systems that leave avoidable welfare and liberty losses on the table.

[[Ludwig et al., 2024|The Unreasonable Effectiveness of Algorithms]] reinforces the effectiveness argument using MVPF comparisons across criminal justice, education, health, and workplace safety. The paper's strongest teaching contribution is the mechanism: algorithmic interventions can look extraordinarily effective when they improve the ranking of cases and operate at scale with low marginal cost.

This concept therefore sits beside, not above, [[Fairness Metrics]] and [[Sociotechnical Fairness]]. Efficiency matters because human systems waste welfare and liberty. Sociotechnical critique matters because efficiency estimates can be misleading if the wrong outcome, payoff function, or institutional unit is evaluated.

## Practical or policy relevance

For [[Digital Nudging]], efficiency asks whether algorithmic assistance actually improves the user's or institution's decision problem. A recommender, fraud screen, triage dashboard, or AI assistant should be judged by the outcomes it changes, the burdens it shifts, and the alternatives it makes possible.

The course should teach this as a double lesson: digital systems can outperform unaided human judgment, but only when the evaluation target is the whole decision workflow.

## Related pages

- [[Kleinberg et al., 2018|Human Decisions and Machine Predictions]]
- [[Ludwig and Mullainathan, 2021|Fragile Algorithms and Fallible Decision-Makers]]
- [[Mullainathan, 2025|Economics in the Age of Algorithms]]
- [[Ludwig et al., 2024|The Unreasonable Effectiveness of Algorithms]]
- [[Prediction Policy Problems]]
- [[Selective Labels]]
- [[Omitted Payoff Bias]]
- [[Override Problem]]
- [[Risk Assessment in Criminal Justice]]
- [[Algorithmic Fairness]]
- [[Digital Nudging]]

## Open questions

How should the course teach efficiency as morally important without letting it crowd out fairness, due process, autonomy, and sociotechnical legitimacy?
