import json
from channels.generic.websocket import AsyncWebsocketConsumer
from .models import ChatModel
from channels.db import database_sync_to_async

class ChatConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        self.room_name = self.scope['url_route']['kwargs']['room_name']
        self.room_group_name = 'chat_%s' % self.room_name

        # Join room group
        await self.channel_layer.group_add(
            self.room_group_name,
            self.channel_name
        )

        await self.accept()

    async def disconnect(self, close_code):
        # Leave room group
        await self.channel_layer.group_discard(
            self.room_group_name,
            self.channel_name
        )

    # Receive message from WebSocket
    async def receive(self, text_data):
        text_data_json = json.loads(text_data)
        message = text_data_json['message']
        owner = text_data_json['owner']

        # Send message to room group
        await self.channel_layer.group_send(
            self.room_group_name,
            {
                'type': 'chat_message',
                'message': message,
                'owner': owner,
            }
        )

    # Receive message from room group
    async def chat_message(self, event):
        message = event['message']
        owner = event['owner']

        # Send message to WebSocket
        await self.send(text_data=json.dumps({
            'message': message,
            'owner' : owner,
        }))



class PersonalChatConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        my_id = self.scope['user'].id
        other_user_id = self.scope['url_route']['kwargs']['id']

        if int(my_id) > int(other_user_id):
            self.room_name = f'{my_id}-{other_user_id}-pro'
        else:
            self.room_name = f'{other_user_id}-{my_id}-pro'

        self.room_group_name = 'chat_%s' % self.room_name

          # Join room group
        await self.channel_layer.group_add(
            self.room_group_name,
            self.channel_name
        )

        await self.accept()


    async def disconnect(self, close_code):
        # Leave room group
        await self.channel_layer.group_discard(
            self.room_group_name,
            self.channel_name
        )

    # Receive message from WebSocket
    async def receive(self, text_data=None, bytes_data=None):
        text_data_json = json.loads(text_data)
        message = text_data_json['message']
        owner = text_data_json['owner']


        await save_message(owner, self.room_group_name, message)

        # Send message to room group
        await self.channel_layer.group_send(
            self.room_group_name,
            {
                'type': 'chat_message',
                'message': message,
                'owner': owner,
            }
        )

    # Receive message from room group
    async def chat_message(self, event):
        message = event['message']
        owner = event['owner']

        # Send message to WebSocket
        await self.send(text_data=json.dumps({
            'message': message,
            'owner' : owner,
        }))


@database_sync_to_async
def save_message(username, thread_name, message):
    savemessage = ChatModel(message=message, sender=username, thread_name=thread_name)
    savemessage.save()
