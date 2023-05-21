from django.urls import path
from .views import activar_empleado,desactivar_empleado, listado_empleados, nuevo_empleado, modificar_empleado

app_name = 'empleado'
urlpatterns = [
    path('activar/<int:id>/', activar_empleado, name='activar_empleado'),
    path('desactivar/<int:id>/', desactivar_empleado, name='desactivar_empleado'),
    path('listado/', listado_empleados, name='listado_empleados'),
    path('nuevo/', nuevo_empleado, name='nuevo_empleado'),
    path('modificar/<int:id>/', modificar_empleado, name='modificar_empleado'),
]