
import json
import datetime
from azure.storage.blob import BlobServiceClient

CONNECTION_STRING = ""
CONTAINER_NAME = "sensordata"

data = {
    "soilMoisture": 34,
    "lightLevel": 250,
    "timestamp": str(datetime.datetime.utcnow())
}

blob_service_client = BlobServiceClient.from_connection_string(CONNECTION_STRING)
container_client = blob_service_client.get_container_client(CONTAINER_NAME)

blob_name = f"reading_{datetime.datetime.utcnow().isoformat()}.json"
blob_client = container_client.get_blob_client(blob_name)

blob_client.upload_blob(json.dumps(data), overwrite=True)
print(f"Dane zostały zapisane jako {blob_name}")
