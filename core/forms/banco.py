from django import forms
from ..models.banco import Banco

class BancoForm(forms.ModelForm):
    """Form for Bank model"""
    class Meta:
        model = Banco
        fields = ['nombre', 'tipo', 'direccion']
        widgets = {
            'nombre': forms.TextInput(attrs={'class': 'form-control'}),
            'tipo': forms.Select(attrs={'class': 'form-control'}),
            'direccion': forms.TextInput(attrs={'class': 'form-control'}),
        } 