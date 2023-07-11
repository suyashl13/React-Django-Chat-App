from django.urls import path

from chat.consumers import ChatConsumer

websocket_urlpatterns = [
    path('chat/<str:room_id>/', ChatConsumer.as_asgi())
]