from rest_framework import permissions


class LanguagePermission(permissions.BasePermission):
    def has_permission(self, request, view):
        if request.method == 'GET':
            return True
        elif request.user.is_superuser:
            return True
        else:
            return False
