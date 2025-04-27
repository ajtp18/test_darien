from django.test import TestCase
from core.models import Cliente, Banco, Credito
from django.core.exceptions import ValidationError

class BancoModelTest(TestCase):
    def setUp(self):
        self.banco = Banco.objects.create(
            nombre='Banco Test',
            tipo='Privado',
            direccion='Calle Test 123'
        )

    def test_banco_creation(self):
        self.assertTrue(isinstance(self.banco, Banco))
        self.assertEqual(str(self.banco), 'Banco Test')

    def test_banco_tipo_choices(self):
        with self.assertRaises(ValidationError):
            banco = Banco(
                nombre='Banco Invalid',
                tipo='Invalid',
                direccion='Test'
            )
            banco.full_clean()

class ClienteModelTest(TestCase):
    def setUp(self):
        self.banco = Banco.objects.create(
            nombre='Banco Test',
            tipo='Privado'
        )
        self.cliente = Cliente.objects.create(
            nombre_apellido='Test User',
            fecha_nacimiento='1990-01-01',
            edad=30,
            nacionalidad='Colombia',
            direccion='Test Address',
            email='test@test.com',
            telefono='1234567890',
            tipo_persona='Natural',
            banco_cuenta=self.banco
        )

    def test_cliente_creation(self):
        self.assertTrue(isinstance(self.cliente, Cliente))
        self.assertEqual(str(self.cliente), 'Test User')

    def test_cliente_email_validation(self):
        with self.assertRaises(ValidationError):
            cliente = Cliente(
                nombre_apellido='Invalid Email',
                fecha_nacimiento='1990-01-01',
                email='invalid-email',
                tipo_persona='Natural',
                banco_cuenta=self.banco
            )
            cliente.full_clean() 