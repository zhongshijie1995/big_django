from rest_framework.permissions import BasePermission


class UserPermission(BasePermission):
    """
    用户操作权限
    1. 操作：管理员+用户自身
    """

    def has_permission(self, req, view):
        if not req.user:
            return False
        if not req.user.is_authenticated:
            return False
        if req.user.is_superuser:
            return True
        if view.kwargs.get('pk') == str(req.user.id):
            return True
        return False
