from django.contrib.postgres.fields import ArrayField
from django.db import models
from django.contrib.auth.models import AbstractUser
import uuid


# Create your models here.
class User(AbstractUser):
    ADMIN = 1
    PHARMACY = 2

    ROLE_CHOICES = (
        (ADMIN, "System admin"),
        (PHARMACY, "pharmacy owner"),

    )

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    username = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    pharmacyName = models.CharField(max_length=250)
    profile = models.ImageField(upload_to="uploads/", null=True, blank=True)
    userType = models.PositiveIntegerField(choices=ROLE_CHOICES, default=PHARMACY)
    created_at = models.DateTimeField(auto_now=True)
    phone_number = models.CharField(max_length=12, unique=True)
    location = models.CharField(max_length=250)
    is_active = models.BooleanField(default=True)

    USERNAME_FIELD = "username"

    def __str__(self):
        return self.username

    class Meta:
        db_table = 'user'

