
import json

from src.azure_inventory import get_azure_resources
from src.audit import audit_resources


resources = get_azure_resources()
report = audit_resources(resources)

print(json.dumps(report, indent=2))
