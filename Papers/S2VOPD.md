---
title: Self-Supervised Visual On-Policy Distillation
time: 2608
author: UC San Diego; University of Maryland, College Park; Georgia Institute of Technology; Johns Hopkins University; University of Oxford
link: https://arxiv.org/pdf/2608.14144
accepted: None
tags:
  - Distillation
  - LLM
  - Image
  - Multimodal
todo: false
scanned: true
read: false
summary: A self supervised on policy distillation for VLM.
---
# Summary
💡 Write a brief summary of this paper here
這篇論文介紹了一項名為 **Self-Supervised Visual On-Policy Distillation ($S^2VOPD$)** 的新技術，旨在解決視覺語言模型（VLM）在進行線上蒸餾（On-Policy Distillation）時，過度依賴外部額外資訊（如更大的教師模型、答案標註或目標區域標記）的問題。

# Methodology
💡 Describe the methodology used in this paper
![[Pasted image 20260821150432.png]]
**核心概念與突破**
- **反轉不對稱性來源**：傳統方法是「給予教師模型更多資訊」，而 $S^2VOPD$ 改為「減少學生模型的資訊」。教師模型觀察原始清晰圖片，學生模型則觀察經過強增強（Augmented/Degraded）的圖片。
- **無須外部標註**：透過輸入視覺資訊的品質差異，自然產生教師與學生之間的預測落差，無須 Ground-truth 標註、獎勵機制（Rewards）或獨立的強大教師模型。

**方法細節（Methodology）**
- **資料增強策略**：系統性探索了資訊減少（如降採樣、高斯噪聲）、幾何變換、光度變換及區域遮擋等四種增強家族。
- **最佳組合（Best Recipe）**：效果最佳的配置為將學生端輸入圖像進行 **降採樣（Downscaling 至 0.3–0.6 倍解析度）並加上高斯噪聲（Gaussian Noise）**。
- **三大關鍵發現**：
    1. 不對稱性至關重要（對稱自蒸餾反而會降低效能）。
    2. 增強強度需適中（強度過高或過低效果皆會下降）。
    3. 增強需維持任務一致性（若完全遮蔽問題關鍵線索會導致無效監督）。
# Experiments
💡 List the experiments settings and results of this paper
**實驗結果與表現**
- **顯著提升**：將 Qwen3.5-4B 的平均準確率從 70.7% 提升至 77.4%（大幅成長 6.7%）。
- **跨級超越**：4B 參數量的模型表現超越了 Qwen3-VL-Instruct-235B (75.8%) 與 GPT-5.4 (72.8%)，並能媲美 Qwen3.5-397B 及 Gemini-3-Flash。
- **資源高效**：在保持訓練資料一致的前提下，恢復了傳統特權監督方法 96% 的增益，同時降採樣也降低了學生模型的計算與推論成本。
# Related Papers
💡 Include any related papers that are relevant to this one
- [[GKD]]
- [[U-OPSD]]
# Appendix
💡 Anything else that’s in this paper but not mentioned before

---
# Resources
💡 Include some useful links for better understanding of this paper

# Personal Notes
💡 Personal thoughts, reflections, or questions about this paper