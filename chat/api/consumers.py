import json
from channels.generic.websocket import WebsocketConsumer
from asgiref.sync import async_to_sync
from .models import Message


class ChatConsumer(WebsocketConsumer):
    def connect(self):
        self.room_name = self.scope['url_route']['kwargs']['room_name']
        self.room_group_name = 'chat_%s' % self.room_name
        # self.user = self.scope['url_route']['kwargs']['user_name']

        async_to_sync(self.channel_layer.group_add)(
            self.room_group_name,
            self.channel_name,
            # self.user
        )

        self.accept()

    def disconnect(self, close_code):
        async_to_sync(self.channel_layer.group_discard)(
            self.room_name,
            self.channel_name,
            # self.user
        )

    def receive(self, text_data):
        text_data_json = json.loads(text_data)
        message = text_data_json['message']
        # username_json = json.loads(username)
        # user = username_json['user']

        async_to_sync(self.channel_layer.group_send)(
            self.room_group_name,
            {
                'type': 'chat_message',
                'message': message,
                # 'user': user
            }
        )

    def chat_message(self, event):
        message = event['message']
        # user = event['user']
        # db = Message.objects.create(author=user, content=message)

        self.send(text_data=json.dumps({
            'type': 'chat',
            # 'author': user,
            'message': message
        }))
