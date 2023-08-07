from rest_framework import permissions
from rest_framework.views import Request, View


class AuthenticatedOrReadOnly(permissions.BasePermission):
    def has_obj_permission(self, request: Request, view: View, obj):
        if request.method == 'GET':
            return obj
        else:
            return request.user.is_authenticated
