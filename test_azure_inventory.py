
import json
import os

from azure.identity import AzureCliCredential
from azure.mgmt.resourcegraph import ResourceGraphClient
from azure.mgmt.resourcegraph.models import QueryRequest


# Use the subscription ID from the environment.
subscription_id = os.environ.get("AZURE_SUBSCRIPTION_ID")

if not subscription_id:
    raise RuntimeError(
        "Set AZURE_SUBSCRIPTION_ID to your test subscription ID."
    )

# Authenticate using your existing Azure CLI login.
credential = AzureCliCredential()
client = ResourceGraphClient(credential)

request = QueryRequest(
    subscriptions=[subscription_id],
    query="""
        Resources
        | project name, type, resourceGroup, location
        | limit 5
    """,
)

response = client.resources(request)

print(json.dumps(response.data, indent=2))
