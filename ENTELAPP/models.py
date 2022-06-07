from statistics import mode
from django.db import models

# Create your models here.

class TIPO_PRODUCTO(models.Model):
    id_tipo_producto = models.IntegerField(primary_key=True,verbose_name='ID TIPO PRODUCTO')
    nom_tipo_producto = models.CharField(max_length=50,verbose_name='Nombre del tipo producto')

    def __str__(self):
        return self.nom_tipo_producto

class PRODUCTO(models.Model):
    id_producto = models.IntegerField(primary_key=True,verbose_name='ID Producto')
    nombre = models.CharField(max_length=50,verbose_name='Nombre del producto')
    precio = models.IntegerField(verbose_name='Precio del producto')
    stock = models.IntegerField(verbose_name='Stock del producto')
    desc = models.IntegerField(verbose_name='Descripcion del producto')
    fabricante = models.CharField(max_length=50,verbose_name='Fabricante del producto')
    imagen = models.ImageField(verbose_name='Imagen del producto')
    nom_tipo_producto = models.ForeignKey(TIPO_PRODUCTO,on_delete=models.CASCADE,verbose_name='Tipo producto')

    def __str__(self):
        return self.nombre