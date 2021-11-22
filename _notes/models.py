from django.db import models


class Note(models.Model):
    order = models.IntegerField()
    title = models.CharField(max_length=100, blank=True, default='')
    body = models.TextField()
    owner = models.ForeignKey('auth.User', related_name='notes', on_delete=models.CASCADE)
