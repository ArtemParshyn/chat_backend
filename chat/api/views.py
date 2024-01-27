from django.shortcuts import render
from .serializers import MessageSerializer, AuthorSerializer
from rest_framework import viewsets
from rest_framework.views import APIView
from rest_framework.response import Response
from api.models import Message
from users.models import User


class MessageViewSet(viewsets.ModelViewSet):
    queryset = Message.objects.all()
    serializer_class = MessageSerializer


class AuthorApiView(APIView):
    def get(self, request):
        user = User.objects.all()
        return Response({'users': AuthorSerializer(user, many=True).data})

    def post(self, request):
        serializer = AuthorSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()

        return Response({'post': serializer.data})


def index(request):
    return render(request, 'api/index.html')


def room(request, room_name):
    return render(request, 'api/room.html', {'room_name': room_name})

