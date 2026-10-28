
import os

from azure.identity import AzureCliCredential, DefaultAzureCredential
from azure.mgmt.resourcegraph import ResourceGraphClient
from azure.mgmt.resourcegraph.models import QueryRequest


def get_azure_resources():
    subscription_id = os.environ.get("AZURE_SUBSCRIPTION_ID")

    if not subscription_id:
        raise ValueError(
            "AZURE_SUBSCRIPTION_ID environment variable is required."
        )

    # Use Azure CLI login for local testing.
    # Use managed identity when running in Azure.
    if os.environ.get("AZURE_USE_CLI_CREDENTIAL", "").lower() == "true":
        credential = AzureCliCredential()
    else:
        credential = DefaultAzureCredential()

    client = ResourceGraphClient(credential)

    request = QueryRequest(
        subscriptions=[subscription_id],
        query="""
            Resources
            | project id, name, type, resourceGroup, location, tags, properties
            | limit 100
        """,
    )

    response = client.resources(request)
    return response.data
