from .models import Product
from rest_framework import viewsets
from rest_framework.response import Response
from .serializers import ProductSerializers


class ProductViewSet(viewsets.ViewSet):
    def list(self, request):  # /api/products
        products=Product.objects.all()
        serializer=ProductSerializers(products,many=True)
        return Response(serializer.data)

    def create(self, request):  # /api/products
        pass

    def retrieve(self, request, pk=None):  # /api/products/<str:id>
        pass
    
    def update(self, request, pk=None):  # /api/products/<str:id>
        pass
    
    def destroy(self, request, pk=None):  # /api/products/<str:id>
        pass