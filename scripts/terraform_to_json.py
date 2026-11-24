
import hcl2
import json
from pathlib import Path

resources = []

for file in Path("terraform").rglob("*.tf"):
    with file.open(encoding="utf-8") as f:
        config = hcl2.load(f)

    for block in config.get("resource", []):
        for resource_type, instances in block.items():
            for name, settings in instances.items():
                resources.append({
                    "type": resource_type,
                    "name": name,
                    "config": settings
                })

Path("terraform-input.json").write_text(
    json.dumps({"resources": resources}, indent=2)
)

print("Terraform converted to JSON")
