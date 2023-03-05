from rest_framework.permissions import BasePermission

from authentication.models import User


# ----------------------------------------------------------------------------------------------------------------------
# Create custom permissions
class IsOwnerOrStaff(BasePermission):
    message: str = "You are not the owner or staff member"

    def has_object_permission(self, request, view, obj):
        if request.user == obj.owner or request.user.role in [User.Roles.MODERATOR, User.Roles.ADMIN]:
            return True
        return False
