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
        model = Product
        fields = "__all__"
        depth = 2


class ProductPostSerializer(serializers.Serializer):
    class Meta:
        model = Product
        fields = [
            "name",
            "pharmacyId",
            "category",
            "code",
            "sellingPrice",
            "totalStock",
            "pic"
        ]


class StockGetSerializer(serializers.Serializer):
    class Meta:
        model = Stock
        fields = "__all__"
        depth = 2


class StockPostSerializer(serializers.Serializer):
    class Meta:
        model = Stock
        fields = [
            "productId",
            "pharmacyId",
            "quantity",
            "pricePerProduct",
            "pricePerProduct"
        ]


class SellGetSerializer(serializers.Serializer):
    class Meta:
        model = Sell
        fields = "__all__"
        depth = 2


class SellPostSerializer(serializers.Serializer):
    class Meta:
        model = Sell
        fields = [
            "pharmacyId",
            "quantity",
            "totalPrice"
        ]


class ProductSellsGetSerializer(serializers.Serializer):
    class Meta:
        model = SellProduct
        fields = "__all__"
        depth = 2


class ProductSellsPostSerializer(serializers.Serializer):
    class Meta:
        model = SellProduct
        fields = [
            "product",
            "sellId",
            "quantity",
            "pricePerProduct"
        ]


class ClientsGetSerializer(serializers.Serializer):
    class Meta:
        model = Client
        fields = "__all__"
        depth = 2


class ClientsPostSerializer(serializers.Serializer):
    class Meta:
        model = Client
        fields = [
            "pharmacyId",
            "name",
            "email",
            "pharmacyName",
            "phone_number"
        ]


class DebtsGetSerializer(serializers.Serializer):
    class Meta:
        model = Debt
        fields = "__all__"
        depth = 2


class DebtsPostSerializer(serializers.Serializer):
    class Meta:
        model = Debt
        fields = [
            "clientId",
            "totalPrice"
        ]


class ProductsDebtsGetSerializer(serializers.Serializer):
    class Meta:
        model = DebtProduct
        fields = "__all__"
        depth = 2


class ProductsDebtsPostSerializer(serializers.Serializer):
    class Meta:
        model = DebtProduct
        fields = [
            "debtId",
            "product",
            "quantity",
            "pricePerProduct"
        ]


