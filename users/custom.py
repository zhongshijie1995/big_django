from rest_framework.permissions import BasePermission, SAFE_METHODS


class UserPermission(BasePermission):
    """
    用户操作权限
    1. 操作：管理员+用户自身
    2. 查询：用户
    """

    def has_permission(self, req, view):
        if req.user.is_superuser:
            return True
        elif view.kwargs.get('pk') == str(req.user.id):
            return True
        elif req.method in SAFE_METHODS and req.user.is_authenticated:
            return True
        return False
