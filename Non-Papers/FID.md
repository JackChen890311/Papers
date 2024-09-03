---
tags:
  - Image
  - Metric
todo: false
summary: Fréchet Inception Distance
---
# Summary
💡 Write a brief summary of this paper here
![[Pasted image 20240610150422.png]]
FID is a metric used to evaluate the quality and diversity of generated images in generative models, particularly in the context of Generative Adversarial Networks (GANs). It measures the similarity between two sets of feature vectors extracted from real images and generated images using a pre-trained Inception-v3 model. The feature vectors represent high-level visual features of the images, and the lower the FID score, the more similar the distributions of real and generated images are perceived to be.

- Compare with [[IS]], FID can be view as a metric focused more on **fidelity**, and also consider more robust
# Resources
💡 Include some useful links or related papers for better understanding of this concept
- [如何評價 GAN? IS 與 FID](https://blog.csdn.net/qq_27261889/article/details/86483505)
- [如何使用Frechet Inception Distance（FID）评估GANs模型？](https://wandb.ai/authors/One-Shot-3D-Photography/reports/-Frechet-Inception-Distance-FID-GANs---Vmlldzo0MzI0MjA)