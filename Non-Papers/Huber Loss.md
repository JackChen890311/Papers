---
tags:
  - Loss
todo: false
summary: A loss for more robustness for hard example by down-weighting the hard examples.
---
# Summary
💡 Write a brief summary of this paper here
[[Huber Loss]]是藉由針對outlier (hard example)進行down-weighting，因此對outlier，loss function還有穩健性。  
[[Focal Loss]]是希望針對inliers(easy example)進行down-weighting，因為 focal loss希望的是在訓練過程中能盡量去訓練hard example，忽略那些easy example。
![[Pasted image 20251022122207.png]]
![[Pasted image 20251022122258.png]]
![[Pasted image 20251022143159.png]]
# Resources
💡 Include some useful links or related papers for better understanding of this concept
- [機器/深度學習: 損失函數(loss function)- Huber Loss和 Focal loss](https://chih-sheng-huang821.medium.com/%E6%A9%9F%E5%99%A8-%E6%B7%B1%E5%BA%A6%E5%AD%B8%E7%BF%92-%E6%90%8D%E5%A4%B1%E5%87%BD%E6%95%B8-loss-function-huber-loss%E5%92%8C-focal-loss-bb757494f85e)