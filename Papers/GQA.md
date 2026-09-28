---
title: "GQA: Training Generalized Multi-Query Transformer Models from Multi-Head Checkpoints"
time: 2305
author: Google Research
link: https://arxiv.org/pdf/2305.13245
accepted: EMNLP23
tags:
  - AttentionMechanism
  - EfficientInference
  - LargeLanguageModels
todo: false
scanned: true
read: false
summary: Introduces Grouped-Query Attention (GQA) interpolating MHA and MQA to retain near-MHA quality at near-MQA inference speed.
---
# Summary
💡 Write a brief summary of this paper here
- Proposes methods for uptraining MHA checkpoints into MQA with ~5% extra pretraining 
- Introduces Grouped-Query Attention (GQA) interpolating MHA and MQA to retain near-MHA quality at near-MQA inference speed.
![[Pasted image 20260928162630.png]]

![[Pasted image 20260928162543.png]]

# Methodology
💡 Describe the methodology used in this paper
- **Uptraining MHA→MQA:** mean-pool K/V projection matrices from all H heads into single head, then continue pretraining for α fraction (α=0.05) with original recipe.
- **Conversion ablation:** mean-pooling > selecting first head > random init (ordered by information preservation).
- **Grouped-Query Attention (GQA-G):** divide H query heads into G groups, each group shares one K/V head via mean-pooling within group; GQA-1 = MQA, GQA-H = MHA.
- Applied only to decoder self- and cross-attention (not encoder self-attention, which is compute-parallel, not bandwidth-bound).
- Motivation: KV-cache bandwidth bottleneck; MQA cuts cache by H× but too aggressive for large models; GQA keeps proportional cut, avoids waste from sharding single KV head across partitions.

# Experiments
💡 List the experiments settings and results of this paper
- **Setup:** T5.1.1 Large/XXL in JAX/Flax/Flaxformer, Adafactor; uptrain from public checkpoints (α=0.05 ≈ 600 TPUv3 chip-days); eval summarization (CNN/DM, arXiv, PubMed, MediaSum, Multi-News), WMT14 En-De, TriviaQA; finetune lr 0.001, batch 128, greedy decoding; timing as ms/sample/TPUv4 chip via xprof.
- **Main (Table 1 / Fig 3):** XXL MQA (0.24s, avg 46.6) faster + better than MHA-Large (0.37s, 46.0); GQA-8-XXL (0.28s, avg 47.1) ≈ MHA-XXL quality (1.51s, 47.2) at MQA-like speed.
- **Ablations:** GQA usable zero-shot after conversion, MQA needs uptraining; both gain to 5% with diminishing returns to 10%; 1→8 groups adds modest overhead, cost grows toward MHA — 8 chosen as sweet spot.

# Related Papers
💡 Include any related papers that are relevant to this one
- Shazeer 2019 Fast Transformer Decoding: One Write-Head Is All You Need (original MQA)
- Pope et al. 2022 Efficiently Scaling Transformer Inference; de Jong et al. 2022 FiDO (MQA for long inputs)
- Komatsuzaki et al. 2022 Sparse Upcycling (inspiration for uptraining dense→MoE)
- Rabe 2023 Memory-efficient attention (independent GQA implementation in Flaxformer)
- Dao et al. 2022 FlashAttention; Dettmers et al. 2022 LLM.int8(), Frantar et al. 2022 GPTQ; Chen et al. 2023 / Leviathan et al. 2022 speculative sampling (alternative inference speedups)

# Appendix
💡 Anything else that’s in this paper but not mentioned before
- **Training stability:** MQA from scratch shows loss spikes + divergence on long-input finetuning; uptrained MQA more stable but high variance (averaged over 3 runs); uptrained GQA appears stable.
- **Limitations:** Rouge-based summarization eval is flawed; no XXL-from-scratch GQA baseline; encoder-decoder only (authors expect stronger GQA advantage for decoder-only models).

---
# Resources
💡 Include some useful links for better understanding of this paper
- https://arxiv.org/abs/2305.13245 (arXiv, v3 Dec 2023)
- https://arxiv.org/html/2305.13245v3 (HTML full text)
- https://aclanthology.org/2023.emnlp-main.298/ (EMNLP 2023)
- https://github.com/google/flaxformer (Flaxformer + memory_efficient_attention.py GQA impl)
- [理解Attention:从起源到MHA,MQA和GQA](https://zhuanlan.zhihu.com/p/686149289)

# Personal Notes
💡 Personal thoughts, reflections, or questions about this paper