---
title: Algorithmic Governance, Management, and the Automated State
page_type: synthesis
status: active
tags:
  - synthesis
  - ai-governance
  - administrative-law
  - management-based-regulation
  - digital-nudging
updated_on: 2026-05-28
related_pages:
  - [[Coglianese and Lehr, 2017|Regulating by Robot]]
  - [[Coglianese and Lehr, 2019|Transparency and Algorithmic Governance]]
  - [[Coglianese, 2021|Administrative Law in the Automated State]]
  - [[Sunstein, 2022|Governing by Algorithm? No Noise and (Potentially) Less Bias]]
  - [[Coglianese and Crum, 2024|Taking Training Seriously]]
  - [[Coglianese and Crum, 2025b|Regulating Multifunctionality]]
  - [[Coglianese and Crum, 2025a|Leashes, Not Guardrails]]
  - [[Algorithmic Governance]]
  - [[Algorithmic Fairness]]
  - [[Digital Nudging]]
---

# Algorithmic Governance, Management, and the Automated State

Predictive and generative AI create a governance problem because they are powerful, dynamic, and heterogeneous. They are powerful because they can rank, classify, predict, recommend, generate, and automate at scale. They are dynamic because they can be updated, fine-tuned, embedded in feedback loops, and repurposed after deployment. They are heterogeneous because the same broad family of techniques can be used in very different institutional settings, with different data, users, objectives, stakes, and harms.

This cluster develops in two movements. The early administrative-law papers ask whether algorithmic government can be legally legitimate at all. The later AI-governance papers assume that algorithmic systems will be used and ask a harder design question: how should law govern systems whose uses and risks cannot be specified exhaustively in advance?

Coglianese and his coauthors provide the main administrative-law backbone for this claim. Coglianese and Lehr, in [[Coglianese and Lehr, 2017|Regulating by Robot]], and Coglianese, in [[Coglianese, 2021|Administrative Law in the Automated State]], show how algorithmic systems can become decision aids, adjudicatory tools, rulemaking inputs, and instruments of expert administration. Sunstein, in [[Sunstein, 2022|Governing by Algorithm?]], supports the same general point from a behavioral angle: algorithms may improve administration by reducing noise and correcting some cognitive biases in human judgment, though his focus is more on prediction, consistency, and discrimination than on administrative-law doctrine.

Coglianese and Crum's later papers shift from administrative power to governance design. [[Coglianese and Crum, 2024|Taking Training Seriously]] and [[Coglianese and Crum, 2025a|Leashes, Not Guardrails]] support the dynamic-lifecycle claim: AI systems are not fixed at deployment but change through training, fine-tuning, monitoring, updating, human oversight, and new organizational uses. [[Coglianese and Crum, 2025b|Regulating Multifunctionality]] supports the heterogeneity claim most directly, especially for foundation and generative models: the same underlying system can be adapted to many tasks, users, institutional contexts, and harms, so it cannot be governed as if it had one stable function.

## Legal compatibility

Coglianese and Lehr, in [[Coglianese and Lehr, 2017|Regulating by Robot]], give the first answer: algorithmic administration is not automatically unlawful. "Adjudicating by algorithm" and "rulemaking by robot" can fit within administrative law and constitutional doctrine if agencies preserve the elements that make ordinary administration legitimate. The key point is that the algorithm is not imagined as an independent sovereign. It is a tool inside a human legal institution.

This matters for doctrines such as nondelegation, due process, equal protection, transparency, and reason-giving. Nondelegation concerns are concerns about who is exercising public power. If an algorithm effectively makes policy, adjudicates cases, or determines legal consequences, the worry is that authority has been delegated to a machine, vendor, or technical system without lawful political guidance. Coglianese and Lehr's answer is the administrative-law idea of an intelligible principle: the system must be tied to an objective function, statutory goal, prediction target, or policy criterion specified by legally responsible humans. On this view, the algorithm is not the sovereign. It is an instrument used inside an institution that remains answerable for the goal and the decision.

Due process worries are also pragmatic rather than categorical. Coglianese and Lehr rely on the Mathews v. Eldridge framework, the standard U.S. procedural-due-process balancing test. Mathews asks courts to weigh three things: the private interest affected by the government action, the risk of erroneous deprivation under the existing procedure and the likely value of additional safeguards, and the government's interest, including administrative burden. For algorithmic administration, this means the question is not "was a model used?" but "what is at stake, how likely is error, would explanation, hearing, human review, audit, or disclosure reduce that risk, and at what cost?"

