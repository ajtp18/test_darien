from .base import BaseService
from ..models.cliente import Cliente

class ClienteService(BaseService[Cliente]):
    def __init__(self):
        super().__init__(Cliente)

    def get_by_tipo_persona(self, tipo):
        return self.model_class.objects.filter(tipo_persona=tipo)

    def get_by_banco(self, banco_id):
        return self.model_class.objects.filter(banco_cuenta_id=banco_id)

    def get_by_email(self, email):
        return self.model_class.objects.filter(email=email).exists()

    def get_by_telefono(self, telefono):
        return self.model_class.objects.filter(telefono=telefono).exists() 