from rest_framework import viewsets
from .models import Message, ApiUser
from .serializers import MessageSerializer, ApiUserSerializer
from .permissions import IsAuthenticatedOrReadOnly
from django.contrib.auth.models import User
from django.shortcuts import render, redirect


class MessageViewSet(viewsets.ModelViewSet):
    queryset = Message.objects.all()
    serializer_class = MessageSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]


def register(request):
    if request.method == 'POST':

        serializer = ApiUserSerializer(data=request.POST)

        if serializer.is_valid():
            user = User.objects.create_user(
                username=serializer.validated_data["username"],
                password=serializer.validated_data["password"],
                email=serializer.validated_data["email"]
               )
            user.save()

            return redirect('')
        else:
            return render(request, 'api/reg.html', {'serializer': serializer})
    else:
        return render(request, 'api/reg.html')


def index(request):
    return render(request, 'api/index.html')


def room(request, room_name):
    return render(request, 'api/room.html', {'room_name': room_name})
