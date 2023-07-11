from django.db import models
import uuid

from users.models import CustomUser


# Create your models here.
class Room(models.Model):
    id = models.UUIDField(
        primary_key=True,
        default=uuid.uuid4,
        editable=False)

    created_user = models.ForeignKey(CustomUser, related_name='created_user',
                                     on_delete=models.CASCADE)
    added_user = models.ForeignKey(CustomUser, related_name='added_user',
                                   on_delete=models.CASCADE)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class Chat(models.Model):
    id = models.UUIDField(
        primary_key=True,
        default=uuid.uuid4,
        editable=False)

    room = models.ForeignKey(Room, on_delete=models.CASCADE, null=True)

    message = models.TextField()

    from_user = models.ForeignKey(CustomUser, related_name='from_user',
                                  on_delete=models.CASCADE)
    to_user = models.ForeignKey(CustomUser, related_name='to_user',
                                on_delete=models.CASCADE)

    is_seen = models.BooleanField(default=False)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
