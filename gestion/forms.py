from django import forms
from .models import Vino, Cliente, Venta


class VinoForm(forms.ModelForm):
    class Meta:
        model = Vino
        fields = [
            "nombre",
            "bodega",
            "categoria",
            "precio",
            "stock",
            "imagen",
            "activo",
        ]


class ClienteForm(forms.ModelForm):
    class Meta:
        model = Cliente
        fields = [
            "nombre",
            "apellido",
            "telefono",
            "email",
        ]


class VentaForm(forms.ModelForm):
    class Meta:
        model = Venta
        fields = ["cliente"]