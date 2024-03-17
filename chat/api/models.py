from django.db import models
from users.models import ApiUser


class Group(models.Model):
    name = models.CharField(max_length=255, unique=True, db_index=True)
    date_create = models.DateField(auto_now_add=True)


class Message(models.Model):
    group = models.ForeignKey(Group, related_name="messages", on_delete=models.CASCADE)
    author = models.ForeignKey(ApiUser, verbose_name='ApiUser', on_delete=models.CASCADE)
    content = models.CharField(max_length=255)
    date = models.DateTimeField(auto_now_add=True)
