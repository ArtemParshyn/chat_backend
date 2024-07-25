import json
from channels.generic.websocket import WebsocketConsumer
from asgiref.sync import async_to_sync
from django.utils import timezone
from users.models import ApiUser
from .serializers import MessageSerializer
from .models import Message, Group


class ChatConsumer(WebsocketConsumer):

    def connect(self):
        self.room_name = self.scope['url_route']['kwargs']['room_name']
        self.room_group_name = 'chat_%s' % self.room_name
        print(f"room_name = {self.room_name}")

        async_to_sync(self.channel_layer.group_add)(
            self.room_group_name,
            self.channel_name,
        )
        self.accept()

    def receive(self, text_data):
        text_data_json = json.loads(text_data)
        print(f"text_data_json: {text_data_json}")
        message = text_data_json['message']
        author = text_data_json['author']

        async_to_sync(self.channel_layer.group_send)(
            self.room_group_name,
            {
                'type': 'chat_message',
                'author': author,
                'message': message
            }
        )

    def chat_message(self, event):
        author = ApiUser.objects.get(username=event["author"])
        group = Group.objects.get(name=self.room_name)

        # Проверяем, было ли в последние N минут сообщение с таким содержанием
        existing_message = Message.objects.filter(
            group=group,
            author=author,
            content=event["message"],
            date__gte=timezone.now() - timezone.timedelta(seconds=0.1)
        ).first()

        if not existing_message:
            serializer = MessageSerializer(data={
                "group": group.pk,
                "content": event["message"],
                "author": author.pk,
            })

            if serializer.is_valid():
                message_instance = serializer.save()

                # Отправляем сообщение всем участникам группы
                self.send_chat_message(message_instance)
            else:
                print(f"Serializer errors: {serializer.errors}")
        else:
            # Если сообщение уже существует,
            # отправляем его всем участникам группы
            self.send_chat_message(existing_message)

    def send_chat_message(self, message_instance):
        self.send(text_data=json.dumps({
            'type': 'chat',
            'author': message_instance.author.username,
            'message': message_instance.content
        }))
