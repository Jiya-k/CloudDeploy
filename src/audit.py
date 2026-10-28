
def audit_resources(resources):
    findings = []

    # Apply the public network access rule only to
    # resource types where we currently support the check.
    public_access_types = {
        "microsoft.storage/storageaccounts",
        "microsoft.web/sites",
        "microsoft.sql/servers",
        "microsoft.recoveryservices/vaults",
    }

    for resource in resources:
        resource_id = resource.get("id", "unknown")
        resource_type = resource.get("type", "unknown").lower()
        properties = resource.get("properties") or {}
        tags = resource.get("tags") or {}

        # Rule 1: Public network access review.
        if (
            resource_type in public_access_types
            and properties.get("publicNetworkAccess") == "Enabled"
        ):
            findings.append({
                "resource_id": resource_id,
                "resource_type": resource_type,
                "severity": "warning",
                "rule": "PUBLIC_NETWORK_ACCESS",
                "message": "Public network access is enabled; review whether this is intended."
            })

        # Rule 2: Missing environment tag.
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
