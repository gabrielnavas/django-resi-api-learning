import pprint
import requests

endpoint = "http://127.0.0.1:8000/api"

# response = requests.get(
#     endpoint, 
# )
# pprint.pprint(response.json())


response = requests.post(
    endpoint, 
    json={
        "title": None,
        "content": "galinha boa",
        "price": None
    }
)
pprint.pprint(response.json())