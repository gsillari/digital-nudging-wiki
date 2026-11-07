---
title: Predictive Algorithms, Bias, and Fairness
page_type: synthesis
status: active
tags:
  - synthesis
  - algorithmic-fairness
  - predictive-algorithms
  - bias
  - digital-nudging
updated_on: 2026-11-07
related_pages:
  - [[Algorithmic Fairness]]
  - [[Algorithmic Fairness]]
  - [[Prediction Policy Problems]]
  - [[Algorithmic Policy Efficiency]]
  - [[Fairness Impossibility Results]]
  - [[Digital Nudging]]
sources_used:
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
---

# Predictive Algorithms, Bias, and Fairness

## Core thesis

Predictive algorithms are powerful because many institutional and digital decisions are [[Prediction Policy Problems]]: they depend on forecasting who is likely to reoffend, fail to appear, repay, need help, click, churn, benefit, cause harm, or respond to an intervention. The fairness problem begins because prediction is never merely prediction once it enters a decision system. A score becomes a threshold, a recommendation, a priority ranking, a detention decision, a fraud flag, a search result, a prompt, or a nudge.

The course should therefore treat predictive algorithms through a double lens. The efficiency lens asks whether algorithmic decision support can improve on noisy, biased, or inconsistent human judgment. The fairness lens asks how the benefits and burdens of prediction are distributed, justified, contested, and embedded in institutions. Neither lens is dispensable. Efficiency without fairness can rationalize harmful systems. Fairness without efficiency can ignore avoidable crime, detention, exclusion, or waste produced by human decision-making.

The central hinge is [[Fairness Impossibility Results]]: plausible fairness conditions can be jointly unavailable. For risk scores, calibration preserves the meaning of a probability across groups, but cannot coexist with both of Kleinberg and coauthors' score-balance conditions when base rates differ and prediction is imperfect. For binary decisions, predictive parity and equal false positive and false negative rates face a related, distinct incompatibility under nondegenerate conditions. These conflicts open the fairness branch. We have to justify which demands govern a setting, through legal, political, philosophical, and institutional reasoning rather than statistics alone.

## Why Predictive Algorithms Matter

Predictive algorithms matter because many decisions are ranking decisions. A judge decides which defendants are too risky to release. A doctor decides which patients should receive additional testing. A regulator decides which worksites to inspect. A college decides which students should enter remedial courses. A platform decides which options, warnings, recommendations, or prompts to show.

In such cases, a better prediction can improve the decision frontier. [[Kleinberg et al., 2018|Human Decisions and Machine Predictions]] gives the canonical example. In pretrial release, Kleinberg et al. estimate that an algorithmic release rule could reduce crime by up to 24.7 percent at the same jailing rate, or reduce jailing by up to 41.9 percent with no increase in crime. This is not merely administrative efficiency. Less crime and less incarceration are both morally serious gains.

[[Mullainathan, 2025|Economics in the Age of Algorithms]] generalizes the point: economists have historically emphasized causal inference, but many important decisions hinge on prediction. [[Ludwig et al., 2024|The Unreasonable Effectiveness of Algorithms]] then reinforces the policy case. Algorithmic interventions can look unusually effective when they improve misranked decisions and scale cheaply. The reason is not mystical. If human decision-makers routinely misorder cases, better ranking can reduce deadweight loss without expanding the coercive or administrative apparatus.

This is the positive case for predictive algorithms: human judgment is not a neutral baseline. It can be noisy, inconsistent, biased, and inaccurate. Algorithms can reveal patterns humans miss, standardize aspects of decision-making, and support better allocation.

## The COMPAS Entry Point

The COMPAS controversy ([[Algorithmic Fairness]]) is the best opening case because it makes all the tensions visible at once. [[Angwin et al., 2016|Machine Bias]] showed that COMPAS risk scores in Broward County produced racially asymmetric errors: Black defendants were more likely to be falsely labeled high risk, while white defendants were more likely to be falsely labeled low risk. The public concern was not simply that an algorithm made mistakes. It was that the mistakes were patterned across race and embedded in legal decisions about liberty.

The controversy also showed why "bias" is not one thing. A score can be criticized because it produces unequal false positives. It can be defended because it is calibrated, so the same score has roughly the same empirical meaning across groups. It can be criticized again because the model is proprietary, hard to contest, and used in a coercive institutional setting. It can be criticized still more broadly because pretrial risk detention itself may be objectionable even if the model satisfies a metric.

This layered structure is why COMPAS should not be taught as a simple morality tale about bad algorithms. It is a case about prediction, measurement, legal burden, institutional authority, racialized error, proprietary opacity, and sociotechnical governance.

