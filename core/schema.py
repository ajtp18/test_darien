from drf_spectacular.utils import extend_schema, OpenApiParameter, OpenApiExample
from drf_spectacular.types import OpenApiTypes

# Esquemas de respuesta
cliente_schema = {
    'type': 'object',
    'properties': {
        'id': {'type': 'integer'},
        'nombre_apellido': {'type': 'string'},
        'fecha_nacimiento': {'type': 'string', 'format': 'date'},
        'edad': {'type': 'integer', 'minimum': 1, 'maximum': 99},
        'nacionalidad': {'type': 'string'},
        'direccion': {'type': 'string'},
        'email': {'type': 'string', 'format': 'email'},
        'telefono': {'type': 'string'},
        'tipo_persona': {'type': 'string', 'enum': ['Natural', 'Jurídico']},
        'banco_cuenta': {'type': 'integer', 'description': 'ID del banco'},
    }
}

credito_schema = {
    'type': 'object',
    'properties': {
        'id': {'type': 'integer'},
        'cliente': {'type': 'integer', 'description': 'ID del cliente'},
        'descripcion': {'type': 'string'},
        'pago_minimo': {'type': 'number', 'format': 'float'},
        'pago_maximo': {'type': 'number', 'format': 'float'},
        'plazo_meses': {'type': 'integer', 'minimum': 1},
        'fecha_registro': {'type': 'string', 'format': 'date-time'},
        'banco_credito': {'type': 'integer', 'description': 'ID del banco'},
        'tipo_credito': {'type': 'string', 'enum': ['Automotriz', 'Hipotecario', 'Comercial']},
    }
}

banco_schema = {
    'type': 'object',
    'properties': {
        'id': {'type': 'integer'},
        'nombre': {'type': 'string'},
        'tipo': {'type': 'string', 'enum': ['Privado', 'Gobierno']},
        'direccion': {'type': 'string'},
    }
} 