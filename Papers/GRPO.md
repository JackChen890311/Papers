---
title: "DeepSeekMath: Pushing the Limits of Mathematical Reasoning in Open Language Models"
time: 2402
author: DeepSeek-AI; Tsinghua University; Peking University
link: https://arxiv.org/pdf/2402.03300
accepted: None
tags:
  - ReinforcementLearning
  - LLM
todo: false
scanned: true
read: false
summary: A improved policy optimization method by using group relative performance.
---
# Summary
💡 Write a brief summary of this paper here
## 核心概念
**PPO 的痛點**：PPO 需要額外訓練一個 critic model（value function）來估計 baseline，用於計算 advantage。這個 critic 通常跟 policy model 一樣大，訓練成本很高，而且對 LLM 這種輸出空間巨大的任務，value function 很難估得準。

**GRPO 的做法**：直接拿掉 critic model，改用「同一個 prompt 取樣多次」的方式來估計 baseline。

## 運作方式

1. 對同一個 prompt，用目前的 policy 取樣出一組（group）回答，例如 G=8 個。
2. 對每個回答用 reward model（或規則式 reward，例如數學題答案對不對）打分數，得到 r1,r2,...,rGr_1, r_2, ..., r_G r1​,r2​,...,rG​。
3. 用這組分數做標準化，算出每個回答的 advantage：

$A_i = \frac{r_i - \text{mean}(r_1,...,r_G)}{\text{std}(r_1,...,r_G)}$

也就是說，advantage 不是靠 critic 預測出來的，而是靠「這個回答比同組其他回答好還是差」來決定。

4. 接著跟 PPO 一樣，用 clipped surrogate objective 更新 policy：

$L = \min\left(\frac{\pi_\theta}{\pi_{\theta_{old}}} A_i,\ \text{clip}\left(\frac{\pi_\theta}{\pi_{\theta_{old}}}, 1-\epsilon, 1+\epsilon\right) A_i\right)$

5. 另外加上一個 KL penalty 項（跟參考模型 πref\pi_{ref} πref​ 比較），直接加在 loss 裡（而不是像 PPO 那樣放進 reward 裡）。

### 跟 PPO 的差異總結

| |PPO|GRPO|
|---|---|---|
|Baseline 來源|Critic model (value function)|Group 內取樣的平均分數|
|額外模型|需要 critic|不需要 critic|
|計算成本|較高（訓練兩個模型）|較低|
|Advantage 估計|GAE (bootstrap)|Group 內 z-score 標準化|
|KL 處理|通常放進 reward|直接加進 loss|

### 直覺理解

你可以把它想成「用同儕比較取代價值預測」——與其訓練一個模型去猜「這個回答應該值多少分」，不如直接讓模型對同一題生成好幾個答案，然後看「這次表現比自己平常（同組平均）好還是差」，用這個相對好壞當作學習訊號。這樣既省了 critic 的訓練成本，也天然適合 reward 稀疏、只有最終結果對錯（如數學題、代碼題）的場景。

![[Pasted image 20260804220947.png]]
# Methodology
💡 Describe the methodology used in this paper

# Experiments
💡 List the experiments settings and results of this paper

# Related Papers
💡 Include any related papers that are relevant to this one
- [[PPO]]
# Appendix
💡 Anything else that’s in this paper but not mentioned before

---
# Resources
💡 Include some useful links for better understanding of this paper

# Personal Notes
💡 Personal thoughts, reflections, or questions about this paper