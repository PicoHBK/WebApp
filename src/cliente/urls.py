from django.urls import path
from .views import listado_clientes, nuevo_cliente,modificar_cliente,activar_cliente, desactivar_cliente

app_name = 'cliente'
urlpatterns =[
    path('activar/<int:id>/', activar_cliente, name='activar_cliente'),
    path('desactivar/<int:id>/', desactivar_cliente, name='desactivar_cliente'),
    path('listado/', listado_clientes, name='listado_clientes'),
    path('nuevo/', nuevo_cliente, name='nuevo_cliente'),
    path('modificar/<int:id>/', modificar_cliente, name='modificar_cliente'),
]