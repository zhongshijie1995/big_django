from rest_framework import serializers

from _notes.models import Note


class NotesSerializer(serializers.HyperlinkedModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')

    class Meta:
        model = Note
        fields = ('url', 'order', 'title', 'body', 'owner')
