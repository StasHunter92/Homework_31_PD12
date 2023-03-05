from rest_framework.permissions import BasePermission

from authentication.models import User


# ----------------------------------------------------------------------------------------------------------------------
# Create custom permissions
class IsStaff(BasePermission):
    message: str = "You are not the moderator or administrator"

    def has_permission(self, request, view):
        if request.user.role in [User.Roles.MODERATOR, User.Roles.ADMIN]:
            return True
        return False
