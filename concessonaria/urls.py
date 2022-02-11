"""concessonaria URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
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
from django.urls import path, include

from rest_framework import routers
from carros import views

router = routers.DefaultRouter()
router.register(r'carros-viewset', views.CarrosViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('carrosx/', views.carros),
    path('main/', views.pag),
    path('carros/', views.CarroView.as_view()),
    path('carros/<int:id>/', views.CarroView.as_view()),
    path('carros-apiview/', views.CarroList.as_view()),
    path('carros-apiview/<int:id>/', views.CarroDetail.as_view()),
    path('carros-generic/', views.CarrosListGeneric.as_view()),
    path('carros-generic/<int:id>/', views.CarroDetailGeneric.as_view()),
    path('', include(router.urls))
]
