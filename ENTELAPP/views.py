from django.shortcuts import render,redirect
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

        if formulariod.is_valid():
            formulariod.save()
            messages.success(request,"Se ha registrado correctamente el nuevo producto")
            return redirect(to="registrarProductos")
        else:
            messages.error(request,"No se ha podido registrar el nuevo producto")

        

    return render(request,'registrarProductos.html',datos)
    
def ordernarFabricante(request):
    producto = PRODUCTO.objects.all().order_by('nombre_fabricante')
    datos = {
        'producto': producto
    }
    
    return render(request,'catalogoOfertas.html',datos)  

def ordernarTipo(request):
    producto = PRODUCTO.objects.all().order_by('nom_tipo_producto')
    datos = {
        'producto': producto
    }
    
    return render(request,'catalogoOfertas.html',datos) 

def catalogoDeOfertas(request):
    producto = PRODUCTO.objects.all().order_by('nom_tipo_producto','nombre')
    datos = {
        'producto': producto
    }
    
    return render(request,'catalogoOfertas.html',datos) 
