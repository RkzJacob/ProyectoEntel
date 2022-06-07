from django.shortcuts import render

# Create your views here.

def registrarProductos(request):
    return render(request,'registrarProductos.html')