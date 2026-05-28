---
title: "Angwin et al., 2016"
page_type: source
source_path: raw/web/Machine Bias - ProPublica.html
source_type: web_article
status: active
tags:
  - source
  - algorithmic-fairness
  - compas
  - criminal-justice
  - risk-assessment
updated_on: 2026-05-26
related_pages:
  - [[Algorithmic Fairness]]
  - [[COMPAS Controversy]]
  - [[Risk Assessment in Criminal Justice]]
  - [[Fairness Metrics]]
  - [[Algorithmic Accountability and Fairness]]
  - [[Julia Angwin]]
  - [[Jeff Larson]]
  - [[Lauren Kirchner]]
  - [[Surya Mattu]]
---

# Angwin et al., 2016: Machine Bias

## Summary

[[Angwin et al., 2016|Machine Bias]] is the ProPublica investigation that made the [[COMPAS Controversy]] a canonical entry point for [[Algorithmic Fairness]]. It studies risk scores assigned to more than 7,000 people arrested in Broward County, Florida, and argues that the scores were racially skewed in their mistakes even when overall error rates looked similar.

The article is useful for the course because it makes algorithmic fairness concrete before the mathematics begins. A score that looks like neutral decision support can become a nudge or pressure on judges, probation officers, and pretrial decision-makers. It shapes attention, frames risk, and can move coercive public decisions while remaining partly hidden behind proprietary software.

## Key claims

- Risk assessment tools were spreading across pretrial release, sentencing, parole, and correctional supervision, often before strong independent validation.
- In the Broward County data, COMPAS had limited predictive performance. Violent recidivism predictions were especially weak, while broader recidivism predictions were only modestly useful.
- The racial disparity appeared in the type of error: Black defendants were more likely to be falsely labeled high risk, while white defendants were more likely to be falsely labeled low risk.
- The disparity did not disappear when the analysis controlled for age, gender, prior criminal history, current charge, and observed recidivism.
- The tool did not explicitly ask for race, but many inputs and background variables can still reflect racialized social structure.
- Proprietary scoring created due-process and accountability problems because defendants and the public could not inspect the full calculation.

## Evidence and methods

ProPublica obtained COMPAS scores for Broward County defendants arrested in 2013 and 2014, then checked subsequent criminal charges over a two-year period. The article pairs statistical analysis with narrative cases, especially Brisha Borden and Vernon Prater, to show how the same score can appear objective while producing sharply different error burdens across groups.

The investigation also reports institutional context: risk assessments were used in multiple legal settings, the software vendor disputed ProPublica's analysis, and judges sometimes treated risk scores as relevant even when the tool's creator warned against using them as the sole basis for sentencing.

## Why it matters for Digital Nudging

This article starts the algorithmic fairness module with a governance problem that is close to digital nudging: algorithmic systems can influence human decisions without formally deciding anything themselves. COMPAS is not a recommender system in the platform sense, but it steers decision-makers through risk labels, salience, and institutional trust in scores.

For digital nudging, the key lesson is that algorithmic choice architecture must be evaluated by how its errors are distributed, who can contest it, which decision points it enters, and whether proprietary opacity prevents public justification. This directly connects to [[Hypernudge]], [[Algorithmic Accountability and Fairness]], [[Transparency and Publicity]], and later work on dark patterns, recommender systems, and automated personalization.

## Links into the wiki

- [[COMPAS Controversy]]: the central case produced by this investigation.
- [[Fairness Metrics]]: explains why ProPublica's focus on asymmetric error rates differs from calibration-based defenses.
- [[Risk Assessment in Criminal Justice]]: situates COMPAS in bail, sentencing, parole, and treatment decisions.
- [[Algorithmic Fairness]]: the course sub-hub for the fairness branch.

## Open questions

- Which later responses best reconstruct the debate between ProPublica and Northpointe?
- How should the course connect COMPAS to non-carceral platform systems such as ranking, feeds, credit scoring, and personalization?
- How much statistical detail should be taught before introducing the normative question of which errors matter most?

## Bibliographic reference

Angwin, J., Larson, J., Kirchner, L., & Mattu, S. (2016, May 23). *Machine bias*. ProPublica. https://www.propublica.org/article/machine-bias-risk-assessments-in-criminal-sentencing
