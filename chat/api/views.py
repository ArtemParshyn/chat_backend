from django.db.models.functions import TruncDate
from django.urls import reverse

from api.models import Message, Group
from api.serializers import GroupSerializer
from django.http import HttpResponse
from django.shortcuts import render, redirect


def index(request):
    return render(request, 'api/index.html')


def room(request, room_name):
    if not Group.objects.filter(name=room_name).exists():
        serializer = GroupSerializer(data={"name": room_name})
        if serializer.is_valid():
            serializer.save()
        return redirect("/")
    else:
        if request.user.is_authenticated:
            room_object = Group.objects.get(name=room_name)
            message_objects_all = Message.objects.filter(group=room_object)
            unique_dates = Message.objects.filter(group=room_object).annotate(date_only=TruncDate('date')).values('date_only').distinct()
            messages_by_date = {}
            for date in unique_dates:
                date_only = date['date_only']
                messages_by_date[date_only] = Message.objects.filter(date__date=date_only)
            #unique_dates_list = unique_dates.values('date_only')

            return render(request, 'api/room.html', {
                'room_name': room_name,
                "user_name": request.user.username,
                'messages_by_date': messages_by_date,

            })
        else:
            return HttpResponse(status=403)
