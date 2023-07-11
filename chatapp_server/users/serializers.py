from rest_framework.serializers import ModelSerializer

from users.models import CustomUser


class CustomUserSerializer(ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ['id', 'username', 'first_name', 'last_name', 'email', 'created_at', 'updated_at']
