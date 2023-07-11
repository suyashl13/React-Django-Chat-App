from django.contrib.auth.models import AbstractUser
from django.db import models
import uuid


# Create your models here.
class CustomUser(AbstractUser):
    id = models.UUIDField(
        primary_key=True,
        default=uuid.uuid4,
        editable=False)

    phone = models.CharField(unique=True, max_length=12)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return "{} {} ({})".format(self.first_name, self.last_name, self.username)
