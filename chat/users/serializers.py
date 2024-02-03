from rest_framework import serializers
from users.models import ApiUser


class ApiUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = ApiUser
        fields = ('username', 'password', 'email')

    # def create(self, validated_data):
    #     password = validated_data.pop('password')
    #     user = ApiUser.objects.create(**validated_data)
    #     user.set_password(password)
    #     user.save()
    #     return user
