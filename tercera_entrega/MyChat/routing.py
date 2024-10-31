from django.urls import path, include
from MyChat.consumer import ChatConsumer

websocket_urlpatterns = [
    path("", ChatConsumer.as_asgi()),
]