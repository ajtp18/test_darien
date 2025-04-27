from django.test import TestCase
from django.core import mail
from core.models import Banco, Cliente, Credito
from core.services.credito_service import CreditoService
from django.conf import settings

class EmailTest(TestCase):
    def setUp(self):
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
        self.service = CreditoService()

    def test_email_sent_on_credito_creation(self):
        credito_data = {
            'cliente': self.cliente,
            'descripcion': 'Test Credit',
            'pago_minimo': 1000,
            'pago_maximo': 2000,
            'plazo_meses': 12,
            'banco_credito': self.banco,
            'tipo_credito': 'Automotriz'
        }
        
        credito = self.service.create(**credito_data)
        
        self.assertEqual(len(mail.outbox), 2)  # Se envían 2 emails
        self.assertEqual(mail.outbox[0].to[0], self.cliente.email)
        self.assertEqual(
            mail.outbox[0].from_email, 
            settings.DEFAULT_FROM_EMAIL
        )