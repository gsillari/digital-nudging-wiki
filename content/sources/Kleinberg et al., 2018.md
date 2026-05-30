---
title: "Kleinberg et al., 2018"
page_type: source
status: active
source_path: raw/papers/Kleinberg et al., 2018.pdf
source_type: journal_article
tags:
  - source
  - algorithmic-decision-support
  - prediction-policy
  - criminal-justice
  - efficiency
updated_on: 2026-05-26
related_pages:
  - [[Algorithmic Fairness]]
  - [[Algorithmic Policy Efficiency]]
  - [[Jon Kleinberg]]
  - [[Himabindu Lakkaraju]]
  - [[Jure Leskovec]]
  - [[Jens Ludwig]]
  - [[Sendhil Mullainathan]]
---

# Kleinberg et al., 2018: Human Decisions and Machine Predictions

## Summary

[[Kleinberg et al., 2018|Human Decisions and Machine Predictions]] is the core source for the efficiency branch of the algorithmic fairness module. Kleinberg, Lakkaraju, Leskovec, Ludwig, and Mullainathan ask whether machine learning can improve human decision-making in bail. Their answer is yes, under careful evaluation: algorithmic predictions can identify combinations of crime and incarceration that dominate the existing judicial status quo.

The headline teaching result is the policy frontier. In one simulation, an algorithmic release rule could reduce crime by up to 24.7 percent at the same jailing rate, or reduce jailing by up to 41.9 percent with no increase in crime. This is the course's cleanest example of why efficiency is morally important: when a system can produce less crime with the same incarceration, or less incarceration with the same crime, ignoring that possibility is itself ethically costly.

## Key claims

- Many high-stakes decisions are prediction policy problems: the decision turns on forecasting an outcome and acting under a payoff trade-off.
- Bail is a useful test case because judges decide whether defendants await trial in jail or at home, and the legal decision is closely tied to predicted flight or public-safety risk.
- Standard prediction accuracy is not enough. A better predictor matters only if it improves the actual decision frontier.
- Evaluation is hard because of selective labels ([[Algorithmic Policy Efficiency]]): crime outcomes are observed for released defendants, but not for defendants judges detained.
- Evaluation is also hard because of omitted payoff bias ([[Algorithmic Policy Efficiency]]): judges or society may care about goals not captured by the single predicted outcome.
- The authors use quasi-random assignment of cases to judges and judge leniency variation to construct counterfactual comparisons.
- Judges appear to release many defendants the algorithm identifies as high risk while jailing lower-risk defendants.
- Stricter judges do not simply jail the riskiest marginal defendants first; algorithmic ranking can dominate that pattern.
- The gains are not only aggregate: the authors report that crime reductions can occur for violent crime as well and can be achieved while reducing racial disparities.
- The paper is not an argument for naive automation. It argues that machine learning must be integrated into an economic framework linking predictions, decisions, payoffs, and valid counterfactuals.

## Conceptual contribution

This paper gives the course a disciplined way to talk about efficiency without treating efficiency as morally thin. If a predictive system can reduce incarceration while holding crime fixed, it can reduce a major liberty burden. If it can reduce crime while holding incarceration fixed, it can reduce victimization without increasing detention. Efficiency here is not merely administrative savings; it is a frontier of social harms.

The paper also supplies the central caution for the branch. The algorithm's value cannot be read from AUC or prediction accuracy alone. It depends on the decision rule, the relevant payoff function, and whether the counterfactual evaluation is unbiased.

## Why it matters for Digital Nudging

For [[Digital Nudging]], the paper is a template for evaluating algorithmic decision support. Digital choice architectures often use predictions to allocate attention, rank options, trigger warnings, prioritize cases, or recommend interventions. The question should not be only whether the prediction is accurate or fair by one metric, but whether the system improves the relevant decision frontier while respecting rights, welfare, and institutional goals.

This branch also balances the earlier fairness readings. fairness metrics ([[Algorithmic Fairness]]), error rate parity ([[Fairness Impossibility Results]]), and sociotechnical fairness ([[Algorithmic Fairness]]) identify real risks. Kleinberg et al. show why the course also needs a positive evaluation question: compared with human-only decision-making, can well-designed algorithmic assistance reduce avoidable harm?

## Bibliographic reference

Kleinberg, J., Lakkaraju, H., Leskovec, J., Ludwig, J., & Mullainathan, S. (2018). Human decisions and machine predictions. *The Quarterly Journal of Economics, 133*(1), 237-293. https://doi.org/10.1093/qje/qjx032
