from django.contrib.auth import get_user_model
from django.db import models

from market.models import Product

user = get_user_model()


# Create your models here.
class Cart(models.Model):
    user = models.ForeignKey(user, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)


class Order(models.Model):
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE)
    address = models.CharField(max_length=150)
    comment = models.TextField()
