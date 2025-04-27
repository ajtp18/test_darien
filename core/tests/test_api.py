from django.test import TestCase
from rest_framework.test import APIClient
from django.contrib.auth.models import User
from core.models import Banco, Cliente, Credito

class APITest(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.user = User.objects.create_user(
            username='testuser',
            password='testpass123'
        )
        self.client.force_authenticate(user=self.user)
        
        self.banco = Banco.objects.create(
            nombre='Test Bank',
            tipo='Privado'
        )

    def test_banco_list_api(self):
        response = self.client.get('/api/bancos/')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(response.data), 1)

    def test_cliente_list_api(self):
        cliente = Cliente.objects.create(
            nombre_apellido='Test Client',
            fecha_nacimiento='1990-01-01',
            edad=30,
            nacionalidad='Colombia',
            email='test@test.com',
            tipo_persona='NATURAL',
            banco_cuenta=self.banco,
            telefono='1234567890',
            direccion='Test Address'
        )
        
        response = self.client.get('/api/clientes/')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(response.data), 1)
        self.assertEqual(response.data[0]['email'], 'test@test.com')

    def test_credito_list_api(self):
        response = self.client.get('/api/creditos/')
        self.assertEqual(response.status_code, 200)