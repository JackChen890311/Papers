---
title: "Towards Foundation Decision Models: Drex"
time: 2611
author: Nace.AI Research Team
link: https://arxiv.org/pdf/2611.07854
accepted: None
tags:
  - DecisionModels
  - Calibration
  - DiscriminativeInference
  - Multimodal
  - ReinforcementLearning
  - InferenceEfficiency
todo: false
scanned: true
read: false
summary: Presents Drex, four open decision models (8B/9B/35B-A3B/27B) that return a calibrated distribution over user-supplied options in a single forward pass, using either a pointer head over cached context or a 255-way readout head, trained with SFT plus consistency losses and RLAF.
---
# Summary
💡 Write a brief summary of this paper here
- **Decision model** = given a *state* (document / record / agent context, optionally images) plus typed questions (`choice` with K≤255 named options, `noul` yes/no, `score` on an integer scale), return a probability distribution over the options **without autoregressive decoding**. No output parsing, calibrated confidence, one prefill.
- Family of four open models on **one interface**: DLM 8B (diffusion LM), v1.5 9B (MiMo/Qwen3.5 hybrid), v2.0 3B-active/35B MoE (Qwen3.6-35B-A3B), Max 27B dense multimodal (Qwen3.8-27B). Claim: can a single model serve *arbitrary* option sets with *calibrated* probabilities, answer *many* questions over one long context, stay *stable* under option reordering, at production latency?
- **Pointer head** (DLM/v1.5/v2.0): query at `<decide>`, key at each `</opt>`, scaled dot product → softmax over exactly the supplied options. State encoded **once and cached** (2.1M / 1.0M head params, T=1).
- **Readout head** (Max): each option labelled with a single-token code (A…Z, AA…, 255 total); bias-free linear layer → 255 logits, softmax over the K codes. Causal mask removed in the 16 full-attention layers (of 64), **one sequence per question, no shared cache**.
- **Training**: SFT (CE + squared Cramér for score + permutation/state-shuffle consistency KL) → **RLAF** (adjusted target from teacher + verified outcome, proper scoring rule) → vision SFT (Max only).
- **Headline numbers**: Decision Index 0.4.1 **67.52 public / 66.60 full** (Jev 1.14: 60.70 / 60.24); Decision Bench v4 **94.0%** (tied with d3-turbo & GPT-6 Sol, −1.6 vs Claude Opus 5.5, +1.7 vs Jev); **183 ms** median vs ~2.0 s / 3.5 s for frontier chat models; **$0.06 per 1k decisions**.
![[Drex Fig1 Pointer Architecture.png]]

