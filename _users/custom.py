from rest_framework.permissions import BasePermission


class UserPermission(BasePermission):
    """
    用户操作权限
    1. 操作：管理员+用户自身
    """

    def has_permission(self, req, view):
        if not req.user or not req.user.is_authenticated:
            return False
        if req.user.is_superuser:
            return True
        if view.kwargs.get('pk') == str(req.user.id):
            return True
        return False


class IsOwner(BasePermission):
    """
    所有者操作权限
    1. 操作：管理员+所有者
    """

    def has_object_permission(self, req, view, obj):
        if not req.user or not req.user.is_authenticated:
            return False
        if req.user.is_superuser:
            return True
        if obj.owner == req.user:
            return True
        return False
