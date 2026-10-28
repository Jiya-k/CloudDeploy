
import json
from collections import Counter
from dotenv import load_dotenv

from src.azure_inventory import get_azure_resources
from src.audit import audit_resources


load_dotenv()


def main():
    print("\n========== AZURE RESOURCE INVENTORY ==========\n")

    resources = get_azure_resources()

    total_resources = len(resources)
    print(f"Total Resources Found: {total_resources}")

    # Count resources by type
    type_counts = Counter(
        resource.get("type", "Unknown")
        for resource in resources
    )

    print("\n--- Resources by Resource Type ---")
    for resource_type, count in sorted(type_counts.items()):
        print(f"{resource_type:<50} : {count}")

    # Count resources by resource group
    group_counts = Counter(
        resource.get("resourceGroup", "Unknown")
        for resource in resources
    )

    print("\n--- Resources by Resource Group ---")
    for resource_group, count in sorted(group_counts.items()):
        print(f"{resource_group:<50} : {count}")

    # Display all returned resources
    print("\n--- Complete Resource List ---")
    print(f"{'Name':<35} {'Resource Type':<45} {'Resource Group':<30}")
    print("-" * 110)

    for resource in sorted(
        resources,
        key=lambda item: (
            item.get("resourceGroup", ""),
            item.get("name", "")
        )
    ):
        print(
            f"{resource.get('name', 'Unknown'):<35} "
            f"{resource.get('type', 'Unknown'):<45} "
            f"{resource.get('resourceGroup', 'Unknown'):<30}"
        )

    # Run the existing security audit
    report = audit_resources(resources)

    print("\n========== SECURITY AUDIT SUMMARY ==========\n")
    print(f"Resources Audited: {total_resources}")
    print(f"Total Findings: {report['findings_count']}")
    print(json.dumps(report, indent=2))


if __name__ == "__main__":
    main()
