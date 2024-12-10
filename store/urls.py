from django.urls import path
from . import views

urlpatterns = [
    path('', views.inicio, name='inicio'),  # URL de inicio, asignándole el nombre 'inicio'
    path('catalogo/', views.catalogo, name='catalogo'), # URL del catálogo
]