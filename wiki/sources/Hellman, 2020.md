---
title: "Hellman, 2020"
page_type: source
source_path: raw/papers/Hellman, 2020.pdf
source_type: paper
status: active
tags:
  - source
  - algorithmic-fairness
  - law
  - predictive-parity
  - error-rate-parity
updated_on: 2026-05-26
related_pages:
  - [[Algorithmic Fairness]]
  - [[Predictive Parity]]
  - [[Error Rate Parity]]
  - [[Fairness Metrics]]
  - [[Fairness Impossibility Results]]
  - [[COMPAS Controversy]]
  - [[Risk Assessment in Criminal Justice]]
  - [[Algorithmic Fairness as Political Philosophy]]
  - [[Algorithmic Accountability and Fairness]]
  - [[Deborah Hellman]]
---

# Hellman, 2020: Measuring Algorithmic Fairness

## Summary

Deborah Hellman argues that two prominent fairness criteria answer different kinds of questions. [[Predictive Parity]] answers an epistemic question: given a score, what should one believe about the scored person? [[Error Rate Parity]], and especially Hellman's preferred error-ratio version, answers a practical question: how are the burdens of false positives and false negatives distributed across legally protected groups?

The paper is crucial for the course because it gives the legal-philosophical case against treating predictive parity as the main fairness criterion. For Hellman, fairness usually concerns action and treatment, not belief alone. If one group bears more false positives while another bears more false negatives, the algorithm may be applying different practical rules to different protected groups.

## Key claims

- Equal predictive accuracy or predictive parity ensures that a score has the same meaning across groups.
- This same-meaning property is important, but it is primarily about belief: how much confidence one should have in the prediction.
- Fairness in the relevant legal and practical sense usually concerns treatment and action.
- Error ratios matter because false positives and false negatives carry different costs in different domains.
- The relevant legal fairness question is not simply whether false positive rates or false negative rates are equal in isolation, but whether the balance between the two error types is applied similarly across protected groups.
- Lack of error ratio parity is not by itself constitutive of unfairness, because aggregate error rates can reflect different base-rate distributions and different mixes of marginal cases.
- Still, lack of error ratio parity is morally important when it concerns historically disadvantaged protected groups, because it gives reason to investigate measurement error and compounding injustice.
- Algorithm designers often overstate the legal prohibition on using protected traits. Hellman argues that using protected traits to improve accuracy may sometimes be legally permissible, especially when the trait is used to determine which other features are predictive rather than to set different action thresholds.

## Evidence and methods

Hellman develops the argument through legal and philosophical analysis. She uses a stylized disease-test example and the COMPAS debate to distinguish predictive parity from error-rate measures. She then uses examples from medicine and legal burdens of proof to show why belief and action come apart: what one should do depends on the cost of different mistakes, not only on the probability of the target fact.

The normative core is the analogy to legal standards such as the Blackstone ratio. Criminal law is structured around the idea that false positives and false negatives have asymmetric moral costs. Hellman argues that algorithmic systems should not, in effect, apply one error-cost balance to one protected group and a different balance to another.

The legal section argues that reducing error burdens can occur either by changing the consequences of scores or by improving accuracy. Hellman contends that constitutional anti-discrimination law does not categorically forbid all race-conscious algorithmic design, though different thresholds by race would be legally problematic.

## Why it matters for Digital Nudging

Hellman gives digital nudging a legal vocabulary for distinguishing fair prediction from fair intervention. Many digital systems score users accurately enough to support belief, but then act on those scores through ranking, targeting, friction, withholding, escalation, or coercive recommendations. The fairness issue often lies in the action rule: which mistakes are tolerated, who bears them, and what happens when the system is wrong.

This matters for recommender systems, risk scoring, content moderation, fraud detection, welfare allocation, targeted persuasion, and personalized nudging. A system can preserve the same evidential meaning across groups while still distributing practical burdens unfairly. Conversely, reducing the practical burden of errors may matter more than maximizing epistemic symmetry.

## Links into the wiki

- [[Predictive Parity]]: the epistemic same-meaning criterion Hellman treats as important but incomplete.
- [[Error Rate Parity]]: the practical error-burden family, with Hellman's error-ratio parity as the central version.
- [[Fairness Metrics]]: the metric taxonomy now needs both evidential and pragmatic criteria.
- [[Algorithmic Fairness as Political Philosophy]]: Hellman supplies the legal-action version of the normative turn.
- [[COMPAS Controversy]]: the motivating case for the conflict between ProPublica-style error analysis and Northpointe-style predictive parity.

## Open questions

- How should Hellman's error-ratio view be taught alongside simpler false positive rate and false negative rate parity measures?
- Which digital nudging examples best show the gap between fair prediction and fair action?
- How should the course connect Hellman's "compounding injustice" claim to later sociotechnical accounts of algorithmic bias?

## Bibliographic reference

Hellman, D. (2020). Measuring algorithmic fairness. *Virginia Law Review, 106*(4), 811-866. https://virginialawreview.org/articles/measuring-algorithmic-fairness/
