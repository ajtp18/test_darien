from django.shortcuts import render, redirect
from django.contrib import messages
from ..services.credito_service import CreditoService
from ..forms.credito import CreditoForm
from ..utils.decorators import method_login_required

class CreditoView:
    def __init__(self, credito_service: CreditoService):
        self.credito_service = credito_service

    @method_login_required
    def list(self, request):
        creditos = self.credito_service.get_all()
        form = CreditoForm()
        
        if request.method == 'POST':
            form = CreditoForm(request.POST)
            if form.is_valid():
                self.credito_service.create(**form.cleaned_data)
                messages.success(
                    request, 
                    'Crédito creado exitosamente. Se ha enviado un email de confirmación.'
                )
                return redirect('core:credito_list')
        
        return render(request, 'core/creditos/list.html', {
            'creditos': creditos,
            'form': form
        })

    @method_login_required
    def delete(self, request, pk):
        try:
            credito = self.credito_service.get_by_id(pk)
            if request.method == 'POST':
                self.credito_service.delete(credito)
                messages.success(request, 'Crédito eliminado exitosamente')
        except Exception as e:
            messages.error(request, 'No se puede eliminar el crédito')
        return redirect('core:credito_list') 