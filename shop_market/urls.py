from django.conf import settings
from django.conf.urls.static import static
from django.urls import path

from . import views

app_name = "shop"

urlpatterns = [
    path('', views.ShopIndexView.as_view(), name='index'),
    path('orders/', views.ShopOrdersView.as_view(), name='orders')
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
