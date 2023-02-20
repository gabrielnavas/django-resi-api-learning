import pprint
import requests

endpoint = "http://127.0.0.1:8000/api/products/"

data = {
    "title": "eita",
    # "content": "bla",
    "price": 123.12
}
response = requests.post(url=endpoint, json=data)
pprint.pprint(response.json())