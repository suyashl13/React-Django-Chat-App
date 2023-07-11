import uuid

from django.contrib.auth import authenticate
from django.core.handlers.asgi import ASGIRequest
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth import login, logout
from rest_framework.pagination import PageNumberPagination


@csrf_exempt
def login_route(request: ASGIRequest):
    """
        @method: POST
        @url: /users/login
        @description: A route to log in the user.
    """
    if request.method == 'POST':
        # Username or password validation.
        try:
            assert 'username' in request.POST.keys(), "Please provide username"
            assert 'password' in request.POST.keys(), "please provide password"
        except Exception as e:
            return JsonResponse({
                "err": str(e),
                "success": False
            }, status=400)

        username = request.POST['username']
        password = request.POST['password']

        usr = authenticate(username=username, password=password)

        if usr is None:
            return JsonResponse({
                "success": False,
                "err": "Incorrect password or username"
            }, status=400)

        login(request=request, user=usr)
        return JsonResponse({
            "success": True,
            "user": CustomUserSerializer(usr).data
        })


from rest_framework.decorators import api_view, permission_classes

from rest_framework.permissions import AllowAny, IsAuthenticated
from users.models import CustomUser

from users.serializers import CustomUserSerializer


# Create your views here.


@csrf_exempt
def logout_route(request: ASGIRequest):
    """
        @method: DELETE
        @url: /users/logout
        @description: A route to log out the user.
    """
    if request.method == 'DELETE':
        logout(request=request)
        return JsonResponse({
            "success": True,
            "message": "Logged out successfully."
        }, status=200)


@csrf_exempt
def create_user_route(request: ASGIRequest):
    if request.method == 'POST':
        req_body = request.POST

        # Validations
        try:
            assert 'username' in req_body.keys(), "Please provide username."
            assert 'email' in req_body.keys(), "Please provide email."
            assert 'first_name' in req_body.keys(), "Please provide first_name."
            assert 'last_name' in req_body.keys(), "Please provide last_name."
            assert 'password' in req_body.keys(), "Please provide password."
            assert 'is_staff' not in req_body.keys(), "Please remove is_staff from request."
            assert 'is_superuser' not in req_body.keys(), "PLease remove is_superuser from request."
        except Exception as e:
            return JsonResponse({
                "success": False,
                "message": str(e)
            }, status=400)

        # Validations (Policy)
        try:
            pass
        except Exception as e:
            return JsonResponse({
                "success": False,
                "message": str(e)
            }, status=400)

        try:
            nw_user = CustomUser()

            for k in req_body.keys():
                if k != 'password':
                    setattr(nw_user, k, req_body.get(k))
                else:
                    nw_user.set_password(req_body[k])

            nw_user.save()
            return JsonResponse({
                "success": True,
                "user": CustomUserSerializer(nw_user).data
            })
        except Exception as e:
            return JsonResponse({
                "success": False,
                "message": str(e)
            }, status=400)

    if request.method == 'GET':
        return JsonResponse({})


@api_view(['GET'])
@permission_classes([IsAuthenticated])
def user_route(request: ASGIRequest):
    if request.method == 'GET':

        if 'search' in request.GET.keys():
            search_username = request.GET['search']
        else:
            search_username = ''

        users_query_set = CustomUser.objects.filter(username__contains=search_username)

        paginator = PageNumberPagination()
        paginator.page_size = 10

        paged_qs = paginator.paginate_queryset(queryset=users_query_set, request=request)
        response = CustomUserSerializer(paged_qs, many=True).data
        # response['success'] = True

        return paginator.get_paginated_response(response)
