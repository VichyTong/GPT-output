import os
import json
from elasticsearch import Elasticsearch

client = Elasticsearch(
  "https://5291253bb9a34a23aaaa6322d07a0f63.asia-east1.gcp.elastic-cloud.com:443",
  api_key="UEZ5WU80c0JaYzZnNHdpVGd1ajU6aU5kc1ZoS1BSdG16VnZMWHQ1b1BkZw=="
)

directory = "./input/protocols/"


for _, _, filenames in os.walk(directory):
    for filename in filenames:
        with open(directory + filename, "r") as f:
            data = json.load(f)
            for content in data["content"]:
                if content["header"] == "Procedure":
                    documents = []
                    procedure = content["content"]
                    documents.append({
                        "index": {
                            "_index": "search-test",
                        }
                    })
                    documents.append({
                        "name": filename,
                        "procedure": procedure
                    })
                    client.bulk(operations=documents, pipeline="ent-search-generic-ingestion")
