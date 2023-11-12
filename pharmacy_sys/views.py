from django.shortcuts import render
from rest_framework.response import Response

from .serializers import *
from rest_framework.views import APIView


class Categories(APIView):
    @staticmethod
    def post(request):
        data = request.data
        serialized = CategoryPostSerializer(data=data)
        if serialized.is_valid():
            serialized.save()
            return Response({"save": True})
        return Response({"save": False, "error": serialized.errors})

    @staticmethod
    def get(request):
        queryType = request.GET.get("queryType")
        if queryType == "all":
            queryset = Category.objects.all()
            serialized = CategoryGetSerializer(instance=queryset, many=True)
            return Response(serialized.data)
        elif queryType == "single":
            category = request.GET.get("categoryId")
            queryset = Category.objects.filter(id=category)
            serialized = CategoryGetSerializer(instance=queryset, many=True)
            return Response(serialized.data)
        elif queryType == "categoryProducts":
            category = request.GET.get("categoryId")
            queryset = Product.objects.filter(category=category)
            serialized = ProductGetSerializer(instance=queryset, many=True)
            return Response(serialized.data)
        else:
            return Response({"message": "Specify the querying type"})


class Products(APIView):
    @staticmethod
    def post(request):
        data = request.data
        serialized = ProductPostSerializer(data=data)
        if serialized.is_valid():
            serialized.save()
            return Response({"save": True})
        return Response({"save": False, "error": serialized.errors})

    @staticmethod
    def get(request):
        queryType = request.GET.get("queryType")
        if queryType == "all":
            queryset = Product.objects.all()
            serialized = ProductGetSerializer(instance=queryset, many=True)
            return Response(serialized.data)
        elif queryType == "single":
            product = request.GET.get("productId")
            queryset = Product.objects.filter(id=product)
            serialized = ProductGetSerializer(instance=queryset, many=True)
            return Response(serialized.data)
        else:
            return Response({"message": "Specify the querying type"})


class StockManagement(APIView):
    @staticmethod
    def post(request):
        data = request.data
        serialized = StockPostSerializer(data=data)
        if serialized.is_valid():
            serialized.save()
            return Response({"save": True})
        return Response({"save": False, "error": serialized.errors})

    @staticmethod
    def get(request):
        queryType = request.GET.get("queryType")
        if queryType == "all":
            queryset = Stock.objects.all()
            serialized = StockGetSerializer(instance=queryset, many=True)
            return Response(serialized.data)
        elif queryType == "single":
            stockId = request.GET.get("stockId")
            queryset = Stock.objects.filter(id=stockId)
            serialized = StockGetSerializer(instance=queryset, many=True)
            return Response(serialized.data)
        else:
            return Response({"message": "Specify the querying type"})


class SellManagement(APIView):
    @staticmethod
    def post(request):
        data = request.data
        serialized = SellPostSerializer(data=data)
        if serialized.is_valid():
            serialized.save()
            return Response({"save": True})
        return Response({"save": False, "error": serialized.errors})

    @staticmethod
    def get(request):
        queryType = request.GET.get("queryType")
        if queryType == "all":
            queryset = Sell.objects.all()
            serialized = SellGetSerializer(instance=queryset, many=True)
            return Response(serialized.data)
        elif queryType == "single":
            sellId = request.GET.get("sellId")
            queryset = Sell.objects.filter(id=sellId)
            serialized = StockGetSerializer(instance=queryset, many=True)
            return Response(serialized.data)
        elif queryType == "productsInSale":
            sellId = request.GET.get("sellId")
            queryset = SellProduct.objects.filter(sellId=sellId)
            serialized = ProductSellsGetSerializer(instance=queryset, many=True)
            return Response(serialized.data)
        else:
            return Response({"message": "Specify the querying type"})


