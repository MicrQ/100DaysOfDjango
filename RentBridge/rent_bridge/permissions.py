from rest_framework import permissions


class IsAdminOrReadOnly(permissions.BasePermission):
    """ custom permission to allow only admin to edit """
    def has_permission(self, request, view):
        return (request.method in permissions.SAFE_METHODS
                or request.user.is_staff)
