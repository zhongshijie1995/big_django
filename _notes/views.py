from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated

from _notes.models import Note
from _notes.serializers import NotesSerializer
from _users.custom import IsOwner


class NotesViewSet(viewsets.ModelViewSet):
    """
    允许用户查看或编辑的API路径。
    """
    queryset = Note.objects.all().order_by('order')
    serializer_class = NotesSerializer

    permission_classes = (IsAuthenticated, IsOwner,)

    def get_queryset(self):
        if self.request.user and self.request.user.is_staff:
            return Note.objects.all().order_by('owner_id', 'order')
        return Note.objects.filter(owner=self.request.user).order_by('order')

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)
