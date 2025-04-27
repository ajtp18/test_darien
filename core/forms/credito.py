from django import forms
from ..models.credito import Credito

class CreditoForm(forms.ModelForm):
    """Form for Credit model"""
    class Meta:
        model = Credito
        fields = [
            'cliente',
            'descripcion',
            'pago_minimo',
            'pago_maximo',
            'plazo_meses',
            'banco_credito',
            'tipo_credito'
        ]
        widgets = {
            'cliente': forms.Select(attrs={'class': 'form-control'}),
            'descripcion': forms.Textarea(attrs={'class': 'form-control', 'rows': 3}),
            'pago_minimo': forms.NumberInput(attrs={'class': 'form-control', 'min': '0', 'step': '0.01'}),
            'pago_maximo': forms.NumberInput(attrs={'class': 'form-control', 'min': '0', 'step': '0.01'}),
            'plazo_meses': forms.NumberInput(attrs={'class': 'form-control', 'min': '1'}),
            'banco_credito': forms.Select(attrs={'class': 'form-control'}),
            'tipo_credito': forms.Select(attrs={'class': 'form-control'}),
        } 