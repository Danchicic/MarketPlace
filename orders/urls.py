from django.urls import path
from . import views

app_name = 'orders'

urlpatterns = [
    path('', views.UserOrders.as_view(), name='view_orders'),
    path('createorder/', views.CreateCart.as_view(), name='create_order'),
    path("sendorder/", views.CreateOrder.as_view(), name='send_order')
]
