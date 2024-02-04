from django.contrib.auth import authenticate, logout as django_logout
from django.contrib.sessions.backends.db import SessionStore
from django.shortcuts import render
from django.urls import reverse
from django.views.decorators.csrf import csrf_exempt

from .serializers import ApiUserSerializer
from .models import ApiUser

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes


from rest_framework_simplejwt.tokens import RefreshToken


class ApiUserView(APIView):

    def get(self, request):
        user = ApiUser.objects.all()
        return Response({'users': ApiUserSerializer(user, many=True).data})


@api_view(['POST']) # Использовал декоратор т.к. в классе можно определить только один метод пост для одного дейсивия(ну по крайней мере я знаю только для одного действия)
@csrf_exempt        # Добавил просто на всякий случай
# @permission_classes(['AllowAny']) пока не работает, хз почему
def login(request):
    '''
    request идет от rest_framework.request.Request изза чего не работает джанговский логин. Джанговский логин принимает
    request.HttpRequest, а не от drf изза чего программа падает, поэтому логин сделал на сессиях, там создается отдельный
    session, который уже логинит пользователя.

    request._request чтобы не возникало проблем с определением самого этого параметра, но если често хз, сам в этом плавю еще,
    на stack overflow порекомендовали использовать его

    refresh_token создает токены для пользователя, если правильно ввел данные и они уже потом отправляются в response,
    refresh_toke.set_cookie я сам не особо понял что это
    '''
    username = request.data.get('username')
    password = request.data.get('password')

    if username is None or password is None:
        return Response({'error': 'Please provide both username and password.'}, status=400)

    user = authenticate(request._request, username=username, password=password)

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

    response = Response(response_data)

    response.set_cookie('sessionid', session.session_key)

    return response


@api_view(['POST'])
@csrf_exempt
# @permission_classes('AllowAny') Пока не работает, хз почему
def register(request):
    '''
    Все то же самое, что и в login, но просто создается новый пользователь, ну и поля username & password обязательны для
    заполнения
    '''
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
@csrf_exempt
# @permission_classes(['IsAuthenticated']) пока не работает, хз почему
def logout(request):
    '''
    Тут просто выходим из системы и все, ну и куки еще удаляются, хотя если у нас токены то куки наверное не нужны
    '''
    django_logout(request) # странно, что для login параметр request от drf не работает, а для остального норм
    response = Response({'message': 'Logged out successfully.'})
    response.delete_cookie('sessionid')
    return response


