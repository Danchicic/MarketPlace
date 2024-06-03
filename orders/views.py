from django.shortcuts import render
from django.views.generic import CreateView, View


# from .models import Order


# Create your views here.
class CreateOrder(View):
    template_name = "orders/index.html"
    # model = Order
