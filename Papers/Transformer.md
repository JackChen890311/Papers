---
title: Attention Is All You Need
time: 1706
author: Google Brain; Google Research; University of Toronto
link: https://arxiv.org/pdf/1706.03762.pdf
accepted: NIPS17
tags:
  - Text
  - Theory
  - Foundation
todo: false
scanned: true
read: false
summary: A structure that attends the data itself to gain a better understanding.
---
# Summary
💡 Write a brief summary of this paper here
The most famous self-attention & cross-attention (q and k, v are from different sources)
Also proposed the idea of positional embedding.
Solved the RNN parallelization problem.
![[Pasted image 20240205122634.png]]

# Methodology
💡 Describe the methodology used in this paper
![[Pasted image 20250525160333.png]]
![[Pasted image 20240205122647.png]]
# Experiments
💡 List the experiments settings and results of this paper

# Related Papers
💡 Include any related papers that are relevant to this one

# Appendix
💡 Anything else that’s in this paper but not mentioned before

---
# Resources
💡 Include some useful links for better understanding of this paper
- [Illustrated Transformer](https://jalammar.github.io/illustrated-transformer/)
![[Pasted image 20240414095758.png]]
- [An In-Depth Look at the Transformer Based Models](https://medium.com/the-modern-scientist/an-in-depth-look-at-the-transformer-based-models-22e5f5d17b6b)
- ![[Pasted image 20240426112534.png]])
# Personal Notes
💡 Personal thoughts, reflections, or questions about this paper
- [Attention Explained](https://docs.google.com/document/d/1IBTa5ZbDyYUM-vjDDumwe1_TVnhVClxqQNAtSMjRYbQ/edit?tab=t.0)
## Cross Attention
Q,K,V -> Attention layer -> Y

Q: bs, seq_len1, dim
K,V: bs, seq_len2, dim

Q\*K^T: bs, seq_len1, seq_len2
Y = (Q\*K^T) * V =  bs, seq_len1, dim