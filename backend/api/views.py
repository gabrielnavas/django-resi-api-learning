import json
from django.http import JsonResponse, HttpRequest

def api_home(request: HttpRequest, *args, **kargs):
    data = {}
    try:
        data = json.loads(request.body)
    except:
        pass
    data["params"] = request.GET
    data["headers"] = request.headers
    return JsonResponse({
        "data": "hello world"
    })