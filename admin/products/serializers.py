from rest_framework import serializers
from .models import Product


class ProductSerializers(serializers):
    class Meta:
        model = Product
        feilds = "__all__"
