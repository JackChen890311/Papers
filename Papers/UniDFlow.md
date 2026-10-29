---
title: "Best of Both Worlds: Multimodal Reasoning and Generation via Unified Discrete Flow Matching"
time: 2606
author: University of Illinois Urbana-Champaign; Sony Research, India; Google Research; Indian Institute of Technology, Roorkee; University of Texas at Austin
link: https://arxiv.org/pdf/2602.12221
accepted: None
tags:
  - UnifiedMultimodal
  - DiscreteFlowMatching
  - ImageGeneration
  - ImageEditing
  - PreferenceAlignment
  - VLM
todo: false
scanned: true
read: false
summary:
---
# Summary
💡 Write a brief summary of this paper here
- UniDFlow is a unified discrete flow-matching model that repurposes a pretrained VLM backbone for multimodal understanding, text-to-image generation, and instruction-guided editing within one probabilistic interface, achieving SOTA across eight benchmarks.

# Methodology
💡 Describe the methodology used in this paper
- Three-stage training on a frozen pretrained VLM (Qwen3-VL) with task-specific LoRA adapters:
  - Stage I (Text Alignment): diffusion-based multimodal understanding via DFM, with KL regularization against AR answer distribution; trains LoRA_text.
  - Stage II (Vision Alignment): conditional visual token generation; trains LoRA_img while keeping understanding adapters frozen.
  - Stage III (Reference-Based Multimodal Preference Alignment): mRef-DPO aligns text/vision/reflection against a frozen reference; trains a lightweight MoRA router composing adapters.
- Time-Step Guided RMSNorm (TSG-RMSNorm): injects diffusion time by modulating RMSNorm scale params (zero-initialized) instead of activations, preserving pretrained priors.
- Single discrete flow-matching objective for all tasks; 20 denoising steps at inference.
- Images tokenized via PyraTok (text-guided multi-scale quantization); bidirectional self-attention for full-context denoising.
- mRef-DPO optimizes pairwise log-likelihood margin between preferred/rejected outcomes under identical conditioning, anchored to frozen reference.

# Experiments
💡 List the experiments settings and results of this paper
- Setup: Stage I on MMInstruct (~1.0M, 0.6T tokens); Stage II on Text-to-Image-4M refined (4.5M, 1.2T tokens); Stage III on 3.5M preference samples (1.8T tokens). Trained on A100/H100 GPUs; BF16.
- Understanding (EvalVLM, 4B): MME-P 1803, MME-S 2555, MMBench 91.2, MMMU 74.3, MM-Vet 82.7, MathVista 85.9, MMVP 80.2; OCRBenchV2 avg 58.4 (4B) / 63.8 (14B).
- Generation: GenEval 0.95, DPGBench 91.19 (4B), surpassing Qwen-Image (7B+20B) and EMMA.
- Editing (ImgEdit/Emu-Edit/GEdit): overall ImgEdit 4.24; Emu-Edit CLIP-I 0.921, CLIP-Out 0.362, DINO 0.862; GEdit SC 8.01, PQ 7.82, Overall 7.12.
- Ablations: separate LoRA adapters + MoRA router critical; removing mRef-DPO degrades performance; TSG-RMSNorm outperforms AdLN/in-context conditioning; reflection improves editing metrics.
- Zero-shot generalization: inpainting, in-context generation, reference-based editing, compositional generation.

# Related Papers
💡 Include any related papers that are relevant to this one
- Gat et al. (2024) Discrete Flow Matching — core objective.
- Deng et al. (2025) BAGEL — unified AR+diffusion baseline.
- Shi et al. (2025) MUDDIT — unified discrete diffusion baseline.
- Shen et al. (2025) MammothModa2 — AR-diffusion with scalar-reward RL.
- He et al. (2025) EMMA — unified understanding/generation/editing.
- Wu et al. (2025b) OmniGenV2 — multimodal reflection.
- Rafailov et al. (2023) DPO; Wallace et al. (2024) Diffusion-DPO — preference alignment baselines.
- Susladkar et al. (2026) PyraTok — visual tokenizer used.

# Appendix
💡 Anything else that’s in this paper but not mentioned before
- Impact: misuse risks for deceptive media; biases may propagate; alignment depends on preference data diversity.
- Efficiency: UniDFlow-4B competitive with larger models; 14B attains highest throughput among compared ~14B models.
- Training data: MMInstruct (Stage I), LAION-5B/JourneyDB/text-to-image-2M (Stage II), OpenGPT-4o-Image/AnyEdit/Pico-Banana (Stage III).
- Visual tokenizer comparison: PyraTok outperforms 3D-MBQ-VAE, MAGVIT-v2, SweetTok.
- Full GenEval/DPGBench breakdowns and qualitative figures in appendices.

---
# Resources
💡 Include some useful links for better understanding of this paper
- Paper: https://arxiv.org/abs/2602.12221
- PDF: https://arxiv.org/pdf/2602.12221
- Project page: https://plan-lab.github.io/unidflow

# Personal Notes
💡 Personal thoughts, reflections, or questions about this paper