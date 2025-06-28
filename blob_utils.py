
from azure.storage.blob import BlobServiceClient
import json

CONNECTION_STRING = ""
CONTAINER_NAME = "sensordata"

def read_latest_blob():
    service_client = BlobServiceClient.from_connection_string(CONNECTION_STRING)
    container_client = service_client.get_container_client(CONTAINER_NAME)

    blobs = list(container_client.list_blobs())
    if not blobs:
        return {"error": "Brak danych"}

    latest_blob = sorted(blobs, key=lambda b: b.last_modified, reverse=True)[0]
    blob_client = container_client.get_blob_client(latest_blob.name)
    content = blob_client.download_blob().readall()
    return json.loads(content)
