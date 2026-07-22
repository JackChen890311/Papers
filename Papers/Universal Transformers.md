---
title: Universal Transformers
time: 1807
author: University of Amsterdam; Deepmind; Google Brain
link: https://arxiv.org/pdf/1807.03819
accepted: None
tags:
  - Text
  - Foundation
todo: false
scanned: true
read: false
summary: A shared parameter version of transformer.
---
# Summary
💡 Write a brief summary of this paper here

標準 [[Transformer]] 是**固定深度**，每一層有各自獨立的參數；Universal Transformer 則是：
- 在**深度方向上共享參數**：所有「層」其實是同一組權重反覆套用，形成一種迴圈結構。
- 但迴圈次數(即有效深度)可以是**動態的**，透過一種叫做 **ACT (Adaptive Computation Time)** 的機制，讓模型針對每個 token 自行決定要「思考」幾輪才輸出。
架構上可以想成：
- 輸入 → Transformer Block 反覆套用 → 每個位置獨立決定何時停止(ACT) → 輸出
	- 參數共享，類似 RNN 的遞迴，但單位是 self-attention + FFN
# Methodology
💡 Describe the methodology used in this paper

# Experiments
💡 List the experiments settings and results of this paper

# Related Papers
💡 Include any related papers that are relevant to this one

# Appendix
💡 Anything else that’s in this paper but not mentioned before

---
# Resources
💡 Include some useful links for better understanding of this paper
- [Universal Transformers原理解读](https://zhuanlan.zhihu.com/p/44655133)

# Personal Notes
💡 Personal thoughts, reflections, or questions about this paper