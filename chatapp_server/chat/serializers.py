from rest_framework.serializers import ModelSerializer

from chat.models import Room, Chat


class RoomSerializer(ModelSerializer):
    class Meta:
        model = Room
        fields = '__all__'


class ChatSerializer(ModelSerializer):
    class Meta:
        model = Chat
        fields = '__all__'
