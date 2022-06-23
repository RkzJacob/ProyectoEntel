from argparse import Namespace
from django.urls import path
from django.urls.resolvers import URLPattern

from django.conf import settings
from django.conf.urls.static import static
from .views import registrarProductos, catalogoDeOfertas,ordernarFabricante,ordernarTipo

urlpatterns = [
    path('',catalogoDeOfertas,name='home'),
    path('registrarProductos',registrarProductos,name='registrarProductos'),
    path('OrdenadoFabricante',ordernarFabricante,name='ordernarFabricante'),
    path('ordernarTipo',ordernarTipo,name='ordernarTipo'),
    

]


if settings.DEBUG:
    urlpatterns+= static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)