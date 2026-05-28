---
title: Algorithmic Fairness
page_type: topic
status: active
tags:
  - topic
  - algorithmic-fairness
  - digital-nudging
  - platform-governance
updated_on: 2026-05-27
related_pages:
  - [[Digital Nudging]]
  - [[Algorithmic Accountability and Fairness]]
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
  - [[Coglianese and Lehr, 2017|Regulating by Robot]]
  - [[Coglianese and Lehr, 2019|Transparency and Algorithmic Governance]]
  - [[Coglianese, 2021|Administrative Law in the Automated State]]
  - [[Algorithmic Governance and the Automated State]]
  - [[Management-Based AI Regulation]]
  - [[Reasoned Transparency]]
  - [[COMPAS Controversy]]
  - [[Fairness Metrics]]
  - [[Predictive Parity]]
  - [[Error Rate Parity]]
  - [[Fairness Impossibility Results]]
  - [[Algorithmic Fairness as Political Philosophy]]
  - [[Fairness as Policy Alignment]]
  - [[Sociotechnical Fairness]]
  - [[Algorithmic Decision Support Efficiency]]
  - [[Prediction Policy Problems]]
  - [[Selective Labels]]
  - [[Omitted Payoff Bias]]
  - [[Override Problem]]
  - [[Risk Assessment in Criminal Justice]]
  - [[Hypernudge]]
  - [[Recommendation Systems]]
  - [[Transparency and Publicity]]
---

# Algorithmic Fairness

## Scope

[[Algorithmic Fairness]] organizes the course's material on bias, parity, prediction, efficiency, transparency, and institutional accountability in algorithmic systems. It sits inside [[Digital Nudging]] because digital choice architecture increasingly works through algorithmic scores, rankings, feeds, recommendations, and decision aids.

The opening sequence is deliberately concrete: begin with [[Angwin et al., 2016|Machine Bias]] and the [[COMPAS Controversy]], then introduce [[Kleinberg et al., 2016|Inherent Trade-Offs in the Fair Determination of Risk Scores]] as the first formal result. The case makes the stakes vivid; the impossibility result explains why the dispute cannot be settled by one neutral mathematical definition.

## Subtopics

- [[COMPAS Controversy]] as the entry case for algorithmic risk scores, racialized error burdens, proprietary opacity, and due process.
- [[Fairness Metrics]] for calibration, [[Predictive Parity]], [[Error Rate Parity]], statistical parity, and later parity measures.
- [[Fairness Impossibility Results]] for structural conflicts between plausible fairness requirements.
- [[Algorithmic Fairness as Political Philosophy]] for the claim that metrics operationalize prior theories of equality, discrimination, justice, and representation.
- [[Fairness as Policy Alignment]] for the claim that fairness constraints should be assessed against regulatory and policy goals.
- [[Sociotechnical Fairness]] for the claim that fairness is a property of the whole decision system, not of the predictive model alone.
- [[Risk Assessment in Criminal Justice]] as the main institutional setting for the opening module.
- Bias and parity branch: mathematical criteria lead into accounts where bias is defined by the consequences of error, political philosophy, regulatory or policy goals, and the full sociotechnical decision system.
- Efficiency and prediction branch: [[Prediction Policy Problems]] and [[Algorithmic Decision Support Efficiency]] ask when algorithms improve judicial or administrative decisions, how [[Selective Labels]] distort evaluation, how [[Omitted Payoff Bias]] complicates claims of welfare improvement, and how the [[Override Problem]] shapes aided decision-making.
- Governance branch: [[Algorithmic Governance and the Automated State]] asks how legal compatibility, [[Reasoned Transparency]], management-based regulation, and human oversight make algorithmic decision systems publicly accountable.

## Canonical pages

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
- [[Coglianese and Lehr, 2017|Regulating by Robot]]
- [[Coglianese and Lehr, 2019|Transparency and Algorithmic Governance]]
- [[Coglianese, 2021|Administrative Law in the Automated State]]
- [[Algorithmic Governance and the Automated State]]
- [[Management-Based AI Regulation]]
- [[Reasoned Transparency]]
- [[COMPAS Controversy]]
- [[Fairness Metrics]]
- [[Predictive Parity]]
- [[Error Rate Parity]]
- [[Fairness Impossibility Results]]
- [[Algorithmic Fairness as Political Philosophy]]
- [[Fairness as Policy Alignment]]
- [[Sociotechnical Fairness]]
- [[Algorithmic Decision Support Efficiency]]
- [[Prediction Policy Problems]]
- [[Selective Labels]]
- [[Omitted Payoff Bias]]
- [[Override Problem]]
- [[Risk Assessment in Criminal Justice]]
- [[Algorithmic Accountability and Fairness]]

