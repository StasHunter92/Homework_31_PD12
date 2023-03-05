from django.db.models import Q
from rest_framework.generics import ListAPIView, RetrieveAPIView, CreateAPIView, UpdateAPIView, DestroyAPIView
from rest_framework.pagination import PageNumberPagination
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.viewsets import ModelViewSet

from ads.models import Category, Advertisement
from ads.permissions import IsStaff, IsOwnerOrStaff
from ads.serializers import CategorySerializer, AdvertisementListSerializer, AdvertisementDetailSerializer, \
    AdvertisementCreateSerializer, AdvertisementUpdateSerializer, AdvertisementDeleteSerializer


# ----------------------------------------------------------------------------------------------------------------------
# Custom paginator
class Paginator(PageNumberPagination):
    page_size: int = 10


# ----------------------------------------------------------------------------------------------------------------------
# Category ViewSet
class CategoriesViewSet(ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer

    default_permission = [AllowAny]
    permissions = {
        "create": [IsAuthenticated, IsStaff],
        "update": [IsAuthenticated, IsStaff],
        "partial_update": [IsAuthenticated, IsStaff],
        "destroy": [IsAuthenticated, IsStaff],
    }

    def get_permissions(self):
        return [permission() for permission in self.permissions.get(self.action, self.default_permission)]


# ----------------------------------------------------------------------------------------------------------------------
# Advertisement ApiView
class AdvertisementListView(ListAPIView):
    """
    GET list of advertisements
    """
    queryset = Advertisement.objects.all()
    serializer_class = AdvertisementListSerializer
    pagination_class = Paginator

    def get(self, request, *args, **kwargs):
        """
        Filter results
        """
        categories = request.GET.getlist("cat", None)
        categories_q = None

        for category in categories:
            if categories_q is None:
                categories_q = Q(category__name__icontains=category)
            else:
                categories_q |= Q(category__name__icontains=category)

        if categories_q:
            self.queryset = self.queryset.filter(categories_q)

        advertisement_text = request.GET.get("text", None)

        if advertisement_text:
            self.queryset = self.queryset.filter(name__icontains=advertisement_text)

        location = request.GET.get("loc", None)

        if location:
            self.queryset = self.queryset.filter(author__locations__name__icontains=location)

        price_from = request.GET.get("price_from", None)

        if price_from:
            self.queryset = self.queryset.filter(price__gt=price_from)

        price_to = request.GET.get("price_to", None)

        if price_to:
            self.queryset = self.queryset.filter(price__lt=price_to)

        return super().get(request, *args, **kwargs)


class AdvertisementDetailView(RetrieveAPIView):
    """
    GET one advertisement
    """
    queryset = Advertisement.objects.all()
    serializer_class = AdvertisementDetailSerializer
    permission_classes = [IsAuthenticated]


class AdvertisementCreateView(CreateAPIView):
    """
    POST to create advertisement
    """
    queryset = Advertisement.objects.all()
    serializer_class = AdvertisementCreateSerializer
    permission_classes = [IsAuthenticated]


class AdvertisementUpdateView(UpdateAPIView):
    """
    PATCH to update advertisement
    """
    queryset = Advertisement.objects.all()
    serializer_class = AdvertisementUpdateSerializer
    permission_classes = [IsAuthenticated, IsOwnerOrStaff]


class AdvertisementDeleteView(DestroyAPIView):
    """
    DELETE to delete advertisement
    """
    queryset = Advertisement.objects.all()
    serializer_class = AdvertisementDeleteSerializer
    permission_classes = [IsAuthenticated, IsOwnerOrStaff]
