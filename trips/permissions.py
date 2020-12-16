from rest_framework.permissions import BasePermission
from authentication.models import User


class IsAdminOnly(BasePermission):
    message = 'You must be an admin to perform this action'
    my_safe_method = ['GET', 'PUT', 'OPTIONS', 'HEAD', 'PATCH']

    def has_object_permission(self, request, view):
        return request.user.is_admin == True
