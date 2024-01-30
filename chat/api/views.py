from django.http import HttpResponse
from django.shortcuts import render


def index(request):
    return render(request, 'api/index.html')


def room(request, room_name):
    if request.user.is_authenticated:
        return render(request, 'api/room.html', {'room_name': room_name, "user_name": request.user.username})
    else:
        return HttpResponse("<h1>User is not authorized</h1>")
