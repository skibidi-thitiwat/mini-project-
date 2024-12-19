from django.contrib import admin
from django.urls import path, include
from .views import Home, Nextpage

urlpatterns = [
    path('', Home, name='Home'),
    path('index/', Nextpage, name='index'),
]