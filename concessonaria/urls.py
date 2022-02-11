from django.contrib import admin
from django.urls import path, include

from rest_framework import routers
from carros import views

router = routers.DefaultRouter()
router.register(r'tipos-viewset', views.TiposViewSet)
router.register(r'marcas-viewset', views.MarcaViewSet)
router.register(r'mecanicos-viewset', views.MecanicosViewSet)
router.register(r'anos-viewset', views.AnosViewSet)
router.register(r'carros-viewset', views.CarroViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('teste/', views.teste),
    path('teste2/', views.teste2),
    path('carros-class/', views.CarroView.as_view()),
    path('carros-class/<int:id>/', views.CarroView.as_view()),
    path('carros-apiview/', views.CarroList.as_view()),
    path('carros-apiview/<int:id>/', views.CarroDetail.as_view()),
    path('carros-generic/', views.CarrosListGeneric.as_view()),
    path('carros-generic/<int:id>/', views.CarroDetailGeneric.as_view()),
    path('', include(router.urls))
]
