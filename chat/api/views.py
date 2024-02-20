from api.models import Message, Group
from api.serializers import GroupSerializer
from django.http import HttpResponse
from django.shortcuts import render


def index(request):
    return render(request, 'api/index.html')


def room(request, room_name):
    if not Group.objects.filter(name=room_name).exists():
        serializer = GroupSerializer(data={"name": room_name})
        if serializer.is_valid():
            serializer.save()
        return HttpResponse(status=200)
    else:
        if request.user.is_authenticated:
            room_object = Group.objects.get(name=room_name)
            message_objects_all = Message.objects.filter(group=room_object)
            messages = [{
                "author": message.author.username,
                "content": message.content
            } for message in message_objects_all]

            return render(request, 'api/room.html', {
                'room_name': room_name,
                "user_name": request.user.username,
                "messages": messages
            })
        else:
            return HttpResponse(status=403)
