from django.urls import path
from .views import *

app_name = 'pharmacy_sys'

urlpatterns = [
   path("product_categories", Categories.as_view()),
   path("products", Products.as_view()),
   path("stock_mgm", StockManagement.as_view()),
   path("sells", SellManagement.as_view()),
   path("product_sells", ProductSells.as_view()),
   path("clients_mgm", Clients.as_view()),
   path("debts", DebtsManagement.as_view())
]