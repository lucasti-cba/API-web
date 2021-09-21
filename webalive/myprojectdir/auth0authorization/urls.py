# auth0authorization/urls.py

from django.urls import path, include

from . import views

urlpatterns = [
    path('public', views.public),
    path('private', views.private),
    path('private-scoped', views.private_scoped),
    path('login', views.loginAPI),
    path('', include('django.contrib.auth.urls')),
    path('', include('social_django.urls')),
]