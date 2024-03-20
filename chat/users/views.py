from django.contrib.auth import authenticate, logout as django_logout
from django.contrib.sessions.backends.db import SessionStore
from django.shortcuts import redirect

from .serializers import UserSerializer
from .models import ApiUser

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated


from rest_framework_simplejwt.tokens import RefreshToken


class ApiUserView(APIView):
    def get(self, request):
        user = ApiUser.objects.all()
        return Response({'users': UserSerializer(user, many=True).data})


@api_view(['POST'])
def login(request):
    username = request.data.get('username')
    password = request.data.get('password')

    if username is None or password is None:
        return Response({'error': 'Please provide both username and password.'}, status=400)

    user = authenticate(request._request, username=username, password=password)
    print("user:", user)

    if user is None:
        return Response({'error': 'Invalid username or password.'}, status=400)

    session = SessionStore()
    session.create()
    session['django.contrib.auth.middleware.SessionMiddleware'] = str(user.id)
    session.save()

    refresh_token = RefreshToken.for_user(user)

    response_data = {
        'refresh_token': str(refresh_token),
        'access_token': str(refresh_token.access_token),
    }

    print(f"access_token: {response_data['access_token']}")

    response = Response(response_data)

    response.set_cookie('sessionid', session.session_key)

    return response



@api_view(['POST'])
def register(request):
    username = request.data.get('username')
    password = request.data.get('password')
    email = request.data.get('email')

    if username is None or password is None:
        return Response({'error': 'Please provide both username and password.'}, status=400)

    try:
        user = ApiUser.objects.create_user(username=username, password=password, email=email)
    except Exception as e:
        return Response({'error': str(e)}, status=400)

    session = SessionStore()
    session.create()
    session['django.contrib.auth.middleware.SessionMiddleware'] = str(user.id)
    session.save()

    refresh_token = RefreshToken.for_user(user)

    response_data = {
        'refresh_token': str(refresh_token),
        'access_token': str(refresh_token.access_token),
    }

    response = Response(response_data)

    response.set_cookie('sessionid', session.session_key)

    return response


@api_view(['POST'])
@permission_classes([IsAuthenticated])
def logout(request):
    django_logout(request)
    response = Response({'message': 'Logged out successfully.'})
    response.delete_cookie('sessionid')
    return response
