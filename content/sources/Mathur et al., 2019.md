---
title: "Mathur et al., 2019"
page_type: source
source_path: raw/papers/Mathur et al., 2019.pdf
source_type: journal_article
status: active
tags:
  - source
  - dark-patterns
  - e-commerce
  - empirical-study
  - manipulation
updated_on: 2026-05-27
related_pages:
  - [[Digital Nudging]]
  - [[Dark Patterns]]
  - [[Sludge]]
  - [[Manipulation]]
  - [[Privacy and Consent]]
  - [[Arunesh Mathur]]
  - [[Arvind Narayanan]]
---

# Mathur et al., 2019: Dark Patterns at Scale

## Summary

[[Mathur et al., 2019|Dark Patterns at Scale]] provides the large-scale empirical anchor for the dark-pattern module. The authors crawled roughly 11,000 shopping websites and documented how deceptive or coercive interface designs appear in ordinary e-commerce.

The paper defines dark patterns as user-interface design choices that benefit an online service by coercing, steering, or deceiving users into unintended and potentially harmful decisions. That definition is crucial for the vault because it combines mechanism and objective: the design steers users, and the steering benefits the service at the user's expense.

## Key findings

- The crawl found 1,818 dark-pattern instances on 1,254 websites, or about 11.1 percent of the shopping sites studied.
- More popular websites were more likely to contain dark patterns.
- The authors identified 15 dark-pattern types grouped into seven categories.
- They found 234 instances across 183 websites that appeared deceptive.
- They also identified 22 third-party entities offering dark-pattern functionality, showing that manipulation can be productized as a service.

## Taxonomy and mechanisms

The seven categories are:

- Sneaking: adding, hiding, or delaying information, including sneak into basket, hidden costs, and hidden subscriptions.
- Urgency: time pressure through countdown timers or limited-time messages.
- Misdirection: directing attention away from the user's preferred action, including confirmshaming, visual interference, trick questions, and pressured selling.
- Social proof: claims about other users' behavior or testimonials.
- Scarcity: low-stock or high-demand messages.
- Obstruction: making a task difficult, especially hard-to-cancel flows.
- Forced action: requiring enrollment or other actions before the user can proceed.

The paper also codes whether patterns are asymmetric, covert, deceptive, information-hiding, or restrictive. This makes it useful for connecting dark patterns to [[Sludge]], [[Manipulation]], and the later normative analysis in [[Mathur et al., 2021|What Makes a Dark Pattern... Dark?]].

## Why it matters for Digital Nudging

This source turns dark patterns from a set of anecdotes into an empirical platform problem. It shows that exploitative choice architecture is not occasional web clutter. It is detectable at scale, can be supplied by specialized vendors, and is often embedded directly into commercial conversion flows.

For digital nudging, the paper also clarifies why examples matter but should not dominate the course. The examples fix the concept: urgency, scarcity, forced action, hidden costs, and hard cancellation. The general lesson is broader: digital interfaces can use behavioral mechanisms familiar from nudging while optimizing for money, data, or retention rather than chooser welfare.

## Links into the wiki

- [[Dark Patterns]]: empirical evidence and central definition.
- dark pattern taxonomy ([[Dark Patterns]]): seven categories and 15 dark-pattern types.
- adversarial choice architecture ([[Dark Patterns]]): service-benefiting steering that harms or frustrates users.
- continuous optimization and experimentation ([[Hypernudge]]): dark patterns can be productized and tested against conversion metrics.
- [[Privacy and Consent]]: forced action and privacy-invasive disclosure connect to consent design.

## Bibliographic reference

Mathur, A., Acar, G., Friedman, M. J., Lucherini, E., Mayer, J., Chetty, M., & Narayanan, A. (2019). Dark patterns at scale: Findings from a crawl of 11K shopping websites. *Proceedings of the ACM on Human-Computer Interaction, 3*(CSCW), Article 81. https://doi.org/10.1145/3359183
