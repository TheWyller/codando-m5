from rest_framework import permissions


class ListUpdateDeletePermission(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):

        if request.user.is_superuser:
            return True
        elif obj == request.user:
            return True
        else:
            return False

class HasPostPermission(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        print(obj)
        print(obj)
        print(obj)
        print(obj)
        print(request)
        print(request)
        print(request)
        print(request)
        return request.user == obj.user
