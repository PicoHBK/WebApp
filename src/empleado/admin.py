from django.contrib import admin
from .models import Empleado

@admin.register(Empleado)
class EmpleadoAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'apellido', 'numero_legajo', 'activo')
    search_fields = ('nombre', 'apellido')
    list_filter = ('activo',)
