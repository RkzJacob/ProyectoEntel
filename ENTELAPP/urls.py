from argparse import Namespace
from django.urls import path
from django.urls.resolvers import URLPattern

from django.conf import settings
from django.conf.urls.static import static
from .views import registrarProductos

urlpatterns = [
    path('',registrarProductos,name='home'),

]