import hcl2
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]


def normalize(value):
    if isinstance(value, str):
        if value.startswith('"') and value.endswith('"'):
            try:
                return json.loads(value)
            except json.JSONDecodeError:
                return value
        return value

    if isinstance(value, list):
        return [normalize(item) for item in value]

    if isinstance(value, dict):
        return {
            normalize(key): normalize(val)
            for key, val in value.items()
            if key != "__is_block__"
        }

    return value

resources = []

for file in (ROOT / "terraform").rglob("*.tf"):
    with file.open(encoding="utf-8") as f:
        config = normalize(hcl2.load(f))

    for block in config.get("resource", []):
        for resource_type, instances in block.items():
            for name, settings in instances.items():
                resources.append({
                    "type": resource_type,
                    "name": name,
                    "config": settings
                })

if not resources:
    raise RuntimeError("No Terraform resources found.")

output = ROOT / "terraform-input.json"

output.write_text(
    json.dumps({"resources": resources}, indent=2),
    encoding="utf-8"
)

print(f"Converted {len(resources)} Terraform resources.")