---
title: "Paint-Anything: Unified Any-Color Control for Image Generation and Editing"
time: 2609
author: ByteDance Seed; Zhejiang University; Nanjing University
link: https://arxiv.org/pdf/2609.20816
accepted: None
tags:
  - Diffusion
  - TextToImage
  - ImageEditing
  - ColorControl
todo: false
scanned: true
read: false
summary: Unified hex-prompt finetuning for any-color (24-bit hex) generation and editing via object-level supervision plus timestep-gated pure-color anchors.
---
# Summary
💡 Write a brief summary of this paper here
![[Pasted image 20260928183220.png]]

![[Pasted image 20260928183505.png]]
- Paint-Anything learns a shared prompt-native hex interface (`<color>#HEX</color>`) for both T2I generation and image editing on FLUX.2 / Z-Image backbones.
- Key idea: object-level hex supervision from real images (Paint-500K) + pure-color anchors gated to high-noise timesteps to ground hex strings to exact RGB.
- Introduces ACBench (ACBench-T2I 1000 prompts + ACBench-Edit 500 prompts) measuring object-region MAE → 0-100 fidelity score.
- On FLUX.2-4B: +85.3% T2I (37.02→68.58) and +28.3% Edit (58.90→75.57); highest CompColor avg among compared methods.

# Methodology
💡 Describe the methodology used in this paper
![[Pasted image 20260928183409.png]]

![[Pasted image 20260928183436.png]]
- Base: rectified-flow DiT (frozen VAE + frozen text encoder, finetune denoiser); editing adds clean source latent concatenation; loss `L = λ_t2i L_t2i + λ_edit L_edit + λ_rgb L_rgb`.
- Explicit wrapping: hex spans written as `<color>#AABBCC</color>` bound to noun phrases / edit instructions (e.g., “a photo of a `<color>#CFEFFB</color>` car”).
- Paint-500K data pipeline: VLM grounding → SAM3 masks → MeanShift clustering in CIELAB → largest cluster as hex label → VLM recaption; 400K T2I (100K single-object crops + 300K multi-object) + 100K editing pairs (pretrained editor synthesizes source, original photo as artifact-free target).
- Pure-color anchors: sampled hex → solid-color image + hex prompt, trained only at `t ∈ [t_gate,1]`, `t_gate=0.8`; real images use `t ∈ (0,1)`; isolates low-level hex→RGB grounding from object semantics.

# Experiments
💡 List the experiments settings and results of this paper
- Setup: finetune FLUX.2-klein-base-4B and Z-Image Base, 4000 steps, 4 GPUs, Adam, batch 72, lr 2e-5; metric: SAM3 mask mean-sRGB MAE vs target hex → score `100*max(0,1-max(0,MAE-16)/48)`; localization failure = 0.
- Main (Table 1): FLUX.2-4B + Ours T2I Single 72.67 / Two 64.49 / Overall 68.58, Edit 75.57; beats 56B FLUX.2-dev (51.70 / 68.87) and specialized ColorWave (46.54) / ColorBind-Edit (60.38); Z-Image + Ours 53.77.
- CompColor: base named 0.72 → hex 0.38 gap; Ours hex 0.79 + named 0.79 (highest avg); also top on GenColorBench NCU + human preference wins (App. A/K).
- Ablations: full FT > LoRA-r256 (68.58 vs 48.45 T2I); wrapping alone 57.16/73.89 vs bare 44.06/65.81; ungated anchors 63.83/70.39; gated (0.8) 68.58/75.57 (+4.75/+5.18); gates 0.7/0.8/0.9 all help, low sensitivity.

# Related Papers
💡 Include any related papers that are relevant to this one
- ColorBind / ColorBind-Edit (CompColor benchmark + compositional binding baseline).
- NumColor (numeric color embeddings; compared via reported NCU, no public ckpt).
- BBQ-to-Image (structured box+RGB prompts); ColorPeel (color prompt learning); ColorWave (training-free guidance); CtrlColor (colorization/editing baseline).
- GenColorBench (NCU numeric-color understanding eval); FLUX.2 / Z-Image / Qwen-Image(-Edit) / SD1.5 / FLUX.1 as base-system baselines.

# Appendix
💡 Anything else that’s in this paper but not mentioned before
- ACBench details: Single (500) / Two (500) / Edit (500); CIELAB/CIEDE2000 variants, reliability, train-eval separation, user study in App. H/L/K.
- CompColor hex-translated protocol: color names → canonical hex, same objects; base collapses, Paint-Anything more than doubles hex avg.
- Limitations: no palette-specific supervision; future: palettes + broader color-control tasks.

---
# Resources
💡 Include some useful links for better understanding of this paper
- arXiv abs: https://arxiv.org/abs/2609.20816 | HTML: https://arxiv.org/html/2609.20816v2 | PDF: https://arxiv.org/pdf/2609.20816
- Backbones: FLUX.2-klein-base-4B, Z-Image Base; Evaluators: SAM3 masks, CompColor, GenColorBench NCU

# Personal Notes
💡 Personal thoughts, reflections, or questions about this paper