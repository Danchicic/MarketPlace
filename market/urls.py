from django.conf import settings
from django.conf.urls.static import static
from django.urls import path

from . import views

app_name = 'catalog'
urlpatterns = [
    path('', views.CatalogView.as_view(), name="index"),
    path('<slug:shop_address>/', views.ShopView.as_view(), name="shop"),

]
