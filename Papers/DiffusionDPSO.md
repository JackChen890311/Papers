---
title: On-Policy Self-Distillation in Diffusion Models
time: 2608
author: ByteDance Seed
link: https://arxiv.org/pdf/2608.24646
accepted: None
tags:
  - DiffusionModels
  - ReinforcementLearning
  - SelfDistillation
todo: false
scanned: true
read: false
summary: Proposes DiffusionOPSD, an on-policy self-distillation framework that converts image-level reward guidance into explicit intermediate supervision for diffusion model post-training.
---
# Summary
💡 Write a brief summary of this paper here

Introduces DiffusionOPSD, which converts endpoint rewards into bounded positive/negative targets for clean-output predictions at sampled queries, achieving best held-out scores in 19/20 settings while reducing GPU-hours by 40-63% vs DiffusionNFT.

# Methodology
💡 Describe the methodology used in this paper

![[Pasted image 20260827191054.png]]
- **On-Policy Query Collection**: Frozen behavior policy generates trajectories, supplying low-noise query states and clean-output anchors
- **Bounded Target Construction**: Reward gradients create positive/negative targets within controlled radius around anchors
- **Finite Fitting + EMA**: Trainable policy fits detached targets under finite budget, then EMA refreshes behavior policy

# Experiments
💡 List the experiments settings and results of this paper

- **Backbones**: SD 3.5-M, Z-Image-Turbo (step-distilled)
- **Results**: Best final held-out scores in 19/20 reward-matched settings; outperforms strongest competitor by up to 44.0%
- **Efficiency**: 40% fewer GPU-hours on SD 3.5-M, 63% on Z-Image-Turbo vs DiffusionNFT

# Related Papers
💡 Include any related papers that are relevant to this one

- DiffusionNFT, FlowGRPO, ReFL (diffusion RL alignment methods)
- DanceOPD, FlowOPD (two-stage OPD baselines)

# Appendix
💡 Anything else that's in this paper but not mentioned before

- Diagnostics show target construction and finite realization should be evaluated separately
- 62.3% of cases show better-constructed targets don't always produce better finite updates
- CFG-free training outperforms CFG-dependent settings

---
# Resources
💡 Include some useful links for better understanding of this paper

- https://arxiv.org/abs/2608.24646
- https://diffusionopsd.github.io
- https://github.com/worldbench/DiffusionOPSD

# Personal Notes
💡 Personal thoughts, reflections, or questions about this paper
