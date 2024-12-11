from django.contrib import admin
from .models import Producto

# Register your models here.

class ProductoAdmin(admin.ModelAdmin):
    model = Producto
    list_display = ['nombre', 'descripcion', 'precio', 'categoria', 'stock']
    search_fields = ['nombre']

admin.site.register(Producto, ProductoAdmin)