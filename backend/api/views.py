import json
from django.forms.models import model_to_dict
from django.http import HttpResponse, HttpRequest, JsonResponse

from products.models import Product

def api_home(request: HttpRequest, *args, **kargs):
    model_data = Product.objects.all().order_by('?').first()
    data = {}
    if model_data:
        data = model_to_dict(model_data, fields=['id', 'title', 'price'])
    return JsonResponse(data)
