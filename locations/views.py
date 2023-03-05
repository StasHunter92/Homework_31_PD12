from rest_framework.pagination import PageNumberPagination
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.viewsets import ModelViewSet

from locations.models import Location
from locations.permissions import IsStaff
from locations.serializers import LocationSerializer


# ----------------------------------------------------------------------------------------------------------------------
# Custom paginator
class Paginator(PageNumberPagination):
    page_size: int = 5


# ----------------------------------------------------------------------------------------------------------------------
# Location ViewSet
class LocationsViewSet(ModelViewSet):
    queryset = Location.objects.all()
    serializer_class = LocationSerializer
    pagination_class = Paginator
    default_permission = [AllowAny]
    permissions = {
        "create": [IsAuthenticated, IsStaff],
        "update": [IsAuthenticated, IsStaff],
        "partial_update": [IsAuthenticated, IsStaff],
        "destroy": [IsAuthenticated, IsStaff],
    }

    def get_permissions(self):
        return [permission() for permission in self.permissions.get(self.action, self.default_permission)]
