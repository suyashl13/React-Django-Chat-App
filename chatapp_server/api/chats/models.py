from django.db import models
import uuid

from api.users.models import CustomUser


# Create your models here.
class GroupChatRoom(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)

    group_name = models.CharField(max_length=40)
    group_description = models.TextField(max_length=125)
    group_admin = models.ForeignKey(CustomUser, on_delete=models.CASCADE)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class IndividualChatRoom(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4(), editable=False)

    person_1 = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name='person_1')
    person_2 = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name='person_2')

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class GroupMember(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4(), editable=False)

    group_room = models.ForeignKey(GroupChatRoom, on_delete=models.CASCADE)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class IndividualChat(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4(), editable=False)

    sender = models.ForeignKey(CustomUser, on_delete=models.SET_NULL, null=True)

    chat_content = models.TextField(max_length=255)
    chat_room = models.ForeignKey(IndividualChatRoom, on_delete=models.CASCADE)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class GroupChat(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4(), editable=False)

    sender = models.ForeignKey(CustomUser, on_delete=models.SET_NULL, null=True)

    chat_content = models.TextField(max_length=255)
    chat_room = models.ForeignKey(IndividualChatRoom, on_delete=models.CASCADE)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
