---
tags:
  - Image
  - Metric
todo: false
summary: Learned Perceptual Image Patch Similarity
---
# Summary
💡 Write a brief summary of this paper here
LPIPS uses DNN (backbones such as VGG, AlexNet) to compute a perceptual similarity metric, it first extracts image features at each layer of DNN, compute their distance and multiply by model layer weights, then average over each layer to get result. Compared to PSNR and SSIM, LPIPS aligns more closely with human visual perception.
# Resources
💡 Include some useful links or related papers for better understanding of this concept