class ProductSells(APIView):
    @staticmethod
    def post(request):
        data = request.data
        serialized = ProductSellsPostSerializer(data=data)
        if serialized.is_valid():
            try:
                product = Product.objects.get(id=request.data['product'])
                stock = Product.objects.get(productId=request.data['product'])
                product.totalStock -= request.data['quantity']
                stock.quantity -= request.data['quantity']
                product.save()
                stock.save()
                serialized.save()
                return Response({"save": True})
            except Product.DoesNotExist:
                return Response({"save": False, "error": "THe product doest exist"})
        return Response({"save": False, "error": serialized.errors})

    @staticmethod
    def get(request):
        queryType = request.GET.get("queryType")
        if queryType == "all":
            queryset = SellProduct.objects.all()
            serialized = ProductSellsGetSerializer(instance=queryset, many=True)
            return Response(serialized.data)
        elif queryType == "single":
            sellprodId = request.GET.get("sellprodId")
            queryset = SellProduct.objects.filter(id=sellprodId)
            serialized = ProductSellsGetSerializer(instance=queryset, many=True)
            return Response(serialized.data)
        else:
            return Response({"message": "Specify the querying type"})


class Clients(APIView):
    @staticmethod
    def post(request):
        data = request.data
        serialized = ClientsPostSerializer(data=data)
        if serialized.is_valid():
            serialized.save()
            return Response({"save": True})
        return Response({"save": False, "error": serialized.errors})

    @staticmethod
    def get(request):
        queryType = request.GET.get("queryType")
        if queryType == "all":
            queryset = Client.objects.all()
            serialized = ClientsGetSerializer(instance=queryset, many=True)
            return Response(serialized.data)
        elif queryType == "single":
            client = request.GET.get("client")
            queryset = Client.objects.filter(id=client)
            serialized = ClientsGetSerializer(instance=queryset, many=True)
            return Response(serialized.data)
        elif queryType == "clientDebts":
            client = request.GET.get("client")
            queryset = Debt.objects.filter(clientId=client)
            serialized = DebtsGetSerializer(instance=queryset, many=True)
            return Response(serialized.data)
        else:
            return Response({"message": "Specify the querying type"})


class DebtsManagement(APIView):
    @staticmethod
    def post(request):
        data = request.data
        serialized = ClientsPostSerializer(data=data)
        if serialized.is_valid():
            serialized.save()
            return Response({"save": True})
        return Response({"save": False, "error": serialized.errors})

    @staticmethod
    def get(request):
        queryType = request.GET.get("queryType")
        if queryType == "all":
            queryset = Debt.objects.all()
            serialized = DebtsGetSerializer(instance=queryset, many=True)
            return Response(serialized.data)
        elif queryType == "single":
            debt = request.GET.get("debt")
            queryset = Debt.objects.filter(id=debt)
            serialized = DebtsGetSerializer(instance=queryset, many=True)
            return Response(serialized.data)
        elif queryType == "debtProducts":
            debt = request.GET.get("debt")
            queryset = DebtProduct.objects.filter(debtId=debt)
            serialized = ProductsDebtsGetSerializer(instance=queryset, many=True)
            return Response(serialized.data)
        else:
            return Response({"message": "Specify the querying type"})


class DebtProducts(APIView):
    @staticmethod
    def post(request):
        data = request.data
        serialized = ProductSellsPostSerializer(data=data)
        if serialized.is_valid():
            try:
                product = Product.objects.get(id=request.data['product'])
                stock = Product.objects.get(productId=request.data['product'])
                product.totalStock -= request.data['quantity']
                stock.quantity -= request.data['quantity']
                product.save()
                stock.save()
                serialized.save()
                return Response({"save": True})
            except Product.DoesNotExist:
                return Response({"save": False, "error": "THe product doest exist"})
        return Response({"save": False, "error": serialized.errors})

    @staticmethod
    def get(request):
        queryType = request.GET.get("queryType")
        if queryType == "all":
            queryset = DebtProduct.objects.all()
            serialized = ProductsDebtsGetSerializer(instance=queryset, many=True)
            return Response(serialized.data)
        elif queryType == "single":
            debtprodId = request.GET.get("debtprodId")
            queryset = DebtProduct.objects.filter(id=debtprodId)
            serialized = ProductsDebtsGetSerializer(instance=queryset, many=True)
            return Response(serialized.data)
        else:
            return Response({"message": "Specify the querying type"})