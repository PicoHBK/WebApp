from django import forms

class ClienteForm(forms.Form):
    nombre = forms.CharField(max_length=100, label="Nombre")
    apellido = forms.CharField(max_length=100, label="Apellido")
    activo = forms.BooleanField(label="Activo")

