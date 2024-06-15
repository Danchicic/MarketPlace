from django.contrib.auth import get_user_model
from django.db import models

from market.models import Product

user = get_user_model()


# Create your models here.
class Cart(models.Model):
    user = models.ForeignKey(user, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    cart_id = models.CharField(max_length=50)
    date_create = models.DateTimeField()


class Order(models.Model):
    name = models.CharField(max_length=20, unique=False)
    cart_id = models.CharField(max_length=50, unique=True)
    address = models.CharField(max_length=150, unique=False)
    comment = models.TextField(null=True)
    country = models.CharField(max_length=50)
