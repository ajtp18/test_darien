from django.contrib import admin
from .models import Banco, Cliente, Credito

@admin.register(Banco)
class BancoAdmin(admin.ModelAdmin):
    """Admin interface for Bank model"""
    list_display = ('nombre', 'tipo', 'direccion')
    list_filter = ('tipo',)
    search_fields = ('nombre', 'direccion')
    ordering = ('nombre',)


@admin.register(Cliente)
class ClienteAdmin(admin.ModelAdmin):
    """Admin interface for Client model"""
    list_display = (
        'nombre_apellido',
        'email',
        'telefono',
        'tipo_persona',
        'banco_cuenta'
    )
    list_filter = ('tipo_persona', 'banco_cuenta')
    search_fields = ('nombre_apellido', 'email', 'telefono')
    ordering = ('nombre_apellido',)
    date_hierarchy = 'fecha_nacimiento'


@admin.register(Credito)
class CreditoAdmin(admin.ModelAdmin):
    """Admin interface for Credit model"""
    list_display = (
        'cliente',
        'tipo_credito',
        'banco_credito',
        'pago_minimo',
        'pago_maximo',
        'plazo_meses',
        'fecha_registro'
    )
    list_filter = ('tipo_credito', 'banco_credito')
    search_fields = ('cliente__nombre_apellido', 'descripcion')
    ordering = ('-fecha_registro',)
    date_hierarchy = 'fecha_registro'
    readonly_fields = ('fecha_registro',)
