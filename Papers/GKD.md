---
title: "ON-POLICY DISTILLATION OF LANGUAGE MODELS: LEARNING FROM SELF-GENERATED MISTAKES"
time: 2306
author: Google DeepMind; Mila; University of Toronto
link: https://arxiv.org/pdf/2306.13649
accepted: ICLR24
tags:
  - LLM
  - Distillation
  - Text
todo: false
scanned: true
read: false
summary: The first paper that unified the idea of on-policy distillation on LLM.
---
# Summary
💡 Write a brief summary of this paper here

**On-policy distillation** 是一種訓練範式(paradigm),不是單純的「大模型教小模型」。

|           | Off-policy Distillation(傳統) | RL             | On-policy Distillation |
| --------- | --------------------------- | -------------- | ---------------------- |
| 訓練資料來源    | Teacher 生成                  | Student 自己生成   | Student 自己生成           |
| Reward 密度 | Dense(每 token)              | Sparse(整條軌跡一次) | Dense(每 token/step)    |
| 分佈一致性     | 訓練/推論不一致(exposure bias)     | 一致             | 一致                     |
 
- **關鍵不是模型大小,而是**:
  1. **On-policy**: student 在「自己生成的軌跡」上被訓練
  2. **Dense feedback**: teacher 在每個 token/step 上都給密集回饋,而非序列結束才給一個 scalar reward
- Teacher 可以是:外部更強模型(大教小)、**同一個模型的不同 context**(self-distillation)、甚至是**架構不同但更早訓練好的模型**(如 AR→Diffusion 轉換)
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
- [On-Policy Distillation by Thinking Machine](https://thinkingmachines.ai/blog/on-policy-distillation/)
# Personal Notes
💡 Personal thoughts, reflections, or questions about this paper