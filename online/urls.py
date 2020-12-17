from django.contrib import admin
from django.urls import path

from . import views

urlpatterns = [
                path('home', views.home, name = 'home'),
                path('contact', views.contact, name = 'contact'),
                path('register', views.register, name = 'register'),
                path('login', views.login, name = 'login'),
                path('main', views.main, name='main'),
                path('Logout', views.Logout, name='Logout'),
                path('forgot', views.forgot, name= 'forgot' ),
                path('otp', views.otp, name='otp')
]