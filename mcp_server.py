"""
MCP Server for Ocular OCTA FAZ Morphology Skill.
Provides standard Model Context Protocol JSON-RPC tool endpoints.
"""

import sys
import json
from client import OCTAFovealAvascularZoneClient


def main():
    client = OCTAFovealAvascularZoneClient()

    for line in sys.stdin:
        line = line.strip()
        if not line:
            continue
        try:
            req = json.loads(line)
        except Exception:
            continue

        method = req.get("method")
        msg_id = req.get("id")

        if method == "tools/list":
            res = {
                "jsonrpc": "2.0",
                "id": msg_id,
                "result": {
                    "tools": [
                        {
                            "name": "evaluate_faz",
                            "description": "Calculates OCTA Foveal Avascular Zone Area (mm2), Perimeter (mm), Circularity Index (C), and Parafoveal Vessel Density (FD-300%) to assess retinal capillary dropout.",
                            "inputSchema": {
                                "type": "object",
                                "properties": {
                                    "faz_area_mm2": {
                                        "type": "number",
                                        "description": "Foveal avascular zone area in square millimeters (mm2)."
                                    },
                                    "faz_perimeter_mm": {
                                        "type": "number",
                                        "description": "Foveal avascular zone perimeter in millimeters (mm)."
                                    },
                                    "parafoveal_fd300_density_pct": {
                                        "type": "number",
                                        "description": "Perifoveal 300 um capillary density percentage (default: 52.0)."
                                    },
                                    "capillary_plexus_layer": {
                                        "type": "string",
                                        "description": "superficial or deep plexus (default: superficial)."
                                    },
                                    "eye_examined": {
                                        "type": "string",
                                        "description": "OD or OS."
                                    }
                                },
                                "required": [
                                    "faz_area_mm2",
                                    "faz_perimeter_mm"
                                ]
                            }
                        }
                    ]
                }
            }
            sys.stdout.write(json.dumps(res) + "\n")
            sys.stdout.flush()

        elif method == "tools/call":
            params = req.get("params", {})
            name = params.get("name")
            args = params.get("arguments", {})

            if name == "evaluate_faz":
                try:
                    out = client.evaluate_faz(**args)
                    res = {
                        "jsonrpc": "2.0",
                        "id": msg_id,
                        "result": {
                            "content": [{"type": "text", "text": json.dumps(out, indent=2)}]
                        }
                    }
                except Exception as e:
                    res = {
                        "jsonrpc": "2.0",
                        "id": msg_id,
                        "isError": True,
                        "error": {"code": -32000, "message": str(e)}
                    }
                sys.stdout.write(json.dumps(res) + "\n")
                sys.stdout.flush()


if __name__ == "__main__":
    main()
