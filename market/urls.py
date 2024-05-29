from django.conf import settings
from django.conf.urls.static import static
from django.urls import path

from . import views

app_name = 'catalog'
urlpatterns = [
    path('', views.CatalogView.as_view(), name="index"),
    path('<slug:shop_address>/', views.ShopView.as_view(), name="shop"),
    path('<slug:shop_address>/<int:product_id>', views.ProductView.as_view(), name="shop"),

]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
