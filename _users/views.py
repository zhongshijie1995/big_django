from django.contrib.auth.models import User, Group
from rest_framework import viewsets
from rest_framework.permissions import IsAdminUser

from _users.custom import UserPermission
from _users.serializers import UserSerializer, GroupSerializer


class UserViewSet(viewsets.ModelViewSet):
    """
    允许用户查看或编辑的API路径。
    """
    queryset = User.objects.all().order_by('pk')
    serializer_class = UserSerializer

    permission_classes = (UserPermission,)

    def get_queryset(self):
        if self.request.user.is_staff:
            return User.objects.all().order_by('pk')
        return User.objects.filter(username=self.request.user.username).order_by('pk')


class GroupViewSet(viewsets.ModelViewSet):
    """
    允许组查看或编辑的API路径。
    """
    queryset = Group.objects.all()
    serializer_class = GroupSerializer

    permission_classes = (IsAdminUser,)
