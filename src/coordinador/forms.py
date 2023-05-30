from django import forms

class CoordinadorForm(forms.Form):
    nombre = forms.CharField(max_length=50, label="Nombre")
    apellido = forms.CharField(max_length=50, label="Apellido")
    numero_documento = forms.IntegerField(label="Número de Documento")
    fecha_alta = forms.DateTimeField(label="Fecha de Alta")
    activo = forms.BooleanField(label="Activo")
