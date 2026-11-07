---
title: AI as Choice Aid
page_type: synthesis
status: active
tags:
  - synthesis
  - ai
  - choice-aids
  - chooser-welfare
  - digital-nudging
updated_on: 2026-11-07
related_pages:
  - [[Digital Nudging]]
  - [[Sunstein, 2023|Behavioral Biases, Choice Engines, and Paternalistic AI]]
  - [[Loewenstein et al., 2014|Disclosure: Psychology Changes Everything]]
  - [[Gabaix and Laibson, 2006|Shrouded Attributes]]
  - [[Kling et al., 2012|Comparison Friction]]
  - [[Bhargava et al., 2017|Choose to Lose]]
  - [[Kleinberg et al., 2023|The Challenge of Understanding What Users Want]]
  - [[Chang et al., 2024|Does Counting Change What Counts?]]
  - [[Behavior-Welfare Gap]]
  - [[Shrouded Attributes]]
  - [[Algorithmic Thought Partners]]
  - [[Recommendation Systems]]
  - [[Smart Disclosure]]
  - [[Chooser Welfare]]
  - [[Cherep et al., 2026|AI Agents Are Sensitive to Nudges]]
  - [[Sunstein, 2026|Paternalism after Behavioral Economics]]
---

# AI as Choice Aid

The constructive case for AI in digital nudging begins from a negative finding: what people choose often fails to reveal what would make them better off. Choices can be distorted by inattention, misunderstanding, self-control problems, poor feedback, comparison costs, hidden fees, misleading salience, and internal conflict between impulsive and reflective selves. In digital environments, the problem becomes sharper because platforms can observe behavior in detail and optimize around it. But observable behavior is not the same as welfare.

This synthesis treats AI as a possible choice aid: a tool that helps people understand, compare, reflect, and act in ways closer to their own considered interests. The point is not that AI is automatically welfare-enhancing. The same capacities can become hypernudging, dark patterns, or engagement traps. The central question is when AI repairs the [[Behavior-Welfare Gap]] rather than exploits it.

## The behavior-welfare problem

The classical revealed-preference assumption says that what people choose is evidence of what they want. This is often useful, but the sources in this cluster show why it can break.

[[Bhargava et al., 2017|Choose to Lose]] is the cleanest example. Employees at a large firm chose among health plans that were otherwise identical except for financial cost-sharing and premiums. Many low-deductible plans were financially dominated by high-deductible alternatives: no plausible health-spending scenario or standard risk preference could justify them. Yet 61% of employees chose nominally dominated plans, with substantial avoidable spending. The likely explanation was not a subtle preference for insurance, but low insurance competence.

[[Kling et al., 2012|Comparison Friction]] shows a milder but equally important version. Medicare Part D beneficiaries could access personalized plan-cost comparisons, but many did not. A mailed letter that delivered personalized cost information increased switching and reduced predicted costs. Information existed, but it was not psychologically or practically available enough.

[[Kleinberg et al., 2023|The Challenge of Understanding What Users Want]] gives the platform version. Users may spend a long time with content and later regret it. Engagement can reflect value, but it can also reflect moreishness, habit, or a System 1 pull that no longer serves reflective welfare. Even a platform trying to maximize user utility can fail if it observes only engagement.

Together these cases make the same point: behavior is evidence, not welfare itself.

## Why information is not enough

Many policy and interface responses rely on disclosure. The user is told the fee, shown the plan, given the privacy terms, or pointed to the comparison website. [[Loewenstein et al., 2014|Disclosure: Psychology Changes Everything]] explains why this often disappoints. Limited attention, motivated attention, complexity, delay, overload, probability misperception, and social pressure can prevent disclosure from improving decisions. Disclosures can even backfire when they morally license conflicted advisors or burden recipients with information they cannot use.

