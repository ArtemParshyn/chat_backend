from django.contrib.auth import authenticate, login
from django.http import HttpResponse
from django.shortcuts import render
from .serializers import ApiUserSerializer
from .models import ApiUser


def register(request):
    if request.method == 'POST':
        serializer = ApiUserSerializer(data=request.POST)

        if serializer.is_valid():
            username = serializer.validated_data["username"]
            password = serializer.validated_data["password"]
            email = serializer.validated_data["email"]
            print(f"username - {username}")
            print(f"password - {password}")
            print(f"email - {email}")

            user = ApiUser.objects.create_user(
                username=username,
                password=password,
                email=email
            )
            user.save()
            print("Logined")
            user = authenticate(username=username, password=password, email=email)
            login(request, user)
            return HttpResponse("<h1>User created, authorized</h1>")
        else:
            return HttpResponse("<h1>Is not valid</h1>")
    else:
        return render(request, 'api/users/reg.html')
