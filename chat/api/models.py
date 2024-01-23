from django.db import models


class Mesage(models.Model):
    author = models.CharField(max_length=255, default = "None")
    content = models.TextField(max_length=255)
    date = models.DateField(auto_now_add=True)
