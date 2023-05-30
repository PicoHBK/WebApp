from django.urls import path
from .views import registrar_coordinador, actualizar_coordinador,activar_coordinador, desactivar_coordinador, listado_coordinadores

app_name = 'coordinador'
urlpatterns = [
    path('activar/<int:id>/', activar_coordinador, name='activar_coordinador'),
    path('desactivar/<int:id>/', desactivar_coordinador, name='desactivar_coordinador'),
    path('listado/', listado_coordinadores, name='listado_coordinadores'),
    path('nuevo/', registrar_coordinador, name='registrar_coordinador'),
    path('modificar/<int:pk>/', actualizar_coordinador, name='modificar_empleado'),
]