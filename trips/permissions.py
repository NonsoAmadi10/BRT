from rest_framework.permissions import BasePermission
from authentication.models import User


class IsAdminOnly(BasePermission):
    message = 'You must be the owner of this object.'
    my_safe_method = ['GET', 'PUT', 'OPTIONS', 'HEAD', 'PATCH']

    def has_permission(self, request, view):
        return request.user.is_admin == True
