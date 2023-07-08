# Generated by Django 4.2.3 on 2023-07-08 10:27

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='GroupChatRoom',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('group_name', models.CharField(max_length=40)),
                ('group_description', models.TextField(max_length=125)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('group_admin', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='IndividualChatRoom',
            fields=[
                ('id', models.UUIDField(default=uuid.UUID('42aa3e0e-2fa5-431f-918d-38f3ae3b7b65'), editable=False, primary_key=True, serialize=False)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('person_1', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='person_1', to=settings.AUTH_USER_MODEL)),
                ('person_2', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='person_2', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='IndividualChat',
            fields=[
                ('id', models.UUIDField(default=uuid.UUID('3a97c8fa-df50-4873-a3ac-da8c6916efde'), editable=False, primary_key=True, serialize=False)),
                ('chat_content', models.TextField(max_length=255)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('chat_room', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='chats.individualchatroom')),
                ('sender', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='GroupMember',
            fields=[
                ('id', models.UUIDField(default=uuid.UUID('97e1f6c1-799e-41c5-b0dc-b57b269276a8'), editable=False, primary_key=True, serialize=False)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('group_room', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='chats.groupchatroom')),
            ],
        ),
        migrations.CreateModel(
            name='GroupChat',
            fields=[
                ('id', models.UUIDField(default=uuid.UUID('af25ffdf-725f-468c-be8c-b5ae44263c0a'), editable=False, primary_key=True, serialize=False)),
                ('chat_content', models.TextField(max_length=255)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('chat_room', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='chats.individualchatroom')),
                ('sender', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
