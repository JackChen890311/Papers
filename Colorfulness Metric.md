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