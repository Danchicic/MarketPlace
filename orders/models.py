from django.contrib.auth import get_user_model
from django.db import models

from market.models import Product

User = get_user_model()


# Create your models here.
class Cart(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    date_create = models.DateTimeField(auto_now=True)


class CartProduct(models.Model):
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)


class Order(models.Model):
    name = models.CharField(max_length=20, unique=False)
    address = models.CharField(max_length=150, unique=False)
    comment = models.TextField(null=True)
    country = models.CharField(max_length=50)
    date_create = models.DateTimeField(auto_now=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=False)
    cart = models.OneToOneField(Cart, on_delete=models.CASCADE)
