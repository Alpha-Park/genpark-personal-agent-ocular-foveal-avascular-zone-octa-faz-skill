# Ocular OCTA Foveal Avascular Zone (FAZ) Personal Agent Skill

[![License: Apache-2.0](https://img.shields.io/badge/License-Apache%202.0-blue.svg)](LICENSE)
[![Python: 3.8+](https://img.shields.io/badge/python-3.8+-blue.svg)](https://www.python.org/)
[![Zero Dependencies](https://img.shields.io/badge/dependencies-zero-brightgreen.svg)]()
[![Model Context Protocol](https://img.shields.io/badge/MCP-Standard%20JSON--RPC-orange.svg)]()
[![Production Ready](https://img.shields.io/badge/status-production--ready-green.svg)]()

Deterministic, zero-mock personal agent micro-skill for calculating Optical Coherence Tomography Angiography (OCTA) Foveal Avascular Zone Area ($A_{\text{FAZ}}$), Perimeter ($P_{\text{FAZ}}$), Circularity Index ($C$), and Parafoveal Capillary Density (FD-300%).

## Architecture

```mermaid
flowchart TD
    A[OCTA En Face Slab at Fovea] --> B[Segment FAZ Boundary & Trace Perimeter]
    B --> C[Compute FAZ Area mm2 & Perimeter mm]
    C --> D[Calculate Circularity C = 4*pi*Area / Perimeter^2]
    D --> E[Quantify 300 um Peri-FAZ Vessel Density FD-300%]
    E --> F[Classify Normal vs Severe Diabetic Macular Ischemia]
```

## Quickstart

```python
from client import OCTAFovealAvascularZoneClient

client = OCTAFovealAvascularZoneClient()
result = client.evaluate_faz(
    faz_area_mm2=0.28,
    faz_perimeter_mm=2.05,
    parafoveal_fd300_density_pct=53.5
)
print(result)
```

## License

Apache-2.0
