---
title: Commonly Interesting Images
time: 2409
author: Zurich University of Applied Sciences
link: https://arxiv.org/pdf/2409.16736v1
accepted: ECCV24
tags:
  - Image
  - Theory
todo: true
scanned: false
read: false
summary: A study on the common interestingness of images.
---
# Summary
💡 Write a brief summary of this paper here
## 核心概念與目的
- **趣味性的主觀與客觀平衡**：圖像的趣味性通常高度取決於觀看者（主觀性），但研究發現，特定類型的圖像特徵能吸引更廣泛的大眾（客觀/大眾趣味性）。
- **打破二元對立**：過去的研究常將圖像硬性區分為「有趣」或「無趣」。本篇論文提出一個「連續體（Continuum）」的概念，將圖像定位在「大眾皆感興趣（Common Interest）」到「高度主觀感興趣（Subjective Interest）」之間。
## 結論與應用
本研究成功利用用戶的真實行為數據，勾勒出視覺趣味性的分佈譜帶，並以此數據訓練出一個計算模型。這項成果未來可廣泛應用於**事件偵測、影片自動摘要、照片優化增強、個人相簿管理**以及**市場行銷與廣告投放**等領域

# Methodology
💡 Describe the methodology used in this paper
## 主要貢獻與研究方法
- **建立 FlickrUser 數據集**：研究團隊從照片分享平台 Flickr 上，收集了近 2,500 名不同用戶所喜愛的 50 萬張圖像。
- **大眾趣味性（CI, Common Interestingness）的量化定義**：
    - 使用 **CLIP** 模型提取圖像的語意特徵。
    - 利用 **k-means 算法與階層式分群（Hierarchical Clustering）** 將圖像空間切分為不同的語意主題。
    - **CI 分數計算**：如果某個圖像主題被越多不同獨立用戶「點讚（Like）」，該主題的 CI 分數就越高，代表它越屬於「大眾感興趣」的圖像
## 重要發現與分析結果
- **大眾 vs 主觀的圖像類型**：
    - **高 CI（大眾感興趣）**：通常具備高美學價值的專業風景照、日落、森林，或者能引發特定情感的黑白照片、獨特視角的建築物等。
    - **低 CI（主觀感興趣）**：偏向小眾社群或個人喜好，例如《第二人生》（Second Life）遊戲截圖、特定體育賽事（摔角、單車）、玩具（星際大戰模型、樂高）、各類昆蟲近照，或具備性暗示的清涼照。
- **有趣特徵的有趣對比**：
    - 火車比公車更有趣；主菜比甜點更有趣；有昆蟲的花朵比單純的花朵更有趣；樂高比娃娃更有趣；貓與狗的趣味度差不多，但都比爬蟲類更有趣。
- **與社群媒體指標（點讚/瀏覽量）的差異**：
    - 論文指出，絕對的點讚數或瀏覽量往往受到平台推薦系統的嚴重干擾，無法準確反映視覺本身的趣味性。很多 CI 分數相同的圖像，其社群點閱率卻可能相差數萬倍。
- **特徵影響**：大眾趣味性主要受到「由下而上（Bottom-up）」的刺激引導，包含知覺特徵（如色彩、構圖）、字面意義特徵（如具體物件）以及隱含意義特徵（如情感聯想）。
# Experiments
💡 List the experiments settings and results of this paper
- **資料集（FlickrUser-dataset）**：研究團隊從照片分享平台 Flickr 上，收集了 2,337 名不同用戶所喜愛的圖像，去除非公開與清洗後，最終建立了一個包含 **504,241 張圖像**的資料集。
- **計算模型**：論文利用 CLIP 模型（ViT-L/14@336px）提取圖像的語意特徵，並透過數據驅動的方式定義出「大眾趣味性（Common Interestingness, CI）」分數。接著，他們以此數據訓練了一個**線性迴歸模型（Linear Regression Model）**，能夠直接輸入圖像特徵並預測其大眾趣味性得分。
# Related Papers
💡 Include any related papers that are relevant to this one
- [[The Interestingness of Images]]

# Appendix
💡 Anything else that’s in this paper but not mentioned before

---
# Resources
💡 Include some useful links for better understanding of this paper

# Personal Notes
💡 Personal thoughts, reflections, or questions about this paper