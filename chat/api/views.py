from django.shortcuts import render
from .serializers import MessageSerializer
from rest_framework import generics
from .models import Message


class MessageViewSet(generics.ListCreateAPIView):
    queryset = Message.objects.all()
    serializer_class = MessageSerializer


def index(request):
    return render(request, 'api/index.html')


def room(request, room_name):
    return render(request, 'api/room.html', {'room_name': room_name})