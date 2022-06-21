from statistics import mode
from django.db import models

# Create your models here.

class TIPO_PRODUCTO(models.Model):
    id_tipo_producto = models.AutoField(primary_key=True)
    nom_tipo_producto = models.CharField(max_length=50,verbose_name='Nombre del tipo producto')

    def __str__(self):
        return self.nom_tipo_producto

class FABRICANTE(models.Model):
    id_fabricante = models.AutoField(primary_key=True)
    nombre_fabricante = models.CharField(max_length=50,verbose_name='Fabricante')

    def __str__(self):
        return self.nombre_fabricante

class PRODUCTO(models.Model):
    id_producto = models.IntegerField(primary_key=True)
    nombre = models.CharField(max_length=50,null=True,verbose_name='Nombre del producto')
    precio = models.IntegerField(verbose_name='Precio del producto',null=True)
    stock = models.IntegerField(verbose_name='Stock del producto',null=True)
    desc = models.TextField(verbose_name='Descripcion del producto',null=True)
    nombre_fabricante = models.ForeignKey(FABRICANTE,on_delete=models.CASCADE,verbose_name='Fabricante')
    imagenProducto = models.ImageField(upload_to="fotoproductos",verbose_name='Imagen del producto',null=True)
    nom_tipo_producto = models.ForeignKey(TIPO_PRODUCTO,on_delete=models.CASCADE,verbose_name='Tipo producto')

    def __str__(self):
        return self.nombre