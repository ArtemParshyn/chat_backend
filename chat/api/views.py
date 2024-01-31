import rest_framework.renderers
from rest_framework import status
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework import viewsets

from api.models import Message
from api.serializers import MessageSerializer


class RoomView(viewsets.ModelViewSet):
    queryset = Message.objects.all()
    http_method_names = ["get"]
    serializer_class = MessageSerializer

    @action(detail=True, methods=['post'])
    def post(self):
        ...

    @action(detail=True, methods=['delete'])
    def delete(self):
        ...
