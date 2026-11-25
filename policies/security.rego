
package security

import rego.v1

deny contains msg if 
    some resource in input.resources
    resource.type == "aws_security_group"

    some ingress in object.get(resource.config, "ingress", [])
    ingress.from_port <= 22
    ingress.to_port >= 22

    "0.0.0.0/0" in ingress.cidr_blocks

    msg := sprintf(
        "CRITICAL: %s exposes SSH to the internet",
        [resource.name]
    )
}
