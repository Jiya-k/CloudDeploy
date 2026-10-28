
# CloudDeploy

CloudDeploy is a Python-based Azure resource health and deployment audit platform.

## Current features

- Scans sample Azure resource data in JSON format.
- Flags resources where public network access is enabled.
- Identifies resources missing an environment tag.
- Generates a structured audit report.
- Includes automated tests using pytest.

## Run locally

### Requirements

- Python 3.13 or compatible Python version
- pytest

### Run the audit

```powershell
python run_audit.py
```

### Run automated tests

```powershell
python -m pytest -v
```

## Roadmap

- [ ] Improve resource-specific audit rules
- [ ] Add more automated tests
- [ ] Set up GitHub Actions CI
- [ ] Integrate Azure Resource Graph
- [ ] Add Terraform infrastructure
- [ ] Explore deployment automation and Kubernetes
