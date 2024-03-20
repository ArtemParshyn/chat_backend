from django.urls import reverse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.decorators import permission_classes
from rest_framework.permissions import IsAuthenticated

from api.models import Message, Group
from api.serializers import GroupSerializer
from django.http import HttpResponse
from django.shortcuts import render, redirect
# views.py

from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from api.models import Message, Group
from api.serializers import GroupSerializer


@api_view(['GET'])
@permission_classes([IsAuthenticated])
def get_room(request, room_name):
    try:
        room_object = Group.objects.get(name=room_name)
        message_objects_all = Message.objects.filter(group=room_object)
        messages = [{
            "author": message.author.username,
            "content": message.content
        } for message in message_objects_all]
        return Response({
            'room_name': room_name,
            "user_name": request.user.username,
            "messages": messages
        })
    except Group.DoesNotExist:
        return Response(status=404)


@api_view(['POST'])
@permission_classes([IsAuthenticated])
def create_room(request):
    serializer = GroupSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=201)
    return Response(serializer.errors, status=400)


var = ("\n"
       "\n"
       "def index(request):\n"
       "    return render(request, 'api/index.html')\n"
       "\n"
       "\n"
       "def room(request, room_name):\n"
       "    if not Group.objects.filter(name=room_name).exists():\n"
       "        serializer = GroupSerializer(data={\"name\": room_name})\n"
       "        if serializer.is_valid():\n"
       "            serializer.save()\n"
       "        return redirect(\"/\")\n"
       "    else:\n"
       "        print(\"user: \",request.user)\n"
       "        print(request.COOKIES[\"sessionid\"])\n"
       "        if not request.user.is_authenticated:\n"
       "            return HttpResponse(status=403)\n"
       "        else:\n"
       "            cookie_value = request.COOKIES.get('sessionid')\n"
       "            print(f\"cookie_value = {cookie_value}\")\n"
       "            room_object = Group.objects.get(name=room_name)\n"
       "            message_objects_all = Message.objects.filter(group=room_object)\n"
       "            messages = [{\n"
       "                \"author\": message.author.username,\n"
       "                \"content\": message.content\n"
       "            } for message in message_objects_all]\n"
       "            print(request)\n"
       "            return render(request, 'api/room.html', {\n"
       "                'room_name': room_name,\n"
       "                \"user_name\": request.user.username,\n"
       "                \"messages\": messages\n"
       "            })\n")
