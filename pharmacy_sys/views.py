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
            stockId = request.GET.get("")
            queryset = Stock.objects.filter(id=stockId)
            serialized = StockGetSerializer(instance=queryset, many=True)
            return Response(serialized.data)
        else:
            return Response({"message": "Specify the querying type"})

