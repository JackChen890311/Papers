---
title: LATENT ON-POLICY SELF-DISTILLATION
time: 2608
author: National University of Singapore; Beijing University of Posts and Telecommunications; Shanghai Jiao Tong University
link: https://arxiv.org/pdf/2608.13040
accepted: None
tags:
  - Distillation
  - LLM
todo: false
scanned: true
read: false
summary: Latent version of on policy self distillation.
---
# Summary
💡 Write a brief summary of this paper here

本論文提出了一種名為 **LOPD（Latent On-Policy Self-Distillation）** 的新架構，旨在解決大型語言模型（LLM）與 AI Agent 在自我演進（Self-Evolving）過程中，過度依賴人工設計「特權資訊」（Privileged Context）的瓶頸。
![[Pasted image 20260821150138.png]]
# Methodology
💡 Describe the methodology used in this paper
![[Pasted image 20260821150148.png]]
**核心問題與痛點**
- **現有 OPSD 的局限：** 同策略自我蒸餾（On-Policy Self-Distillation, OPSD）通常讓「自我教師」（Self-Teacher）與「學生」（Student）使用相同模型，但給予教師特權資訊（如正確答案、環境反饋或固定技能提示）來引導學生。然而，這些特權資訊大多由設計者手動規則提取，限制了模型端到端學習與自主進化的擴展性。

**LOPD 的創新機制**
- **可學習的隱空間特權上下文：** LOPD 將原本固定的文字特權資訊，轉化為**可端到端學習的連續隱向量（Latent Tokens）**。系統先檢索先前的成功經驗，再透過可訓練的組合器（Composer）壓縮成隱向量，作為教師模型的特權資訊。
- **特權邊界約束（Privileged-Margin Constraint）：** 為防止教師模型退化或直接崩潰至與學生一致，LOPD 引入了基於結果驗證的邊界約束，確保教師在引導時始終保持優於學生的 Log 概率優勢。
- **部署零額外負擔：** 訓練完成後僅保留學生模型，推理階段完全不需要檢索模組、經驗庫或隱向量組合器。
# Experiments
💡 List the experiments settings and results of this paper
**主要實驗結果**
- **效能出色：** 在 Agent 工具使用與程式碼生成（Code Generation）等 7 個基準測試中，顯著優於 RLVR 以及 OPSD、SDPO、Skill-SD 等代表性自我蒸餾方法。
- **採樣效率極高：** LOPD 僅需不到 30% 的 Rollout 預算，即可超越 GRPO 與 Skill-SD。
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