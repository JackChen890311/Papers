---
title: "OUTRAGEOUSLY LARGE NEURAL NETWORKS: THE SPARSELY-GATED MIXTURE-OF-EXPERTS LAYER"
time: 1701
author: Google Brain; Jagiellonian University
link: https://arxiv.org/pdf/1701.06538.pdf
accepted: None
tags:
  - Text
  - Foundation
todo: false
scanned: true
read: false
summary: Introduce a huge LSTM based model with soft MoE Layer.
---
# Summary
💡 Write a brief summary of this paper here
Introduce a huge LSTM based [[MoE]] model, with 2048 experts works together.
The output of [[MoE Layer]] will be the weighted sum of top k (k=4, 32, 256) experts. (Soft)

![[Pasted image 20240206155428.png]]
# Methodology
💡 Describe the methodology used in this paper
- Gating Network
	![[Pasted image 20240206160907.png]]
# Experiments
💡 List the experiments settings and results of this paper

# Related Papers
💡 Include any related papers that are relevant to this one

# Appendix
💡 Anything else that’s in this paper but not mentioned before

---
# Resources
💡 Include some useful links for better understanding of this paper

# Personal Notes
💡 Personal thoughts, reflections, or questions about this paper