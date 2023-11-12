from django.db import models
from user_management.models import User
import uuid


# Create your models here.
class Category(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=100)
    createdAt = models.DateTimeField(auto_now=True)
    isActive = models.BooleanField(default=True)
    pharmacyId = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.name


class Product(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    code = models.CharField(max_length=100)
    createdAt = models.DateTimeField(auto_now=True)
    isActive = models.BooleanField(default=True)
    sellingPrice = models.PositiveBigIntegerField()
    totalStock = models.PositiveIntegerField()
    pharmacyId = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.name


class Stock(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    productId = models.ForeignKey(Product, on_delete=models.CASCADE)
    pharmacyId = models.ForeignKey(User, on_delete=models.CASCADE)
    quantity = models.PositiveBigIntegerField()
    pricePerProduct = models.PositiveIntegerField()
    expiryDate = models.DateField()
    createdAt = models.DateTimeField(auto_now=True)
    isActive = models.BooleanField(default=True)


class Sell(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    pharmacyId = models.ForeignKey(User, on_delete=models.CASCADE)
    quantity = models.PositiveBigIntegerField()
    totalPrice = models.PositiveBigIntegerField()
    createdAt = models.DateTimeField(auto_now=True)
    isActive = models.BooleanField(default=True)


class SellProduct(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    pharmacyId = models.ForeignKey(User, on_delete=models.CASCADE)
    sellId = models.ForeignKey(Sell, on_delete=models.CASCADE)
    quantity = models.PositiveBigIntegerField()
    pricePerProduct = models.PositiveIntegerField()


class Client(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    pharmacyId = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=250)
    email = models.EmailField()
    pharmacyName = models.CharField(max_length=250)
    createdAt = models.DateTimeField(auto_now=True)
    isActive = models.BooleanField(default=True)

    def __str__(self):
        return self.name


class Debt(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    clientId = models.ForeignKey(Client, on_delete=models.CASCADE)
    totalPrice = models.PositiveBigIntegerField()
    createdAt = models.DateTimeField(auto_now=True)
    isActive = models.BooleanField(default=True)


class DebtProduct(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    debtId = models.ForeignKey(Debt, on_delete=models.CASCADE)
    pharmacyId = models.ForeignKey(User, on_delete=models.CASCADE)
    quantity = models.PositiveBigIntegerField()
    pricePerProduct = models.PositiveIntegerField()





