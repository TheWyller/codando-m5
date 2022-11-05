from rest_framework import permissions


class ListUpdateDeletePermission(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):

        if request.method == 'GET':
            return True

        if request.user.is_superuser:
            return True
        elif obj.user == request.user:
            return True
        else:
            return False


class HasPostPermission(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):

        return request.user == obj.user
