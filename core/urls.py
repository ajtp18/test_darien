from django.urls import path, include
from . import views
from .views.auth import login_view, logout_view
from .views.banco import BancoView
from .views.cliente import ClienteView
from .views.credito import CreditoView
from .services.banco_service import BancoService
from .services.cliente_service import ClienteService
from .services.credito_service import CreditoService
from django.contrib.auth.decorators import login_required
from rest_framework.routers import DefaultRouter
from .api_views import BancoViewSet, ClienteViewSet, CreditoViewSet

# inject dependencies
banco_service = BancoService()
banco_view = BancoView(banco_service)

cliente_service = ClienteService()
cliente_view = ClienteView(cliente_service)

credito_service = CreditoService()
credito_view = CreditoView(credito_service)

# decorate views
banco_list = login_required(login_url='core:login')(banco_view.list)
banco_delete = login_required(login_url='core:login')(banco_view.delete)

cliente_list = login_required(login_url='core:login')(cliente_view.list)
cliente_delete = login_required(login_url='core:login')(cliente_view.delete)
cliente_validate = login_required(login_url='core:login')(cliente_view.validate_field)

credito_list = login_required(login_url='core:login')(credito_view.list)
credito_delete = login_required(login_url='core:login')(credito_view.delete)

# create api
router = DefaultRouter()
router.register(r'bancos', BancoViewSet)
router.register(r'clientes', ClienteViewSet)
router.register(r'creditos', CreditoViewSet)

app_name = 'core'

urlpatterns = [
    path('login/', login_view, name='login'),
    path('logout/', logout_view, name='logout'),
    path('', views.home, name='home'),
    path('clientes/', cliente_list, name='cliente_list'),
    path('clientes/<int:pk>/delete/', cliente_delete, name='cliente_delete'),
    path('clientes/validate/', cliente_validate, name='cliente_validate'),
    path('bancos/', banco_list, name='banco_list'),
    path('bancos/<int:pk>/delete/', banco_delete, name='banco_delete'),
    path('creditos/', credito_list, name='credito_list'),
    path('creditos/<int:pk>/delete/', credito_delete, name='credito_delete'),
    path('api/', include(router.urls)),
] 