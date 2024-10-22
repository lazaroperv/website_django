#--> Se importan los forms propios de Django 
from django import forms
#--> Y aca se importan los modelos(tablas) de models.py
from .models import *
#--> se crea una clase en la que se arma el formulario
class NuevoProducto(forms.ModelForm):
    #-->sub clase donde indicas que vas a llamar al modelo "Productos" y a todos los campos.
    class Meta:
        model=Productos
        fields='__all__'