The pedagogical pivot comes immediately after the case: ProPublica's error-rate critique and calibration-based defenses need not contradict each other, because they measure different things. Kleinberg, Mullainathan, and Raghavan's [[Kleinberg et al., 2016|Inherent Trade-Offs in the Fair Determination of Risk Scores]] establishes a structural conflict among score-based criteria. It does not establish every claimed conflict between threshold-based error rates, nor show that COMPAS itself is justified. The case and the theorem together force the question: when attractive criteria conflict, which should govern this domain?

That is the entry into fairness as a branch of inquiry. Not "which metric is the fair one?" but "what kind of fairness is at stake here, and what institutional choice follows when metrics conflict?"

## Bias Is Not One Concept

In the algorithmic fairness branch, bias should be separated into at least five questions.

First, there is measurement bias: are the data and labels themselves distorted by policing, surveillance, reporting, access, or historical inequality?

Second, there is predictive meaning: does a score, or a positive classification, mean the same thing across groups? Calibration and binary predictive parity address these respective questions ([[Fairness Impossibility Results]]).

Third, there is error burden: who bears false positives and false negatives? This is the concern behind error rate parity ([[Fairness Impossibility Results]]), especially when mistakes lead to detention, exclusion, denial, surveillance, or loss of opportunity.

Fourth, there is policy alignment: does the metric serve the legitimate goal of the decision system, or does it optimize a proxy that omits relevant values?

Fifth, there is sociotechnical harm: does the whole decision system remain unjust even if the model performs well by some statistical measure?

These questions overlap, but they are not interchangeable. A system can be well calibrated and still distribute error burdens unequally. A system can equalize error rates and still optimize the wrong institutional goal. A system can serve a stated policy goal and still be procedurally opaque, politically illegitimate, or harmful in its broader social effects.

## The Impossibility Hinge

The first formal lesson concerns scores, before any threshold turns them into decisions. Calibration within groups means that a probability score of 0.7 corresponds to a 70% observed outcome frequency in each group. Balance for the positive class means that people who experience the outcome receive the same average score across groups. Balance for the negative class requires the same for people who do not experience it. Kleinberg, Mullainathan, and Raghavan prove that satisfying all three requires either perfect prediction or equal group base rates. With unequal base rates and imperfect prediction, at least one must fail.

