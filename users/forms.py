from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm
from .models import Client


class CreateUserForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = Client
        fields = ('first_name', 'last_name', 'username', 'email', 'phone')
