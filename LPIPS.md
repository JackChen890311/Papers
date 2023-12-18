LPIPS (Learned Perceptual Image Patch Similarity): LPIPS uses DNN (backbones such as VGG, AlexNet) to compute a perceptual similarity metric, it first extracts image features at each layer of DNN, compute their distance and multiply by model layer weights, then average over each layer to get result. Compared to PSNR and SSIM, LPIPS aligns more closely with human visual perception.
# Reference
- [有真實參照的評估指標：SSIM、PSNR、LPIPS](https://zhuanlan.zhihu.com/p/309892873)
- [評估生成模型優劣指標 - LPIPS & PSNR & SSIM](https://ithelp.ithome.com.tw/articles/10332547)