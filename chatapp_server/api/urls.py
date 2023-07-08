from django.urls import path, include
from .views import home, login_usr

urlpatterns = [
    path('add_admin/', home),
    path('users/', include('api.users.urls')),
    path('login/', login_usr)
]
