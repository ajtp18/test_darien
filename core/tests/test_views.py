from django.test import TestCase, Client
from django.urls import reverse
from core.models import Banco, Cliente, Credito
from django.contrib.auth.models import User

class ViewsTest(TestCase):
    def setUp(self):
        self.client = Client()
        self.user = User.objects.create_user(
            username='testuser',
            password='testpass123'
        )
        self.client.login(username='testuser', password='testpass123')
        
        self.banco = Banco.objects.create(
            nombre='Test Bank',
            tipo='Privado'
        )

    def test_banco_list_view(self):
        response = self.client.get(reverse('core:banco_list'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'core/bancos/list.html')

    def test_cliente_list_view(self):
        cliente = Cliente.objects.create(
            nombre_apellido='Test Client',
            fecha_nacimiento='1990-01-01',
            edad=30,
            nacionalidad='Colombia',
            email='test@test.com',
            tipo_persona='NATURAL',
            banco_cuenta=self.banco,
            telefono='1234567890'
        )
        response = self.client.get(reverse('core:cliente_list'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'core/clientes/list.html')

    def test_credito_list_view(self):
        response = self.client.get(reverse('core:credito_list'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'core/creditos/list.html')