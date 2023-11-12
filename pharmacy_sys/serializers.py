from rest_framework import serializers
from .models import *


class CategoryGetSerializer(serializers.Serializer):
    class Meta:
        model = Category
        fields = "__all__"
        depth = 2


class CategoryPostSerializer(serializers.Serializer):
    class Meta:
        model = Category
        fields = [
            "name",
            "pharmacyId"
        ]


class ProductGetSerializer(serializers.Serializer):
    class Meta:
        model = Category
        fields = "__all__"
        depth = 2


class ProductPostSerializer(serializers.Serializer):
    class Meta:
        model = Category
        fields = [
            "name",
            "pharmacyId",
            "category",
            "code",
            "sellingPrice",
            "totalStock"
        ]


class StockGetSerializer(serializers.Serializer):
    class Meta:
        model = Category
        fields = "__all__"
        depth = 2


class StockPostSerializer(serializers.Serializer):
    class Meta:
        model = Category
        fields = [
            "productId",
            "pharmacyId",
            "quantity",
            "pricePerProduct",
            "pricePerProduct"
        ]


