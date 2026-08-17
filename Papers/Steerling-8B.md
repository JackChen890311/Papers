---
title: Scaling Inherently Interpretable Language Models
time: 2608
author: Guide Labs Team
link: https://arxiv.org/pdf/2608.07594
accepted: None
tags:
  - XAI
  - LLM
  - Text
todo: false
scanned: true
read: false
summary: A LLM that includes interpretability into training process.
---
# Summary
💡 Write a brief summary of this paper here
## 核心觀點與突破
- **打破事後解釋（Post-hoc Methods）的局限**：傳統方法多在模型訓練後進行逆向工程，無法保證解釋與實際計算過程的真實綁定與因果干預。
- **原生可解釋性（Inherent Interpretability）**：將可解釋性約束納入訓練資料、架構設計與損失函數中。實驗表明，隨著計算規模擴大，模型表徵會變得更加解耦（Disentangled），且更符合人類可理解的概念。
- **極低的擴展成本**：引入可解釋性模組僅帶來固定且微小的計算擴展偏差（Scaling Offset），且該成本不會隨著模型規模放大而增加。
# Methodology
💡 Describe the methodology used in this paper
## 實作模型：Steerling-8B
團隊基於具有因果注意力遮罩的擴散語言模型（Causal Diffusion LM）實作了 **Steerling-8B**，提供三大維度的歸因能力與閉環控制：
1. **輸入歸因（Input Attribution）**：利用訓練好的缺失基準（Absence Baseline），精確量化各輸入 Token 對產出結果的影響。
2. **概念歸因（Concept Attribution）**：透過加性概念瓶頸層（Additive Concept Bottleneck），將輸出分解為人類可理解的概念（Concepts）。
3. **訓練資料歸因（Training Data Attribution）**：精確檢索出與當前生成內容最為相似的訓練資料。
4. **可控轉向（Concept Steering）**：透過診斷概念歸因，無需重新訓練即可直接放大或抑制特定概念方向，精準修正模型行為。
# Experiments
💡 List the experiments settings and results of this paper
## 數據基礎設施與模型效能
- **Atlas 概念自動標註系統**：針對大規模預訓練語料缺乏概念標籤的問題，構建 Atlas Pipeline，歸納出超過 33,000 個規範化概念，並標註超過 1 兆（Trillion）個 Token。
- **競爭力表現**：Steerling-8B 在經過 1.2 兆 Pretraining Token 與 1,500 億 Mid-training Token 的訓練後，綜合基準測試表現達到其他訓練計算量高出 2–16 倍的同規模開源模型的 90% 以上。
# Related Papers
💡 Include any related papers that are relevant to this one

# Appendix
💡 Anything else that’s in this paper but not mentioned before

---
# Resources
💡 Include some useful links for better understanding of this paper

# Personal Notes
💡 Personal thoughts, reflections, or questions about this paper