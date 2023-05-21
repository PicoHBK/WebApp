from django.db import models
from cliente.models import Cliente
from coordinador.models import Coordinador
from empleado.models import Empleado
from servicio.models import Servicio

class ReservaServicio(models.Model):
    fecha_creacion = models.DateTimeField()
    fecha_reserva = models.DateField()
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE)
    responsable = models.ForeignKey(Coordinador, on_delete=models.CASCADE)
    empleado = models.ForeignKey(Empleado, on_delete=models.CASCADE)
    servicio = models.ForeignKey(Servicio, on_delete=models.CASCADE)
    precio = models.IntegerField()

    def __str__(self):
        return f"ReservaServicio #{self.pk}"
