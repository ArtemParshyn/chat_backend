from rest_framework import viewsets
from .models import Message
from .serializers import MessageSerializer
from django.shortcuts import render


class MessageViewSet(viewsets.ModelViewSet):
    queryset = Message.objects.all()
    serializer_class = MessageSerializer


def index(request):
    return render(request, 'api/index.html')


def room(request, room_name):
    return render(request, 'api/room.html', {'room_name': room_name})
