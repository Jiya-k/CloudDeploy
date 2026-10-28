
import json
from pathlib import Path

from src.audit import audit_resources

# Find the sample data file relative to this script.
data_file = Path(__file__).parent / "sample-data" / "resources.json"

# Read the JSON file and convert it into Python data.
with data_file.open("r", encoding="utf-8") as file:
    resources = json.load(file)

# Run our audit rules.
report = audit_resources(resources)

# Display the report in a readable format.
print(json.dumps(report, indent=2))
