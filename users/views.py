from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic import CreateView
from .forms import CreateUserForm


# Create your views here.
class Registration(CreateView):
    template_name = 'users/registration_html.html'
    success_url = reverse_lazy('catalog:index')
    form_class = CreateUserForm
    extra_context = {'title': 'Registration'}
