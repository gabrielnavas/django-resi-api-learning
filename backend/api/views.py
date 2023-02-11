from django.http import JsonResponse

def api_home(request, *args, **kargs):
    return JsonResponse({
        "message": "hello world"
    })