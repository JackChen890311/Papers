# Summary
20/03
NeRF learns a model (MLP) that takes spatial locations and view directions and output the predicted colors and densities of a scene. NeRF model will then use a technique called 'volume rendering’ to render 2d image by projecting predicted color and density into it, hence makes it possible to render 2d image in any viewpoints.

Since volume rendering is a differentiable process, by computing losses between the rendered images and the corresponding real images, NeRF model can update its weights by stochastic gradient descent and learns a good representation for the given scene.

![[Pasted image 20231203232418.png]]
![[Pasted image 20231204102044.png]]
![[Pasted image 20231204101950.png]]


# Reference
- [NeRF 論文筆記](https://zhuanlan.zhihu.com/p/360365941)
- [Novel View Synthesis 介紹](https://zhuanlan.zhihu.com/p/486710656)
# PDF
![[NeRF - Representing Scenes as Neural Radiance Fields for View Synthesis.pdf]]