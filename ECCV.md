# Workshops
## [Self Supervised Learning: What is Next?](https://sslwin.org/)
### From unsupervised object localization to open-vocabulary semantic segmentation
- [MaskCLIP](https://arxiv.org/pdf/2208.12262)
- [CLIP-Dinoiser](https://arxiv.org/pdf/2312.12359)
	- Adding SSL to CLIP
- [A Study of Test-time Contrastive Concepts for Open-world, Open-vocabulary Semantic Segmentation](https://arxiv.org/pdf/2407.05061)

### What world priors do generative visual models learn?
- [SelfEval: Diffusion model as classifier](https://arxiv.org/pdf/2311.10708)
	- Pick one class that maximize the probability
	- Winoground challenge: same word but different meaning (relationship)
	- ![[Pasted image 20240929094734.png]]
- [EmuVideo](https://arxiv.org/pdf/2311.10709)
	- With Zero SNR in [Common Diffusion Scheduler are flawed](https://arxiv.org/pdf/2305.08891)is better
- [InstanceDiffusion](https://arxiv.org/pdf/2402.03290): Instance-level control on diffusion models
	- ![[Pasted image 20240929095935.png]]
	- ![[Pasted image 20240929095955.png]]
### Diffusion Models for Self-Supervised Learning: A Deconstructive Journey
SSL for diffusion model? For better understanding?
- [Deconstructing Denoising Diffusion Models for Self-Supervised Learning](https://arxiv.org/pdf/2401.14404)
- [PiT](https://arxiv.org/pdf/2406.09415)
## [FAILED Workshop](https://failed-workshop-eccv-2024.github.io/)
- [Prompt and Prejudice](https://arxiv.org/pdf/2408.04671): LLM bias on first name
## [Explainable Computer Vision: Where are We and Where are We Going?](https://excv-workshop.github.io/)
### Yossi Gandelsman: Interpreting Models by Reverse Engineering
- Different head in image models are for different concepts
- MLP do not have much influence
- Models can be reverse engineered into layers, head
- [Interpreting CLIP](https://arxiv.org/pdf/2406.04341)
### Alexei A. Efros: Instead of “explaining” the Algorithms, we need to understand the Data
- [Evaluating Data Attribution for Text-to-Image Model](https://arxiv.org/pdf/2306.09345)
- [Interpreting the Weight Space of Customized Diffusion Models](https://arxiv.org/pdf/2406.09413)
	- generate customized model using other customized models
	- weights-2-weights
	- meta learning? on model weights space?

## [Vision for Art (VISART) VII Workshop](https://visarts.eu/)
### Mining and discovery in historical documents, and collaborations with historians", Mathieu Aubry
- [General Detection-based Text Line Recognition](https://www.arxiv.org/pdf/2409.17095 )
- [The learnable typewriter](https://arxiv.org/pdf/2302.01660)
- [Diffusion Models as Data Mining Tools](https://arxiv.org/pdf/2408.02752)
### Oral Session 1
- [DIFF-NST](https://arxiv.org/pdf/2307.04157)
	- Style transfer
	- Generate style different pair image, changes mostly happen in V value of self-attention layer
	- DDIM inversion on style, only train MLP, unconditional generation
	- Combine with traditional neural transfer loss
	- ![[Pasted image 20240930094917.png]]
- Saliency-driven 3D Reconstruction
- Gaussian Heritage: 3D Digitization of Cultural Heritage with Integrated Object Segmentation
- Tangible Computer Vision for Heritage
- Analysis of Hybrid Compositions in Animation Film with Weakly Supervised Learning
- Context-Infused Visual Grounding for Art
- [ColorwAI: Generative Colorways of Textiles through GAN and Diffusion Disentanglement](https://arxiv.org/pdf/2407.11514)
	- Textile Recolorization
	- Disentangle color, then add a vector to do recolorization
	- ![[Pasted image 20240930115440.png]]
## [Emerging Trends in Disentanglement and Compositionality](https://trend-in-disen-and-compo.github.io/)
- [DisDiff](https://arxiv.org/pdf/2301.13721)
- Current LM and VLM do not perform well on compositionality
- D&C seems to be key for generalization
- SEE SLIDES!!!
## [Instance-Level Recognition](https://ilr-workshop.github.io/ECCVW2024/)
- ZipLoRA
- [ZeST: Zero-Shot Material Transfer from a Single Image](https://arxiv.org/pdf/2404.06425)
- [DreamBooth3D: Personalized 3D model generation](https://arxiv.org/pdf/2303.13508)
	- DreamBooth + DreamFusion
## [Synthetic Data for Computer Vision](https://syntheticdata4cv.wordpress.com/program/)
## [Visual Concepts](https://sites.google.com/cs.stanford.edu/visualconcepts)
- [Cross-Image Attention for Zero-Shot Appearance Transfer](https://arxiv.org/pdf/2311.03335)
- [Be Yourself: Bounded Attention for Multi-Subject Text-to-Image Generation](https://arxiv.org/pdf/2403.16990)
	- Attention layers is powerful!
- [What Makes a Maze Look Like a Maze?](https://arxiv.org/pdf/2409.08202v1)
- [Finding structure in logographic writing with library learning](https://arxiv.org/pdf/2405.06906)
- Ioannis Siglidis: Diffusion Models as Data Mining Tools
- Rohit Gandikota: Concept Sliders: LoRA Adaptors for Precise Control in Diffusion Models
- Amita Kamath: The Hard Positive Truth about Vision-Language Compositionality
- Andong Tan: Explain via Any Concept: Concept Bottleneck Model with Open Vocabulary Concepts
# Main Conference
## Oral 2A
- [Action2Sound](https://arxiv.org/pdf/2406.09272): Generate sound based on video
- [TexDreamer](https://arxiv.org/pdf/2403.12906):Zero-shot 3D Human texture generation 
## Oral 4B
- [Video Editing via Factorized Diffusion Distillation](https://arxiv.org/pdf/2403.09334)
	- With the help of Emu Edit and Emu Video
	- Beats previous SOTA ([Instruct vid2vid](https://arxiv.org/pdf/2305.12328))
- [Audio-Synchronized Visual Animation](https://arxiv.org/pdf/2403.05659)
- [DynamiCrafter: Animating Open-domain Images with Video Diffusion Priors](https://arxiv.org/pdf/2310.12190)
- [MotionDirector: Motion Customization of Text-to-Video Diffusion Models](https://arxiv.org/pdf/2310.08465)
## Oral 5C
- [Emergent Visual-Semantic Hierarchies in Image-Text Representations](https://arxiv.org/pdf/2407.08521)
- [Decoupling Common and Unique Representations for Multimodal Self-supervised Learning](https://arxiv.org/pdf/2309.05300)
- [SINDER: Repairing the Singular Defects of DINOv2](https://arxiv.org/pdf/2407.16826)
	- Find our that there are some defects in DINOv2 attention map (PCA), then proposed a method (predict defect pixel + smoothed) to repair it, and achieve better performance
- [Denoising Vision Transformers](https://arxiv.org/pdf/2401.02957)
	- Train a appended denoising network to use at the output of vaious ViT model

## Oral 6A
- [Controlling the World by Sleight of Hand](https://arxiv.org/pdf/2408.07147)
- Pyramid Diffusion for Fine 3D Large Scene Generation
- FMBoost: Boosting Latent Diffusion with Flow Matching
- [ConceptExpress: Harnessing Diffusion Models for Single-image Unsupervised Concept Extraction](https://arxiv.org/pdf/2407.07077)
	- Kind of like break-a-scene, but with unsupervised concept mask 
- Exact Diffusion Inversion via Bidirectional Integration Approximation
- Tackling Structural Hallucination in Image Translation with Local Diffusion
- Diffusion Prior-Based Amortized Variational Inference for Noisy Inverse Problems
- Adversarial Diffusion Distillation
- Arc2Face: A Foundation Model for ID-Consistent Human Faces
- Diffusion-Driven Data Replay: A Novel Approach to Combat Forgetting in Federated Class Continual Learning
- OmniSSR: Zero-shot Omnidirectional Image Super-Resolution using Stable Diffusion Model
