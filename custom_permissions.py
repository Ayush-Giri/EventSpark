from rest_framework.permissions import BasePermission

class IsOrganiser(BasePermission):
    message = "only organniser can perform this action"
    def has_permission(self, request, view):
        if request.user.role == "organiser":
            return True
        return False