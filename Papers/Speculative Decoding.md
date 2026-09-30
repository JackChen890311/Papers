---
title: Fast Inference from Transformers via Speculative Decoding
time: 2211
author: Google Research
link: https://arxiv.org/pdf/2211.17192
accepted: ICML 2023
tags:
  - SpeculativeDecoding
  - InferenceAcceleration
  - Transformers
todo: false
scanned: true
read: false
summary:
---
# Summary
💡 Write a brief summary of this paper here
- Proposes speculative decoding to accelerate autoregressive Transformer inference 2-3X with identical output distribution, by drafting γ tokens with a small efficient model and verifying them in parallel with the large target model via novel speculative sampling.

# Methodology
💡 Describe the methodology used in this paper
- Draft-then-verify: approximation model Mq autoregressively generates γ guesses, target model Mp evaluates p1..pγ+1 in parallel
- Speculative sampling: accept xi if q(xi) ≤ p(xi), else reject w.p. 1-p/q and resample from norm(max(0,p-q)); guarantees x ~ p
- Standardized sampling: casts argmax / top-k / nucleus / temperature into sampling from adjusted distribution
- Analysis: α = E[β] = E[min(p,q)] = 1-E[D_LK]; E[#tokens] = (1-α^{γ+1})/(1-α); speedup = (1-α^{γ+1})/((1-α)(γc+1))
- Draft choices: 100X smaller Transformer best balances α vs c; negligible-cost n-gram / copy heuristics, non-autoregressive or random drafts also valid

# Experiments
💡 List the experiments settings and results of this paper
- Setup: T5-XXL 11B target on WMT EnDe translation and CNN/DM summarization, drafts T5-small (77M) / base (250M) / large (800M), TPU-v4 bs=1, temp=0/1; α also measured for GPT-like 97M on lm1b and LaMDA 137B dialog on 10K tokens
- Main results: EnDe 3.4X (temp0, small, γ7, α0.75) and 2.6X (temp1, α0.62); CNN/DM 3.1X (temp0, α0.65) and 2.3X (temp1, α0.53); T5-small gives best speedup vs larger drafts
- Key ablations: α rises with draft size and with argmax vs sampling; GPT-like 6M draft α0.88-0.89; LaMDA 100M/2B/8B α0.61/0.71/0.75 (t0); bigram draft α~0.2 on EnDe → 1.25X with c≈0; empirical walltime matches theory

# Related Papers
💡 Include any related papers that are relevant to this one
- Stern et al. 2018 Blockwise Parallel Decoding: parallel decoding but greedy-only, needs retraining, no distribution guarantee
- Sun et al. 2021 Shallow Aggressive Decoding: copy-input heuristic only, for GEC-like tasks
- Chen et al. 2023 Accelerating LLM Decoding with Speculative Sampling: concurrent independent work, 2-2.5X on Chinchilla 70B
- Adaptive computation / early-exit / Wisdom of Committees, distillation / quantization / sparsification: save compute but require arch/training change and alter outputs

# Appendix
💡 Anything else that’s in this paper but not mentioned before
- A.1 proof of speculative sampling correctness; A.2 difference vs standard rejection sampling
- A.4 beam-search extension, A.5 lenience (trade distribution fidelity for speed)
- Limitation: improves latency via concurrency at cost of extra FLOPs; ideal when memory-bandwidth bound; total ops increase (1-α)(γĉ+γ+1)/(1-α^{γ+1})
- Future: oracle-adaptive γ (+~60%), hierarchical drafts, custom-distilled drafts optimizing α directly

---
# Resources
💡 Include some useful links for better understanding of this paper
- https://arxiv.org/abs/2211.17192
- https://proceedings.mlr.press/v202/leviathan23a.html
- https://research.google/blog/looking-back-at-speculative-decoding/

# Personal Notes
💡 Personal thoughts, reflections, or questions about this paper