---
title: HIGH-DIMENSIONAL CONTINUOUS CONTROL USING GENERALIZED ADVANTAGE ESTIMATION
time: 1506
author: Department of Electrical Engineering and Computer Science; University of California, Berkeley
link: https://arxiv.org/pdf/1506.02438
accepted: None
tags:
  - ReinforcementLearning
todo: false
scanned: true
read: false
summary: A advantage estimation for reinforcement learning.
---
# Summary
💡 Write a brief summary of this paper here
### 先想一下,為什麼需要 Advantage

Policy gradient 的更新方向是「讓好的動作機率變高」,但問題是「好」要跟什麼比較才有意義。單純用 return(累積 reward)當訊號,雜訊(variance)會很大;單純用 value function 當 baseline 扣掉,又可能有 bias。**Advantage = 這個動作比「平均水準」好多少**,公式上是:

$A_t = Q(s_t, a_t) - V(s_t)$

也就是「這個動作實際帶來的價值」減去「這個 state 平均能拿到的價值」。問題是 Q 沒辦法直接算,所以要用其他方式估計。

### 兩種極端做法的取捨

1. **Monte Carlo(用完整 rollout 的真實 return 減去 baseline)**
    - $A_t = \sum_{l=0}^{\infty}\gamma^l r_{t+l} - V(s_t))$
    - 優點:bias 低(用的是真實拿到的 reward)
    - 缺點:variance 很高(因為後面一長串 reward 都有隨機性)
2. **TD residual(只往前看一步)**
    - $\delta_t = r_t + \gamma V(s_{t+1}) - V(s_t)$
    - 優點:variance 低
    - 缺點:bias 高(完全依賴 value function 準不準,而 value function 通常沒有訓練到完美)

### GAE 的做法:兩者的加權平均

GAE 的核心想法是:**把「看 1 步」「看 2 步」...「看無限步」的 TD estimate 全部用指數衰減的方式加權平均起來**,用一個參數 λ 控制要偏向哪一邊。

先定義每一步的 TD residual:

$\delta_t = r_t + \gamma V(s_{t+1}) - V(s_t)$

然後 GAE 的 advantage 定義成這些 residual 的指數加權和:

$A_t^{GAE(\gamma,\lambda)} = \sum_{l=0}^{\infty} (\gamma\lambda)^l \delta_{t+l}​$

實務上因為 rollout 長度有限,會從**後面往前遞迴計算**(這也是程式碼裡最常見的寫法):

$A_t = \delta_t + \gamma\lambda \cdot A_{t+1}​$

從最後一個 timestep 開始,$A_T = \delta_T​$,然後往回推。

### λ 這個參數在幹嘛

- **λ = 0**:GAE 退化成純 TD residual,$A_t = \delta_t​$ → variance 低、bias 高
- **λ = 1**:GAE 退化成 Monte Carlo advantage → bias 低、variance 高
- **0 < λ < 1**(常用 0.9~0.97):在兩者之間取平衡,實務上通常比兩個極端都好

直覺上可以把 λ 想成一個「要相信 value function 估計到多深」的旋鈕:λ 越小,越依賴 value function 的預測(也就越快截斷);λ 越大,越依賴實際觀察到的 reward 序列。
### 在 PPO 訓練迴圈裡怎麼用

1. Rollout 一段 trajectory,同時記錄每個 timestep 的 reward 和 value function 估計 $V(s_t)$
2. 從後面往前算 TD residual $\delta_t$​,再遞迴算出 $A_t$​
3. 這個 $A_t$​ 拿去代入 PPO 的 clipped surrogate objective:
	$L^{CLIP} = \mathbb{E}_t\left[\min\left(r_t(\theta) A_t,\ \text{clip}(r_t(\theta), 1-\epsilon, 1+\epsilon) A_t\right)\right]$
	其中 $r_t(\theta) = \frac{\pi_\theta(a_t|s_t)}{\pi_{\theta_{old}}(a_t|s_t)}​$
4. Value function 本身也同時訓練,目標是讓 $V(s_t)$ 逼近算出來的 return(通常用 $A_t + V(s_t)$ 當 target),這樣下一輪 rollout 的 advantage 估計才會更準

### 一句話總結

**GAE 就是用 λ 這個旋鈕,把「只看一步就相信 value function」跟「完全相信實際觀察到的完整 reward 序列」這兩個極端做指數加權平均,藉此在 bias 和 variance 之間找一個實務上更好的甜蜜點,算出來的 advantage 再丟進 PPO 的 clipped objective 裡更新 policy。**
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