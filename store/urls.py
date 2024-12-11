from django.urls import path
from . import views

urlpatterns = [
    path('', views.inicio, name='inicio'),  # URL de inicio, asignándole el nombre 'inicio'
    path('crear_producto/', views.crear_producto, name='crear_producto'),
    path('catalogo/', views.catalogo, name='catalogo'), # URL del catálogo
]