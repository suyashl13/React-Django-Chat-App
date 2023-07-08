from django.contrib import admin

from api.users.models import CustomUser

# Register your models here.
admin.site.register(CustomUser)