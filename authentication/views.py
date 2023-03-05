from rest_framework.generics import ListAPIView, RetrieveAPIView, CreateAPIView, UpdateAPIView, DestroyAPIView
from rest_framework.pagination import PageNumberPagination
from rest_framework.permissions import IsAuthenticated

from authentication.models import User
from authentication.permissions import IsOwnerOrStaff
from authentication.serializers import UserListSerializer, UserDetailSerializer, UserCreateSerializer, \
    UserUpdateSerializer, UserDeleteSerializer


# ----------------------------------------------------------------------------------------------------------------------
# Custom paginator
class Paginator(PageNumberPagination):
    page_size: int = 5


# ----------------------------------------------------------------------------------------------------------------------
# User ApiView
class UserListView(ListAPIView):
    """
    GET list of users
    """
    queryset = User.objects.all()
    serializer_class = UserListSerializer
    pagination_class = Paginator


class UserDetailView(RetrieveAPIView):
    """
    GET one user
    """
    queryset = User.objects.all()
    serializer_class = UserDetailSerializer
    permission_classes = [IsAuthenticated]


class UserCreateView(CreateAPIView):
    """
    POST to create user
    """
    queryset = User.objects.all()
    serializer_class = UserCreateSerializer


class UserUpdateView(UpdateAPIView):
    """
    PATCH to update user
    """
    queryset = User.objects.all()
    serializer_class = UserUpdateSerializer
    permission_classes = [IsAuthenticated, IsOwnerOrStaff]


class UserDeleteView(DestroyAPIView):
    """
    DELETE to delete user
    """
    queryset = User.objects.all()
    serializer_class = UserDeleteSerializer
    permission_classes = [IsAuthenticated, IsOwnerOrStaff]
