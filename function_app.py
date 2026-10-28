
import json

import azure.functions as func

from src.azure_inventory import get_azure_resources
from src.audit import audit_resources

app = func.FunctionApp(
    http_auth_level=func.AuthLevel.FUNCTION
)


@app.route(
    route="audit",
    methods=["GET", "POST"],
    auth_level=func.AuthLevel.FUNCTION
)
def audit(req: func.HttpRequest) -> func.HttpResponse:
    try:
        resources = get_azure_resources()
        report = audit_resources(resources)

        return func.HttpResponse(
            json.dumps(report),
            status_code=200,
            mimetype="application/json"
        )

    except Exception:
        return func.HttpResponse(
            json.dumps({
                "error": "The Azure resource audit failed. Check the Function logs."
            }),
            status_code=500,
            mimetype="application/json"
        )