Binary decisions introduce different conditions. Predictive parity means equal positive predictive value: among those classified positive, the same fraction actually has the outcome in each group. Error-rate parity means equal false positive rates among actual negatives and equal false negative rates among actual positives. These are conditional rates, not raw counts or measures of the severity of harm. At equal nondegenerate error rates, the positive predictive value rises with the base rate, so unequal base rates preclude predictive parity. The formula and its exceptions are unpacked in [[Fairness Impossibility Results#What the impossibility results establish]].

Keeping these statements separate matters. Calibrating each score does not guarantee predictive parity when several scores are pooled above a threshold. Nor are Kleinberg's average-score balance conditions identical to equalizing error rates at one threshold. Figure FIR.3 in [[Fairness Impossibility Results#A worked threshold example]] makes the distinction concrete: two calibrated groups have different false positive and false negative rates, but also different positive predictive values. The example illustrates a possible disparity; it is not a proof that its direction is inevitable.

The normative question begins where these statistical distinctions leave off. Hedden's [[Hedden, 2021|On Statistical Criteria of Algorithmic Fairness]] defends calibration's special evidential role. Hellman's [[Hellman, 2020|Measuring Algorithmic Fairness]] asks how errors translate into treatment and legal burdens, with particular attention to the balance between error types. Her argument is not simply a demand to equalize both error rates in every domain.

The conflict blocks the idea that technical improvement can always satisfy every attractive fairness demand. It does not say fairness is impossible, authorize arbitrary metric choice, or make existing base rates morally unproblematic. The institution must explain what each criterion protects and what is lost by relaxing it:

- If we prioritize calibration or predictive parity, we prioritize evidential consistency at the score or classification level respectively.
- If we prioritize error-rate parity, we prioritize equal conditional exposure to specified types of mistake, while still investigating their consequences.
- If we prioritize policy alignment, we ask which metric best serves the legitimate goal of the decision system.
- If we prioritize sociotechnical fairness, we ask whether the whole decision system is the right object of reform.

The impossibility result is therefore not an abstract theorem on the side. It is the branch point. It forces the course from statistics into normative theory, legal reasoning, public policy, and institutional design.

## From Metrics to Normative Theory

[[Binns, 2018|Fairness in Machine Learning: Lessons from Political Philosophy]] moves the discussion from metric selection to normative justification. Fairness metrics operationalize theories of equality, discrimination, opportunity, desert, representation, and historical injustice. There is no purely technical way to decide whether demographic parity, predictive parity, equality of opportunity, error-rate parity, or another criterion is the right one.

[[Corbett-Davies et al., 2017|Algorithmic Decision Making and the Cost of Fairness]] adds a policy-design layer. A fairness constraint can reduce one disparity while worsening the decision system's stated objective. That does not mean fairness should be sacrificed to efficiency. It means the trade-off must be explicit: what goal is the system supposed to serve, what cost does the fairness constraint impose, and is that cost justified by the legal and moral stakes?

Together, these arguments respond to the impossibility hinge without settling it by definition. Hedden gives calibration a special epistemic role. Hellman emphasizes the practical balance and consequences of errors. Binns makes the choice among metrics a question for political philosophy. Corbett-Davies and coauthors require attention to policy goals and decision costs.

Metrics are therefore instruments. Their legitimacy depends on the theory of justice and the policy context in which they are used.

## The Efficiency Branch

The efficiency branch matters because fairness debates often treat human decision-making as the implicit alternative to algorithmic prediction. But the human baseline can be bad. Judges can release high-risk defendants while jailing low-risk ones. Doctors can overtest some low-risk patients while missing high-risk patients. Agencies can misrank worksites, students, applicants, cases, or users.

[[Algorithmic Policy Efficiency]] captures this point. If an algorithm can reduce jail without increasing crime, that is a fairness-relevant fact, not a technocratic distraction. Avoided detention is a liberty gain. Avoided crime is a welfare gain. Better ranking can reduce harm without increasing the overall burden of intervention.

But [[Ludwig and Mullainathan, 2021|Fragile Algorithms and Fallible Decision-Makers]] warns against the naive version of the efficiency argument. The hardest part is not always building a predictor. It is evaluating whether the predictor improves decisions. selective labels ([[Algorithmic Policy Efficiency]]) make counterfactual evaluation difficult because we do not observe outcomes for people whose earlier human decision prevented the label from appearing. omitted payoff bias ([[Algorithmic Policy Efficiency]]) arises when the algorithm predicts one outcome while the real decision depends on a richer objective function. The override problem ([[Algorithmic Policy Efficiency]]) arises because algorithms are often decision aids, not decision-makers; humans may have useful private information, or they may add noise and bias.

The efficiency branch therefore does not say "algorithms are better." It says: predictive algorithms can improve decision frontiers, but only when the decision, payoff function, counterfactual evaluation, and human-machine workflow are specified carefully.

## The Sociotechnical Turn

[[Narayanan, 2026|What If Algorithmic Fairness Is a Category Error?]] pushes the argument further. Narayanan's central claim is that fairness is not a property of a predictive algorithm alone. It is a property of a sociotechnical decision system: data, model, threshold, user interface, human discretion, institutional goal, legal context, appeal procedure, procurement process, and downstream consequence.

This is not a rejection of fairness metrics. It is a demotion of metrics from final verdicts to diagnostics. Unequal false positive rates can reveal a serious problem. Calibration can preserve the meaning of scores. Policy alignment can discipline metric choice. But none of these proves that the system is fair.

The COMPAS example makes the point stark. Even if a risk score were calibrated and error-balanced, the broader use of pretrial detention based on predicted future conduct could still be morally troubling. The model might be transparent and still be embedded in an unjust institution. The decision aid might improve ranking and still legitimate a coercive system that deserves deeper reform.

Sociotechnical fairness is the capstone because it keeps both branches in view. Efficiency is also a property of the system, not just the model. Fairness is also a property of the system, not just the metric.

## Implications for Digital Nudging

For [[Digital Nudging]], predictive algorithms are everywhere: recommendation systems, search rankings, fraud detection, content moderation, risk scores, personalization engines, targeting systems, adaptive prompts, and AI assistants. These systems often do not formally deny a benefit or impose a sentence. They shape choice environments by changing visibility, salience, timing, friction, defaults, and recommendations.

That makes fairness harder, not easier. A user may be nudged away from an opportunity without seeing the opportunity. A group may receive more friction, fewer beneficial recommendations, or more manipulative prompts without a clear adverse decision. A platform may optimize engagement, conversion, retention, or risk reduction while omitting welfare, autonomy, privacy, dignity, and long-term learning.

The course should therefore carry over four lessons:

- Predictive performance is not enough; the question is what decision frontier the system changes.
- Fairness metrics are necessary but incomplete; they identify possible harms but do not settle legitimacy.
- Bias must be analyzed at the level of data, prediction, action, policy goal, and sociotechnical system.
- Digital nudging systems should be audited as choice architectures, not just as models.

### A worked ranking case

Consider an invented online training marketplace that ranks subsidized courses for visitors. Its model predicts the probability of applying, not eligibility, completion, or benefit. Among 1,000 eligible visitors in each of two groups, the course appears in the first three results for 600 in A and 300 in B. Of those exposed, 120 in A and 60 in B apply. Both exposed groups have a 20% application rate, yet the groups receive very different access to a salient opportunity: 60% versus 30% exposure and 12% versus 6% applications across all eligible visitors.

Those numbers do not establish that the ranking is unjust, or even that the prediction is calibrated across all visitors. They show why the denominator matters. Equal response among people selected for exposure can conceal unequal exposure itself. Past applications may reflect previous rankings, language barriers, or limited time; learning from them can reproduce those constraints rather than identify who would benefit. Applications from unexposed people also cannot simply be assumed to be zero under exposure. A randomized exposure study could help estimate that counterfactual, subject to the ethics of allocating opportunity.

The competing judgments are substantive. A conversion objective rewards likely applicants. An access objective asks whether eligible people have a meaningful opportunity to discover the course. A benefit objective asks who would gain from attending, which requires evidence beyond predicted applications. Binns's political-philosophy argument, Corbett-Davies and coauthors' policy analysis, and Narayanan's system-level critique locate different parts of this disagreement. None dictates an automatic 50/50 allocation. Their common lesson is to justify the target, the eligible population, the distribution of visibility, and the way users can find or contest omitted opportunities.

The [[Hypernudge#Worked example: testing a subscription recommendation|subscription experiment]] raises the same issue on the consumer side: an aggregate conversion gain can conceal subgroup differences in comprehension or regret. A fairness audit should examine who receives which design and who benefits, not only whether one predictor satisfies a parity equation. Neither teaching example is evidence reported by the cited papers.

## Teaching Sequence

A clean teaching sequence would move in four stages.

First, start with [[Angwin et al., 2016|Machine Bias]] and the COMPAS controversy ([[Algorithmic Fairness]]). Students see the concrete stakes: risk scores, race, errors, opacity, and liberty.

Second, introduce [[Fairness Impossibility Results]] immediately. Separate Kleinberg's score theorem from the binary conflict between predictive parity and equal error rates, then work through FIR.3's counts and denominators. Students should see both why some choices are unavoidable and why a precise theorem does not license a vague claim that all fairness criteria always conflict.

Third, move to normative and policy interpretation: algorithmic fairness as political philosophy ([[Algorithmic Fairness]]), fairness as policy alignment ([[Algorithmic Fairness]]), and sociotechnical fairness ([[Algorithmic Fairness]]). Students learn that metrics require moral and institutional justification.

Fourth, introduce the efficiency branch: [[Kleinberg et al., 2018|Human Decisions and Machine Predictions]], [[Ludwig and Mullainathan, 2021|Fragile Algorithms and Fallible Decision-Makers]], [[Mullainathan, 2025|Economics in the Age of Algorithms]], and [[Ludwig et al., 2024|The Unreasonable Effectiveness of Algorithms]]. Students see that algorithmic decision support can produce real gains, but only under careful evaluation and governance.

The resulting synthesis is deliberately ambivalent. Predictive algorithms are neither neutral technical tools nor inherently illegitimate machines. They are powerful components of decision systems. Their promise lies in better prediction, ranking, and support. Their danger lies in hidden objectives, unequal errors, metric laundering, institutional opacity, and the temptation to treat a model's score as a moral conclusion.

## Working Formulation

Predictive algorithms should be evaluated by asking:

- What decision does the prediction support?
- What outcome is predicted, and is it the right target?
- What are the costs of false positives and false negatives?
- Do scores have the same evidential meaning across groups?
- Who bears the burdens of errors?
- When predictive parity and error-rate parity conflict, which one is justified in this setting?
- What fairness metric, if any, matches the relevant theory of justice?
- What policy goal is being optimized, and what values are omitted?
- How does the human-machine workflow function in practice?
- Can affected people understand, contest, or exit the system?
- Does the whole sociotechnical system deserve to exist in this role?

That checklist keeps the core lesson alive: predictive algorithms can improve decisions, but fairness belongs to the governed decision system, not to the prediction alone.
