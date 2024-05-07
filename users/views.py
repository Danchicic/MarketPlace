from django.shortcuts import render
from django.views.generic import CreateView
from .forms import CreateUserForm


# Create your views here.
class Registration(CreateView):
    template_name = 'users/registration.html'
    success_url = 'catalog:index'
    form_class = CreateUserForm
