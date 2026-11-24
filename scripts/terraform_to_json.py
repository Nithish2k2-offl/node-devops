
import hcl2
import json
from pathlib import Path

def clean(value):
    if isinstance(value, str):
        return value.strip('"')
    if isinstance(value, list):
        return [clean(v) for v in value]
    if isinstance(value, dict):
        return {k: clean(v) for k, v in value.items()}
    return value

resources = []

for file in Path("terraform").rglob("*.tf"):
    with file.open(encoding="utf-8") as f:
        config = hcl2.load(f)

    for block in config.get("resource", []):
        for resource_type, instances in block.items():
            for name, settings in instances.items():
                resources.append({
                    "type": clean(resource_type),
                    "name": clean(name),
                    "config": clean(settings)
                })

Path("terraform-input.json").write_text(
    json.dumps({"resources": resources}, indent=2)
)

print("Terraform converted to JSON")
