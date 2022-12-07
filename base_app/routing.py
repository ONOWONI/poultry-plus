from django.urls import re_path, path

from . import consumers

websocket_urlpatterns = [
    re_path(r'ws/chat/(?P<room_name>\w+)/$', consumers.ChatConsumer.as_asgi()),
    re_path(r'ws/personalchat/(?P<id>[0-9])/$', consumers.PersonalChatConsumer.as_asgi()),
]