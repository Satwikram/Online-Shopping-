from django.contrib import admin
from django.urls import path
from django.conf import settings
from . import views
from .views import *
from django.conf.urls.static import static


urlpatterns = [
                # Django URLS
                path('', views.Main, name = 'main'),
                path('collection', views.collection, name = 'collection'),
                path('sell', views.sell, name = 'sell'),
                path('buy/<str:slug>', views.buy, name = 'buy'),
                path('search', views.search, name = "search"),
                path('addcart/<str:slug>', views.addcart, name = 'addcart'),
                path('checkout', views.checkout, name = 'checkout'),

                # Django RestAPI URLS
                path('search/', SearchListAPIView.as_view(), name = "search"),
                path('products/', ProductsAPIView.as_view(), name = "products"),
                path('details/<str:slug>', ProductDetailsAPIView.as_view(), name = "ProductDetails"),
                path('add-to-cart', CartAPIView.as_view(), name="addcart"),

]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

