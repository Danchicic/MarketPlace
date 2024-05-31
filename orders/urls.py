from django.urls import path
from . import views

app_name = 'orders'
urls = [
    path('', views.CreateOrder.as_view(), name='create_order')
]
