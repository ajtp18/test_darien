from django import forms
from ..models import Cliente

class ClienteForm(forms.ModelForm):
    """Form for Client model"""
    class Meta:
        model = Cliente
        exclude = ['edad']
        fields = [
            'nombre_apellido', 
            'fecha_nacimiento',
            'nacionalidad',
            'direccion',
            'email',
            'telefono',
            'tipo_persona',
            'banco_cuenta'
        ]
        widgets = {
            'nombre_apellido': forms.TextInput(attrs={'class': 'form-control'}),
            'fecha_nacimiento': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
            'nacionalidad': forms.TextInput(attrs={'class': 'form-control'}),
            'direccion': forms.TextInput(attrs={'class': 'form-control'}),
            'email': forms.EmailInput(attrs={'class': 'form-control'}),
            'telefono': forms.TextInput(attrs={'class': 'form-control'}),
            'tipo_persona': forms.Select(attrs={'class': 'form-control'}),
            'banco_cuenta': forms.Select(attrs={'class': 'form-control'}),
        } 