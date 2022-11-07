from rest_framework import permissions
from rest_framework.views import Request


class CategoryPermission(permissions.BasePermission):
    def has_permission(self, request:Request, view):
        if request.method == 'GET':
            return True
        elif request.user.is_authenticated:
            return True
        else:
            return False
