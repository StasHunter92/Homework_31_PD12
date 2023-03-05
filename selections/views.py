from rest_framework.pagination import PageNumberPagination
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.viewsets import ModelViewSet

from selections.models import Selection
from selections.permissions import IsOwnerOrStaff
from selections.serializers import SelectionListSerializer, SelectionDetailSerializer, \
    SelectionCreateSerializer, SelectionUpdateSerializer, SelectionDeleteSerializer


# ----------------------------------------------------------------------------------------------------------------------
# Custom paginator
class Paginator(PageNumberPagination):
    page_size: int = 10


# ----------------------------------------------------------------------------------------------------------------------
# Selection ViewSet
class SelectionsViewSet(ModelViewSet):
    queryset = Selection.objects.all()
    pagination_class = Paginator
    default_permission = [AllowAny]
    permissions = {
        "create": [IsAuthenticated],
        "update": [IsAuthenticated, IsOwnerOrStaff],
        "partial_update": [IsAuthenticated, IsOwnerOrStaff],
        "destroy": [IsAuthenticated, IsOwnerOrStaff],
    }

    default_serializer = SelectionListSerializer
    serializers = {
        "retrieve": SelectionDetailSerializer,
        "create": SelectionCreateSerializer,
        "update": SelectionUpdateSerializer,
        "destroy": SelectionDeleteSerializer,
    }

    def get_permissions(self):
        return [permission() for permission in self.permissions.get(self.action, self.default_permission)]

    def get_serializer_class(self):
        return self.serializers.get(self.action, self.default_serializer)
