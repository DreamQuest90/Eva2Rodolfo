from django.contrib import admin
from djangoVerRodolfo.models import *


class ProductoAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'descripcion', 'precio', 'stock', 'categoria', 'estado', 'observaciones', 'proveedor')

class ClienteAdmin(admin.ModelAdmin):
    list_display = ('nombreCliente', 'correo', 'telefono', 'direccion', 'ciudad', 'pais', 'tipoCliente', 'preferencias',  'fechaNacimiento', 'genero')

admin.site.register(Producto, ProductoAdmin)
admin.site.register(Cliente, ClienteAdmin)