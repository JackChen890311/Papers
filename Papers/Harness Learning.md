---
title: "Harness Learning Enables Generalizable Test-Time Adaptation"
time: 2609
author: Johns Hopkins University; Carnegie Mellon University
link: https://arxiv.org/pdf/2609.35738
accepted: None
tags:
  - LLM
  - Agent
  - ReinforcementLearning
  - MetaLearning
  - TestTimeAdaptation
todo: false
scanned: true
read: false
summary: Trains a small proposer LM with RL to rewrite a frozen solver's executable harness from execution feedback, so test-time adaptation happens in program space instead of weight space and transfers to unseen task families.
---
# Summary
💡 Write a brief summary of this paper here
- An agent = **model + harness**, where the harness is plain executable Python (context building, tool dispatch, control flow, retry/verification) deciding what the model sees and when it is called. Adapting the harness improves the agent **without touching weights**.
- **Harness learning** = train a *proposer* to emit code edits to a *solver's* harness given (task description, current harness, execution report). Revisions play the role of weight updates ⇒ **meta-learning over executable programs**.
- Proposer trained with **GRPO**, reward = task score of the revised harness + validity bonus; optional SFT from a 35B teacher. At test time both proposer and solver are frozen — adaptation is purely code-space.
- **21 unseen Reasoning Gym families: 0.32 → 0.62** (Base → RL) mean single-revision score, and the **4B proposer beats its 35B teacher** (0.62 vs 0.56) on average. QA proposer trained only on HotpotQA transfers zero-shot to MuSiQue / 2Wiki, where 10 revision rounds reach 0.27 EM vs 0.15 for independent proposals.
![[Harness Learning Fig1 Method Overview.png]]

