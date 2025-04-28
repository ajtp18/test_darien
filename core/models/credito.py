from django.db import models
from django.core.validators import MinValueValidator
from django.utils import timezone
from .cliente import Cliente
from .banco import Banco
from django.core.exceptions import ValidationError

class Credito(models.Model):
    """Credit entity with details about the loan"""
    TIPO_CREDITO_CHOICES = [
        ('AUTOMOTRIZ', 'Automotriz'),
        ('HIPOTECARIO', 'Hipotecario'),
        ('COMERCIAL', 'Comercial'),
    ]
    
    cliente = models.ForeignKey(
        Cliente,
        on_delete=models.CASCADE,
        related_name='creditos'
    )
    descripcion = models.TextField()
    pago_minimo = models.DecimalField(
        max_digits=10,
        decimal_places=2,
        validators=[MinValueValidator(0.01, 'El pago mínimo debe ser mayor a 0')]
    )
    pago_maximo = models.DecimalField(
        max_digits=10,
        decimal_places=2,
        validators=[MinValueValidator(0.01, 'El pago máximo debe ser mayor a 0')]
    )
    plazo_meses = models.PositiveIntegerField(
        validators=[MinValueValidator(1, 'El plazo debe ser de al menos 1 mes')]
    )
    fecha_registro = models.DateTimeField(
        auto_now_add=True,
        editable=False
    )
    tipo_credito = models.CharField(
        max_length=20,
        choices=TIPO_CREDITO_CHOICES,
        default='AUTOMOTRIZ'
    )
    banco_credito = models.ForeignKey(
        'Banco',
        on_delete=models.PROTECT,
        related_name='creditos_otorgados'
    )

    def clean(self):
        if self.pago_maximo and self.pago_minimo:
            if self.pago_maximo <= self.pago_minimo:
                raise ValidationError({
                    'pago_maximo': 'El pago máximo debe ser mayor al pago mínimo'
                })

    class Meta:
        verbose_name = 'Crédito'
        verbose_name_plural = 'Créditos'
        ordering = ['-fecha_registro']

    def __str__(self):
        return f"{self.cliente} - {self.get_tipo_credito_display()}" 