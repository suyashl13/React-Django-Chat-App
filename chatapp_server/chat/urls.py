from django.urls import path
from chat.views import room_router

urlpatterns = [
    path('room/', room_router)
]
