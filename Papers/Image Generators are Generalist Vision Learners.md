---
title: Image Generators are Generalist Vision Learners
time: 2604
author: Google Deepmind
link: https://arxiv.org/pdf/2604.20329
accepted: None
tags:
  - Image
  - Generation
  - Understanding
todo: false
scanned: true
read: false
summary: Reframe understanding problem as generation problem for image generators.
---
# Summary
💡 Write a brief summary of this paper here
這篇論文探討了將「影像生成模型」轉化為「通用視覺理解模型」的巨大潛力。  

# Methodology
💡 Describe the methodology used in this paper
### 核心亮點
- **影像生成即視覺理解**：論文指出，影像生成模型的預訓練過程與大型語言模型（LLM）類似，能讓模型學習到強大且通用的視覺表示能力 。  
- **統一看待視覺任務**：研究團隊將各種視覺感知任務（如分割遮罩、深度圖等）的輸出結果參數化為 RGB 影像格式，成功將「視覺感知」問題無縫轉換為單純的「影像生成」問題 。  
    

### 研究方法與成果
- **Vision Banana 模型**：研究團隊對原有的影像生成模型 Nano Banana Pro (NBP) 進行了輕量級的指令微調（Instruction-tuning），在原本的訓練數據中加入少量的視覺任務數據，打造出通用的視覺模型 Vision Banana 。  
- **超越特定領域專家**：在完全不犧牲原有影像生成能力的前提下 ，Vision Banana 在 2D 與 3D 視覺理解任務上皆達到了 SOTA（業界最先進）水準，甚至擊敗或媲美了專門針對單一任務的零樣本（zero-shot）模型（例如在分割任務上超越了 SAM 3，在深度估計上超越了 Depth Anything 系列）。  
    

### 結論與意義
- 這項研究證明了，影像生成的預訓練本身就是一種強大的「通用視覺學習器」。  
- 影像生成有望成為未來所有視覺任務的「通用介面」，這與文字生成在自然語言處理中所扮演的角色如出一轍 。  
- 該研究預示了電腦視覺領域的重大典範轉移：生成式視覺預訓練將成為打造兼具「生成」與「理解」能力之「視覺基礎模型」的核心 。

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