---
title: Memory Attention
time: 2609
author: Jiale Kang
link: https://arxiv.org/pdf/2609.28399
accepted: None
tags:
  - AttentionMechanism
  - EfficientInference
  - LargeLanguageModels
  - MemoryAugmented
todo: false
scanned: true
read: false
summary: Replaces the value projection with layer-specific token memory added to contextual keys, improving LM and downstream averages with CPU-offloadable tables.
---
# Summary
💡 Write a brief summary of this paper here
- Proposes Memory Attention (MA): V = K + Norm(M), where M is layer-specific token-indexed memory retrieved by token ID, replacing the dedicated W_V projection while keeping standard attention weighting/aggregation.
- Keys supply context-dependent content, memory supplies token-specific content; RMSNorm folded into tables at inference so value construction is lookup + addition.
- Adds MA-Offload (CPU store + prefetch, lower GPU param storage) and analyzes MA-Recall (reconstruct V from K + token IDs to halve KV-cache).
- Under matched token budgets with extra memory params: better perplexity + avg downstream accuracy across MHA/GQA/MQA/Gated, better NIAH retrieval in-window and at 2x length.
![[Pasted image 20260930142733.png]]
# Methodology
💡 Describe the methodology used in this paper
- **Memory-based values:** per-layer table E in R^(N x dv); M = RMSNorm(E[s]) per KV-head; Q=X W_Q, K=X W_K, V=K+M; with RoPE: Q^R, K^R for scores, V from pre-RoPE K.
- **MLA connection:** both reuse shared representation for scoring + aggregation; MLA does (A Z) W_V, MA does A(Z+M)=A Z + A M — direct key reuse + additive memory read, not equivalent reformulation.
- **Cost:** replaces L d dv params with L(N dv + p_norm); training ~O(L S dv) vs 6 L S d dv; inference folds Norm into E_bar, online cost L S dv vs 2 L S d dv.
- **MA-Offload:** stores folded tables on CPU/SSD; addresses depend only on token+layer IDs so prefetch + overlap with compute; decode payload bw L B dv per step with KV-cache.
- **MA-Recall (analysis only, not measured):** V_1:T = K_1:T + E_bar[s_1:T]; retain one key repr. → 50% cache saving (2 bc L B T dv → bc L B T dv), cost L B R dv adds + transfer D_Recall.

# Experiments
💡 List the experiments settings and results of this paper
![[Pasted image 20260930143343.png]]

![[Pasted image 20260930143417.png]]

![[Pasted image 20260930143429.png]]
- **Setup:** H800 + flash-linear-attention; 24-layer + gated MLP + RoPE + RMSNorm; FineWeb-10BT; 10B tokens (D1024, 0.5M/batch) and 20B tokens (D2048, 1M/batch); zero-shot via lm-eval-harness (LAMBADA/WikiText PPL, ARC-E/C, HellaSwag, PIQA, WinoGrande, OBQA).
- **LM + downstream (Table 2):** MA wins both PPLs + avg accuracy in all pairs — e.g. small MHA Wiki 31.55→28.64, avg 40.68→41.39; GQA Lamb 50.46→43.68, avg 40.90→41.51; large MHA 49.06→50.22 (+3.0 OBQA, +2.65 ARC-C, slight drop ARC-E/PIQA); gains confound structure + extra params.
- **Retrieval NIAH 2K ctx (Table 3):** MA > Standard all 9 cols; 1K mean 97.4% vs 82.6%, 2K 96.8% vs 82.1% (single_3 1K 62.4%→98.2%); 4K extrap mean 41.9% vs 25.9% but both degrade.
- **Efficiency:** token efficiency 1.42x (L24-D1024) / 1.16x (L24-D2048) to matched loss (~29.6%/13.8% fewer tokens, not wall-clock); H800 BF16 B8 L2048: prefill 90.97→88.20ms (-3.04%), decode 17.64→17.79ms (+0.86%) despite 2.08x params; MA-Offload 90.69/17.19ms, GPU params 5410→2410 MiB (-55.45%), 192 MiB less than Standard.

# Related Papers
💡 Include any related papers that are relevant to this one
- Vaswani et al. 2017 Attention Is All You Need (standard QKV attention MA modifies)
- Value Embeddings (KoszarskyB 2024) / DeepEmbed (BoPeng 2025) — supplement V with token embeddings, retain W_V, vs MA replaces it
- Per-Layer Embeddings (Gemma 3n, 2025) — per-layer token tables + gated injection
- STEM (Sadhukhan et al. 2026) / Engram (Cheng et al. 2026, n-gram lookup + prefetchable memory)
- MLA / GQA / MQA — shared-KV and latent-compression attention configs MA is tested on

# Appendix
💡 Anything else that’s in this paper but not mentioned before
- **Pretraining:** FineWeb-10BT, 20480 steps x 2048 len x 256 seqs; AdamW lr 3e-4, eps 1e-15, warmup 1024, cosine to 10%, clip 1.0, seed 42; matched budgets/seeds per pair.
- **Backbones:** D1024: MHA 16/16x64, GQA 16/8x64, MQA 4/1x256; D2048 large MHA 32/32; RoPE base 10000, RMSNorm eps 1e-6, untied embeddings.
- **Caveats stated:** gains include extra capacity, not structure-isolated; latency is forward-pass only (excl. sampling, table-init, token-ID transfer); storage excl. KV-cache/activations/buffers; prototype overlap, small timing deltas not general speedup claim.

---
# Resources
💡 Include some useful links for better understanding of this paper
- https://arxiv.org/abs/2609.28399 (arXiv abs, v1 23 Sep 2026)
- https://arxiv.org/html/2609.28399v1 (HTML full text)
- https://github.com/Joluck/memory-attention (official code)

# Personal Notes
💡 Personal thoughts, reflections, or questions about this paper
- 小料非大料：`V=K+M` 砍 `W_V` 的減法思路乾淨，offload 自洽且有 code，但增益混雜 2-3x 參數，未做 param-matched 對照。
- 效率數字約等於 noise（prefill -3%, decode +0.8%），NIAH 暴漲（62%→98%）待復現；MA-Recall 未實測。
- 定位：留作 attention variant / KV-cache / offload 的 related work，待後續版本再細讀。