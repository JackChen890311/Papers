---
title: "Post-LayerNorm Is Back: Stable, Expressive, and Deep"
time: 2601
author: ByteDance Seed
link: https://arxiv.org/pdf/2601.19895
accepted: None
tags:
  - Foundation
  - LLM
  - Text
  - Theory
  - Normalization
todo: false
scanned: true
read: false
summary: A Post-LN Transformer that uses a Highway-style scaled shortcut (α = L) plus an extra LN inside the residual branch, enabling stable training beyond 1000 layers with consistently better depth scaling than Pre-LN.
---
# Summary
💡 Write a brief summary of this paper here
- Depth (not width, not context) is the under-exploited scaling axis; its blocker is optimization instability, not capacity.
- Pre-LN (the modern default) trains stably but suffers *effective depth* loss — gradients mostly flow through the identity path, so deep layers contribute little.
- The authors trace Post-LN's instability to the **ResNet-style residual sum before LayerNorm**, which makes the per-layer LN Jacobian ≈ `O(1/√2)` and the gradient product `O(2^{-L/2})` → exponential vanishing.
- **KEEL** = Post-LN + Highway-style shortcut scaling `α = L` + one extra LayerNorm on the input of `F`. No special init, no residual-scaling tricks. Trains at **>1000 sub-layers**, tolerates 2 orders of magnitude larger LR than vanilla Post-LN, and beats Pre-LN at every depth tested (64→1024) with a fixed 3B-parameter budget.
- Core claim: the Pre-LN/Post-LN dichotomy is decided by **the shortcut branch**, not by the input to `F`.
![[KEEL Fig1 Stability Expressiveness Depth.png]]

# Methodology
💡 Describe the methodology used in this paper
- **Formulation**
  - KEEL layer: `x_{l+1} = LN( α·x_l + F_l( LN(x_l) ) )`, with `α = L` (L = total number of sub-layers, i.e. Attn + FFN counted separately).
  - vs. Post-LN `LN(x_l + F(x_l))` and Pre-LN `x_l + F(LN(x_l))`.
