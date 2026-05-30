---
title: "Sunstein, 2022"
page_type: source
status: active
source_path: raw/papers/Sunstein, 2022.pdf
source_type: paper
source_kind: law_review_article
tags:
  - source
  - algorithmic-governance
  - administrative-law
  - algorithmic-decision-support
  - bias
  - noise
updated_on: 2026-05-28
related_pages:
  - [[Algorithmic Governance, Management, and the Automated State]]
  - [[Algorithmic Governance]]
  - [[Algorithmic Policy Efficiency]]
  - [[Algorithmic Fairness]]
  - [[Prediction Policy Problems]]
  - [[Digital Nudging]]
  - [[Cass R. Sunstein]]
---

# Sunstein, 2022: Governing by Algorithm? No Noise and (Potentially) Less Bias

## Summary

[[Sunstein, 2022|Governing by Algorithm? No Noise and (Potentially) Less Bias]] gives the algorithmic-governance cluster a behavioral-law argument for why administrative agencies should take algorithms seriously. Sunstein distinguishes two sources of human error: bias and noise. Bias is systematic error in a particular direction; noise is unwanted variability across or within decision-makers. Human administrators, judges, prosecutors, doctors, and other officials can exhibit both.

The article's constructive claim is that well-designed algorithms can eliminate noise and reduce some cognitive biases because they apply the same rule to identical cases and rely on statistical predictors rather than intuitive shortcuts. The caution is that algorithms can still be biased, especially when inputs, targets, or outcomes reflect discrimination. Sunstein therefore does not defend algorithmic governance as automatically legitimate. He argues that algorithms can improve administrative decision-making when they are properly designed, evaluated, and constrained by legal and policy goals.

## Key claims

- Human administrative judgment is vulnerable to cognitive biases such as availability bias, anchoring, affect-driven judgment, optimism bias, present bias, and current-offense bias.
- Human systems are also noisy: similarly situated people may receive different outcomes because of occasion noise, level noise, or pattern noise.
- Algorithms are "silent" in Sunstein's sense: the same algorithm does not treat identical cases differently because of the day, decision-maker, sequence of prior cases, mood, or local salience.
- Eliminating noise is morally and administratively important because random variation creates unequal treatment and increases total error.
- Algorithms can counteract cognitive bias in prediction problems by giving appropriate statistical weight to information that humans over- or underweight.
- The bail example from [[Kleinberg et al., 2018|Human Decisions and Machine Predictions]] shows the point: algorithmic ranking could reduce crime at the same detention rate or reduce detention at the same crime rate.
- Discrimination remains a distinct problem. Algorithms can encode or perpetuate discrimination through biased inputs, proxy variables, historically contaminated labels, or prediction targets that are themselves infected by discrimination.
- A major virtue of algorithms is that they can make tradeoffs more explicit: agencies and publics can see what happens when a system is constrained for accuracy, detention, racial balance, or other policy goals.

## Evidence and examples

Sunstein uses the administrative state as the main institutional setting. Asylum adjudication illustrates noise: outcomes may vary sharply depending on the adjudicator, sequence of prior decisions, or other irrelevant factors. Pretrial bail illustrates the efficiency case: judges overweight the current charge and release many defendants whom the model identifies as high risk, while detaining some lower-risk defendants.

The article distinguishes two kinds of bias. Cognitive bias is a prediction error produced by heuristics or intuitive judgment. Discriminatory bias is unequal treatment or impact connected to legally and morally salient groups. Algorithms are especially promising for the first, but require careful legal and policy scrutiny for the second.

## Course use

Use this article as a compact supplement to [[Coglianese and Lehr, 2017|Regulating by Robot]] and [[Coglianese, 2021|Administrative Law in the Automated State]]. Coglianese and Lehr explain why algorithmic administration can fit administrative-law doctrine; Sunstein explains why agencies might want algorithmic tools in the first place: to reduce noise, correct cognitive bias, and make prediction-policy tradeoffs more explicit.

It also belongs beside [[Algorithmic Policy Efficiency]]. Sunstein does not replace the econometric argument in [[Kleinberg et al., 2018|Human Decisions and Machine Predictions]] or [[Ludwig and Mullainathan, 2021|Fragile Algorithms and Fallible Decision-Makers]]. He gives that argument a legal-behavioral frame: the relevant comparison is not algorithm versus ideal human judgment, but algorithmic decision support versus actual human systems that are noisy, biased, and institutionally consequential.

## Why it matters for Digital Nudging

Digital nudging often uses algorithms to rank, recommend, target, warn, personalize, or triage. Sunstein's article helps separate two questions that the course should keep apart. First, can an algorithmic system reduce human error by improving prediction and consistency? Sometimes yes. Second, can that same system reproduce discrimination, omit relevant values, or make the wrong policy tradeoff? Also yes.

For the course, this is useful because it resists both algorithmic enthusiasm and algorithmic rejection. Digital choice architecture can be better than human-only choice architecture when it reduces noise and cognitive bias. But its legitimacy depends on objectives, inputs, validation, discrimination analysis, policy alignment, and the broader sociotechnical decision system.

## Links into the wiki

- [[Algorithmic Governance, Management, and the Automated State]]: synthesis page where this article reinforces the positive case for algorithmic administration.
- [[Algorithmic Policy Efficiency]]: connects Sunstein's noise-and-bias argument to the efficiency frontier in prediction policy.
- [[Algorithmic Fairness]]: keeps the discrimination warning tied to model inputs, targets, impacts, and institutional use.
- fairness as policy alignment ([[Algorithmic Fairness]]): captures Sunstein's point that algorithms can reveal tradeoffs among policy goals rather than settle them automatically.

## Open questions

How should the course distinguish useful consistency from harmful rigidity when an algorithm eliminates administrative noise but also reduces opportunities for mercy, individualized treatment, or empathic escalation?

## Bibliographic reference

Sunstein, C. R. (2022). Governing by algorithm? No noise and (potentially) less bias. *Duke Law Journal, 71*(6), 1175-1206.