# Methodology
💡 Describe the methodology used in this paper
- **Request** `(S, I, {q_k})`; question `q_k=(τ_k, u_k, O_k)` with `K_k ≤ 255`. Confidence follows Jev's System One: `c_choice = (max_j p_j − 1/K)/(1 − 1/K)`, `c_score = 1 − E|i−î|/(L−1)`.
- **Packed encoding** (pointer models): `<state> S` then one block per question `<q> instr ∏(<opt> o_j </opt>) <decide>`. Delimiters reuse rare Qwen tokens (`<|fim_prefix|>`, `<|fim_middle|>`, `<|box_start|>`, `<|box_end|>`, `<|fim_suffix|>`) so no new embedding rows; user text is rewritten so it cannot emit them. Segment ids, position ids restarting after the state, option index per token.
- **Attention / question independence**: block-causal mask (question sees state + itself, never another question). DLM adds bidirectional attention inside the state; hybrid DeltaNet backbones cannot take arbitrary masks, so v1.5/v2.0 use **row form** `[S; b_k]` starting from the cached state → same outputs up to float error, and adding/removing questions never changes `p_k`. Optional *option isolation* (permutation-equivariance by construction) only works on attention-only backbones.
- **Pointer head**: `z_{k,j} = (W_k h_{</opt>})ᵀ(W_q h_{<decide>})/√d_p`, `d_p=256`, `p=softmax(z/T)`, T=1 in released v1.5/v2.0. One softmax, no decoding; options never seen in training are scored by the same mechanism.
- **Drex Max**: 64 layers, d=5120, 48 DeltaNet + 16 full-attention (every 4th); `M=1` in the full-attention layers (non-causal), causal elsewhere. `x_k = [I; S; u_k; A:o_1; …; <ans>]`, readout `z=W_r h ∈ R^255`, **T=1.009** fitted on held-out records. Order robustness is *learned* here (codes bind to positions), unlike the pointer.
- **Data**: 1,150,460 verified text decision records over 11 domains (Language & reading 18.3%, Tools/routing/home 15.7%, Knowledge 11.6%, Code/math 10.2%, …); labels checked against gold / execution / engine; Decision Index + JevBench excluded, near-duplicate (2×8-word) filtering; VQA data collected separately.
- **SFT loss**: `CE + λ_ord·D_C²` (squared Cramér distance for score questions) `+ λ_π·KL̄(p(S,b), π⁻¹p(S,πb)) + λ_s·KL(sg[p(S,b)] ‖ p(S̃,b))`. Options shuffled for K≥3; random `NONE`/distractor option injected so the model can decline.
- **RLAF (pointer)**: build *adjusted target* `q̃` = teacher distribution corrected by verified outcome `y*`; reward `R = Σ q̃_j log p_j + 0.5·(q̃ᵀp/‖p‖) − 1[score]·D_C²(p,q̃)`. All terms are proper ⇒ optimum is `p=q̃` ⇒ accuracy and calibration improve **together**. Optimized by direct differentiation (REINFORCE did not help); "the RL is in how q̃ is built".
- **RLAF (Max)**: KL-regularized policy `r(a) = ρ·1[a=y*] + η·log q^J_a` with `ρ=0.2, η=0.05`, `β=0.1` KL to the SFT model `π_0`; judge = generative **Qwen3.8-27B at high reasoning effort** (not stronger than Max — it contributes a second, CoT-shaped opinion).
- **Stages (Max)**: SFT full-parameter (1.15M records / 2.9M questions, 9k steps, lr 1e-5 backbone, λ_π=0.05, λ_s=1.0) → RLAF LoRA r=64 + head (180k records, 1.2k steps) → vision SFT of encoder+projector, 0.6B (95k records); 16,384-token sequences. v2.0 additionally has a **specialization stage** (LoRA on solver-verified hard examples + replay + KL to previous checkpoint, selected on held-out data, not benchmarks).
- **Serving**: shared prefill (6–8× at 8k, 11–12× at 32k with 16 questions, bit-identical), CUDA Graphs (−⅔ latency at 1k tokens), kernel rewrites (FlashInfer prefill for Blackwell, −9–16% at 8k–128k). A cached 114k–117k-token state answers the next question in **21.6 ms**, faster than a 2k state pass (35.6 ms).
![[Drex Fig2 Pointer vs Readout.png]]
![[Drex Fig3 Training Pipeline.png]]

# Experiments
💡 List the experiments settings and results of this paper
- **Setup**: Decision Index 0.4.1 (37 benchmarks, 140,620 public requests, chance-corrected skill), Decision Bench v4 (1,071 decisions: 949 text, 62 text+image, 60 image), Artificial Analysis Decision Index, JevBench-231, DecideBench, OpenSpiel arena, OSWorld judging, 11 vision suites. 95% Wilson intervals, paired bootstrap (5k resamples), exact McNemar; no multiple-comparison correction.
- **Decision Index 0.4.1** (public / full): Max **67.52 / 66.60**, v2.0 61.25 / 52.76, v1.5 58.08 / 45.78, Jev 1.14 60.70 / 60.24, GPT-6 Luna Decisions 47.78. New-domain private subset: Max 56.45 vs 39.22 (v2.0) vs 30.82 (v1.5) — the lead **widens** out of distribution. Per-domain: Max best everywhere except Arts (v2.0 53.9 vs 53.4) and a Knowledge tie with Jev (57.1).
- **Regressions vs v2.0**: POP909-CL next-chord 79.5 → 55.6 and Habermas Machine preference aggregation 62.4 → 50.5 — binding an option *code* to a long structured option hurts.
- **Decision Bench v4**: Max 94.0% with the image encoder (92.1% with text renderings only); image-only questions 63.3% → **98.3%**; statistically tied with d3-turbo (93.7) and GPT-6 Sol (94.7), +1.7 vs Jev (p=.048), −1.6 vs Opus 5.5 (p=.046); ECE 1.40% (d3-turbo 1.18%), 0.66 s end-to-end.
- **Artificial Analysis index**: 63.7, ~1 point behind d1-ultra/SubQ Snap/Elephant 9B; +6.6 over Jev; the gain over v1.5 comes mostly from **non-hallucination** (0.6% → 71.3%) while accuracy *drops* (37.6% → 27.6%).
- **Calibration** (~230k decisions, 108k requests): ECE at deployed temperature — v2.0 **1.37%**, Max 3.61%, v1.5 4.54%, Luna 4.87%. Re-fitting one temperature on Decision Index gives 0.79 / 1.35 / 1.17% (T*=0.91 / 1.35 / 1.48). Max is mildly **over-confident** (confidence 91.2% vs accuracy 87.9%); outside the Language domain per-domain ECE is 7.2–9.2%, and 8.4% for questions with 6–20 options — aggregate ECE hides this.
- **Selective prediction works**: keeping the 80% most confident decisions raises Max from 87.9% to **96.1%**, top-50% to **99.3%** (v2.0: 94.4% / 98.9%).
- **Option order** (1,591 decisions × 3 orderings, via public APIs): random-permutation flip rate 4.3% Max, 5.9% v2.0, 5.3% v1.5, 4.3% Jev; reversing is worse (5.7–8.4%). K=2 flips ~1–2%, K≥6 flips **13–16%**. Accuracy moves ≤1.2 points; averaging the three distributions helps log loss, not accuracy.
- **Instability ⇒ wrong**: decisions whose top option changes are 37.6% accurate for Max (vs 87.2% stable); but abstaining on instability is no better than abstaining on low confidence (87.2% vs 87.1%) — flips are largely already-low-confidence decisions.
- **Ablations on Max's own recipe** (the only clean causal comparison): SFT 64.9 → +RLAF **66.9** (+2.0 DI, +1.5 acc, −0.9 ECE, all significant); removing consistency terms leaves accuracy/DI unchanged but flip rate 4.2% → **6.3%** (17.8% at K≥6); vision stage changes nothing on text (66.9 → 66.8) and fixes images.
- **v2.0 checkpoints**: most of the gain is SFT (58.27 → 60.02), specialist +0.6 (almost all Retrieval, JevBench 84.0 → 87.0), RLAF +0.2 (Tools/Arts).
- **Latency / cost (Oct 2026)**: 183 ms Max, 151 ms v2.0, 145 ms v1.5, 196 ms Jev vs ~2.0 s GPT-6 Sol, ~3.5 s Opus 5.5; $0.06 / $0.06 / $0.04 per 1k decisions vs $3.33 / $10.17.
![[Drex Fig4 Other Benchmarks.png]]
![[Drex Fig5 Calibration.png]]
![[Drex Fig6 Option Order.png]]

