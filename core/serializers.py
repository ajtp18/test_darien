from rest_framework import serializers
from .models import Cliente, Credito, Banco

class BancoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Banco
        fields = ['id', 'nombre', 'tipo', 'direccion']

class ClienteSerializer(serializers.ModelSerializer):
    banco_cuenta = BancoSerializer(read_only=True)
    
    class Meta:
        model = Cliente
        fields = [
            'id', 'nombre_apellido', 'fecha_nacimiento', 'edad',
            'nacionalidad', 'direccion', 'email', 'telefono',
            'tipo_persona', 'banco_cuenta'
        ]

class CreditoSerializer(serializers.ModelSerializer):
    cliente = ClienteSerializer(read_only=True)
    banco_credito = BancoSerializer(read_only=True)
    
    class Meta:
        model = Credito
        fields = [
            'id', 'cliente', 'descripcion', 'pago_minimo',
            'pago_maximo', 'plazo_meses', 'fecha_registro',
            'banco_credito', 'tipo_credito'
        ] 