---
title: Visual Instruction Tuning
time: 2304
author: University of Wisconsin–Madison; Microsoft Research; Columbia University
link: https://arxiv.org/pdf/2304.08485
accepted: NeurIPS23
tags:
  - Foundation
  - Image
  - LLM
  - Multimodal
  - Text
  - QuestionAnswering
todo: false
scanned: true
read: false
summary: A multimodal network connected CLIP and Vicuna using 2-layer MLP.
---
# Summary
💡 Write a brief summary of this paper here
- Proposed a multimodal language-image instruction-following dataset
- Connected off-the-shelf language/vision models with a projection layer
![[Pasted image 20240523154236.png]]
# Methodology
💡 Describe the methodology used in this paper
LLaVa connects pre-trained [CLIP ViT-L/14](https://openai.com/research/clip) (see more at [[CLIP]]) visual encoder and large language model [Vicuna](https://github.com/lm-sys/FastChat), using a simple projection matrix. 

A two-stage instruction-tuning procedure is employed:
- **Stage 1: Pre-training for Feature Alignment**. Only the projection matrix is updated, based on a subset of CC3M.
- **Stage 2: Fine-tuning End-to-End**. Both the projection matrix and LLM are updated for two different use senarios:
    - **Visual Chat**: LLaVA is fine-tuned on our generated multimodal instruction-following data for daily user-oriented applications.
    - **Science QA**: LLaVA is fine-tuned on this multimodal reasonsing dataset for the science domain.

# Experiments
💡 List the experiments settings and results of this paper
- Proposed a multimodal dataset: LLaVa-Bench (COCO, In-the-Wild)
![[Pasted image 20240523155205.png]]
- ScienceQA
![[Pasted image 20240523155240.png]]
# Related Papers
💡 Include any related papers that are relevant to this one

# Appendix
💡 Anything else that’s in this paper but not mentioned before

---
# Resources
💡 Include some useful links for better understanding of this paper
- [Demo Page](https://llava-vl.github.io/)
# Personal Notes
💡 Personal thoughts, reflections, or questions about this paper