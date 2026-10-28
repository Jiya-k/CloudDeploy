
def audit_resources(resources):
    findings = []

    for resource in resources:
        resource_id = resource.get("id", "unknown")
        resource_type = resource.get("type", "unknown")
        properties = resource.get("properties") or {}
        tags = resource.get("tags") or {}

        # Rule 1: Check whether public network access is enabled.
        if properties.get("publicNetworkAccess") == "Enabled":
            findings.append({
                "resource_id": resource_id,
                "resource_type": resource_type,
                "severity": "warning",
                "rule": "PUBLIC_NETWORK_ACCESS",
                "message": "Public network access is enabled."
            })

        # Rule 2: Check whether the environment tag is missing.
        if not tags.get("environment"):
            findings.append({
                "resource_id": resource_id,
                "resource_type": resource_type,
                "severity": "info",
                "rule": "MISSING_ENVIRONMENT_TAG",
                "message": "The resource has no environment tag."
            })

    return {
        "resources_scanned": len(resources),
        "findings_count": len(findings),
        "findings": findings
    }
