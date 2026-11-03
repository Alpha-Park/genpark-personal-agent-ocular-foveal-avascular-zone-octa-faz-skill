"""
Ocular Optical Coherence Tomography Angiography (OCTA) FAZ Morphology Client.
Zero-mock pure Python standard library implementation.
Calculates Foveal Avascular Zone Area (mm2), Perimeter (mm), Circularity Index (C),
and Parafoveal Capillary Density (FD-300%) for macular microvascular evaluation.
"""

import math
from typing import Dict, Any, Optional


class OCTAFovealAvascularZoneClient:
    """
    Evaluates retinal microvascular architecture and macular capillary dropout via OCTA:
    - FAZ Area (mm2): central capillary-free zone
    - FAZ Perimeter (mm): border length of terminal capillary ring
    - Circularity Index C: 4 * pi * Area / Perimeter^2 (1.0 = perfect circle)
    - FD-300 (%): vessel density in a 300 um ring surrounding the FAZ
    """

    def __init__(self):
        pass

    def evaluate_faz(
        self,
        faz_area_mm2: float,
        faz_perimeter_mm: float,
        parafoveal_fd300_density_pct: Optional[float] = 52.0,
        capillary_plexus_layer: Optional[str] = "superficial",
        eye_examined: Optional[str] = "OD"
    ) -> Dict[str, Any]:
        """
        Calculates FAZ geometric and microvascular metrics.
        faz_area_mm2: area of FAZ in square millimeters (0.10 to 1.20 mm2).
        faz_perimeter_mm: perimeter of FAZ boundary in millimeters (1.5 to 5.0 mm).
        parafoveal_fd300_density_pct: vessel density in 300 um peri-FAZ zone (default 52%).
        capillary_plexus_layer: 'superficial' (SCP) or 'deep' (DCP).
        eye_examined: OD or OS.
        """
        if faz_area_mm2 <= 0 or faz_perimeter_mm <= 0:
            raise ValueError("FAZ area and perimeter must be strictly positive.")

        # Circularity Index C = 4 * pi * Area / Perimeter^2
        # Max theoretical circularity is 1.0 (isoperimetric inequality)
        circularity = (4.0 * math.pi * faz_area_mm2) / (faz_perimeter_mm * faz_perimeter_mm)
        circularity = max(0.0, min(1.0, circularity))

        # Effective circular diameter (mm)
        effective_diameter_mm = 2.0 * math.sqrt(faz_area_mm2 / math.pi)

        # Clinical microvascular staging (Early Diabetic Retinopathy / Retinal Vein Occlusion):
        # Normal FAZ: Area 0.20 - 0.40 mm2, Circularity >= 0.70, FD-300 >= 48%
        # Mild capillary dropout / notch: Circularity 0.55 - 0.69, Area 0.40 - 0.50 mm2
        # Severe macular ischemia / FAZ expansion: Area > 0.50 mm2 or Circularity < 0.55
        if faz_area_mm2 > 0.50 or circularity < 0.55 or (parafoveal_fd300_density_pct and parafoveal_fd300_density_pct < 42.0):
            microvascular_status = "Severe Macular Capillary Ischemia & FAZ Expansion"
            clinical_significance = "Profound terminal capillary loop dropout, contour notching, and peri-foveal capillary non-perfusion; high risk of diabetic maculopathy."
        elif faz_area_mm2 > 0.40 or circularity < 0.70 or (parafoveal_fd300_density_pct and parafoveal_fd300_density_pct < 48.0):
            microvascular_status = "Early Capillary Non-Perfusion / Irregular FAZ Contour"
            clinical_significance = "Subclinical capillary rarefaction and contour distortion; early biomarker of systemic microangiopathy."
        else:
            microvascular_status = "Normal Foveal Microvascular Geometry"
            clinical_significance = "Continuous, well-defined terminal capillary arcade with preserved circularity and optimal capillary perfusion."

        return {
            "status": "success",
            "morphometry": {
                "faz_area_mm2": round(faz_area_mm2, 3),
                "faz_perimeter_mm": round(faz_perimeter_mm, 3),
                "effective_diameter_mm": round(effective_diameter_mm, 3),
                "circularity_index": round(circularity, 3)
            },
            "perfusion_density": {
                "fd300_perifoveal_density_pct": round(parafoveal_fd300_density_pct, 1) if parafoveal_fd300_density_pct else None,
                "capillary_plexus_layer": capillary_plexus_layer,
                "eye_examined": eye_examined
            },
            "clinical_interpretation": {
                "microvascular_status": microvascular_status,
                "clinical_significance": clinical_significance
            }
        }
