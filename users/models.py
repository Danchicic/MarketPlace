from django.contrib.auth import get_user_model
from django.core.validators import RegexValidator
from django.db import models

# Create your models here.
User = get_user_model()


class Client(User):
    user = User
    phone_regex = RegexValidator(regex=r'^\+?1?\d{9,15}$',
                                 message="Phone number must be entered in the format: '+999999999'. Up to 15 digits allowed.")

    phone = models.CharField(max_length=17, null=False, blank=False, unique=True, validators=[phone_regex])
