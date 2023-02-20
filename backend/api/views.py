from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.exceptions import ValidationError

from products.models import Product
from products.serializers import ProductSerializer

# @api_view(["GET"])
# def get_product(request, *args, **kargs):
#     """
#     DRF API View
#     """
#     instance = Product.objects.last()
#     data = {}
#     if instance:
#         # data = model_to_dict(instance, fields=['id', 'title', 'price', 'sale_price'])
#         data = ProductSerializer(instance).data
#     return Response(data)

@api_view(["POST"])
def create_post (request, *args, **kargs):
    """
    DRF API View
    """
    try:
        serializer = ProductSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            instance = serializer.save()
            print(instance)
            return Response(serializer.data)
        return Response(serializer.data)
    except Exception as ex:
        print(type(ex))
        if isinstance(ex, ValidationError):
            return Response(ex.detail, status=400)
        return Response({
            "detail": "server error"
        }, status=500)
