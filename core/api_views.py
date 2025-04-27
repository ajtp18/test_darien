from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from drf_spectacular.utils import extend_schema, extend_schema_view, OpenApiParameter
from .models import Cliente, Credito, Banco
from .serializers import ClienteSerializer, CreditoSerializer, BancoSerializer

@extend_schema(tags=['Bancos'])
class BancoViewSet(viewsets.ModelViewSet):
    """
    API endpoint para gestionar Bancos.
    Permite listar y crear bancos en el sistema.
    """
    queryset = Banco.objects.all()
    serializer_class = BancoSerializer
    permission_classes = [IsAuthenticated]

    @extend_schema(
        summary="Listar bancos",
        description="Obtiene la lista de todos los bancos registrados"
    )
    def list(self, request, *args, **kwargs):
        return super().list(request, *args, **kwargs)

@extend_schema(tags=['Clientes'])
class ClienteViewSet(viewsets.ModelViewSet):
    """
    API endpoint para gestionar Clientes.
    Permite listar y crear clientes en el sistema.
    """
    queryset = Cliente.objects.all()
    serializer_class = ClienteSerializer
    permission_classes = [IsAuthenticated]

    @extend_schema(
        summary="Listar clientes",
        description="Obtiene la lista de todos los clientes registrados"
    )
    def list(self, request, *args, **kwargs):
        return super().list(request, *args, **kwargs)

@extend_schema(tags=['Créditos'])
class CreditoViewSet(viewsets.ModelViewSet):
    """
    API endpoint para gestionar Créditos.
    Permite listar y crear créditos en el sistema.
    """
    queryset = Credito.objects.all()
    serializer_class = CreditoSerializer
    permission_classes = [IsAuthenticated]

    @extend_schema(
        summary="Listar créditos",
        description="Obtiene la lista de todos los créditos registrados"
    )
    def list(self, request, *args, **kwargs):
        return super().list(request, *args, **kwargs) 