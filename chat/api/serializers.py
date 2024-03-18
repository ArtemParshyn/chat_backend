from rest_framework import serializers
from .models import Message, Group


class GroupSerializer(serializers.ModelSerializer):
    class Meta:
        model = Group
        fields = ("name", "date_create")

    def create(self, validated_data):
        name = validated_data["name"]
        print("creating new group")
        return Group.objects.create(
            name=name
        )


class MessageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Message
        fields = ('group', 'author', 'content', 'date')

    def create(self, validated_data):
        group = validated_data["group"]
        author = validated_data["author"]
        content = validated_data["content"]
        print("creating message")
        return Message.objects.create(
            group=group,
            author=author,
            content=content,
        )