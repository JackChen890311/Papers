---
title: "DiffusionOPD: A Unified Perspective of On-Policy Distillation in Diffusion Models"
time: 2605
author: Fudan University; Wan Team, Alibaba Group
link: https://arxiv.org/pdf/2605.15055
accepted: None
tags:
  - Diffusion
  - Image
  - Distillation
todo: false
scanned: true
read: false
summary: Apply on-policy distillation on diffusion model, final model outperforms 3 teacher models.
---
# Summary
💡 Write a brief summary of this paper here
## 總結
**Stage 1 — 分別訓練專精 Teacher(靠 RL,不是靠模型變大)**
- 每個任務(GenEval 組合式生成 / OCR 文字渲染 / Aesthetics 美學)各自用 RL(GRPO-Guard / DiffusionNFT)訓練一個獨立 teacher
- 好處:各自優化不會互相干擾,天花板比 joint multi-task RL 更高
- 代價:每個 teacher 偏科(Aesthetics teacher 在 OCR 上表現差,反之亦然)

**Stage 2 — On-policy 蒸餾進統一 Student**
1. Student 自己跑一遍去噪過程,產生自己的軌跡(no_grad)
2. 在 student 走過的每個中間狀態,同時問 student 和對應任務 teacher「下一步要去哪」→ 各自得到一個高斯轉移分佈(mean 不同,covariance 相同)
3. 因為兩個高斯 covariance 相同,reverse KL 有 **closed-form 解**:就是兩者 mean 的 L2 距離平方(除以 2 倍 variance)
4. 多任務輪流採樣,累積 loss 後才做一次反向傳播更新(gradient accumulation = 任務數)

### 為何不用 PPO,而直接用 closed-form KL?
- 兩者期望梯度數學上相等
- 但 PPO 的 score-function estimator 多了一個跟高斯取樣噪聲成正比的隨機項 → 增加梯度變異數
- Closed-form KL 是 pathwise gradient,直接反向傳播,無取樣雜訊,收斂更快更穩

### 實驗結果重點
- DiffusionOPD 平均分數 0.929,勝過任一 single-task teacher、multi-task RL baseline、cascade RL baseline
- 訓練時間比 multi-task RL 更短
# Methodology
💡 Describe the methodology used in this paper

# Experiments
💡 List the experiments settings and results of this paper
![[Pasted image 20260730165731.png]]
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