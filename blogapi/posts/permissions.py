from rest_framework import permissions


class IsAuthorOrReadOnly(permissions.BasePermission):
    """ used to grant permission on a post to the author only """

    def has_permission(self, request, view):
        """ returns true if permission is granted. false otherwise """
        if request.user.is_authenticated:
            return True
        return False
    
    def has_object_permission(self, request, view, obj):
        """ returns true is object access is granted. false otherwise """
        if request.method in permissions.SAFE_METHODS:
            return True

        return obj.author == request.user