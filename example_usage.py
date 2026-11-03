"""
Example usage of Ocular OCTA FAZ Morphology Skill.
Demonstrates normal circular foveal avascular zone vs enlarged irregular FAZ in diabetic retinopathy.
"""

import json
from client import OCTAFovealAvascularZoneClient


def main():
    print("=== Testing Ocular OCTA FAZ Skill ===")
    client = OCTAFovealAvascularZoneClient()

    # 1. Healthy young subject with round, regular FAZ (Area = 0.28 mm2, Perimeter = 2.05 mm -> Circularity = 4*pi*0.28 / 2.05^2 = 3.518 / 4.202 = 0.837, FD-300 = 53.5%)
    res_normal = client.evaluate_faz(
        faz_area_mm2=0.28,
        faz_perimeter_mm=2.05,
        parafoveal_fd300_density_pct=53.5,
        capillary_plexus_layer="superficial",
        eye_examined="OD"
    )
    print("\n[Case 1: Normal Intact FAZ Geometry]")
    print(json.dumps(res_normal, indent=2))

    # 2. Patient with diabetic macular ischemia (Area enlarged to 0.62 mm2, perimeter irregular 3.95 mm -> Circularity = 4*pi*0.62 / 3.95^2 = 7.79 / 15.60 = 0.499, FD-300 dropped to 36.2%)
    res_ischemia = client.evaluate_faz(
        faz_area_mm2=0.62,
        faz_perimeter_mm=3.95,
        parafoveal_fd300_density_pct=36.2,
        capillary_plexus_layer="superficial",
        eye_examined="OS"
    )
    print("\n[Case 2: Diabetic Macular Ischemia / FAZ Expansion]")
    print(json.dumps(res_ischemia, indent=2))

    # Assertions
    assert res_normal["morphometry"]["circularity_index"] >= 0.70
    assert "Normal" in res_normal["clinical_interpretation"]["microvascular_status"]
    assert res_ischemia["morphometry"]["circularity_index"] < 0.55
    assert "Severe" in res_ischemia["clinical_interpretation"]["microvascular_status"]
    print("\n[SUCCESS] OCTA FAZ tests passed!")


if __name__ == "__main__":
    main()
