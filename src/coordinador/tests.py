from django.test import TestCase
from django.urls import reverse
from .models import Coordinador


class CoordinadorTests(TestCase):
    def setUp(self):
        # Configuración inicial para los tests
        self.coordinador = Coordinador.objects.create(nombre="Juan", apellido="Perez", numero_documento=123456789, fecha_alta="2023-05-01", activo=True)

    def test_listado_coordinadores(self):
        # Prueba la vista listado_coordinadores
        response = self.client.get(reverse('coordinador:listado_coordinadores'))
        self.assertEqual(response.status_code, 200)  # Verifica el código de estado de la respuesta
        self.assertTemplateUsed(response, 'coordinadores/listado.html')  # Verifica que se haya utilizado el template correcto
        self.assertContains(response, self.coordinador.nombre)  # Verifica que el nombre del coordinador esté presente en la respuesta
        self.assertContains(response, self.coordinador.apellido)  # Verifica que el apellido del coordinador esté presente en la respuesta

    def test_activar_coordinador(self):
        # Prueba la vista activar_coordinador
        response = self.client.get(reverse('coordinador:activar_coordinador', args=[self.coordinador.id]))
        self.assertEqual(response.status_code, 302)  # Verifica el código de estado de la respuesta
        self.assertTrue(Coordinador.objects.get(id=self.coordinador.id).activo)  # Verifica que el coordinador esté activado

    def test_desactivar_coordinador(self):
        # Prueba la vista desactivar_coordinador
        response = self.client.get(reverse('coordinador:desactivar_coordinador', args=[self.coordinador.id]))
        self.assertEqual(response.status_code, 302)  # Verifica el código de estado de la respuesta
        self.assertFalse(Coordinador.objects.get(id=self.coordinador.id).activo)  # Verifica que el coordinador esté desactivado

    def test_nuevo_coordinador(self):
        # Prueba la vista registrar_coordinador con una solicitud POST
        data = {
            'nombre': 'Pedro',
            'apellido': 'Gomez',
            'numero_documento': 987654321,
            'fecha_alta': '2023-05-15',
            'activo': True
        }
        response = self.client.post(reverse('coordinador:registrar_coordinador'), data)
        self.assertEqual(response.status_code, 302)  # Verifica el código de estado de la respuesta
        self.assertTrue(Coordinador.objects.filter(nombre='Pedro', apellido='Gomez', numero_documento=987654321, fecha_alta='2023-05-15', activo=True).exists())  # Verifica que se haya creado un nuevo coordinador con los datos proporcionados

    def test_modificar_coordinador(self):
        # Prueba la vista actualizar_coordinador con una solicitud POST
        data = {
            'nombre': 'Carlos',
            'apellido': 'Lopez',
            'numero_documento': 555555555,
            'fecha_alta': '2023-05-10',
            'activo': False
        }
        response = self.client.post(reverse('coordinador:modificar_empleado', args=[self.coordinador.id]), data)
        self.assertEqual(response.status_code, 302)  # Verifica el código de estado de la respuesta
        self.assertEqual(Coordinador.objects.get(id=self.coordinador.id).nombre, 'Carlos')  # Verifica que el nombre del coordinador se haya modificado correctamente
        self.assertEqual(Coordinador.objects.get(id=self.coordinador.id).apellido, 'Lopez')  # Verifica que el apellido del coordinador se haya modificado correctamente
        self.assertFalse(Coordinador.objects.get(id=self.coordinador.id).activo)  # Verifica que el coordinador esté desactivado