## Current synthesis

The first lesson is that algorithmic fairness disputes are often metric disputes. ProPublica's COMPAS analysis focused on unequal error burdens: Black defendants were more likely to be falsely classified as high risk, while white defendants were more likely to be falsely classified as low risk. Calibration-centered defenses can respond that a score has the same meaning across groups. Kleinberg, Mullainathan, and Raghavan show why both intuitions cannot generally be satisfied at once when base rates differ and prediction is imperfect. Hedden then strengthens the calibration side: predictive parity is not just one metric among others, but the condition that preserves the evidential meaning of scores or predictions across groups.

The second lesson is that metric choice is normative, but not all metrics play the same role. Hedden's view gives calibration or [[Predictive Parity]] a privileged place for fair prediction, while leaving open the possibility that unfairness enters through thresholds, downstream decisions, background injustice, or stereotype-reinforcing side effects.

The third lesson is Hellman's legal-action lesson. Predictive parity preserves what scores mean, but fairness usually concerns what institutions do with scores. [[Error Rate Parity]] matters because false positives and false negatives impose different burdens, and those burdens can reflect measurement error or compound prior injustice.

The fourth lesson is Binns's political-philosophy lesson: fairness metrics are not self-justifying. Demographic parity, equality of opportunity, counterfactual fairness, accuracy equity, and error-rate metrics each express a different view about what should be equal, which differences are legitimate, and whether the relevant harm is distributive, historical, or representational.

The fifth lesson is the policy-alignment lesson from Corbett-Davies et al. Fairness constraints should be evaluated against the actual regulatory or policy goal: public safety in their pretrial example, but welfare, access, exposure diversity, or user well-being in other settings. This makes the cost of a fairness metric visible without implying that the policy objective is beyond moral scrutiny.

The sixth lesson is Narayanan's category-error lesson. Fairness metrics, normative theories, and policy goals remain useful, but they are incomplete if they evaluate only the predictive algorithm. Fairness belongs to the whole sociotechnical decision system: data, model, threshold, interface, human discretion, institutional goal, appeal path, political economy, and downstream consequences.

The seventh lesson is the efficiency-frontier lesson from Kleinberg et al. Human decision-making is not the neutral baseline. In bail, the authors estimate that algorithmic release rules could reduce crime by up to 24.7 percent at the same jail rate, or reduce jail by up to 41.9 percent at the same crime rate. Efficiency is therefore morally important when it means less victimization or less incarceration rather than mere administrative speed.

The eighth lesson is the fragile-algorithms lesson from Ludwig and Mullainathan. Efficiency gains do not come from prediction accuracy alone. They require solving [[Selective Labels]], avoiding [[Omitted Payoff Bias]], and designing for the [[Override Problem]] because human decision-makers remain part of the system.

The ninth lesson is Mullainathan's summary lesson. Bail is one example of a broader class of [[Prediction Policy Problems]] in which economics should study and improve decisions that hinge on prediction. Algorithms matter because they can reveal misranking, scale decision aids at low marginal cost, and force economists to model human-plus-algorithm decision systems.

The tenth lesson is the unreasonable-effectiveness lesson from Ludwig, Mullainathan, and Rambachan. Some algorithmic interventions can have very high apparent returns because they improve rankings in domains where human decision-makers misorder cases and because software can scale cheaply. This strengthens the efficiency branch while also motivating careful pilots and in-context evaluation.

The eleventh lesson is the governance lesson from Coglianese and collaborators. Algorithmic systems can fit administrative law when objectives, validation, due process, and reasons are preserved, but legal compatibility is not enough. Heterogeneous and multifunctional AI needs [[Management-Based AI Regulation]], lifecycle oversight, and human accountability.

The twelfth lesson is that algorithmic fairness belongs in digital nudging even when the example is criminal justice rather than platforms. Risk scores guide human attention and action. In digital systems, the same structure appears in feeds, rankings, eligibility scores, personalization engines, recommender systems, and automated prompts.

## Open questions

- Which source should be added as the main reference on parity measures beyond predictive parity: Barocas and Narayanan, another taxonomy paper, or both?
- How should the class pair the efficiency frontier with the sociotechnical critique so students see both the promise and the limits of algorithmic decision support?
