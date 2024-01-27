from django.db import models
from users.models import User


class Message(models.Model):
    author = models.ForeignKey(User, verbose_name='User', on_delete=models.CASCADE)
    content = models.TextField(max_length=255)
    date = models.DateField(auto_now_add=True)


