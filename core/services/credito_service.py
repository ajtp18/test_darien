from .base import BaseService
from ..models.credito import Credito
from .email_service import EmailService
from django.core.mail import send_mail
from django.conf import settings

class CreditoService(BaseService[Credito]):
    def __init__(self):
        super().__init__(Credito)
        self.email_service = EmailService()
    
    def get_by_cliente(self, cliente_id):
        return self.model_class.objects.filter(cliente_id=cliente_id)
    
    def get_by_banco(self, banco_id):
        return self.model_class.objects.filter(banco_credito_id=banco_id)
    
    def get_by_tipo(self, tipo):
        return self.model_class.objects.filter(tipo_credito=tipo)

    def create(self, **kwargs):
        credito = super().create(**kwargs)
        try:
            self.email_service.send_credit_notification(credito)
            send_mail(
                subject='Crédito Registrado',
                message=f'Su crédito por {credito.pago_maximo} ha sido registrado exitosamente.',
                from_email=settings.DEFAULT_FROM_EMAIL,
                recipient_list=[credito.cliente.email]
            )
        except Exception as e:
            print(f"Error sending email: {e}")
        return credito 