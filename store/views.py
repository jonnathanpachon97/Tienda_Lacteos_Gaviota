from django.shortcuts import render
from .models import Producto

# Create your views here.
def inicio(request):
    return render(request, 'tienda/base.html')

def catalogo(request):
    productos = Producto.objects.all()
    return render(request, 'tienda/catalogo.html', {'productos': productos})