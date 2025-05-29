from rest_framework.permissions import BasePermission

class IsAdminOrAssignedUser(BasePermission):

    def has_object_permission(self, request, view, obj):
        return request.user.is_staff or obj.assigned_to == request.user
