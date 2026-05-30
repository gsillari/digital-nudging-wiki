---
title: Manipulation
page_type: concept
status: active
tags:
  - concept
  - manipulation
  - dark-patterns
  - autonomy
  - ethics
updated_on: 2026-05-30
source_count: 10
related_pages:
  - [[Digital Nudging]]
  - [[Ethics of Nudging]]
  - [[Sunstein, 2016|The Ethics of Influence: Government in the Age of Behavioral Science]]
  - [[Hansen and Jespersen, 2013|Nudge and the Manipulation of Choice]]
  - [[Yeung, 2017|Hypernudge: Big Data as a Mode of Regulation by Design]]
  - [[Gray et al., 2018|The Dark (Patterns) Side of UX Design]]
  - [[Mathur et al., 2019|Dark Patterns at Scale]]
  - [[Narayanan et al., 2020|Dark Patterns: Past, Present, and Future]]
  - [[Mathur et al., 2021|What Makes a Dark Pattern... Dark?]]
  - [[Luguri and Strahilevitz, 2021|Shining a Light on Dark Patterns]]
  - [[Gray et al., 2024|An Ontology of Dark Patterns Knowledge]]
  - [[Hypernudge]]
  - [[Nudge]]
  - [[Choice Architecture]]
  - [[Transparency and Disclosure]]
  - [[Sludge]]
  - [[Dark Patterns]]
  - [[Dark Patterns as Adversarial Choice Architecture]]
---

# Manipulation

## Core idea

[[Manipulation]] is influence that insufficiently engages or appeals to people's capacities for reflective and deliberative choice. The concern is not that influence exists, or even that it sometimes works through automatic processes. The concern is that some influence bypasses reflection in ways that fail to respect autonomy and dignity. Sunstein's [[Sunstein, 2016|The Ethics of Influence: Government in the Age of Behavioral Science]] supplies the main ethical vocabulary for that concern.

The strongest distinction is between manipulating behavior and manipulating choice. A non-transparent nudge can alter automatic behavior without manipulating reflective choice, while a non-transparent nudge that shapes the premises of reflection is the stronger manipulation case. Hansen and Jespersen develop that distinction in [[Hansen and Jespersen, 2013|Nudge and the Manipulation of Choice]].

The digital version is opaque algorithmic manipulation. A system can continuously personalize rankings, feeds, recommendations, and prompts in ways that users cannot detect or reconstruct. Yeung's [[Yeung, 2017|Hypernudge: Big Data as a Mode of Regulation by Design]] is the anchor for this adaptive version of the problem.

The most concrete digital form is the dark pattern. [[Dark Patterns]] manipulate by modifying the decision space and information flow so that users are steered toward choices that benefit the service while frustrating their own welfare, privacy, or autonomy.

## Key distinctions

- Influence vs manipulation: all choice architecture influences; only some influence bypasses, exploits, or undermines reflection in objectionable ways.
- Transparency vs justification: transparency is a safeguard, but a transparent design can still manipulate if it predictably exploits vulnerability or inattention.
- Consent vs permissibility: consent can reduce the ethical problem, but it does not automatically make manipulative treatment respectful.
- Nudge vs dark pattern: a nudge should be defensible by reference to the chooser's welfare; a dark pattern uses behavioral insight to serve the architect at the user's expense.
- Sludge vs manipulation: [[Sludge]] can manipulate when friction is strategically used to exhaust, confuse, or trap users.
- Manipulation of behavior vs manipulation of choice: nudge typology ([[Nudge]]) treats non-transparent automatic-behavior nudges as manipulation of behavior and non-transparent reflective-choice nudges as manipulation of choice.
- Dark patterns vs legitimate persuasion: legitimate persuasion can present reasons, benefits, or recommendations; dark patterns distort the conditions under which users can recognize, evaluate, refuse, or reverse the proposal.

## Digital mechanisms

Digital manipulation can appear through hidden defaults, asymmetric friction, confirmshaming, countdown pressure, scarcity cues, confusing consent banners, deceptive hierarchy, hard-to-cancel flows, algorithmic ranking, recommender loops, personalized persuasion, and notification timing.

The digital problem is structural as well as intentional. A platform can manipulate deliberately, but it can also build optimization systems that discover manipulative interfaces because those interfaces increase conversion, retention, or engagement.

Hypernudging expands the mechanism: data collection and feedback loops allow manipulation to become adaptive. The system can learn which users respond to which cues and when.

Manipulation can also be discovered experimentally rather than fully planned in advance. Growth hacking and A/B testing can reveal which interface variants move users most effectively, even when the resulting design is difficult to justify as user-serving. [[Narayanan et al., 2020|Narayanan et al.]] connect dark patterns to that experimentation pipeline; [[Luguri and Strahilevitz, 2021|Luguri and Strahilevitz]] show why subtlety matters, because mild dark patterns can strongly affect behavior while avoiding the backlash that makes users realize they were pushed.

## Dark-pattern manipulation

Dark-pattern manipulation is not only a list of named tricks; it can be described by attributes such as asymmetry, restrictiveness, disparate treatment, covertness, deception, and information hiding. Mathur and coauthors' [[Mathur et al., 2021|What Makes a Dark Pattern... Dark?]] is especially useful for that attribute-based diagnosis because it explains how a design can undermine reflection without literally forcing the user's hand.

The dark-pattern cases also preserve the course's System 1/System 2 distinction. Many patterns exploit automatic, low-effort responses: following a default, trusting a visual hierarchy, reacting to social proof, avoiding shame, or acting before a timer expires. The ethical concern is that the design is arranged to prevent slower reflection from correcting the automatic response.

The concrete pattern vocabulary comes from several sources: [[Gray et al., 2018|The Dark (Patterns) Side of UX Design]] names strategies such as obstruction and interface interference; [[Mathur et al., 2019|Dark Patterns at Scale]] documents their prevalence in e-commerce; and [[Gray et al., 2024|An Ontology of Dark Patterns Knowledge]] harmonizes the taxonomy across levels of abstraction.

## Evaluation questions

- Does the design help users understand the choice, or exploit what they are unlikely to notice?
- Does it create urgency, fear, social pressure, or shame disproportionate to the stakes?
- Are refusal, reversal, and exit as visible and easy as acceptance?
- Would users still endorse the design if they knew the objective being optimized and the data used to target them?
- Does the system learn which users are more vulnerable to a particular prompt, default, or pressure tactic?
- Is the platform using experiments to find the most effective way to bypass refusal, exit, or deliberation?

## Related pages

- [[Ethics of Nudging]]
- [[Hypernudge]]
- [[Dark Patterns]]
- [[Dark Patterns as Adversarial Choice Architecture]]
- [[Recommendation Systems]]
- [[Transparency and Disclosure]]
- [[Nudge]]
- [[Choice Architecture]]
- [[Sludge]]
- [[Digital Nudging]]

## Open questions

How should the course distinguish strong but legitimate personalization from manipulative personalization when both may rely on the same data and predictive infrastructure?
