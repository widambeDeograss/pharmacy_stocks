from django.urls import path
from .views import *

app_name = 'pharmacy_sys'

urlpatterns = [
   path("product_categories", Categories.as_view()),
   path("products", Products.as_view()),
]