
from src.audit import audit_resources


def test_audit_detects_public_access_and_missing_tag():
    resources = [
        {
            "id": "storage-account-1",
            "type": "Microsoft.Storage/storageAccounts",
            "properties": {
                "publicNetworkAccess": "Enabled"
            },
            "tags": {}
        }
    ]

    report = audit_resources(resources)

    assert report["resources_scanned"] == 1
    assert report["findings_count"] == 2

    rules_found = {
        finding["rule"]
        for finding in report["findings"]
    }

    assert "PUBLIC_NETWORK_ACCESS" in rules_found
    assert "MISSING_ENVIRONMENT_TAG" in rules_found
