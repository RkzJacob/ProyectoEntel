from django.contrib import admin
from .models import FABRICANTE, PRODUCTO,TIPO_PRODUCTO
# Register your models here.
admin.site.register(PRODUCTO)
admin.site.register(TIPO_PRODUCTO)
admin.site.register(FABRICANTE)