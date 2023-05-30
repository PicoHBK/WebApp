from django.test import TestCase
from django.urls import reverse
from .models import Empleado


class EmpleadoTests(TestCase):
    def setUp(self):
        # Configuración inicial para los tests
        self.empleado = Empleado.objects.create(nombre="Juan", apellido="Perez", numero_legajo=123, activo=True)

    def test_listado_empleados(self):
        # Prueba la vista listado_empleados
        response = self.client.get(reverse('empleado:listado_empleados'))
        self.assertEqual(response.status_code, 200)  # Verifica el código de estado de la respuesta
        self.assertTemplateUsed(response, 'empleados/listado.html')  # Verifica que se haya utilizado el template correcto
        self.assertContains(response, self.empleado.nombre)  # Verifica que el nombre del empleado esté presente en la respuesta
        self.assertContains(response, self.empleado.apellido)  # Verifica que el apellido del empleado esté presente en la respuesta

    def test_activar_empleado(self):
        # Prueba la vista activar_empleado
        response = self.client.get(reverse('empleado:activar_empleado', args=[self.empleado.id]))
        self.assertEqual(response.status_code, 302)  # Verifica el código de estado de la respuesta
        self.assertTrue(Empleado.objects.get(id=self.empleado.id).activo)  # Verifica que el empleado esté activado

    def test_desactivar_empleado(self):
        # Prueba la vista desactivar_empleado
        response = self.client.get(reverse('empleado:desactivar_empleado', args=[self.empleado.id]))
        self.assertEqual(response.status_code, 302)  # Verifica el código de estado de la respuesta
        self.assertFalse(Empleado.objects.get(id=self.empleado.id).activo)  # Verifica que el empleado esté desactivado

    def test_nuevo_empleado(self):
        # Prueba la vista nuevo_empleado con una solicitud POST
        data = {'nombre': 'Pedro', 'apellido': 'Gomez', 'numero_legajo': 456}
        response = self.client.post(reverse('empleado:nuevo_empleado'), data)
        self.assertEqual(response.status_code, 302)  # Verifica el código de estado de la respuesta
        self.assertTrue(Empleado.objects.filter(nombre='Pedro', apellido='Gomez', numero_legajo=456).exists())  # Verifica que se haya creado un nuevo empleado con los datos proporcionados

    def test_modificar_empleado(self):
        # Prueba la vista modificar_empleado con una solicitud POST
        data = {'nombre': 'Carlos', 'apellido': 'Lopez', 'numero_legajo': 789}
        response = self.client.post(reverse('empleado:modificar_empleado', args=[self.empleado.id]), data)
        self.assertEqual(response.status_code, 302)  # Verifica el código de estado de la respuesta
        self.assertEqual(Empleado.objects.get(id=self.empleado.id).nombre, 'Carlos')  # Verifica que el nombre del empleado se haya modificado correctamente
        self.assertEqual(Empleado.objects.get(id=self.empleado.id).apellido, 'Lopez')  # Verifica que el apellido del empleado se haya modificado correctamente
        self.assertEqual(Empleado.objects.get(id=self.empleado.id).numero_legajo, 789)  # Verifica que el número de legajo del empleado se haya modificado correctamente
        self.assertFalse(Empleado.objects.get(id=self.empleado.id).activo)


