---
tags:
  - Foundation
  - Generation
  - Image
  - Diffusion
todo: false
summary: A image generation model using denoising process.
---
# Summary
💡 Write a brief summary of this paper here
[[Diffusion Models]] is a kind of image generative model, by iteratively predict and subtract the noise in the given image (starting from complete noise), diffusion models can usually output decent result, thus SOTA image generation models usually use diffusion based methods.

Using methods like [[Latent Diffusion]] or [[ControlNet]], [[Diffusion Models]] are able to take in text or different modalities of inputs.
![[Pasted image 20240116203329.png]]

## Cross Attention
### 📌 **Key Findings from Research & Analysis**
1. **Downsampling (Encoder) Layers**:
    - These layers **capture the global layout** of the image.
    - Early layers focus on positioning of major objects.
    - Cross-attention maps at this stage show broad **spatial structure** (e.g., where the sky, ground, or main objects should be).
        
2. **Middle (Bottleneck) Layer**:
    - Acts as a **bridge** between high-level structure and fine details.
    - It encodes **semantic coherence** but not fine textures.
    - Attention maps here refine object identities and relationships.
        
3. **Upsampling (Decoder) Layers**:
    - Higher layers refine **textures and intricate details**.
    - Attention is more **localized**, attending to specific parts of objects.
    - Cross-attention maps show sharper object boundaries and feature-level enhancements (e.g., textures on surfaces).
        

---

### 🔍 **Empirical Observations**
- **Lower-resolution layers (Downsampling)** → Best for **spatial arrangement**.
- **Middle layer (Bottleneck)** → Helps with **semantic consistency**.
- **Higher-resolution layers (Upsampling)** → Capture **fine-grained details**.
# Resources
💡 Include some useful links or related papers for better understanding of this concept
- [Controlling Diffusion Models - Texas A&M University - Google 簡報](https://docs.google.com/presentation/d/12svjPQlZcnk5bykRguWeX1wEMGJ5XiBgzYFNWT3GMK0/edit#slide=id.p)


