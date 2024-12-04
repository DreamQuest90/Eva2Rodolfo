from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.urls import reverse
from djangoVerRodolfo.forms import *
from djangoVerRodolfo.models import *

def principal(request):
    return render(request, 'djangoVerRodolfo/index.html')

def Clientes(request):
    Clientes = Cliente.objects.all()
    data = {'Clientes':Clientes}
    return render(request, 'djangoVerRodolfo/listadoClientes.html',data)

def Productos(request):
    Productos = Producto.objects.all()
    data = {'Productos':Productos}
    return render(request, 'djangoVerRodolfo/listadoProductos.html',data)

def registroCliente(request):
    form = ClienteForm()

    if request.method == 'POST':
        form = ClienteForm(request.POST)
        if form.is_valid():
            Cliente.objects.create(nombreCliente=form.cleaned_data['nombreCliente'], correo=form.cleaned_data['correo'], telefono=form.cleaned_data['telefono'], direccion=form.cleaned_data['direccion'], ciudad=form.cleaned_data['ciudad'], pais=form.cleaned_data['pais'], tipoCliente=form.cleaned_data['tipoCliente'], preferencias=form.cleaned_data['preferencias'],fechaNacimiento=form.cleaned_data['fechaNacimiento'], genero=form.cleaned_data['genero'])
            return HttpResponseRedirect(reverse('listadoClientes'))
    data = {'form': form}
    return render(request, 'djangoVerRodolfo/registroClientes.html', data)

def registroProducto(request):
    form = ProductoForm()

    if request.method == 'POST':
        form = ProductoForm(request.POST)
        if form.is_valid():
            Producto.objects.create(nombre=form.cleaned_data['nombre'], descripcion=form.cleaned_data['descripcion'], precio=form.cleaned_data['precio'], stock=form.cleaned_data['stock'], categoria=form.cleaned_data['categoria'], estado=form.cleaned_data['estado'], observaciones=form.cleaned_data['observaciones'], proveedor=form.cleaned_data['proveedor'])
            return HttpResponseRedirect(reverse('listadoProductos'))
    data = {'form': form}
    return render(request, 'djangoVerRodolfo/registroProductos.html', data)