from rest_framework.permissions import BasePermission, IsAdminUser, IsAuthenticated


class IsAdminOrUser(BasePermission):
    SAFE_METHODS = ['OPTIONS', 'HEAD', 'GET', "POST"]

    def has_permission(self, request, view):
        if IsAuthenticated().has_permission(request, view) and request.method in self.SAFE_METHODS:
            return True
        return IsAdminUser().has_permission(request, view)
