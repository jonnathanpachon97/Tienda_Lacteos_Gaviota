from django.shortcuts import render, redirect
from .forms import ProductoForm
from .models import Producto

# Create your views here.

def inicio(request):
    return render(request, 'tienda/base.html')


def catalogo(request):
    productos = Producto.objects.all()
    return render(request, 'tienda/catalogo.html', {'productos': productos})


def crear_producto(request):
    if request.method == 'POST':
        form = ProductoForm(request.POST, request.FILES)  # request.FILES es necesario para cargar archivos (imágenes)
        if form.is_valid():
            form.save()  # Guarda el nuevo producto
            return redirect('catalogo')  # Redirige a una página de lista de productos u otra
    else:
        form = ProductoForm()

    return render(request, 'tienda/crear_producto.html', {'form': form})