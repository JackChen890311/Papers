---
title: "Visual Generation in the New Era: An Evolution from Atomic Mapping to Agentic World Modeling"
time: 2604
author: Tsinghua University; Nanyang Technological University; University of Hong Kong; National University of Singapore; University of Waterloo; StepFun; MiroMind; Baidu; Fudan University; Hong Kong University of Science and Technology; Hong Kong University of Science and Technology (Guangzhou); LMMs-Lab
link: https://arxiv.org/pdf/2604.28185
accepted: None
tags:
  - VisualGeneration
  - Survey
  - WorldModeling
  - AgenticGeneration
  - Diffusion
todo: false
scanned: true
read: false
summary: A capability-centered roadmap proposing a five-level taxonomy (Atomic → Conditional → In-Context → Agentic → World-Modeling) for visual generation, reviewing modeling foundations, training, data/infrastructure, applications, and stress tests showing current models remain strong at plausibility but fragile at structure, state, and causality.
---
# Summary
💡 Write a brief summary of this paper here
- A capability-centered roadmap arguing visual generation is evolving from appearance synthesis toward intelligent visual generation, proposing a five-level taxonomy (Atomic → Conditional → In-Context → Agentic → World-Modeling) and showing current models are strong at plausibility but fragile at structure, state, and causality.

# The Big Picture
💡 List the overall summarization or comparison in this paper
- Five-level taxonomy of visual intelligence as nested capability expansion: L1 Atomic (one-shot text→image), L2 Conditional (single explicit condition), L3 In-Context (rich context in one forward pass), L4 Agentic (control loop with plan/verify/tools), L5 World-Modeling (causal simulation).
- Key technical drivers: flow matching, unified understanding-and-generation models, improved visual representations (VAE/VQ/tokenizer-free), post-training (SFT/RL/GRPO/reward models), data curation, synthetic distillation, sampling acceleration.
- Current evals overestimate progress by emphasizing perceptual quality; in-the-wild stress tests expose spatial, physical, identity, and causal failures.
- Applications progress from conditional generation/domain adaptation to reasoning-driven editing and embodied prediction, demanding structure, memory, state tracking, closed-loop control.
- Frontiers: vCoT, closed-loop agents, tool-augmented rendering, synthetic self-play, world simulation (neural game engines), data-centric visual intelligence, structural/correctness-focused evaluation.

# The Details
💡 Describe the details of each section or comparison
- §1 Introduction: paradigm shift from static rendering to world simulation; frontier (Nano Banana/GPT-Image) gains in prompt comprehension, typography, editing coexist with blind spots (spatial, state, identity, physics); conventional metrics insufficient.
- §2 Evolution: L1 (DDPM/DiT/LDM/AR) uncontrolled variation; L2 (ControlNet/IP-Adapter/GLIGEN/SD3) spatial precision & attribute binding; L3 (SEED-Data-Edit/ImgEdit/StoryMaker) coherence under cumulative context & drift; L4 (GEMS/JarvisArt/CoT-VLA) grounded verification under intervention; L5 (Genie 2/GameNGen/Oasis/UniSim/GAIA-1) causal simulation.
- §3 Method: paradigms (GAN, diffusion/flow matching, AR, hybrid AR+diffusion); architecture (encoders/tokenizers VAE/VQ/tokenizer-free; U-Net→Transformer/MoE backbones; condition modules & fusion late/early/hybrid); closed-source frontier speculation (VLM upstream, dual-path encoder, generation-time understanding, external agent loop).
- §4 Training: pre-training (waterfall filtering, active curation, synthetic captioning/VLM CoT, systems engineering, staged curriculum); post-training (SFT mode-seeking trade-off, RL: DDPO/DPOK/AlignProp/Diffusion-DPO/GRPO/credit assignment/reward models); inference acceleration (sampling solvers/distillation, pruning, feature caching).
- §5 Resources: data construction (web→synthetic engines, source acquisition, instruction construction, generation/editing, QC, scale/quality/efficiency); evaluation (VLM-as-judge, instruction following, identity, spatial reasoning, world knowledge/physics, text rendering, visual quality, holistic/domain benchmarks, arena-based human preference); infrastructure (sequence parallelism, RL memory wall, serving, open-source ecosystem).
- §6 Applications: conditional image generation, custom domain adaptation, conditional editing, embodied (data generation/augmentation, visual prediction for interaction).
- §7 Stress tests: spatial (jigsaw, metro map, isometric tile); physical/causal (fluid buoyancy, action-conditioned navigation, robotic manipulation, spatiotemporal trajectory, video re-rendering, irreversible state transitions) — models prioritize semantic plausibility over causal/physical logic.
- §8 Frontiers: vCoT, closed-loop agents, tool-augmented rendering, synthetic data/self-play, world simulation challenges (long-horizon consistency, physical plausibility, real-time, compositional generalization), data-centric, evaluation of structural correctness.
- §9 Conclusion: path from atomic mapping to playable world models is a shift from image synthesis to verifiable visual reasoning.

# Related Papers
💡 Include any related papers that are relevant to this one
- Rombach et al. (2022) High-Resolution Image Synthesis with Latent Diffusion Models (Stable Diffusion)
- Esser et al. (2024) Scaling Rectified Flow Transformers for High-Resolution Image Synthesis (SD3)
- Zhang et al. (2023) Adding Conditional Control to Text-to-Image Diffusion Models (ControlNet)
- Ye et al. (2023) IP-Adapter: Text Compatible Image Prompt Adapter
- Bruce et al. (2024) Genie: Generative Interactive Environments
- Valevski et al. (2024) Diffusion Models Are Real-Time Game Engines (GameNGen)
- Parker-Holder et al. (2024) Genie 2: A Large-Scale Foundation World Model
- Ha & Schmidhuber (2018) World Models
- LeCun (2022) A Path Towards Autonomous Machine Intelligence (JEPA)
- Wallace et al. (2024) Diffusion Model Alignment Using Direct Preference Optimization (Diffusion-DPO)

# Appendix
💡 Anything else that’s in this paper but not mentioned before
- Preprint (arXiv 2604.28185, v2 revised 14 Jun 2026); 411 post-2014 references; 2025 alone 188 papers (45.7%).
- Project page: https://github.com/EvolvingLMMs-Lab/Evolving-Visual-Generation
- Declared as evolving roadmap; manuscript may be corrected/updated.
- Includes stress-test case studies with Nano Banana outputs as embedded probes.

## Key Figures

![Figure 3: Five-level taxonomy overview](https://arxiv.org/html/2604.28185v2/img/level/fig_5levels_overview.jpg)

![Figure 7: Unified architecture for visual generation and editing](https://arxiv.org/html/2604.28185v2/img/method/fig_unified_architecture.jpg)

![Figure 10: Three-stage training and inference pipeline](https://arxiv.org/html/2604.28185v2/fig_training_pipeline.png)

---
# Resources
💡 Include some useful links for better understanding of this paper
- Paper: https://arxiv.org/abs/2604.28185
- PDF: https://arxiv.org/pdf/2604.28185
- HTML: https://arxiv.org/html/2604.28185v2
- Project page: https://github.com/EvolvingLMMs-Lab/Evolving-Visual-Generation
- Awesome list: https://github.com/EvolvingLMMs-Lab/Awesome-New-Era-Visual-Gen

# Personal Notes
💡 Personal thoughts, reflections, or questions about this paper