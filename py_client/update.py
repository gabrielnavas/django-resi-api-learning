import pprint
import requests

endpoint = "http://127.0.0.1:8000/api/products/1/update"

data = {
    "title": "hello my old friend",
    "price": 123.12,
}
response = requests.put(endpoint, json=data)
pprint.pprint(response.json())