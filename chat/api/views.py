from django.urls import reverse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.decorators import permission_classes
from rest_framework.permissions import IsAuthenticated

from api.models import Message, Group
from api.serializers import GroupSerializer
from django.http import HttpResponse
from django.shortcuts import render, redirect


def index(request):
    return render(request, 'api/index.html')


@csrf_exempt
def room(request, room_name):
    if not Group.objects.filter(name=room_name).exists():
        serializer = GroupSerializer(data={"name": room_name})
        if serializer.is_valid():
            serializer.save()
        return redirect("/")
    else:
        print(request.user)
        print(request.COOKIES["sessionid"])
        if not request.user.is_authenticated:
            return HttpResponse(status=403)
        else:
            cookie_value = request.COOKIES.get('sessionid')
            print(f"cookie_value = {cookie_value}")
            room_object = Group.objects.get(name=room_name)
            message_objects_all = Message.objects.filter(group=room_object)
            messages = [{
                "author": message.author.username,
                "content": message.content
            } for message in message_objects_all]
            print(request)
            return render(request, 'api/room.html', {
                'room_name': room_name,
                "user_name": request.user.username,
                "messages": messages
            })