The useful lesson is not anti-disclosure. It is anti-formalism. Good disclosure must be simplified, standardized, comparative, timely, vivid where appropriate, and often mediated by intermediaries. This is exactly where digital and AI tools become relevant. They can turn disclosure into sense-making: reading the terms, comparing the options, calculating the user's likely costs, explaining why one option dominates another, and helping the user act.

But comparison itself can distort. [[Chang et al., 2024|Does Counting Change What Counts?]] shows that people overweight numeric dimensions because numbers are comparison-fluent. A choice aid that makes only prices, ratings, probabilities, or efficiency scores fluent may cause users to neglect qualitative dimensions such as fit, dignity, care, trust, or meaning. The design target is not "more numbers." It is balanced intelligibility.

## Markets can be adversarial

[[Gabaix and Laibson, 2006|Shrouded Attributes]] explains why choice aids are needed in markets where firms profit from consumer mistakes. A firm can advertise a low base price while shrouding expensive add-ons, fees, or penalties. Sophisticated consumers may exploit the low base price and avoid the add-ons, while myopic consumers pay. Competition does not necessarily unshroud the market because educating consumers may benefit competitors as much as, or more than, the educating firm.

This matters for digital nudging because many online interfaces are built around the same structure: visible benefits, delayed costs, hidden renewals, late fees, hard-to-compare bundles, opaque privacy costs, or cancellation burdens. In such settings, an AI choice aid is not merely a convenience tool. It can become adaptive armor ([[Algorithmic Thought Partners]]): a user-side system that surfaces hidden attributes, summarizes terms, compares total costs, and resists strategic obfuscation.

The danger is that the aid itself may be funded, ranked, or optimized by actors with conflicting incentives. A comparison tool can become a paid placement system. An AI assistant can become a sales agent. The ethics of choice aids therefore depends on institutional incentives as well as interface quality.

## The aid can itself be nudged

Delegating a decision does not remove the influence of choice architecture. It changes who encounters it. An assistant asked to compare options or implement a user's intentions may itself respond disproportionately to defaults, suggestions, and selectively available information. Even a system assigned a user-serving objective may therefore be steered by the environment it is supposed to help the user navigate.

Cherep, Maes, and Singh's [[Cherep et al., 2026|AI Agents Are Sensitive to Nudges]] gives this concern an empirical basis. Across fourteen models in a controlled information-search task, many agents respond more strongly than human participants to ordinary choice cues. Some accept a proposed default almost universally; others acquire too much information, too little, or follow rigid search patterns. Human examples and chain-of-thought prompting do not reliably resolve the problem. Some stronger reasoning configurations improve robustness, with additional computational costs and uneven effects.

The important test is whether the agent responds appropriately to the cue's value. A helpful default can produce a good payoff even when the system accepts it indiscriminately. An intervention that supplies genuinely useful information should influence a good decision-maker. Human-like behavior is therefore a comparison baseline, not the definition of success. Evaluation needs to examine how choices change when suggestions are arbitrary, information quality varies, or a helpful default becomes unsuitable, alongside the outcomes achieved.

These findings qualify the promise of adaptive armor. The protective assistant must be able to evaluate the architecture's steering signals; a benign objective alone does not establish that ability. The controlled experiment does not measure the effects of every commercial interface, and its highlighting treatment changes information costs rather than visual salience alone. Nevertheless, it identifies a mechanism relevant to delegated choice. A firm's ability to steer a consumer through cues aimed at the consumer's agent is a plausible extension to [[Dark Patterns]], clearly distinguished from the behavior demonstrated here.

## From prediction to choice aid

Digital choice aids often begin as prediction systems. They infer what a person might click, buy, watch, choose, or prefer from past behavior and from the behavior of similar users. That predictive capacity is useful, but it does not settle the welfare question.

The first problem is target selection. If the target is engagement, purchase, retention, or acceptance, the system may be accurate while still missing welfare. The second problem is interpretation. A predicted preference can encode confusion, impulse, inertia, or manipulation as easily as considered endorsement.

