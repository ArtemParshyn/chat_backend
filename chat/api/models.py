from django.db import models
from users.models import ApiUser


class Message(models.Model):
    author = models.ForeignKey(ApiUser, verbose_name='ApiUser', on_delete=models.CASCADE)
    content = models.CharField(max_length=255)
    date = models.DateTimeField(auto_now_add=True)
