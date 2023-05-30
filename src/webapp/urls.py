from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('clientes/', include('cliente.urls', namespace='cliente')),
    path('coordinadores/', include('coordinador.urls', namespace='coordinador')),
    path('empleados/', include('empleado.urls', namespace='empleado')),
    path('reservas/', include('reservas.urls', namespace='reservas')),
    path('servicios/', include('servicio.urls', namespace='servicio')),
]

