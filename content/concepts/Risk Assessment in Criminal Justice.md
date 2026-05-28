---
title: Risk Assessment in Criminal Justice
page_type: concept
status: active
tags:
  - concept
  - criminal-justice
  - risk-assessment
  - algorithmic-fairness
  - decision-support
updated_on: 2026-05-26
source_count: 11
related_pages:
  - [[Angwin et al., 2016|Machine Bias]]
  - [[Kleinberg et al., 2016|Inherent Trade-Offs in the Fair Determination of Risk Scores]]
  - [[Hedden, 2021|On Statistical Criteria of Algorithmic Fairness]]
  - [[Hellman, 2020|Measuring Algorithmic Fairness]]
  - [[Binns, 2018|Fairness in Machine Learning: Lessons from Political Philosophy]]
  - [[Corbett-Davies et al., 2017|Algorithmic Decision Making and the Cost of Fairness]]
  - [[Narayanan, 2026|What If Algorithmic Fairness Is a Category Error?]]
  - [[Kleinberg et al., 2018|Human Decisions and Machine Predictions]]
  - [[Ludwig and Mullainathan, 2021|Fragile Algorithms and Fallible Decision-Makers]]
  - [[Mullainathan, 2025|Economics in the Age of Algorithms]]
  - [[Ludwig et al., 2024|The Unreasonable Effectiveness of Algorithms]]
  - [[Predictive Parity]]
  - [[Error Rate Parity]]
  - [[Algorithmic Fairness as Political Philosophy]]
  - [[Fairness as Policy Alignment]]
  - [[Sociotechnical Fairness]]
  - [[Algorithmic Decision Support Efficiency]]
  - [[Selective Labels]]
  - [[Omitted Payoff Bias]]
  - [[Override Problem]]
  - [[COMPAS Controversy]]
  - [[Fairness Metrics]]
  - [[Algorithmic Fairness]]
  - [[Algorithmic Accountability and Fairness]]
---

# Risk Assessment in Criminal Justice

## Core idea

[[Risk Assessment in Criminal Justice]] refers to tools that score people by predicted likelihood of future arrest, recidivism, violence, failure to appear, or supervision failure. These tools are often presented as decision support rather than automated decisions, but they can influence bail, sentencing, parole, probation, treatment eligibility, and supervision intensity.

## Key distinctions

- Prediction target: general rearrest, violent rearrest, failure to appear, or criminogenic need are different targets with different stakes.
- Decision point: pretrial release, sentencing, parole, and treatment allocation create different error costs.
- Score use: a score can inform support services, justify release, justify detention, or intensify supervision.
- Transparency: proprietary models can block adversarial testing and public justification.
- Fairness: the same tool can appear accurate overall while imposing different error burdens across racial groups.

## Evidence and debate

[[Angwin et al., 2016|Machine Bias]] supplies the concrete case. COMPAS scores in Broward County entered a legal environment already marked by racial inequality, jail overcrowding, and limited transparency. [[Kleinberg et al., 2016|Inherent Trade-Offs in the Fair Determination of Risk Scores]] then explains why risk-score fairness is formally contested when different groups have different base rates and prediction is imperfect. [[Hedden, 2021|On Statistical Criteria of Algorithmic Fairness]] adds that fair prediction may require risk scores to preserve the same evidential meaning across groups, even if downstream legal decisions require separate moral and institutional evaluation. [[Hellman, 2020|Measuring Algorithmic Fairness]] argues that criminal justice fairness is especially about action and error costs: detention, release, supervision, or services. [[Corbett-Davies et al., 2017|Algorithmic Decision Making and the Cost of Fairness]] adds the policy optimization question: what is the cost of a fairness constraint relative to the public goal the decision rule is supposed to serve? [[Binns, 2018|Fairness in Machine Learning: Lessons from Political Philosophy]] pushes the question further: criminal justice may require different fairness ideals depending on whether the relevant concern is equal civic standing, distributive burden, historical injustice, public safety, or representation.

[[Narayanan, 2026|What If Algorithmic Fairness Is a Category Error?]] adds the broader system question. Even if a risk score were calibrated and error-balanced, pretrial detention based on predicted future crime may still be procedurally and morally troubling. The score must be evaluated within the court workflow, the legitimacy of preemptive detention, the possibility of contesting the model, the distribution of spillover harms, and the political choice to use prediction as a substitute for deeper reform.

[[Kleinberg et al., 2018|Human Decisions and Machine Predictions]] opens the efficiency branch. It argues that bail prediction can improve the crime/incarceration frontier: algorithmic release rules can potentially produce much less crime at the same jail rate, or much less jail at the same crime rate. [[Ludwig and Mullainathan, 2021|Fragile Algorithms and Fallible Decision-Makers]] then explains why that promise is conditional on sound construction, evaluation, regulation, and human-machine integration.

[[Mullainathan, 2025|Economics in the Age of Algorithms]] turns pretrial risk assessment into the canonical example of a broader prediction policy problem: a decision where social welfare depends on predicting risk and ranking cases well, not only on estimating a causal treatment effect.

[[Ludwig et al., 2024|The Unreasonable Effectiveness of Algorithms]] adds the public-finance version of the efficiency claim. If a pretrial decision aid produces even a fraction of the potential detention reduction, the avoided jail costs can make the intervention highly cost-effective.

## Practical or policy relevance

This concept connects the fairness module to digital nudging because criminal justice risk tools shape human choice environments. A score makes some facts salient, frames a person as risky or safe, and can shift responsibility from a judge or officer to an apparently objective system.

The efficiency branch asks whether predictive tools can reduce jail without increasing crime, or reduce crime without increasing jail. The fairness branch asks what such gains omit if they ignore unequal errors, social meaning, rights, or institutional context.

The sociotechnical branch asks what the tool does to the institution itself: which decisions it makes salient, which alternatives it forecloses, how it changes human discretion, and whether it turns a political problem into an apparently technical one.

## Related pages

- [[COMPAS Controversy]]
- [[Fairness Metrics]]
- [[Fairness Impossibility Results]]
- [[Sociotechnical Fairness]]
- [[Algorithmic Decision Support Efficiency]]
- [[Prediction Policy Problems]]
- [[Ludwig et al., 2024|The Unreasonable Effectiveness of Algorithms]]
- [[Selective Labels]]
- [[Omitted Payoff Bias]]
- [[Override Problem]]
- [[Algorithmic Fairness]]
- [[Algorithmic Accountability and Fairness]]

## Open questions

How should students evaluate the crime/incarceration frontier without treating crime, detention, due process, and dignity as commensurable in a simple way?
