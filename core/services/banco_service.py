from .base import BaseService
from ..models.banco import Banco

class BancoService(BaseService[Banco]):
    def __init__(self):
        super().__init__(Banco)

    def get_by_tipo(self, tipo):
        return self.model_class.objects.filter(tipo=tipo) 