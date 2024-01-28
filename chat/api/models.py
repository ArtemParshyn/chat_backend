from django.contrib.auth.models import AbstractUser
from django.db import models


class ApiUser(AbstractUser):
    ...


class Message(models.Model):
    author = models.ForeignKey(ApiUser, verbose_name='ApiUser', on_delete=models.CASCADE)
    content = models.TextField(max_length=255)
    date = models.DateField(auto_now_add=True)
