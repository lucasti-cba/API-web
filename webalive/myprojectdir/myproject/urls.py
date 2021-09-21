"""myproject URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import include, path
from myproject import settings
from django.conf.urls.static import static
from rest_framework import routers
from app.api import *
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

api_router = routers.DefaultRouter()
api_router.register(r"loja", LojaDetail)
api_router.register(r"endereco", EnderecoDetail)



urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('unimagem.urls')),
    path('app/', include('app.urls')),
    path('unimagem/', include('unimagem.urls')),
    path("api/", include(api_router.urls)),
    path('api/token/', TokenObtainPairView.as_view()),
    path('api/token/refresh/', TokenRefreshView.as_view()),
    path('api/auth/', include('djoser.urls.authtoken')),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
if settings.DEBUG:
    urlpatterns = urlpatterns + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
