from django.test import TestCase
from django.urls import reverse
from .models import Cliente


class ClienteTests(TestCase):
    def setUp(self):
        self.cliente = Cliente.objects.create(nombre="Juan", apellido="Perez", activo=True)

    def test_listado_clientes(self):
        response = self.client.get(reverse('cliente:listado_clientes'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'clientes/listado.html')
        self.assertContains(response, self.cliente.nombre)
        self.assertContains(response, self.cliente.apellido)

    def test_activar_cliente(self):
        response = self.client.get(reverse('cliente:activar_cliente', args=[self.cliente.id]))
        self.assertEqual(response.status_code, 302)
        self.assertTrue(Cliente.objects.get(id=self.cliente.id).activo)

    def test_desactivar_cliente(self):
        response = self.client.get(reverse('cliente:desactivar_cliente', args=[self.cliente.id]))
        self.assertEqual(response.status_code, 302)
        self.assertFalse(Cliente.objects.get(id=self.cliente.id).activo)

    def test_nuevo_cliente(self):
        data = {'nombre': 'Pedro', 'apellido': 'Gomez', 'activo': True}
        response = self.client.post(reverse('cliente:nuevo_cliente'), data)
        self.assertEqual(response.status_code, 302)
        self.assertTrue(Cliente.objects.filter(nombre='Pedro', apellido='Gomez', activo=True).exists())

    def test_modificar_cliente(self):
        data = {'nombre': 'Carlos', 'apellido': 'Lopez', 'activo': False}
        response = self.client.post(reverse('cliente:modificar_cliente', args=[self.cliente.id]), data)
        self.assertEqual(response.status_code, 302)
        self.assertEqual(Cliente.objects.get(id=self.cliente.id).nombre, 'Carlos')
        self.assertEqual(Cliente.objects.get(id=self.cliente.id).apellido, 'Lopez')
        self.assertFalse(Cliente.objects.get(id=self.cliente.id).activo)