Equal protection worries depend on the system's design, data, training labels, validation, thresholds, deployment, and human use, not merely on the fact that the system is algorithmic. This connects directly to [[Algorithmic Fairness]]. The constitutional point is not identical to the later metrics debate, but it pushes in the same direction: bias is not settled by saying "the model did not use race" or "the model is mathematically accurate." We have to ask whether proxy variables, historical labels, subgroup performance, threshold choices, and institutional reliance distribute benefits and burdens unequally. That is where legal equal-protection analysis meets fairness metrics ([[Algorithmic Fairness]]), including the tension between predictive parity ([[Fairness Impossibility Results]]) and error rate parity ([[Fairness Impossibility Results]]), and where it also needs the broader lens of sociotechnical fairness ([[Algorithmic Fairness]]).

The deeper move is to treat machine learning as continuous with older administrative instruments. Agencies already rely on technical tools, statistical models, inspections, scoring systems, instruments, and expert analyses that ordinary citizens and judges cannot fully reconstruct from the inside. What law usually demands is not mystical access to every causal mechanism. It demands responsibility, validation, an adequate explanation, and an opportunity to contest the decision where the stakes require it.

Sunstein, in [[Sunstein, 2022|Governing by Algorithm?]], adds the behavioral case for why legal compatibility might matter in practice. Human administration is not only biased in the discriminatory sense; it is also vulnerable to cognitive bias and noise. Noise means unwanted variability: similarly situated people can be treated differently because of the identity of the official, the sequence of earlier cases, or other irrelevant circumstances. Algorithms are "silent" in Sunstein's sense: the same system gives the same answer to identical cases. That can reduce unequal treatment and total error, especially in prediction problems. But Sunstein also marks the limit: a quiet algorithm can still be wrong, rigid, or discriminatory if its inputs, targets, proxies, or policy constraints are defective.

## Transparency

Coglianese and Lehr, in [[Coglianese and Lehr, 2019|Transparency and Algorithmic Governance]], then clarify what "transparency" should mean in this setting. Their crucial distinction is between fishbowl transparency and reasoned transparency ([[Transparency and Disclosure]]). Fishbowl transparency is access transparency. It asks whether outsiders can inspect records, code, data, meetings, documents, logs, and other materials showing what the government has done. It is the transparency of looking inside the fishbowl. Reasoned transparency is justification transparency. It asks whether the government can explain why a decision, policy, or system is justified. For an algorithmic system, this means explaining the objective function or public goal, the basic design choice, the data and validation strategy, the system's known limits, and the role the system plays in the final decision.

The distinction is important because full fishbowl transparency is neither always possible nor always sufficient. Source code can be proprietary, technically opaque, or too complex to make meaningful sense to most affected people. Conversely, dumping code or data into public view may not explain why the system is legitimate. The legal and democratic demand is therefore not simply "show me the code." It is "give an account of what the system is for, why this design is justified, how it was tested, what risks it creates, and how affected people can challenge it."

This also helps avoid a false binary between perfect interpretability and unacceptable black boxes. A technically complex model may still be governable if its objective, data, validation, performance, limitations, and institutional use are explained. This is one route toward intelligible AI: intelligibility can mean a responsible public account of the system, not full intuitive access to every internal computation. But this is not a blank check. Reasoned transparency depends on evidence. If an agency or platform cannot say what the system optimizes, how it was validated, or how errors are handled, then opacity has become an accountability failure.

## The automated state

Coglianese, in [[Coglianese, 2021|Administrative Law in the Automated State]], gives the legal argument a normative endpoint. Automation might strengthen expert administration. It can improve prediction, make decisions more consistent, reduce some arbitrary human discretion, and make public objectives more explicit. In that sense, the automated state may realize part of the administrative-law ideal: expert, evidence-based government acting under publicly specified goals.

But Coglianese also warns that expertise and accountability do not exhaust legitimacy. An automated state can be accurate and still alienating. It can be consistent and still unresponsive. It can produce legally defensible outcomes while leaving people with the sense that no one has heard them, understood their circumstances, or taken responsibility for the human meaning of the decision.

That is the role of empathy in the argument. Empathy is not sentimentality or a decorative user-experience layer. It is the institutional capacity to recognize affected people as situated agents rather than mere cases, scores, or inputs. In administrative settings, empathy can require escalation to a human, meaningful contestation, attention to unusual circumstances, explanation in language people can use, and care about how the process feels to those subject to it.

For the course, this matters because nudging has always depended on a view of the human subject. Behavioral public policy begins from the fact that people have limited attention, partial information, context-sensitive preferences, and emotional lives. If algorithmic government treats those same people only as optimization targets, it betrays the behavioral insight at the moment it becomes technologically powerful.

