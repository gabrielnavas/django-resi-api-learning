import pprint
import requests

endpoint = "http://127.0.0.1:8000/api"

response = requests.get(
    endpoint, 
)
pprint.pprint(response.json())