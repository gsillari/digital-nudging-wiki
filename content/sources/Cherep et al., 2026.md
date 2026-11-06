---
title: "Cherep et al., 2026"
page_type: source
source_path: raw/papers/Cherep et al., 2026.pdf
source_type: journal_article
status: active
coverage_status: main_article_complete
doi: https://doi.org/10.1073/pnas.2537030123
tags:
  - source
  - ai
  - choice-architecture
  - defaults
  - decision-support
updated_on: 2026-11-06
related_pages:
  - [[AI as Choice Aid]]
  - [[Algorithmic Thought Partners]]
  - [[Choice Architecture]]
  - [[Defaults]]
  - [[Chooser Welfare]]
  - [[Dark Patterns]]
  - [[Sunstein, 2026|Paternalism after Behavioral Economics]]
---

# Cherep et al., 2026: AI Agents Are Sensitive to Nudges

## Summary

Delegating a choice to an AI agent does not remove the effects of its presentation. Agents can themselves be influenced by defaults, suggestions, and the organization of information, sometimes more strongly than human participants. Cherep, Maes, and Singh demonstrate this in a controlled sequential decision task, showing that apparently successful outcomes can conceal excessive responsiveness to environmental cues.

The paper qualifies the promise of [[AI as Choice Aid]]: assistance must be evaluated for how it searches, interprets cues, and responds to changes in [[Choice Architecture]], as well as for the payoff it achieves. The authors do not show that every AI agent is always more susceptible than humans, or that all sensitivity is harmful. Effects vary across models, interventions, and reasoning settings.

## Evidence and methods

The study adapts a human multiattribute choice experiment into a text-based tool environment. Rows represent prize categories and columns represent baskets. Agents can pay to reveal hidden values before selecting a basket. Good performance requires balancing information value against acquisition costs. Human data come from the earlier experiment by Callaway, Hardy, and Griffiths (2023), rather than a newly recruited human sample (pp. 2, 8).

Fourteen models from OpenAI, Anthropic, and Google are tested with base instructions, zero-shot chain-of-thought prompting, and twelve human examples in few-shot prompts. The study samples approximately 300-340 trials per model-prompting condition per intervention family; those figures are trial counts, not numbers of human participants. Further experiments vary reasoning effort for selected reasoning models (p. 8).

The four intervention families differ substantively:

- Defaults: an initial option, selected using a heuristic, can be accepted or declined. This is an explicit acceptance opportunity, not a direct test of what happens when an agent takes no action.
- Suggestions: a randomly selected basket is suggested early or late, with one high-value cell revealed for free. The suggested basket is not selected because it is the best overall option.
- Information highlighting: cells in one row cost one point to reveal, compared with three points elsewhere. This changes information-acquisition incentives; it is not a pure visual-salience manipulation.
- Optimal nudges: six cells are revealed initially. Holding quantity constant, the design compares random, extreme-value, and human resource-rational-model-based selections to test sensitivity to information quality.

The analysis compares information acquisition, intervention responsiveness, and net payoffs. It uses logistic and linear regressions with cluster-robust standard errors, and Kolmogorov-Smirnov comparisons of reveal-count distributions (p. 8).

## Main findings

Many agents respond disproportionately to interventions. In the default task, human selection of the designated basket rises from 51% without the default to 88% with it. Several models reach 99-100% selection, while some stronger reasoning models do not differ significantly from the human baseline. Suggestion timing can produce either excessive acceptance or excessive rejection; susceptibility is not equivalent to always following a cue (pp. 2-3).

Information search also diverges. Some models reveal little or nothing; others buy information excessively or follow rigid spatial patterns. Chain-of-thought and human examples do not reliably remove intervention sensitivity, even where they improve aspects of search behavior (pp. 5, 7).

Helpful defaults and informative prereveals can improve payoffs, including for agents that respond indiscriminately. Thus, matching human earnings does not establish that an agent evaluates cues selectively. Conversely, a search strategy differing from human behavior is not automatically worse: the task's information value and payoff structure provide additional standards for evaluation (pp. 4-7).

Increased reasoning effort can reduce some sensitivities, but effects are inconsistent and carry substantial computational costs. More reasoning sometimes produces excessive rejection of a useful default rather than appropriate calibration. Reasoning budgets are not directly comparable across providers (pp. 5-8).

## Interpretation and limits

The paper concerns meaningful features of the task environment, rather than only arbitrary formatting changes, adversarial instructions, or agreement with an interlocutor. It does not establish that the human psychological mechanisms behind default effects also explain agent behavior. Human likeness is a descriptive comparison; appropriate use of information and reliable performance under interventions remain separate questions.

The controlled task supports interpretation of the tested interventions, but does not establish their magnitude in every deployed shopping, financial, or browser agent. The authors report additional real-data and robustness analyses in supporting information. Coverage here is the complete nine-page main article, including methods and references; the separate supporting information has not been independently reviewed. Claims about those additional analyses remain attributed to the authors (pp. 2, 7-8).

## Why it matters for Digital Nudging

The paper extends the empirical subject of nudging to an agent acting for a human. This adds a condition to adaptive armor ([[Algorithmic Thought Partners]]): a protective assistant must itself evaluate the steering signals in the environment it is meant to help users navigate.

It also sharpens the distinction between legitimate delegation and competent delegation. Sunstein's [[Sunstein, 2026|Paternalism after Behavioral Economics]] explains how choosing to delegate can express agency. Cherep and coauthors supply an empirical reason to examine the delegate's reliability. That connection is a course synthesis, rather than a claim that this experiment tests Sunstein's normative argument.

Agent-targeted [[Dark Patterns]] are a plausible implication, not what these experiments demonstrate. The interventions need not be malicious. A useful future question is whether firms can influence the user's eventual choice by designing cues for the intermediary agent, including when the human never encounters those cues directly.

## Bibliographic reference

Cherep, M., Maes, P., & Singh, N. (2026). AI agents are sensitive to nudges. *Proceedings of the National Academy of Sciences, 123*(25), Article e2537030123. https://doi.org/10.1073/pnas.2537030123
