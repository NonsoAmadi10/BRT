from rest_framework.permissions import BasePermission, IsAdminUser
from authentication.models import User


class IsAdminOnly(BasePermission):
    message = 'You must be an admin to perform this action'
    SAFE_METHODS = ['GET', 'PUT', 'OPTIONS', 'HEAD', 'PATCH']

    def has_permission(self, request, view):
        if request.method in self.SAFE_METHODS:
            return True

    def has_object_permission(self, request, view):
        return IsAdminUser().has_permission(request, view)
