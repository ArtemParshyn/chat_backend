from rest_framework import serializers
from users.models import ApiUser


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = ApiUser
        fields = ('username', 'password', 'email')