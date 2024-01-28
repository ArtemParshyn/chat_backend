from django.shortcuts import render
from .serializers import MessageSerializer, AuthorSerializer
from rest_framework import viewsets
from rest_framework.views import APIView
from rest_framework.response import Response
from api.models import Message
from api.models import ApiUser


from rest_framework import viewsets
from .models import Message
from .serializers import MessageSerializer
from .permissions import IsAuthenticatedOrReadOnly

class MessageViewSet(viewsets.ModelViewSet):
    queryset = Message.objects.all()
    serializer_class = MessageSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]


class AuthorApiView(APIView):
    def get(self, request):
        user = ApiUser.objects.all()
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

