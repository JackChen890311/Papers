---
title: THREE-BODY SCATTERING FOR GENERATIVE MODELING
time: 2607
author: Westlake University; Zhejiang University; University College London
link: https://arxiv.org/pdf/2607.18198
accepted: None
tags:
  - Image
  - Generation
  - Theory
todo: false
scanned: true
read: false
summary: Three body scattering loss for one step image generation.
---
# Summary
💡 Write a brief summary of this paper here
![[Pasted image 20260731160315.png]]

**論文在做什麼(一句話)**  
提出 TBSM,用「一吸一斥」的粒子力學比喻,設計出一個訓練訊號,教會一個「一步生成」的生成器該怎麼移動,不需要 GAN 判別器、不需要多步 teacher 蒸餾。

**核心機制**
- 生成器架構:雜訊 → 一次前向傳播 → 直接輸出圖片(推論時 one-step,NFE=1)
- 訓練時的 loss:每個生成樣本(projectile)被「一張真實圖片」吸引、被「另一張自己生成的圖片」排斥,這個合力方向當作回歸目標去訓練生成器
- 理論支撐:證明這個力場的期望值,剛好等於最小化 energy distance 的最優移動方向(Wasserstein gradient flow),不是憑感覺設計的

**難點與應對**
- 單一樣本估計排斥力,方差大、訊號吵 → 用 "online tracked scattering"(類似追蹤/EMA 的機制)降噪,並給出誤差收斂的理論分析
- 一步到位天生比多步難學,但論文聲稱免蒸餾也能逼近甚至超越蒸餾方法

**成果**  
ImageNet-256 上,one-step 生成 FID 達到 1.63~2.23,屬於目前該領域數一數二的成績,且開源了代碼。
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