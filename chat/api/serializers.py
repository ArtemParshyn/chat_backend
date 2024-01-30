from rest_framework import serializers
from .models import Message


class MessageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Message
        fields = ('author', 'content', 'date')

    def create(self, validated_data):
        author = validated_data["author"]
        content = validated_data["content"]
        print("creating")
        return Message.objects.create(
            author=author,
            content=content,
        )
