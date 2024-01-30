from rest_framework import serializers
from .models import ApiUser


class ApiUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = ApiUser
        fields = ('username', 'password', 'email')

