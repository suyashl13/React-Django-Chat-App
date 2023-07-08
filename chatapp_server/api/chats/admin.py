from django.contrib import admin
from .models import IndividualChatRoom, GroupChatRoom, IndividualChat, GroupChat, GroupMember

# Register your models here.
admin.site.register(IndividualChat)
admin.site.register(IndividualChatRoom)
admin.site.register(GroupChatRoom)
admin.site.register(GroupChat)
admin.site.register(GroupMember)