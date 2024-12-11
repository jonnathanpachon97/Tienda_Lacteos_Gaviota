from django import forms
from .models import Producto

class ProductoForm(forms.ModelForm):
    class Meta:
        model = Producto
        fields = ['nombre', 'descripcion', 'precio', 'categoria', 'stock', 'imagen']  # Define los campos que deseas en el formulario

    # Opcional: puedes agregar validaciones adicionales o personalizar los widgets
    descripcion = forms.CharField(widget=forms.Textarea(attrs={'rows': 4, 'cols': 40}))
    imagen = forms.ImageField(required=False)  # Si la imagen no es obligatoria
