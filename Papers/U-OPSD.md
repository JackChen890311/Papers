---
title: On-Policy Self-Distillation without Any Supervision
time: 2608
author: UC San Diego; Georgia Institute of Technology; University of Maryland, College Park; ByteDance
link: https://arxiv.org/pdf/2608.06296
accepted: None
tags:
  - Distillation
  - LLM
  - Text
todo: false
scanned: true
read: false
summary: A unsupervised method for on policy self distillation.
---
# Summary
💡 Write a brief summary of this paper here
## 核心問題與背景
- **現有方法痛點**：現有的線上蒸餾（OPD）與自我蒸餾（OPSD）方法仍高度依賴**外部監督**（如真實答案/標準解答、環境反饋或更大型的模型指導），無法實現真正的「自我」蒸餾，且難以擴展至無標籤資料。
- **主要突破**：研究團隊發現，即使單一生成的軌跡可能不可靠，多個獨立採樣結果之間的內部一致性（Internal Consistency）即可提供足夠的信心訊號，無需任何外部標籤即可達成自我蒸餾

![[Pasted image 20260813181852.png]]
# Methodology
💡 Describe the methodology used in this paper
## U-OPSD 方法機制
1. **多路採樣與多數決（Sample & Vote）**：
    - 針對無標籤問題採樣多條解答軌跡（Rollouts），並對提取出的答案進行多數決，產生**偽解答（Pseudo-answer）**。
2. **自洽性門檻與篩選（Confidence Thresholding）**：
    - 設定自洽性門檻 $\tau$（如絕對多數 $\tau = 1/2$）。當勝出的票數比例達標時，將最長的同意解答作為偽解決方案（Pseudo-solution）充當教師參考；票數過低或完全一致（無分歧）的題目則不參與更新。
3. **分歧路徑蒸餾（Distill on Disagreements）**：
    - 以偽解決方案作為條件建立「教師分布」，並沿著與多數決答案不一致的軌跡（Disagreeing completions）進行逐 Token 的機率分布蒸餾，使模型在其「自信地犯錯」之處精準自我糾正。


![[Pasted image 20260813181903.png]]
# Experiments
💡 List the experiments settings and results of this paper
## 實驗結果與表現
- **基準測試**：在五個競賽級數學推理基準（AIME24、AIME25、HMMT25、MATH500、AMC23）上，針對 Qwen3 系列模型進行評測。
- **非思考模式（Non-thinking mode）**：
    - 相較於基底模型（Base model），Qwen3-4B 與 8B 規模分別提升了 **8.5%** 與 **10.7%**。
    - 效果超越需要真實解答（GT）的有監督 OPSD（平均高出 **3.2%** 與 **2.3%**）。
- **思考模式（Thinking mode）**：
    - 性能與使用真實解答的 OPSD 持平甚至微幅超越（4B 領先 0.9%，8B 持平），並超越強化學習方法 GRPO（分別高出 0.7% 與 1.1%）。
- **大幅優於自我獎勵 RL（Self-rewarding RL）**：
    - 證明將「內部共識」作為條件化上下文進行 Token 級別蒸餾，比單純將共識作為純量獎勵（Scalar Reward）進行策略優化更為有效。
# Related Papers
💡 Include any related papers that are relevant to this one
- [[GKD]]
# Appendix
💡 Anything else that’s in this paper but not mentioned before

---
# Resources
💡 Include some useful links for better understanding of this paper

# Personal Notes
💡 Personal thoughts, reflections, or questions about this paper