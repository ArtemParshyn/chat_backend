from rest_framework import serializers
from api.models import Message
from api.models import ApiUser


class MessageSerializer(serializers.ModelSerializer):
    author = serializers.HiddenField(default=serializers.CurrentUserDefault())

    class Meta:
        model = Message
        fields = ('id', 'author', 'content', 'date')


class ApiUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = ApiUser
        fields = ('id', 'username', 'password')

    def create(self, validated_data):
        return ApiUser.objects.create_user(**validated_data)