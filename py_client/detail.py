import pprint
import requests

endpoint = "http://127.0.0.1:8000/api/products/2/"

response = requests.get(endpoint)
pprint.pprint(response.json())