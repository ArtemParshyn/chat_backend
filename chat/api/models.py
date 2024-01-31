from django.db import models


class Room(models.Model):
    name = models.CharField(max_length=255)


class Message(models.Model):
    room = models.ForeignKey(Room, on_delete=models.CASCADE)
    content = models.CharField(max_length=255)
    date = models.DateTimeField(auto_now_add=True)
