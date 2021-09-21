from django.contrib import admin
from django.urls import path, include
from . import views
from rest_framework import routers

urlpatterns = [
    path('', views.index, name ='index'),
    path('cadastrar_usuario', views.cadastrar_usuario, name="cadastrar_usuario"),
    path('login', views.logar_usuario, name="logar_usuario"),
    path('logout', views.logout, name="logoutt"),
]

