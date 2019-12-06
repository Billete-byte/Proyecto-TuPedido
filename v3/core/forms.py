from django import forms
from django.forms import ModelForm
from .models import Producto
import datetime
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class ProductoForm(ModelForm):

    nombre = forms.CharField(min_length=2, max_length=50)
    precio = forms.IntegerField(min_value=100,max_value=9999999)

    class Meta:
        model = Producto
        fields =['nombre','precio','stock','tipo_prodcuto','informacion','fecha_entrega','descuento','imagen']

        widgets = {
            'fecha_entrega':forms.SelectDateWidget(years=range(1980,2020))
        }
    
    def clean_fecha_entrega(self):
        fecha = self.cleaned_data['fecha_entrega']

        if fecha > datetime.date.today():
            raise forms.ValidationError("Fecha no puede ser mayor al dia de hoy")
        return fecha

class CustomUserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['first_name','last_name','email','username','password1','password2']