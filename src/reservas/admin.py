from django.contrib import admin
from .models import ReservaServicio

class ReservaServicioAdmin(admin.ModelAdmin):
    list_display = ['fecha_creacion', 'fecha_reserva', 'cliente', 'responsable', 'empleado', 'servicio', 'precio']
    search_fields = ['responsable__nombre', 'responsable__apellido', 'cliente__nombre', 'cliente__apellido', 'empleado__nombre', 'empleado__apellido', 'servicio__nombre']

admin.site.register(ReservaServicio, ReservaServicioAdmin)
