from django.contrib import admin
from .models import *

# Register your models here.
admin.site.register(Category)
admin.site.register(Product)
admin.site.register(Stock)
admin.site.register(Sell)
admin.site.register(SellProduct)
admin.site.register(Client)
admin.site.register(Debt)
admin.site.register(DebtProduct)
