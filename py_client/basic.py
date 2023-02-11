import pprint
import requests

endpoint = "http://127.0.0.1:8000/api?a=2"

response = requests.get(
    endpoint, 
    params={"abc": 123}, 
    json={"query": "hello"}
)
pprint.pprint(response.json())