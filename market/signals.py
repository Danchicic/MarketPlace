from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import Shop, Review, Product


@receiver(post_save, sender=Shop)
def create_shop_review(instance, created, **kwargs):
    if created:
        shop_review = Review.objects.create()
        instance.review_id = shop_review.id
        instance.save()


@receiver(post_save, sender=Product)
def create_product_review(instance, created, **kwargs):
    if created:
        shop_review = Product.objects.create()
        instance.review_id = shop_review.id
        instance.save()
