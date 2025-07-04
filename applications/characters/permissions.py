from rest_framework import permissions

class IsAdminOrReadOnly(permissions.BasePermission):
    """
    Permite solo lectura a usuarios autenticados y escritura solo a admin.
    """
    def has_permission(self, request, view):
        if request.method in permissions.SAFE_METHODS:
            return request.user and request.user.is_authenticated
        return request.user and request.user.is_staff
