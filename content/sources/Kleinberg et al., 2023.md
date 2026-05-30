---
title: "Kleinberg et al., 2023"
page_type: source
source_path: raw/papers/Kleinberg et al., 2023.pdf
source_type: preprint
status: active
tags:
  - source
  - engagement
  - revealed-preference
  - platform-design
  - recommendation-systems
  - choice-aids
updated_on: 2026-05-28
related_pages:
  - [[AI as Choice Aid]]
  - [[Behavior-Welfare Gap]]
  - [[Recommendation Systems]]
  - [[Chooser Welfare]]
  - [[Dark Patterns]]
---

# Kleinberg et al., 2023: The Challenge of Understanding What Users Want: Inconsistent Preferences and Engagement Optimization

## Summary

[[Kleinberg et al., 2023|The Challenge of Understanding What Users Want]] formalizes a central digital-nudging problem: platforms often infer what users want from what users do, but engagement can diverge from welfare when users have inconsistent preferences.

The paper does not rely on the simple story that platforms are selfishly optimizing ad revenue. It considers a platform that wants to maximize user utility but observes only behavioral engagement. Even then, the platform can make users worse off if it treats engagement as revealed preference.

## Key claims

- Online platforms often use behavioral traces such as clicks, likes, watch time, and session length as proxies for user preferences.
- Revealed preference is fragile when users have conflicts between impulsive and reflective selves.
- Longer sessions can reflect high value, but they can also reflect "moreishness": content that keeps users consuming after reflective utility has fallen.
- Engagement and utility can be aligned in some regions of a content space and misaligned in others.
- Engagement optimization can produce familiar patterns such as regretful overuse and sudden "cold turkey" quitting.
- Platforms need signals beyond engagement, such as satisfaction surveys, regret measures, and design experiments that test whether increased engagement also increases welfare.

## Evidence and methods

The paper develops a formal model of media consumption. Users have a System 2 component that evaluates utility and a System 1 component that can continue consuming. Platforms optimize over a "content manifold," a space of possible content properties including value, span, and moreishness.

The model shows when engagement maximization approximates welfare and when it fails. Misalignment can arise because engagement-maximizing content has higher moreishness, or because it has higher span but lower value than utility-maximizing content.

## Why it matters for Digital Nudging

This is the central platform source for the [[Behavior-Welfare Gap]]. Digital choice architecture cannot assume that more engagement, longer dwell time, or repeated choice means that users are better off.

For [[AI as Choice Aid]], the paper provides a negative design requirement: a choice aid should not simply predict or optimize observed behavior. It must seek additional evidence about what users would endorse, regret, sustain, or find valuable after reflection.

It also deepens the ethics of [[Recommendation Systems]]. A recommender can be user-serving in intention and still harmful if the metric standing in for welfare is wrong.

## Links into the wiki

- [[Behavior-Welfare Gap]]: the platform version of the gap between observed behavior and welfare.
- [[Recommendation Systems]]: engagement optimization is one recommender objective, not a welfare standard.
- continuous optimization and experimentation ([[Hypernudge]]): A/B testing can optimize the wrong proxy.
- [[Chooser Welfare]]: user welfare requires more than inferred behavioral preference.

## Open questions

Which combinations of engagement data, satisfaction reports, regret measures, and long-run outcomes should count as evidence of user welfare in digital platforms?

## Bibliographic reference

Kleinberg, J., Mullainathan, S., & Raghavan, M. (2023). *The challenge of understanding what users want: Inconsistent preferences and engagement optimization* (arXiv:2202.11776v3). arXiv. https://arxiv.org/abs/2202.11776
