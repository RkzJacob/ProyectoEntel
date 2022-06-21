from django import forms
from django.forms import ModelForm
from .models import PRODUCTO

class ProductoForm(ModelForm):
    
    class Meta:
        model = PRODUCTO
        fields = ['id_producto','nombre','precio','stock','desc','nombre_fabricante','imagenProducto','nom_tipo_producto']
    

