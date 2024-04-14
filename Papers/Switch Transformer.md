---
title: "Switch Transformers: Scaling to Trillion Parameter Models with Simple and Efficient Sparsity"
time: 2101
author: Google
link: https://arxiv.org/pdf/2101.03961.pdf
accepted: JMLR22
tags:
  - Text
todo: false
scanned: true
read: false
summary: A transformer with switch FFN layer which works as hard MoE Layer.
---
# Summary
💡 Write a brief summary of this paper here
[[Switch Transformer]] is a improved model from the paper [[MoE Layer]].
Appends switching FFN layer after self-attention layer from [[Transformer]].
Instead of top-k gating used in [[MoE Layer]], the author thinks it's beneficial to set k=1. (Hard)

![[Pasted image 20240206142229.png]]
# Methodology
💡 Describe the methodology used in this paper

# Experiments
💡 List the experiments settings and results of this paper

# Related Papers
💡 Include any related papers that are relevant to this one

# Appendix
💡 Anything else that’s in this paper but not metioned before
![[Pasted image 20240206170400.png]]
![[Pasted image 20240206170417.png]]

---
# Resources
💡 Include some useful links for better understanding of this paper

# Personal Notes
💡 Personal thoughts, reflections, or questions about this paper