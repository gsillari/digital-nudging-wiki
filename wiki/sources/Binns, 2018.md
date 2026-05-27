---
title: "Binns, 2018"
page_type: source
source_path: raw/papers/Binns, 2018.pdf
source_type: paper
status: active
tags:
  - source
  - algorithmic-fairness
  - political-philosophy
  - fairness-metrics
  - egalitarianism
updated_on: 2026-05-26
related_pages:
  - [[Algorithmic Fairness]]
  - [[Algorithmic Fairness as Political Philosophy]]
  - [[Fairness Metrics]]
  - [[Fairness Impossibility Results]]
  - [[COMPAS Controversy]]
  - [[Risk Assessment in Criminal Justice]]
  - [[Algorithmic Accountability and Fairness]]
  - [[Reuben Binns]]
---

# Binns, 2018: Fairness in Machine Learning: Lessons from Political Philosophy

## Summary

Reuben Binns argues that fair machine learning cannot define fairness or bias by technical statistical criteria alone. Statistical definitions such as demographic parity, equality of opportunity, accuracy equity, disparate mistreatment, and counterfactual fairness each presuppose normative ideas about discrimination, equality, justice, responsibility, and legitimate grounds for differential treatment.

The paper is the course's first explicit bridge from [[Fairness Metrics]] to political philosophy. It does not reject formalization. Instead, it argues that formalization has to be guided by the philosophical question: what kind of equality, discrimination, or injustice is at stake in this specific decision context?

## Key claims

- Fair machine learning faces a prior conceptual problem: before technical mitigation begins, one must decide which fairness ideal is appropriate for the context.
- Metric conflict is not only a mathematical inconvenience. It reveals deeper normative disagreement about what fairness requires.
- "Discrimination" and "fairness" are not interchangeable. Some algorithmic harms may be morally serious without fitting classic philosophical accounts of wrongful discrimination.
- Mental-state accounts of discrimination do not transfer easily to algorithmic systems because algorithms do not possess animus, contempt, or disrespect in the way human decision-makers do.
- Accounts centered on "treating people as individuals" also face difficulty because predictive systems necessarily generalize, and generalization is not always wrongful.
- Binns treats fairness in fair ML as a placeholder for multiple egalitarian concerns rather than a single technical property.
- Relevant egalitarian questions include the currency of equality, spheres of justice, luck and desert, deontic or historical justice, and representational harms.

## Evidence and methods

The paper surveys political-philosophical theories and maps them onto fair ML debates. It connects existing technical measures to older debates about discrimination, egalitarianism, equality of opportunity, luck egalitarianism, Rawlsian and Dworkinian resources, Senian capabilities, Andersonian democratic equality, Walzerian spheres of justice, and recognition or representation.

The argument is conceptual rather than empirical. Binns shows that different technical metrics implicitly answer different philosophical questions: whether fairness is about equal outcomes, equal opportunities, accuracy, individualized treatment, counterfactual worlds without protected-class membership, protection from brute luck, political equality, or cultural representation.

## Why it matters for Digital Nudging

Digital nudging systems increasingly classify, rank, recommend, score, and personalize. Binns is crucial because these systems often import a fairness metric as if it were a neutral technical choice. In digital environments, that is especially dangerous: the same model may allocate attention, opportunity, visibility, friction, surveillance, or persuasion, and each of those goods may belong to a different sphere of justice.

For the course, this paper shifts algorithmic fairness from "which metric should we optimize?" to "which philosophical account of fairness explains the relevant harm?" That matters for recommendation systems, content moderation, ranking, personalization, targeted nudges, and platform governance, where distributional harms and representational harms often overlap.

## Links into the wiki

- [[Algorithmic Fairness as Political Philosophy]]: the main concept extracted from the paper.
- [[Fairness Metrics]]: Binns explains why metrics need normative justification.
- [[Fairness Impossibility Results]]: metric incompatibility creates a need for philosophical choice.
- [[COMPAS Controversy]]: Binns helps interpret why COMPAS cannot be resolved by statistical analysis alone.
- [[Algorithmic Accountability and Fairness]]: connects metric choice to accountable institutional design.

## Open questions

- Which political-philosophical theories should be foregrounded for each digital nudging domain: ranking, recommendation, risk scoring, content moderation, and targeting?
- How should Binns be sequenced with Hellman on the moral significance of different errors?
- How should the course distinguish distributive fairness from representational fairness in platform settings?

## Bibliographic reference

Binns, R. (2018). Fairness in machine learning: Lessons from political philosophy. In S. A. Friedler & C. Wilson (Eds.), *Proceedings of the 1st Conference on Fairness, Accountability and Transparency* (PMLR Vol. 81, pp. 149-159). PMLR. https://proceedings.mlr.press/v81/binns18a.html
