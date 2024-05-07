from django.conf import settings
from django.conf.urls.static import static
from django.urls import path

from . import views

app_name = 'catalog'
urlpatterns = [
    path('', views.Registration.as_view(), name="registration"),

]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)
