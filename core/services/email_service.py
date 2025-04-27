from django.core.mail import send_mail
from django.conf import settings

class EmailService:
    @staticmethod
    def send_credit_notification(credito):
        """Send simple email notification when a credit is created"""
        subject = 'Tu Crédito - Nuevo Crédito Registrado'
        
        message = f"""
Hola {credito.cliente.nombre_apellido},

Se ha registrado un nuevo crédito a su nombre con los siguientes detalles:

- Descripción: {credito.descripcion}
- Tipo: {credito.get_tipo_credito_display()}
- Banco: {credito.banco_credito}
- Pago Mínimo: ${credito.pago_minimo}
- Pago Máximo: ${credito.pago_maximo}
- Plazo: {credito.plazo_meses} meses
- Fecha: {credito.fecha_registro.strftime('%d/%m/%Y')}

Saludos,
Tu Crédito
        """
        
        send_mail(
            subject=subject,
            message=message,
            from_email=settings.DEFAULT_FROM_EMAIL,
            recipient_list=[credito.cliente.email],
            fail_silently=False
        ) 