## Heterogeneity and multifunctionality

Coglianese and Crum shift the argument from legal defense to regulatory design. Their starting point is AI heterogeneity and multifunctionality ([[Algorithmic Governance]]). AI is not one thing. Its risks vary by use, design, domain, data, institutional setting, and decision role. A medical triage model, a benefits chatbot, a social-media recommender, and a hiring screen do not present the same governance problem just because all use machine learning.

In [[Coglianese and Crum, 2025b|Regulating Multifunctionality]], Coglianese and Crum argue that foundation models and generative AI intensify this problem. These systems are multifunctional: the same underlying model can perform many tasks for many users. This undermines one-size-fits-all regulation. A rule written for one function may be irrelevant or harmful for another. A performance standard may be hard to define when the model's tasks are open-ended. Ex post liability may come too late, especially when harms are diffuse, hard to observe, or produced by interactions among model, user, interface, and organization.

This is why the "Swiss Army knife" analogy matters. The regulatory object is not a single blade with one expected use. It is a tool whose risk profile changes as different blades are opened in different contexts. For digital nudging, the same foundation model might explain a pension choice, sell a product, screen welfare eligibility, recommend news, or coach a user through a health decision. The ethical status of the system depends on the deployment and the objective, not merely on the model family.

## Management-based regulation

Coglianese and Crum answer heterogeneity with management-based AI regulation ([[Algorithmic Governance]]). Across [[Coglianese and Crum, 2024|Taking Training Seriously]], [[Coglianese and Crum, 2025b|Regulating Multifunctionality]], and [[Coglianese and Crum, 2025a|Leashes, Not Guardrails]], their argument is that law should not try to prescribe every permitted output or banned design pattern in advance. Instead, it should require organizations to maintain internal systems for identifying, assessing, mitigating, documenting, auditing, and revising risks.

The reason is practical rather than permissive. If risks are context-specific and changing, regulators need organizations to do structured risk work continuously. That includes deciding what harms are plausible, what evidence would reveal them, who is responsible for monitoring them, how they will be mitigated, when a system should be stopped or escalated, and what documentation will let outsiders verify that this work happened.

The "leash" metaphor clarifies the difference from "guardrails." Guardrails are fixed barriers. They make sense when the road is known and the vehicle should stay in a lane. AI, especially multifunctional AI, often does not move on a fully known road. It can create new uses and new risks. A leash allows movement, exploration, and adaptation, but only because a human remains responsible at the other end. A leash without a grip is just permission dressed up as governance.

This is also why Coglianese and Crum make human-guided AI training ([[Algorithmic Governance]]) central. If regulation is about lifecycle risk management, then governance should not begin only after deployment. Training choices determine what the system learns, what it treats as success, what errors it reproduces, what explanations it can support, and what signals it treats as relevant. Human guidance during training can bring domain judgment, value judgments, fairness concerns, and human-salient distinctions into the development process before harms are scaled.

## Course synthesis

The full argument moves from legality to legitimacy to management. Coglianese and Lehr show that algorithmic government can be legally compatible with administrative law. Sunstein shows why algorithmic tools may sometimes improve on human administration by reducing noise and cognitive bias. Coglianese then adds that legitimacy requires empathy, not only expertise and accountability. Coglianese and Crum complete the sequence by arguing that modern AI's heterogeneity and multifunctionality require flexible governance through management systems, human-guided training, auditing, and lifecycle oversight.

For [[Digital Nudging]], this cluster reframes the ethics of algorithmic choice architecture. It is not enough to ask whether an individual nudge is transparent or welfare-promoting at the moment of exposure. We also need to ask whether the system that generates the nudge has legitimate objectives, human-guided training, reasoned transparency, auditability, fairness monitoring, contestability, and empathic escalation.

The course-level bridge is from interface ethics to institutional governance. Once nudges are produced by ranking models, recommender systems, adaptive defaults, experiments, and AI assistants, legitimacy depends on more than the visible screen. These systems need leashes: flexible enough to allow beneficial adaptation, but held by humans who remain responsible across the lifecycle.

The final payoff is that digital nudging ethics becomes institutional rather than merely interface-level. A dark pattern is not only a bad screen. A recommendation is not only a ranked list. An AI assistant is not only a conversation. Each is the visible surface of a managed or unmanaged system: objectives, data, training, experiments, audits, explanations, escalation procedures, and organizational incentives. The governance question is whether that whole system can give reasons, manage risk, preserve agency, and remain answerable to the people it steers.
