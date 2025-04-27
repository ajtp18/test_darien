from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator, RegexValidator
from .banco import Banco
from django.utils import timezone
from datetime import date

class Cliente(models.Model):
    """Client entity with personal information and bank account details"""
    TIPO_PERSONA_CHOICES = [
        ('NATURAL', 'Natural'),
        ('JURIDICO', 'Jurídico')
    ]
    
    nombre_apellido = models.CharField(
        max_length=100,
        validators=[
            RegexValidator(
                regex=r'^[a-zA-ZáéíóúÁÉÍÓÚñÑ\s]+$',
                message='El nombre solo debe contener letras'
            )
        ]
    )
    fecha_nacimiento = models.DateField()
    edad = models.IntegerField(
        validators=[
            MinValueValidator(1, 'La edad debe ser mayor a 0'),
            MaxValueValidator(99, 'La edad debe ser menor a 100')
        ]
    )
    nacionalidad = models.CharField(max_length=100)
    direccion = models.CharField(max_length=200, blank=True)
    email = models.EmailField(
        unique=True,
        validators=[
            RegexValidator(
                regex=r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$',
                message='Ingrese un email válido'
            )
        ]
    )
    telefono = models.CharField(max_length=20, blank=True)
    tipo_persona = models.CharField(
        max_length=10,
        choices=TIPO_PERSONA_CHOICES,
        default='NATURAL'
    )
    banco_cuenta = models.ForeignKey(
        Banco, 
        on_delete=models.PROTECT,
        related_name='clientes'
    )

    class Meta:
        verbose_name = 'Cliente'
        verbose_name_plural = 'Clientes'
        ordering = ['nombre_apellido']

    def __str__(self):
        return self.nombre_apellido 

    def save(self, *args, **kwargs):
        # Calculate age based on date of birth
        if self.fecha_nacimiento:
            today = date.today()
            self.edad = (today.year - self.fecha_nacimiento.year - 
                ((today.month, today.day) < 
                (self.fecha_nacimiento.month, self.fecha_nacimiento.day)))
        super().save(*args, **kwargs) 