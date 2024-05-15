from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator

percentage_validator = [MinValueValidator(0), MaxValueValidator(100)]


# Create your models here.

class Review(models.Model):
    worth_it = models.DecimalField(decimal_places=0, max_digits=3, validators=percentage_validator, default=0)
    accuracy = models.DecimalField(decimal_places=0, max_digits=3, validators=percentage_validator, default=0)
    delivery = models.DecimalField(decimal_places=0, max_digits=3, validators=percentage_validator, default=0)
    rating = models.DecimalField(max_digits=3, decimal_places=2, default=0)
    reviews_count = models.IntegerField(default=0)


class Shop(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    review = models.ForeignKey(Review, on_delete=models.CASCADE, null=True)
    address = models.SlugField(unique=True, blank=False, null=False)
    preview = models.ImageField(upload_to=f'media/shops/{name}/',
                                db_default='/Users/danya/CodeProject/djangoMarketPlace/static/img/catalog/kates.png',
                                default='/Users/danya/CodeProject/djangoMarketPlace/static/img/catalog/kates.png')
    views_count = models.IntegerField(default=0, db_default=0)

    def __str__(self):
        return self.name + ', ' + self.address


class Categories(models.Model):
    name = models.CharField(max_length=25)


class Product(models.Model):
    name = models.CharField(max_length=100)
    price = models.IntegerField()
    product_description = models.TextField(default='', db_default='', null=False)
    key_features = models.TextField(default='', db_default='', null=False)
    review = models.ForeignKey(Review, on_delete=models.CASCADE, null=True)
    shop = models.ForeignKey(Shop, on_delete=models.CASCADE)
    preview = models.ImageField(
        upload_to=f'media/shops/{shop.name}/',
        default='/Users/danya/CodeProject/djangoMarketPlace/static/img/catalog/default_product_view.jpeg')
    category = models.ForeignKey(Categories, on_delete=models.CASCADE)