# Methodology
💡 Describe the methodology used in this paper
- **Components**: *Proposer* `π_θ` (only trained network, 4B; input = task + harness `h_{t-1}` + report, action = code edit) → *Harness* (frozen solver's orchestration program) → *Solver* (frozen LLM, Qwen3.5-4B / Qwen3-8B).
- **Objective**: harness quality `J(h;Q) = mean_q score(h,q)`; outer loop `max_θ E[J(h_T; Q_eval)]`, inner loop = the revision rounds. Question sets are disjoint: `Q_fb` (build report) / `Q_score` (score candidates) / `Q_eval` (held-out).
- **Structured edit interface**: SEARCH/REPLACE patches + diagnosis + change manifest; must parse, define `run`, pass sandbox (3 retries), or score 0.
- **Loop**: sample `G` edits → apply → `Select` on `Q_score` → re-execute retained harness on fresh feedback questions. RG: `G=1`, keep only if dev score improves. QA: `G=8`, always take the best-scoring candidate.
- **Reward** `r_i = J(h'_i; Q_score) + v_i`, with `v_i = 0.05·1[parses] + 0.10·1[h'≠⊥] + 0.15·ρ_run` (runnable-but-wrong already earns 0.30) → group-normalized advantages → GRPO. Reformulated as a *local, single-edit* surrogate for final harness quality (no credit across rounds).
- **SFT init**: 432 teacher (Qwen3.6-35B-A3B) first-round edits that beat the seed by ≥0.08, audited; 48% are "interpreter loops". **Single-step vs Multistep RL** differ only in whether parent harnesses come from earlier revisions (same immediate-reward update).
![[Harness Learning Fig2 RL Training.png]]

# Experiments
💡 List the experiments settings and results of this paper
- **Setup**: RG — Qwen3.5-4B proposer+solver, SFT→RL, 21 SFT / 5 RL families, 21 unseen families, 8 independent proposals or 5 rounds × 1. QA — Qwen3-4B proposer + Qwen3-8B solver, RL from base (no SFT) on HotpotQA, evaluated on MuSiQue / 2Wiki, 80 proposals or 4 runs × 10 rounds × 8.
- **Single revision, 21 unseen families**: 0.32 (Base) → 0.49 (SFT) → **0.62 (RL)**, i.e. the *average* proposal improves (no cherry-picking), and only after RL does the average beat the seed.
- **4B student > 35B teacher**: 0.62 vs 0.56 mean; teacher still wins under oracle best-of-8 (0.85 vs 0.83) — better highlights, worse average edits ⇒ RL exceeds the imitation ceiling.
- **Reliability**: invalid/zero-scoring proposals 38%→23%→15% (canonical), 34%→22%→6% (format-varied), 38%→35%→8% (OOD). Almost all gain comes from RL, not SFT.
- **Multistep (RG)**: 5 sequential proposals reach/exceed oracle best-of-8 of independent ones; round-5 means over 24 families: 0.593 Base / 0.698 SFT / 0.699 RL / 0.701 Multistep (canonical); 0.498 / 0.688 / **0.725** / 0.649 (format-varied).
- **QA transfer**: RL proposers improve past round 1 on all three benchmarks and end above Base (Base even *damages* the seed on HotpotQA/MuSiQue). MuSiQue: 0.15 EM (80 independent) vs **0.27** (10 rounds); average final run beats oracle best-of-80 on both unseen sets.
- **Ablations / null results**: single-step vs multistep *training* ≈ tie (canonical +0.002, format-varied −0.076; QA within noise) ⇒ single-step training already yields a revision skill that generalizes to intermediate harnesses. Composition/helper-tool rewards give no consistent gain (correct helper + broken parsing/tool-message/answer-extraction); harder-task RL better single-step (0.600 vs 0.576) but worse after repeated revision.
- **Learned structure**: RG → interpreter loops (77–78% of unseen-family harnesses; solver writes Python, runtime executes). QA → keeps multi-hop retrieval and separates "summaries for the next query" from "passages for the answer", plus third-hop / re-search edits.
![[Harness Learning Fig3 Single-Step Revision.png]]
![[Harness Learning Fig6 Reliability Structure.png]]

# Related Papers
💡 Include any related papers that are relevant to this one
- **Harness / workflow optimization**: DSPy, AFlow, Meta-Harness, AutoHarness, Ecdysis, EvoHarness-RL, WHALE (alternating harness + weight updates).
- **Concurrent learned editors**: Harness-R1 (teacher SFT → GRPO, frozen target agent), JIT-Agent (SFT + exec-DPO + repair + Evo-GDPO, harness archive), Ornith (joint scaffold + solving RL). This paper: revise the *current* harness with a frozen solver, and study transfer + repeated adaptation.
- **Meta-learning**: MAML, RL², AdaptFlow, The Last Harness, EvoX, MAGE, Tajwar et al. (transferable exploration without parameter updates). Twist: the adapted object is code, so control flow and tool interfaces can change.
- **Self-improvement**: Self-Refine, Reflexion, Feedback Friction, STOP, Darwin Gödel Machine, TTHE, STaR / Self-Rewarding LMs / SEAL, SIA.
- **Benchmarks**: Reasoning Gym, HotpotQA, MuSiQue, 2WikiMultihopQA; harness-evolution evaluation: Evo-Bench, HarnessCompass, "Rethinking the Evaluation of Harness Evolution".

# Appendix
💡 Anything else that's in this paper but not mentioned before
- **RG protocol**: 25 dev (feedback + selection) / 75 held-out instances per family; 3 generation attempts, 32k response budget; seed harness = one solver call; a fixed 5-turn "tool loop" baseline already averages 0.69 on the 21 OOD families.
- **Training**: LoRA r=32, 32k context, lr 1e-4 cosine, ~2.9 epochs, 4-fold family-disjoint CV; RL 640 contexts, `G=8`, 40 contexts/update, lr 1e-6, 16 updates, report checkpoint 10; solver T=0.7, 300 s/trial, partial credit.
- **QA**: full-wiki BM25 over 5.23M abstracts for HotpotQA, but MuSiQue/2Wiki use *pooled dev paragraphs* (easier retrieval); 6 feedback + 64 scoring questions per context; reward = EM + 0.1 validity, ≤200 lines, 12 calls / 12 retrievals.
- **Limitations**: single teacher ⇒ narrow SFT distribution; proposer is not agentic (no code inspection / test running / environment queries — reports are externally built); solver frozen ⇒ no co-adaptation; no cross-round credit assignment; sequential vs independent comparisons do not match compute/feedback budgets.

---
# Resources
💡 Include some useful links for better understanding of this paper
- [arXiv abs](https://arxiv.org/abs/2609.35738) · [HTML](https://arxiv.org/html/2609.35738v1) · [PDF](https://arxiv.org/pdf/2609.35738)
- Related: [Harness-R1](https://arxiv.org/abs/2608.02276) · [JIT-Agent](https://arxiv.org/abs/2608.25593) · [Meta-Harness](https://arxiv.org/abs/2603.28052) · [WHALE](https://arxiv.org/abs/2609.00196) · [TTHE](https://arxiv.org/abs/2607.08124) · [GRPO](https://arxiv.org/abs/2402.03300) · [MAML](https://arxiv.org/abs/1703.03400)

# Personal Notes
💡 Personal thoughts, reflections, or questions about this paper
- The framing is the contribution: the LLM is the brain, the harness is the body/OS (context builder, tool dispatcher, control flow, verification/retry, budget guard). Once accepted, "adapt the program, not the weights" is the natural alternative to fine-tuning — no forgetting, no inference-time gradients, and the optimized object is human-readable.
- The strongest evidence is **not** 0.32→0.62 (the RG seed is deliberately minimal, huge headroom) but (a) reliability 38%→15% / 34%→6%, and (b) MuSiQue 0.15→0.27 beating best-of-80 — the proposer *uses feedback on its own edits*, which single-step evaluation cannot measure.
- Caveat: each sequential run uses 80 proposals but *sees* intermediate harnesses, so budgets are unmatched; "average proposal" and "best harness from a feedback loop" are different regimes.
- "Single-step ≈ multistep training" suggests local immediate reward already induces a compositional revision skill — but both use the same local objective, so cross-round credit assignment is still untested.
- Biggest gap for real agents: the proposer never runs anything (editor, not debugger). Agentic proposer + joint proposer–solver training is future work.
- Open questions: does it hold with a solver stronger than the proposer? Does the skill transfer across *harness families* (QA retrieval → coding/browser agents)? Does a dev-set hill-climb overfit with only 25/64 questions? Would a harness archive (DGM/STOP style) compound with the proposer?
- Cheap takeaway: keep agent logic in explicit code, log a structured execution report (per-case outcomes, failed traces, missed evidence), and let a small model propose targeted SEARCH/REPLACE edits — implementable today without RL; RL mainly buys reliability.