For the course, this distinguishes ordinary [[Recommendation Systems]] from [[Algorithmic Thought Partners]]. A recommender predicts what the user or similar users will like, click, buy, or watch. A choice aid helps the user reason about what they should do by their own lights. Sometimes prediction helps; sometimes it reproduces the very behavior that needs correction.

## Choice engines and paternalism

[[Sunstein, 2023|Behavioral Biases, Choice Engines, and Paternalistic AI]] names the constructive instrument: the choice engine. A choice engine can ask what matters to a user, compute the consequences of options, incorporate future costs, and present a simple set of recommendations such as Good, Better, and Best. It can be more personalized than a mass nudge and less coercive than a mandate.

The hard question is paternalism. A choice engine may simply organize information, or it may recommend, default, warn, add friction, or block options. Some of these moves can be justified when options are dominated, shrouded, or predictably harmful. But the same moves become dangerous when the system is coarse, biased, self-interested, opaque, or overconfident about welfare.

The design standard should therefore be stronger than behavioral effectiveness. A choice aid should improve decisions under conditions the user could endorse: better information, clearer comparisons, reduced manipulation, preserved exit, and explanation adequate for trust.

The [[Hypernudge#Worked example: testing a subscription recommendation|worked subscription experiment]] shows what this changes in evaluation. A seller calls the highlighted annual plan successful because it increases purchases. A user-serving assistant must ask whether the plan fits the person's expected use and whether the commitment is understood. It could recommend the monthly plan to an uncertain user and the annual plan to a regular one, reducing aggregate annual conversion while improving fit. Evaluate understanding, total cost, later endorsement, and practical reversibility alongside choices. Do not compare only the users who purchased: the aid may have changed who buys at all. These are implications for the hypothetical example, not experimental results from the choice-aid papers.

Choosing to delegate can itself express agency. Sunstein develops that point in [[Sunstein, 2026|Paternalism after Behavioral Economics]]: people may reasonably prefer assistance or delegation to making every decision directly. The question raised by Cherep and coauthors concerns the reliability of the delegate. Respecting the choice to delegate and establishing that the agent will act competently are distinct requirements.

## Design principles

The sources converge on a small set of design principles for AI choice aids.

First, do not equate behavior with welfare. Engagement, retention, purchase, plan inertia, and acceptance are starting points for inquiry, not final welfare measures.

Second, make comparison usable. Personalized, standardized, action-guiding comparisons matter more than passive information access.

Third, build competence. In complex domains such as insurance, the aid should explain the structure of the choice, not only output a recommendation.

Fourth, surface hidden attributes. Fees, add-ons, renewal terms, privacy costs, penalties, and long-run consequences should move from the periphery to the decision surface.

Fifth, explain enough for contestability. Users need to understand the relevant reasons, assumptions, and tradeoffs, especially when the aid asks them to defer to algorithmic judgment.

Sixth, keep qualitative values in view. Simplification should not turn the easiest-to-number attribute into the only attribute that counts.

Seventh, audit incentives. A choice aid built by a platform, seller, insurer, or affiliate network may optimize for conversion, revenue, or retention while presenting itself as user-serving assistance.

Eighth, test the aid's susceptibility to choice architecture. Check whether it distinguishes useful information from arbitrary steering, and whether information-search costs are justified. A good payoff in one favorable environment is insufficient evidence of robustness.

## Course payoff

AI as choice aid is the constructive counterpart to the dark-pattern and hypernudge warnings. Digital systems can personalize, test, rank, recommend, and adapt continuously. Those capacities can exploit attention, extract data, and maximize engagement. They can also help people make sense of complex options, resist shrouding, avoid dominated choices, and act on their own considered interests.

The hinge is welfare. If AI systems merely learn what people do, they may scale mistakes. If they help people understand what they would endorse under better conditions, they can become a genuine extension of nudging's original paternalistic aspiration: not just changing behavior, but helping choosers by their own lights.
