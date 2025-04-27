from django.shortcuts import render, redirect
from django.contrib import messages
from ..services.cliente_service import ClienteService
from ..forms.cliente import ClienteForm
from django.http import JsonResponse
from ..utils.decorators import method_login_required

class ClienteView:
    def __init__(self, cliente_service: ClienteService):
        self.cliente_service = cliente_service

    @method_login_required
    def list(self, request):
        clientes = self.cliente_service.get_all()
        form = ClienteForm()
        
        if request.method == 'POST':
            form = ClienteForm(request.POST)
            if form.is_valid():
                self.cliente_service.create(**form.cleaned_data)
                messages.success(request, 'Cliente creado exitosamente')
                return redirect('core:cliente_list')
        
        return render(request, 'core/clientes/list.html', {
            'clientes': clientes,
            'form': form
        })

    @method_login_required
    def delete(self, request, pk):
        try:
            cliente = self.cliente_service.get_by_id(pk)
            if request.method == 'POST':
                self.cliente_service.delete(cliente)
                messages.success(request, 'Cliente eliminado exitosamente')
        except Exception as e:
            messages.error(request, 'No se puede eliminar el cliente porque tiene registros asociados')
        return redirect('core:cliente_list')

    @method_login_required
    def validate_field(self, request):
        field = request.GET.get('field')
        value = request.GET.get('value')
        
        if field == 'email':
            exists = self.cliente_service.get_by_email(value)
            return JsonResponse({
                'valid': not exists,
                'message': 'Este email ya está registrado' if exists else ''
            })
        elif field == 'telefono':
            exists = self.cliente_service.get_by_telefono(value)
            return JsonResponse({
                'valid': not exists,
                'message': 'Este teléfono ya está registrado' if exists else ''
            }) 