# Related Papers
💡 Include any related papers that are relevant to this one
- **System One / decision models**: Jev (Typesafe) and its open reconstruction **Kev** (packing, block-causal mask, pointer head, permutation consistency); **pplx-decider-v1.1-27b** (Perplexity) supplies Max's attention pattern + readout design. Baselines: Jev 1.13/1.14, GPT-6 Luna Decisions, d3-turbo, Decider v1.2, d1-ultra, SubQ Snap, Elephant 9B.
- **Backbones**: Qwen3.8-27B, Qwen3.6-35B-A3B (MoE), MiMo-V2.6-Distill-Qwen-9B, NVIDIA Efficient-DLM-8B (autoregressive→diffusion), Gated DeltaNet / hybrid linear attention.
- **Discriminative readouts**: BERT-style classification heads, cross-encoder rerankers (Nogueira & Cho), Sentence-BERT / LLM2Vec embeddings, pointer networks, multiple-choice prompting and symbol binding (Robinson et al.), constrained decoding (Anderson; Hokamp & Liu; Park et al.).
- **Calibration & proper scoring**: Guo et al. (temperature scaling), Gneiting & Raftery (proper scoring rules), Brier, Bellemare et al. (Cramér distance / ranked probability score), ECE (Naeini), selective classification (Geifman & El-Yaniv), LLM confidence (Kadavath; Jiang).
- **Order sensitivity**: Pezeshkpour & Hruschka (option order in MCQs).
- **Training**: RLHF (Ouyang), DPO, label smoothing (Müller et al.), LoRA.
- **Benchmarks**: Decision Index, Decision Bench v4, JevBench-231, DecideBench v1.1, HLE, GPQA, MMLU-Pro, BBH, OSWorld, OpenSpiel.

