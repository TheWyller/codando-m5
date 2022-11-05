from rest_framework import permissions


class CreateListPermission(permissions.BasePermission):
    def has_permission(self, request, view):
        if request.method == 'POST':
            return True
        elif request.user.is_superuser:
            return True
        else:
            return False


class ListUpdateDeletePermission(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):

        if request.user.is_superuser:
            return True
        elif obj == request.user:
            return True
        else:
            return False
