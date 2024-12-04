from django import forms

class ProductoForm(forms.Form):
    nombre = forms.CharField(max_length=100)
    descripcion = forms.CharField(max_length=100)
    precio = forms.FloatField()
    stock = forms.IntegerField()
    categoria = forms.CharField(max_length=100)
    estado = forms.CharField(max_length=100)
    observaciones = forms.CharField(max_length=100)
    proveedor = forms.CharField(max_length=100)
    
    nombre.widget.attrs['class'] = 'form-control'
    descripcion.widget.attrs['class'] = 'form-control'
    precio.widget.attrs['class'] = 'form-control'
    stock.widget.attrs['class'] = 'form-control'
    categoria.widget.attrs['class'] = 'form-control'
    estado.widget.attrs['class'] = 'form-control'
    observaciones.widget.attrs['class'] = 'form-control'
    proveedor.widget.attrs['class'] = 'form-control'

class ClienteForm(forms.Form):
    nombreCliente = forms.CharField(max_length=100)
    correo = forms.EmailField(max_length=100)
    telefono = forms.CharField(max_length=100)
    direccion = forms.CharField(max_length=100)
    ciudad = forms.CharField(max_length=100)
    pais = forms.CharField(max_length=100)
    tipoCliente = forms.CharField(max_length=100)
    preferencias = forms.CharField(max_length=100)
    fechaNacimiento = forms.DateField(widget=forms.DateInput(attrs={'type': 'date'}))
    genero = forms.CharField(max_length=100)

    nombreCliente.widget.attrs['class'] = 'form-control'
    correo.widget.attrs['class'] = 'form-control'
    telefono.widget.attrs['class'] = 'form-control'
    direccion.widget.attrs['class'] = 'form-control'
    ciudad.widget.attrs['class'] = 'form-control'
    pais.widget.attrs['class'] = 'form-control'
    tipoCliente.widget.attrs['class'] = 'form-control'
    preferencias.widget.attrs['class'] = 'form-control'
    fechaNacimiento.widget.attrs['class'] = 'form-control'
    genero.widget.attrs['class'] = 'form-control'
