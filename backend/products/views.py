from rest_framework import generics
from rest_framework.response import Response

from .models import Product
from .serializers import ProductSerializer

class ProductCreateAPIView(generics.CreateAPIView):
    serializer_class = ProductSerializer

    def perform_create(self, serializer: ProductSerializer):
        title = serializer.validated_data.get('title')
        content = serializer.validated_data.get('content')
        price = serializer.validated_data.get('price')
        serializer.save(
            title=title,
            content=content or title,
            price=price
        )

class ProductDetailAPIView(generics.RetrieveAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
