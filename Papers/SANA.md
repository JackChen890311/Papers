---
title: "SANA: EFFICIENT HIGH-RESOLUTION IMAGE SYNTHESIS WITH LINEAR DIFFUSION TRANSFORMERS"
time: 2410
author: NVIDIA; MIT; Tsinghua University
link: https://arxiv.org/pdf/2410.10629
accepted: None
tags:
  - Diffusion
  - Foundation
  - Generation
  - Image
todo: false
scanned: true
read: false
summary: A efficient T2I model that applies different techniques.
---
# Summary
💡 Write a brief summary of this paper here
![[Pasted image 20250103174608.png]]
![[Pasted image 20250103174629.png]]
# Methodology
💡 Describe the methodology used in this paper
(1) [[DC-AE]]: unlike traditional AEs, which compress images only 8×, we trained an AE that can compress images 32×, effectively reducing the number of latent tokens.  
(2) **Linear DiT**: we replace all vanilla attention in DiT with linear attention, which is more efficient at high resolutions without sacrificing quality.  
(3) **Decoder-only text encoder**: we replaced T5 with modern decoder-only small LLM as the text encoder and designed complex human instruction with in-context learning to enhance the image-text alignment.  
(4) **Efficient training and sampling**: we propose **Flow-DPM-Solver** to reduce sampling steps, with efficient caption labeling and selection to accelerate convergence.
![[Pasted image 20250103174644.png]]
# Experiments
💡 List the experiments settings and results of this paper

# Related Papers
💡 Include any related papers that are relevant to this one

# Appendix
💡 Anything else that’s in this paper but not metioned before

---
# Resources
💡 Include some useful links for better understanding of this paper
- [Sana Playground](https://nv-sana.mit.edu/)
- [Github Repo](https://github.com/NVlabs/Sana)
- [HuggingFace](https://huggingface.co/collections/Efficient-Large-Model/sana-673efba2a57ed99843f11f9e)
# Personal Notes
💡 Personal thoughts, reflections, or questions about this paper