from rest_framework.permissions import BasePermission

from medeina.exceptions import NotAuthenticatedException, SuperuserException


class UserIsAuthenticated(BasePermission):
    """A custom API permission for raising custom error message when user is not
    authenticated
    """

    def has_permission(self, request, view):
        allowed_access = request.user and request.user.is_authenticated()

        if not allowed_access:
            raise NotAuthenticatedException

        return allowed_access


class UserIsSuperuser(BasePermission):
    """A custom API permission for raising custom error message when user is not
    superuser
    """

    def has_permission(self, request, view):
        allowed_access = request.user.is_superuser

        if not allowed_access:
            raise SuperuserException

        return allowed_access
