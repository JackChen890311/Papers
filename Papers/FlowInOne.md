---
title: "FLOWINONE: UNIFYING MULTIMODAL GENERATION AS IMAGE-IN, IMAGE-OUT FLOW MATCHING"
time: 2604
author: University of Electronic Science and Technology of China; National University of Singapore; Central South University; Microsoft; University of Science and Technology of China
link: https://arxiv.org/pdf/2604.06757
accepted: ECCV 2026
tags:
  - FlowMatching
  - MultimodalGeneration
  - ImageInImageOut
  - VisualPrompt
  - GenerativeModel
todo: false
scanned: true
read: false
summary:
---
# Summary
💡 Write a brief summary of this paper here
- FlowInOne reformulates multimodal generation as a purely visual image-in, image-out flow matching pipeline: text, layouts, and editing instructions are rendered into visual prompts, and a single flow model transports them into target images, eliminating text encoders and cross-modal bottlenecks.

# Methodology
💡 Describe the methodology used in this paper
- Core idea: unify all modalities (text, layout, instructions) into a single visual representation by rendering them onto an input canvas, then learn a continuous flow from source latent to target image latent in a shared VAE latent space.
- Unified text processing: render textual instructions onto image canvas; encode with Janus-Pro-1B SigLIP ViT + MLP projector into patch features; map to source latent via a text-image VAE (samples from posterior).
- Target images encoded by frozen LDM VAE into isomorphic latent; flow matching trains velocity field with MSE between interpolated latents.
- Dual-Path Spatially-Adaptive Modulation: for T2I (no source image), bypass cross-attention; for editing, cross-attention with source image latent plus token-level gating (Λ) to balance preservation vs. reconstruction.
- Joint training on VisPrompt-5M (5M pairs) for 240k steps, 256×256, 1.2B model based on CrossFlow.

# Experiments
💡 List the experiments settings and results of this paper
- Setup: VP-Bench with 8 task categories (C2I, T2I, TIE, FU, TBE, TU, VME, DE); evaluated by Gemini3, GPT5.2, Qwen3.5 and human; metrics CLIP-IQA, CLIP Score, Directional CLIP, DINOv3 Sim.
- Baselines: OmniGen2, FLUX.1-Kontext-dev, Qwen-Image-Edit-2509, Nano Banana (commercial).
- Results: FlowInOne best among open-source across evaluators (total pass: 54.0% Gemini3, 39.2% GPT5.2, 50.3% Qwen3.5, 44.9% human); competitive with Nano Banana; best spatial precision (3.42/3.24/3.30) and DINOv3 Sim (48.7%).
- Ablations: MLP+MLP compression best; Dual-Path SAM > cross-attention > none; joint training (47.8%) >> two-stage (29.1%).

# Related Papers
💡 Include any related papers that are relevant to this one
- CrossFlow: flowing from words to pixels (noise-free cross-modality evolution)
- Janus-Pro: unified multimodal understanding and generation
- FLUX.1 Kontext: flow matching for in-context image generation/editing
- OmniGen2: advanced multimodal generation
- Qwen-Image-Edit: text-guided image editing
- InstructPix2Pix, GLIGEN, ControlNet (conditional image generation/editing)

# Appendix
💡 Anything else that’s in this paper but not mentioned before
- VisPrompt-5M: 5M visual prompt pairs across 8 task types (class-to-image, T2I, text-in-image editing, bbox editing, visual marker editing, doodles, force, trajectory).
- VP-Bench leakage prevention and data analysis; limitations and future work in Appendix E.
- Model details: 1.2B params, trained at 256×256, 240k steps, balanced WebDataset, combined FM + KL + CLIP loss.

---
# Resources
💡 Include some useful links for better understanding of this paper
- Paper: https://arxiv.org/abs/2604.06757
- Project page: https://csu-jpg.github.io/FlowInOne.github.io/
- PDF: https://arxiv.org/pdf/2604.06757

# Personal Notes
💡 Personal thoughts, reflections, or questions about this paper
- Vision-centric paradigm is elegant; rendering instructions as images removes cross-modal alignment. Questions: scalability to higher resolution, handling long text, and how it compares to native multimodal LLMs.