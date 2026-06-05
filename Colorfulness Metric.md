---
title: Measuring Colourfulness in Natural Images
time: 2306
author: Haslera & Susstrunk
link: https://infoscience.epfl.ch/server/api/core/bitstreams/77f5adab-e825-4995-92db-c9ff4cd8bf5a/content
accepted: None
tags:
  - Metric
todo: false
scanned: true
read: false
summary: A metric for measuring colorfulness.
---
# Summary
💡 Write a brief summary of this paper here

# Methodology
💡 Describe the methodology used in this paper
## Implementation
```python=
import numpy as np
from PIL import Image

def colorfulness(img: Image.Image) -> float:
    arr = np.array(img, dtype=float)
    R, G, B = arr[..., 0], arr[..., 1], arr[..., 2]
    
    rg = R - G
    yb = 0.5 * (R + G) - B
    
    std_rg, std_yb = rg.std(), yb.std()
    mu_rg, mu_yb   = rg.mean(), yb.mean()
    
    std_root = np.sqrt(std_rg**2 + std_yb**2)
    mu_root  = np.sqrt(mu_rg**2  + mu_yb**2)
    
    return std_root + 0.3 * mu_root
```

## Explanation
#### 核心思路：模擬人眼的色彩感知

人眼有三種錐狀細胞（感知 R、G、B），但大腦處理色彩時**不是直接用 RGB**，而是轉換成「對立色通道」（opponent color channels）。這個指標就是在模擬這個過程。

---

#### Step 1：對立色通道（Opponent Channels）

```
rg = R - G        # 紅-綠對立軸
yb = 0.5(R+G) - B # 黃-藍對立軸
```

這來自 **Hering 對立色理論**（1878）：大腦感知顏色的方式是：

- 「這個像素偏紅還是偏綠？」→ `rg`
- 「這個像素偏黃還是偏藍？」→ `yb`

灰色圖像的 rg ≈ 0、yb ≈ 0，因為 R≈G≈B，差值幾乎為零。

---

#### Step 2：標準差（σ）代表「色彩變化的廣度」

```
std_root = sqrt(σ_rg² + σ_yb²)
```

σ 衡量的是整張圖的**色彩分散程度**：

- σ 大 → 圖中同時存在很多不同的顏色（紅的、綠的、黃的都有）
- σ 小 → 圖的顏色很單一，接近灰階或只有一種色調

這是歐幾里德距離，把兩個色彩軸的變化量合併成一個純量。

---

#### Step 3：平均值（μ）代表「整體色彩偏移量」

```
mu_root = sqrt(μ_rg² + μ_yb²)
```

μ 衡量的是整張圖**平均偏向哪個顏色**：

- 一張全紅的圖 → μ_rg 很大，即使 σ 可能不大
- 純灰圖 → μ ≈ 0

光有 σ 不夠——想像一張圖每個像素都是飽和紅色，σ 接近 0，但它明顯很「有色彩」。μ 就是來補捉這個情況的。

---

#### Step 4：最終公式

```
colorfulness = std_root + 0.3 × mu_root
```

- **σ 的權重是 1**（主要貢獻）：色彩的多樣性最重要
- **μ 的權重是 0.3**（次要修正）：整體色偏也算，但影響較小

`0.3` 這個係數是 Hasler & Süsstrunk 透過**心理物理學實驗**校正出來的——讓公式的輸出跟人類受試者的主觀評分盡量吻合。

---

#### 直覺總結

|概念|對應到什麼|
|---|---|
|`rg`, `yb`|模擬大腦的對立色感知|
|σ（標準差）|圖中色彩的「多樣性」|
|μ（平均值）|圖中色彩的「強度/偏移」|
|加權相加|兩種效果都重要，但多樣性更主要|

簡單說：**一張圖如果同時擁有很多不同的顏色（高 σ），又整體帶有鮮明的色調（高 μ），就會得到高分。**
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
## Hering 對立色理論
德國生理學家埃瓦爾德·海林（Ewald Hering）於 1878 年提出的**對立色理論**（Opponent Process Theory）認為，人類的視覺系統是基於互補色的對立機制來感知色彩的。此理論成功解釋了三原色理論無法說明的「視覺後像」（殘像）現象。

### 核心運作機制

海林提出人類視網膜與大腦視覺中樞存在三組獨立的「對立通道」，它們以正負相抗衡的方式運作：
- **紅 vs. 綠**（Red-Green）
- **黃 vs. 藍**（Yellow-Blue）
- **黑 vs. 白**（Black-White，負責明暗感知）

### 理論兩大關鍵

1. **色彩互斥現象**：我們能感知到「偏綠的黃色」或「偏藍的紅色」，但人類的視覺不可能同時感知到「紅綠色」或「黃藍色」，因為這兩組顏色在神經層面上是互相拮抗、抵銷的。
2. **正負反應模式**：當通道受其中一種顏色刺激而產生興奮時，就會抑制對立顏色的反應。例如，長時間凝視紅色的區塊會使紅錐細胞疲乏，當視線移開到白紙上時，受抑制的綠色通道就會活躍起來，產生綠色的視覺後像（殘像）。
3. 
現代神經生理學已經證實了海林的假設，在大腦外側膝狀核（LGN）中確實存在專門處理這些對立色彩的神經節細胞。您可以參考 [維基百科：後像](https://zh.wikipedia.org/zh-tw/%E5%BE%8C%E5%83%8F) 了解更多關於視覺殘像的科學原理解析。