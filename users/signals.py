from django.contrib.auth import get_user_model
from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import Client

user = get_user_model()


@receiver(post_save, sender=user)
def create_shop_review(instance, created, **kwargs):
    if created:
        client = Client.objects.create()
        instance.review_id = client.id
        instance.save()
