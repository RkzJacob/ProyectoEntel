from django.shortcuts import render
from django.contrib import messages
from .forms import ProductoForm
from .models import PRODUCTO

# Create your views here.

def registrarProductos(request):
    Producto =PRODUCTO.objects.all()
    datos={
        'Producto' :Producto,
        'form': ProductoForm
    }
    if request.method == 'POST':
        formulariod= ProductoForm(request.POST,request.FILES)

        if formulariod.is_valid:
            formulariod.save()
            messages.success(request,"Datos guardados correctamente")
        else:
            messages.error(request,"No te has registrado correctamente")

    return render(request,'registrarProductos.html',datos)

def catalogoDeOfertas(request):
    producto = PRODUCTO.objects.all
    datos = {
        'producto': producto
    }
    return render(request,'catalogoOfertas.html',datos) 
