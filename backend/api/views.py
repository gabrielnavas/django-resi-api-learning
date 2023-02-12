from django.http import JsonResponse, HttpRequest

from products.models import Product

def api_home(request: HttpRequest, *args, **kargs):
    model_data = Product.objects.all().order_by('?').first()
    data = {}
    if model_data:
        # manual serialization 
        data["id"] = model_data.id
        data["title"] = model_data.title
        data["content"] = model_data.content
        data["price"] = model_data.price
    return JsonResponse(data)