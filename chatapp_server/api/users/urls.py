from django.urls import path
from .views import users_route

urlpatterns = [
    path('', users_route)
]
