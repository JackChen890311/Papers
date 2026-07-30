---
title: EXPLORATION BY RANDOM NETWORK DISTILLATION
time: 1810
author: OpenAI; University of Edinburgh
link: https://arxiv.org/pdf/1810.12894
accepted:
tags:
  - ReinforcementLearning
  - Distillation
todo: false
scanned: true
read: false
summary:
---
# Summary
💡 Write a brief summary of this paper here

RND 是拿來解決強化學習裡「探索」（exploration）問題的方法，核心概念是：**用一個固定的隨機神經網路當作「參考答案」，再訓練另一個網路去模仿它，模仿得越差的地方,代表 agent 越少去過那裡。**
### 具體怎麼運作
1. **兩個網路**
    - **Target network（目標網路）**：隨機初始化,權重固定不動,永遠不訓練。給它一個 state,它會吐出一個固定的向量(可以想成是這個 state 的「隨機指紋」)。
    - **Predictor network（預測網路）**：架構跟 target 一樣,但會被訓練,目標是讓它輸出盡量逼近 target network 對同一個 state 的輸出。
2. **訓練 predictor**
    - 每次 agent 走到一個新的 state,就把這個 state 丟給兩個網路。
    - 算兩者輸出的差距(MSE),用這個誤差去更新 predictor,讓它學著去逼近 target。
3. **這個誤差就是「內在獎勵」(intrinsic reward)**
    - 如果某個 state 常常出現,predictor 已經被訓練到很會模仿 target 在這個 state 上的輸出,誤差就很小 → 給的內在獎勵低。
    - 如果某個 state 很少出現(新奇、沒探索過),predictor 沒被訓練過怎麼模仿,誤差就大 → 給的內在獎勵高。
4. **把內在獎勵加到外在獎勵上**
    - Total reward = 環境給的 extrinsic reward + 這個 novelty-based intrinsic reward
    - Agent 因此有動機去找誤差大(也就是新奇)的地方探索。

### 為什麼要用「隨機網路」而不是別的
- 用固定隨機網路當 target,好處是**不需要任何 label 或環境模型**,單純利用「一個網路要模仿另一個網路輸出」這件事的可預測性當作代理指標。
- 這比起以前用 forward model(預測下一個 state)或 count-based 方法簡單很多,而且在 pixel-based 高維度 state(像 Atari、Montezuma's Revenge)上特別有效,是因為它不會被「環境本身的隨機性」(stochasticity)搞混——這是它比 curiosity-driven exploration(ICM 那種預測下一狀態的方法)更穩定的地方,因為 ICM 常常會被環境雜訊騙,誤以為雜訊很有趣。

### 一句話總結
**RND = 拿一個永遠不變的隨機網路當「新奇度探測器」,agent 越搞不定的地方(predictor 學不會模仿 target 的地方),就代表越少去過,越值得探索。**
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

# Personal Notes
💡 Personal thoughts, reflections, or questions about this paper