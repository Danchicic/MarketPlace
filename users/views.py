from django.core.handlers.wsgi import WSGIRequest
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic import CreateView, View
from .forms import CreateUserForm

from django.contrib.auth.views import LoginView
from .models import Client


# Create your views here.
class Registration(CreateView):
    template_name = 'users/registration.html'
    success_url = reverse_lazy('catalog:index')
    form_class = CreateUserForm
    extra_context = {'title': 'Registration'}


class Login(LoginView):
    template_name = 'users/login.html'
    extra_context = {'title': 'Login'}
    success_url = reverse_lazy('catalog:index')


class Profile(View):
    template_name = 'users/_profile.html'

    def get(self, request):
        return render(request, self.template_name)
