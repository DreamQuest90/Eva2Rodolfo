from django.db import models

class Producto(models.Model):
    nombre = models.CharField(max_length=100)
    descripcion = models.CharField(max_length=100)
    precio = models.FloatField()
    stock = models.IntegerField()
    categoria = models.CharField(max_length=100)
    estado = models.CharField(max_length=100)
    observaciones = models.CharField(max_length=100)
    proveedor = models.CharField(max_length=100)

class Cliente(models.Model):
    nombreCliente = models.CharField(max_length=100)
    correo = models.EmailField(max_length=100)
    telefono = models.CharField(max_length=100)
    direccion = models.CharField(max_length=100)
    ciudad = models.CharField(max_length=100)
    pais = models.CharField(max_length=100)
    tipoCliente = models.CharField(max_length=100)
    preferencias = models.CharField(max_length=100)
    fechaNacimiento = models.DateField()
    genero = models.CharField(max_length=100)