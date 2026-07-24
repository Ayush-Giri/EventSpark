from rest_framework.permissions import BasePermission

class IsOrganiser(BasePermission):
    message = "only organniser can perform this action"
    def has_permission(self, request, view):
        if request.user.role == "organiser":
            return True
        return False


class IsEventOwner(BasePermission):
    def has_object_permission(self, request, view, obj):
        # view is the view or viewset using this permission
        # obj is the specific models intance being accessed
        return obj.organiser == request.user