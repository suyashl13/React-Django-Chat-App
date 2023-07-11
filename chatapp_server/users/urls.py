from django.urls import path

from users.views import login_route, logout_route, create_user_route, user_route

urlpatterns = [
    path('login/', login_route),
    path('logout/', logout_route),
    path('create/', create_user_route),
    path('', user_route)
]
