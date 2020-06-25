from django.contrib import admin
from django.urls import path

from django.conf import settings
from . import views
from django.conf.urls.static import static


urlpatterns = [

                path('', views.Main, name = 'main'),
                path('collection', views.collection, name = 'collection'),
                path('sell', views.sell, name = 'sell'),
                path('buy', views.buy, name = 'buy'),


]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

