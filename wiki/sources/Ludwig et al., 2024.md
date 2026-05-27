---
title: "Ludwig et al., 2024"
page_type: source
status: active
source_path: raw/papers/Ludwig et al., 2024.pdf
source_type: journal_article
tags:
  - source
  - algorithmic-decision-support
  - effectiveness
  - prediction-policy
  - public-policy
updated_on: 2026-05-26
related_pages:
  - [[Algorithmic Decision Support Efficiency]]
  - [[Prediction Policy Problems]]
  - [[Mullainathan, 2025|Economics in the Age of Algorithms]]
  - [[Kleinberg et al., 2018|Human Decisions and Machine Predictions]]
  - [[Ludwig and Mullainathan, 2021|Fragile Algorithms and Fallible Decision-Makers]]
  - [[Selective Labels]]
  - [[Omitted Payoff Bias]]
  - [[Override Problem]]
  - [[Risk Assessment in Criminal Justice]]
  - [[Algorithmic Fairness]]
  - [[Digital Nudging]]
  - [[Jens Ludwig]]
  - [[Sendhil Mullainathan]]
  - [[Ashesh Rambachan]]
---

# Ludwig et al., 2024: The Unreasonable Effectiveness of Algorithms

## Summary

[[Ludwig et al., 2024|The Unreasonable Effectiveness of Algorithms]] reinforces the effectiveness argument for the efficiency branch. Ludwig, Mullainathan, and Rambachan compare algorithmic policy interventions with traditional public policy levers using marginal value of public funds, or MVPF: social benefit divided by net government cost.

Their provocative result is that the algorithmic interventions they examine have infinite MVPF values. In their framing, that means the interventions generate social benefits while also saving government money. The point is not that algorithms are automatically magic. The point is that prediction-guided decision aids deserve serious policy R&D because they may be unusually cost-effective.

## Key claims

- The paper evaluates algorithms in criminal justice, education, health, and workplace regulation.
- Each studied algorithm has an MVPF of infinity and falls in the top 15 percent of the Policy Impacts MVPF library.
- The pretrial release case restates the [[Kleinberg et al., 2018|Human Decisions and Machine Predictions]] result: an algorithmic decision aid could reduce detention rates by up to 40 percent without increasing pretrial failure rates.
- Algorithms can be unusually effective because many policy problems are ranking problems. When humans misrank cases, better ranking can reduce deadweight loss without expanding the policy.
- Algorithms can also be unusually effective because software scales with low marginal cost and does not face the same diminishing implementation fidelity as many traditional programs.
- The authors do not treat retrospective estimates as final. They argue for an iterative policy pipeline: promising estimates should motivate improved design, careful pilots, and rigorous in situ evaluation.
- The major open implementation questions concern human-plus-algorithm use: whether humans ignore the tool, misuse it, or understand when they and the algorithm each have comparative advantage.

## Cases used

- Pretrial release: better risk ranking could reduce detention while holding pretrial failure fixed, with potential large government savings from fewer jail stays.
- OSHA workplace inspections: algorithmic targeting of inspections could better predict future injuries and reduce serious workplace injuries.
- Heart attack testing: algorithmic referral for stress tests could reduce unnecessary testing while preserving welfare.
- College course placement: algorithmic placement into remedial or college-level courses can increase college-level placement, reduce remedial credits, and narrow race and ethnic disparities without lowering pass rates.

## Why it matters for Digital Nudging

For [[Digital Nudging]], this paper strengthens the positive case for algorithmic choice architecture. Digital systems can do more than manipulate attention or exploit behavioral bias. When well designed and evaluated, they can improve rankings, triage, targeting, and timing at scale.

The caution is equally important. Effectiveness estimates do not license uncritical deployment. The course should present the paper as an argument for policy R&D: test algorithmic interventions seriously, pilot them in context, evaluate actual human use, and track both benefits and omitted harms.

## Bibliographic reference

Ludwig, J., Mullainathan, S., & Rambachan, A. (2024). The unreasonable effectiveness of algorithms. *AEA Papers and Proceedings, 114*, 623-627. https://doi.org/10.1257/pandp.20241072
