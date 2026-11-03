---
name: genpark-personal-agent-ocular-foveal-avascular-zone-octa-faz-skill
version: 1.0.0
description: Calculates OCTA Foveal Avascular Zone Area (mm2), Perimeter (mm), Circularity Index (C), and Parafoveal Vessel Density (FD-300%) to assess retinal capillary dropout.
authors:
  - GenPark Ecosystem
tags:
  - personal-agent
  - ophthalmology
  - octa
  - faz
  - diabetic-retinopathy
  - zero-dependency
---

# Ocular OCTA Foveal Avascular Zone (FAZ) Skill

## Mathematical Formulation

Circularity Index ($C$):

$$C = \frac{4\pi \times A_{\text{FAZ}}}{P_{\text{FAZ}}^2}$$

- $C = 1.0$: Ideal circle.
- $C < 0.70$: Disrupted, notched terminal capillary arcade indicative of localized capillary occlusion.

Equivalent Circular Diameter (mm):

$$D_{\text{eff}} = 2 \times \sqrt{\frac{A_{\text{FAZ}}}{\pi}}$$

## Clinical Microvascular Staging
- **Normal FAZ Morphology**: $A_{\text{FAZ}} \in [0.20, 0.40]\text{ mm}^2$, $C \ge 0.70$, $\text{FD-300} \ge 48\%$
- **Mild Capillary Dropout / Preclinical Retinopathy**: $C \in [0.55, 0.69]$ or $A_{\text{FAZ}} \in [0.40, 0.50]\text{ mm}^2$
- **Severe Macular Ischemia**: $A_{\text{FAZ}} > 0.50\text{ mm}^2$ or $C < 0.55$ (diabetic maculopathy, retinal vein occlusion)
