from rest_framework import permissions


class IsManager(permissions.BasePermission):
    def has_permission(self, request, view):
        # CRUD for Manager, R for Developer
        if request.method == 'GET':
            return True
        return "M" == request.user.role