- **Why Post-LN dies (Sec. 3.2)** — with `LN(x) = x/‖x‖₂ ⊙ γ`:
  - Jacobian magnitude through the shortcut: `J* = O( γ_l / (√2 γ_{l-1}) )`; with γ = 1 the product over L layers is `O(2^{-L/2})` → gradients vanish toward the bottom.
  - So the failure is **gradient vanishing**, not forward-magnitude explosion (DeepNorm's premise).
- **Why α fixes it (Sec. 3.3)**
  - With the extra LN and the shortcut scale: `J* = O( γ_{l,1} α / √(γ_{l-1,1}² α² + γ_{l,2}²) )`.
  - With `α = L`: `(α/√(α²+1))^L = (1 + 1/L²)^{-L/2} → 1` as `L → ∞`; gradient norm stays ≈ 1 at any depth.
  - The inner `γ_{l,2}` is cancelled by the previous layer's `γ_{l-1,1}`, which is exactly why the extra LN does **not** attenuate the learning signal for Attn/FFN.
- **Design evolution (Sec. 4.2)**
  - Attempt 1: shortcut scaling `α = L` only → still worse than Pre-LN (unnormalized input to `F` has high variance).
  - Attempt 2: learnable vector `β` scaling the input to `F` → stabilizes forward pass but `β↓` also scales down gradients (attenuation).
  - Attempt 3: `LN` placed *before* the learnable scale → decouples variance control from gradient scale.
  - Final: `β` is absorbed into the inner `LN`'s affine `γ` (redundant parameter) → `LN(α x_l + F(LN(x_l)))`.
- **Why it is still "Post-LN"** (Sec. 3.4)
  - In both Pre-LN and Post-LN the input to `F` is effectively normalized; the real difference is whether the *shortcut* is normalized. KEEL's shortcut carries `LN_{l-1}` output, so it is Post-LN by structure.
  - The two stacked LNs cannot be merged: `γ_{l-1}` is applied between the two normalizations.
- **Implementation details**
  - First attention layer: drop the Post-LN; first Attn & FFN: drop `α` → they degrade to plain Pre-/Post-LN blocks for stable embedding-level init.
  - All LNs keep affine `γ`, drop bias `β` (= 0).
  - Benefits from (and tolerates) a much larger peak LR.
- **Depth-wise Test-Time Training view (Sec. 4.3)**
  - A residual update `x_{l+1} = x_l + G(x_l)W_oᵀ` is isomorphic to a TTT gradient step on `L_depth = -⟨x_l W_o, G(x_l)⟩`, mirroring linear-attention state updates `S_{t+1} = S_t + v_t k_tᵀ`.
  - `α` ↔ gating in Titans/LaCT; the extra residual LN ↔ state normalization. Suggests long-context recurrent tricks and infinite-depth propagation are transferable.
![[KEEL Fig2 Architecture.png]]

# Experiments
💡 List the experiments settings and results of this paper
- **Stability = Maximum Tolerable LR** (η_peak = 5e-2 stress test; divergence = loss stagnation, unrecoverable spike, or silent slow-down). KEEL beats all baselines; vanilla Post-LN is ~30x worse.

| Config | Post-LN | DeepNorm | HybridNorm | Mix-LN | Pre-LN | KEEL |
|---|---|---|---|---|---|---|
| 64L | 3.0e-4 | 3.5e-4 | 4.9e-4 | 8.6e-4 | 7.65e-3 | **1.01e-2** |
| 512L | 2.8e-4 | 3.5e-4 | 3.5e-4 | 3.5e-4 | 4.67e-3 | **6.31e-3** |

- **LR sweep** (512L, d=1024, 250B tokens, η ∈ {1.5, 3, 6}e-3): Pre-LN oscillates/degrade at high LR (ARC-Easy 75.8→74.0, MBPP 25.0→22.8), avg 52.3; KEEL improves monotonically (avg 50.5→55.5; GSM-8K 43.8 vs Pre-LN 38.1).
- **Depth scaling** (64/128/512/1024 layers; 190B pre-train + 60B CPT; batch 1024, seq 4096, AdamW, grad clip 1.0): avg gain over Pre-LN = +1.7 / +1.2 / +3.8 / +3.0; 1024L GSM-8K 58.6 vs 49.8; Pre-LN plateaus between 512L and 1024L on reasoning.
![[KEEL Table3 Depth Scaling.png]]
- **Data scaling** (FineWeb-EDU, 256L, 3B params, 10B vs 40B tokens): avg +1.2 → +1.5; HellaSwag gain grows 0.9 → 2.6. Advantage shrinks in low-data regimes.
- **Deeper vs Wider** (fixed 3B budget, 250B tokens): Deep Pre-LN 52.3 / Wide (128L, d=2048) Pre-LN 52.2 / **Deep 512L KEEL 55.5** — with KEEL, depth finally beats width, especially on reasoning (GSM-8K 43.8 vs 38.1 / 35.3).
- **Main run** (512L, 3B, d=1024, depth:width = 0.5, 1T tokens = 750B PT + 250B CPT, batch 2048, seq 4096; peak LR 4.5e-3 for KEEL vs 3.0e-3 forced for Pre-LN):
  - Pre-training avg **62.5 vs 58.7** (+3.8); GSM-8K 60.9 vs 51.0; AGI-Eval 46.5 vs 37.9; MBPP 40.6 vs 35.0; HumanEval 33.5 vs 29.9.
  - After SFT: avg **54.8 vs 49.3**; MMLU-Pro 35.6 vs 26.6; BBH 51.7 vs 46.4; GSM-8K 68.8 vs 58.7.
- **Caveat the authors flag (App. B)**: training loss and downstream score decouple in deep LLMs — wide/shallow has lower loss but worse benchmarks; so must evaluate tasks, not just PPL.

# Related Papers
💡 Include any related papers that are relevant to this one
- [[ResNet]] — the identity shortcut whose interaction with LN is the diagnosed root cause.
- Highway Networks (Srivastava et al., 2015) — gated carry/transform path that KEEL borrows.
- [[Transformer]] — original Post-LN block; [[Universal Transformers]] — depth-recurrent view.
- Xiong et al., 2020 (*On Layer Normalization in the Transformer Architecture*) — the Pre-LN stability argument KEEL inverts.
- DeepNorm (Wang et al., 2024) — `α = L^0.25` + `L^-0.25` init; KEEL keeps the scaling but drops the init dependency and targets gradients, not output magnitude.
- Admin (Liu et al., 2020), Mix-LN (Li et al., 2024), HybridNorm (Zhuo et al., 2025) — hybrid normalization baselines that KEEL outperforms/departs from.
- "The Curse of Depth in LLMs" (Sun et al., 2025) — effective-depth / layer-redundancy problem KEEL addresses.
- Titans (Behrouz et al., 2024), DeltaNet (Yang et al., 2024), TTT/LaCT (Zhang et al., 2025) — the sequence-side TTT analogy in Sec. 4.3.
- Attention sink (Xiao et al., 2024; Gu et al., 2025) — analog of "first few layers are critical" in depth (App. A).

# Appendix
💡 Anything else that’s in this paper but not mentioned before
- **Layer redundancy (App. A)**: remove-one-layer ΔPPL over C4. First layer is critical (PPL explodes >1e4); redundancy decreases with depth; KEEL has larger ΔPPL in shallow layers → less shallow redundancy and larger *effective* depth. Same pattern reproduced on Qwen2.5-72B-Instruct and LLaMA-3.3-70B.
- **Loss vs downstream mismatch (App. B)**: 256L/d=1024 vs 64L/d=2048 at 250B tokens, and Pre-LN vs KEEL at η=1.5e-3 — lower training loss does not mean better benchmarks.
- **Model config (App. C)**: d=1024 (FFN 3072) or d=2048 (FFN 6144); 16 heads / 8 KV heads; init N(0, 0.02²); no dropout; RMSNorm ε=1e-5; RoPE θ=10000.
- **Limitations**: only depth is studied — width/expert-count scaling may need larger α; gains shrink when width/depth ratio is already high; requires large data (not recommended in low-data regimes).

---
# Resources
💡 Include some useful links for better understanding of this paper
- Paper: https://arxiv.org/abs/2601.19895
- Related: DeepNorm (https://arxiv.org/abs/2203.00555), Mix-LN (https://arxiv.org/abs/2412.13795), HybridNorm (https://arxiv.org/abs/2503.04598)

# Personal Notes
💡 Personal thoughts, reflections, or questions about this paper
- `α = L` (linear in depth) is aggressive — the shortcut dominates the pre-LN sum, so the normalized output is almost a pure function of `x_{l-1}`'s LN, with `F` acting as a small perturbation. It explains both stability and "no vanishing", but raises: does the model actually use the transform branch enough? (They argue the extra LN preserves `∂F` scale.)
- DeepNorm uses `√L`-ish schedules; here the distinction matters — worth re-deriving Eq. 18/19 by hand, and checking whether `α = √L` also works empirically (they claim `α` > 1 is tunable for smaller models).
- All experiments are ≤3B params/1T tokens from an internal corpus; no law-fitting, no MoE, no long-context, no inference cost discussion (extra LN + α are cheap, but depth itself is latency-hostile).
- The Pre-LN baseline's LR was capped at 3.0e-3 while KEEL got 4.5e-3 — part of the +3.8 gain is an LR effect, not pure architecture. A matched-LR comparison is in Table 2 (avg 52.7 vs 55.5 at 3e-3), which is the fairer number.
- Depth-wise TTT framing is elegant and probably the most interesting seed for follow-up (gating/normalization ideas transfer from linear attention to depth).
- Open question: does KEEL compose with other depth tricks (depth recurrence, Universal-Transformer-style weight sharing, mHC/hyper-connections)?