# Appendix
💡 Anything else that's in this paper but not mentioned before
- **Family table**: DLM 8B / v1.5 9B / v2.0 3B-active of 35B / Max 27B; heads 256-d pointer (2.1M, 1.0M) vs 255-way readout (1.3M); context 32k / 131k / 131k / 262k; bf16 weights 16 / 18 / 70 / 49 GB (Q8 GGUF 8.7 / 9.5 / 36.9 / 27.3 GB); engines Py, llama.cpp, Ollama (+vLLM, Kev for v2.0). Licenses: Open RAIL-M for Max/v2.0/v1.5, CC BY-NC 4.0 for DLM, Apache-2.0 code; Max/v2.0/v1.5 also on a hosted API and OpenRouter.
- **Cost asymmetry**: Max has **no shared state cache** (proof: from the first full-attention layer on, a state token's hidden state depends on the question/option tokens that follow), so it pays the state once per question; pointer models pay it once per request. Cheap for short states, expensive for many questions over long documents; worst case ~2.7 s for a fresh 131k-token context.
- **Document search routing** (Appendix M): Max decides *lookup* vs *investigation* over a workspace query; threshold p(investigate) ≥ 0.80 routes to the search agent — **93.8%** correct on 662 held-out queries (AUROC 0.966).
- **Inference QA**: every answer-changing optimization (FP8, kernel fusion, graph padding) was accepted only if the accuracy delta stayed inside a paired-bootstrap threshold; this process also caught a packed-prefill bug that returned valid-looking but wrong answers (not visible in latency measurements).
- **Limitations**: closed-book knowledge gap is real and largest on hard items (HLE 21% vs 39% / 56%; GPQA Diamond 55% vs 90% / 89%); a single forward pass may be no substitute for CoT or tools (untested); Max vs pointer gains are confounded (backbone, mask, head, data all differ) — no same-backbone head ablation; the judge can in principle override the verified answer with ρ=0.2/η=0.05, possibly explaining over-confidence (unmeasured); one temperature cannot fix miscalibration that differs by domain and option count; the order study (1,591 decisions) excludes structured options rejected by APIs; many tests without Bonferroni.

---
# Resources
💡 Include some useful links for better understanding of this paper
- [arXiv abs](https://arxiv.org/abs/2611.07854) · [HTML](https://arxiv.org/html/2611.07854v1) · [PDF](https://arxiv.org/pdf/2611.07854)
- [Weights & inference code](https://github.com/nace-ai/drex-decision-models) · [Hugging Face org](https://huggingface.co/nace-ai) (drex-v1.5, drex-v2.0, drex-dlm) · [Launch page](https://www.nace.ai/drex) · [OpenRouter](https://openrouter.ai/nace-ai)
- Baselines / context: [Kev](https://github.com/jaredpalmer/kev) · [pplx-decider-v1.1-27b](https://huggingface.co/perplexity-ai/pplx-decider-v1.1-27b) · [Jev / System One](https://typesafe.ai/blog/introducing-system-one-models-and-jev)
- Benchmarks: [Decision Index](https://huggingface.co/spaces/multimodalart/jev-decision-index) · [Decision Bench](https://decisionbench.ai) · [Artificial Analysis Decision Index](https://artificialanalysis.ai/evaluations/artificial-analysis-decision-index)

# Personal Notes
💡 Personal thoughts, reflections, or questions about this paper
- The interface is the contribution: **the label set is an input, not a weight matrix**. Everything else (calibration, abstention, routing, audit records) follows from returning a normalized distribution instead of text. Compared with prompting a chat model, the win is not accuracy but *shape of the output*.
- The real product claim is **183 ms and $0.06/1k**. A decision model is not a chatbot competitor; it is the judge/router/scorer layer sitting in the request path of another system (their own Appendix M search router is the best example).
- Pointer vs readout is a clean architectural story: **cache vs context**. Pointer amortizes one state encoding across questions but is causally limited and order-sensitive unless isolated; readout buys bidirectional comparison of options at the price of re-encoding the state per question and *learning* symbol binding. Note the paper never isolates this (backs are different), so "readout is better" is still a confounded observation.
- Calibration is the weak spot in an otherwise strong report: ECE 3.61% aggregate but 7–9% per domain, 8.4% for 6–20 options, and the deployed T=1.009 is nowhere near the 1.35 fitted on Decision Index — i.e. **their own calibration set is not the deployment distribution**. Any threshold-based routing must be re-tuned per workload; the audit record (request + full distribution) is the practical takeaway.
- The option-order result is reassuringly boring: flips ≈ low-confidence decisions, so ordering is not an independent failure mode; abstaining on confidence already captures it. Worth remembering before building "order-robustness" machinery.
- RLAF is best read as **soft-target distillation from (verified label + a CoT judge) with a KL leash**, not as RL in the policy-gradient sense — the pointer variant is literally a deterministic loss on soft targets, and REINFORCE underperformed. The interesting knob is that the judge can outvote the label; that deserves a measured rate, not a caveat.
- Open questions: same-backbone pointer-vs-readout ablation; does a think-then-readout hybrid close the HLE/GPQA gap; is the 27B dense model actually necessary, or does the readout head + non-causal mask do the work at 9B; how does the interface compose with tools (a readout over retrieved evidence, iterated)?
