from django.db import models
from django.core.validators import RegexValidator

class Banco(models.Model):
    """Bank entity that can provide credits or hold client accounts"""
    TIPO_CHOICES = [
        ('PRIVADO', 'Privado'),
        ('GOBIERNO', 'Gobierno')
    ]
    
    nombre = models.CharField(
        max_length=100,
        unique=True,
        validators=[
            RegexValidator(
                regex=r'^[a-zA-Z\s]+$',
                message='El nombre solo debe contener letras'
            )
        ]
    )
    tipo = models.CharField(
        max_length=10,
        choices=TIPO_CHOICES,
        default='PRIVADO'
    )
    direccion = models.CharField(
        max_length=200,
        blank=True,
        validators=[
            RegexValidator(
                regex=r'^[a-zA-Z0-9\s,.-]+$',
                message='La dirección contiene caracteres inválidos'
            )
        ]
    )

    class Meta:
        verbose_name = 'Banco'
        verbose_name_plural = 'Bancos'
        ordering = ['nombre']

    def __str__(self):
        return self.nombre 