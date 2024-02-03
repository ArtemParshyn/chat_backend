import json
from channels.generic.websocket import WebsocketConsumer
from asgiref.sync import async_to_sync


class ChatConsumer(WebsocketConsumer):

    def connect(self):
        self.room_name = self.scope['url_route']['kwargs']['room_name']
        self.room_group_name = 'chat_%s' % self.room_name
        print(self.scope["user"])
        self.user = self.scope['user']
        if self.user.is_authenticated:
            async_to_sync(self.channel_layer.group_add)(
                self.room_group_name,
                self.channel_name
            )
            self.accept()
        else:
            print("User is not authenticated")

    def receive(self, text_data):
        text_data_json = json.loads(text_data)
        message = text_data_json['message']

        if self.user.is_authenticated:
            async_to_sync(self.channel_layer.group_send)(
                self.room_group_name,
                {
                    'type': 'chat_message',
                    'author': (self.user),
                    'message': message
                }
            )

    def chat_message(self, event):
        message = event['message']
        if self.user.is_authenticated:
            self.send(text_data=json.dumps({
                'type': 'chat',
                'author': str(self.user),
                'message': message
            }))
