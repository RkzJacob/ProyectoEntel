from django import forms
from django.forms import ModelForm
from .models import PRODUCTO

class ProductoForm(ModelForm):
    
    class Meta:
        model = PRODUCTO
        fields = ['nombre','precio','stock','desc','fabricante','imagenProducto','nom_tipo_producto']
    

