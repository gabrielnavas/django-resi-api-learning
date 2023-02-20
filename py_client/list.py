import pprint
import requests

endpoint = "http://127.0.0.1:8000/api/products/"

response = requests.get(url=endpoint)
pprint.pprint(response.json())