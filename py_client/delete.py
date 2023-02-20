import pprint
import requests

endpoint = "http://127.0.0.1:8000/api/products/2/delete"

response = requests.delete(endpoint)
pprint.pprint(response.status_code)