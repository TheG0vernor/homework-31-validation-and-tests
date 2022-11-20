from rest_framework.permissions import BasePermission


class SelectionPermission(BasePermission):
    message = 'not access for its owner'

    def has_object_permission(self, request, view, obj):
        if obj.owner != request.user:
            return False
        return True
