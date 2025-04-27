from django.shortcuts import render, redirect
from django.contrib import messages
from ..services.banco_service import BancoService
from ..forms.banco import BancoForm
from ..utils.decorators import method_login_required

class BancoView:
    def __init__(self, banco_service: BancoService):
        self.banco_service = banco_service

    @method_login_required
    def list(self, request):
        bancos = self.banco_service.get_all()
        form = BancoForm()
        
        if request.method == 'POST':
            form = BancoForm(request.POST)
            if form.is_valid():
                self.banco_service.create(**form.cleaned_data)
                messages.success(request, 'Banco creado exitosamente')
                return redirect('core:banco_list')
        
        return render(request, 'core/bancos/list.html', {
            'bancos': bancos,
            'form': form
        })

    @method_login_required
    def delete(self, request, pk):
        try:
            banco = self.banco_service.get_by_id(pk)
            if request.method == 'POST':
                self.banco_service.delete(banco)
                messages.success(request, 'Banco eliminado exitosamente')
        except Exception as e:
            messages.error(request, 'No se puede eliminar el banco porque tiene registros asociados')
        return redirect('core:banco_list') 