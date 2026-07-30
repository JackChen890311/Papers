---
title: Proximal Policy Optimization Algorithms
time: 1707
author: OpenAI
link: https://arxiv.org/pdf/1707.06347
accepted: None
tags:
  - ReinforcementLearning
  - Theory
todo: false
scanned: true
read: false
summary: The most commonly use policy gradient reinforcement learning strategy.
---
# Summary
💡 Write a brief summary of this paper here

核心目標是:**在每次更新時,讓新 policy 相對舊 policy 不要走太遠**,避免傳統 policy gradient 常見的「一步踩太大導致訓練崩潰」問題。
### 先回顧基本 policy gradient

最原始的 policy gradient(REINFORCE)長這樣:

$\nabla_\theta J(\theta) = \mathbb{E}\left[\nabla_\theta \log \pi_\theta(a|s) \cdot A(s,a)\right]$

直覺:如果某個動作 a 的 advantage(比平均好多少)是正的,就增加它的機率;是負的,就降低它的機率。

問題是:這個梯度估計變異數很大,而且每次更新完,舊的 rollout 資料就不能再用(因為分佈已經變了),樣本利用率很差。

### PPO 的解法:重要性採樣 + Clipping

**Step 1 — 用重要性採樣重複利用舊資料**

PPO 允許你用「舊 policy(θ_old)產生的 rollout」去更新「新 policy(θ)」,透過機率比值做校正:

$\rho(\theta) = \frac{\pi_\theta(a|s)}{\pi_{\theta_{old}}(a|s)}$

目標函數變成:

$L(\theta) = \mathbb{E}\left[\rho(\theta) \cdot A(s,a)\right]$

這樣一份 rollout 資料可以拿來做好幾個 epoch 的梯度更新,而不是每次都要重新採樣。

**Step 2 — Clip,防止更新走太遠**

問題是:如果 ρ(θ) 偏離 1 太多(代表新舊 policy 差太多),重要性採樣的估計會不準,甚至讓 policy 崩潰。PPO 的解法就是直接把 ratio 夾住:

$L^{CLIP}(\theta) = \mathbb{E}\left[\min\big(\rho(\theta) A,\ \text{clip}(\rho(\theta), 1-\epsilon, 1+\epsilon) A\big)\right]$

直覺拆解:

- 如果 A > 0(這個動作是好的):目標函數會鼓勵 ρ(θ) 變大(提高這個動作機率),但一旦 ρ(θ) > 1+ε,clip 就會讓梯度停止繼續推——也就是說,「好動作也不能無限制地一直提高機率」
- 如果 A < 0(這個動作不好):目標函數會鼓勵 ρ(θ) 變小,但一旦 ρ(θ) < 1-ε,同樣會被夾住

用 min 取兩者中較保守(較小)的那個,確保目標函數是一個「悲觀下界」,更新永遠不會過度樂觀。

這個機制的效果等同於:**只要新舊 policy 差距在 ±ε 的範圍內,就正常更新;一旦超出這個信任區域,就不再給額外獎勵去鼓勵它繼續偏離**——這就是「Proximal(鄰近)」這個字的來源,新 policy 要保持在舊 policy 的「附近」。
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