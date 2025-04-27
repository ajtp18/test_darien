from django.test import TestCase
from core.services.banco_service import BancoService
from core.services.cliente_service import ClienteService
from core.services.credito_service import CreditoService
from core.models import Banco, Cliente, Credito

class BancoServiceTest(TestCase):
    def setUp(self):
        self.service = BancoService()

    def test_get_all_bancos(self):
        banco = Banco.objects.create(
            nombre='Test Bank',
            tipo='Privado'
        )
        bancos = self.service.get_all()
        self.assertEqual(len(bancos), 1)
        self.assertEqual(bancos[0].nombre, 'Test Bank')

class CreditoServiceTest(TestCase):
    def setUp(self):
        self.service = CreditoService()
        self.banco = Banco.objects.create(
            nombre='Test Bank',
            tipo='Privado'
        )
        self.cliente = Cliente.objects.create(
            nombre_apellido='Test Client',
            fecha_nacimiento='1990-01-01',
            edad=30,
            nacionalidad='Colombia',
            email='test@test.com',
            tipo_persona='NATURAL',
            banco_cuenta=self.banco,
            telefono='1234567890'
        )

    def test_get_by_cliente(self):
        credito = Credito.objects.create(
            cliente=self.cliente,
            descripcion='Test Credit',
            pago_minimo=1000,
            pago_maximo=2000,
            plazo_meses=12,
            banco_credito=self.banco,
            tipo_credito='Automotriz'
        )
        creditos = self.service.get_by_cliente(self.cliente.id)
        self.assertEqual(len(creditos), 1)
        self.assertEqual(creditos[0].descripcion, 'Test Credit') 