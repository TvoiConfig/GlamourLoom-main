from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [

    path('', views.index, name='index'),
    path('orders', views.orders, name = 'orders')   
] + static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)