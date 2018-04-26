""" Custom API permissions. """

from rest_framework import permissions


class IsAdminUserOrInGroup(permissions.BasePermission):
    """
    Find the requesting user is either staff or belong to 'ENTERPRISE_API_ALLOWED_GROUPS'.
    It will return a 403 forbidden response with a message if the user is not authorized to access the view.
    """
    message = 'User is not allowed to access the view.'
    def has_permission(self, request, view, *args):
        if request.user.is_staff or request.user.groups.filter(name__in=view.ENTERPRISE_API_ALLOWED_GROUPS).exists():
            return True

        return False
