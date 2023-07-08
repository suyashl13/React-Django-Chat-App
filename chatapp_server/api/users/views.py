import re

from django.core.handlers.asgi import ASGIRequest
from django.http import JsonResponse
from rest_framework.decorators import permission_classes
from rest_framework.permissions import IsAuthenticated

from rest_framework.pagination import PageNumberPagination
from api.users.models import CustomUser
from api.users.serializers import CustomUserSerializer
from rest_framework.decorators import api_view


# Create your views here.


@api_view(['GET', 'POST'])
@permission_classes([IsAuthenticated])
def users_route(request: ASGIRequest):
    if request.method == 'GET':
        try:
            if 'search' in request.GET.keys():
                users = CustomUser.objects.filter(username__contains=request.GET.get('search'))
            else:
                users = CustomUser.objects.all()

            # Configure paginator
            paginator = PageNumberPagination()
            paginator.page_size = 10

            result_queryset = paginator.paginate_queryset(users, request=request)
            response = CustomUserSerializer(result_queryset, many=True)

            return paginator.get_paginated_response(response.data)
        except Exception as e:
            return JsonResponse({
                "success": False,
                "message": str(e)
            }, status=500)
    elif request.method == 'POST':
        try:
            nw_user_body = request.POST

            # Validation Block
            try:
                # Not Null Validations
                assert 'username' in nw_user_body.keys(), "Please provide username."
                assert 'email' in nw_user_body.keys(), "Please provide email."
                assert 'phone' in nw_user_body.keys(), "Please provide phone."
                assert 'password' in nw_user_body.keys(), "Please provide password."

                # Policy Validations
                assert str(nw_user_body.get('username')).isalnum() or str(nw_user_body.get('username')).isalpha(), \
                    "Username should be alpha numeric"
                assert str(nw_user_body['username']).islower(), "Username must have only lowercase alphabets"
                assert re.match(r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$', str(nw_user_body['email'])), \
                    "Please provide a valid email. "
                assert len(nw_user_body['phone']) == 12, "Please provide country code along with phone number."
            except Exception as e:
                return JsonResponse({
                    "success": False,
                    "message": str(e)
                }, status=400)

            # User Existence check.
            if len(CustomUser.objects.filter(username=nw_user_body.get('username'))) > 0:
                return JsonResponse({
                    "success": False,
                    "message": "User with similar username already exists."
                }, status=400)

            if len(CustomUser.objects.filter(phone=nw_user_body.get('phone'))) > 0:
                return JsonResponse({
                    "success": False,
                    "message": "User with similar phone already exists."
                }, status=400)

            if len(CustomUser.objects.filter(email=nw_user_body.get('email'))) > 0:
                return JsonResponse({
                    "success": False,
                    "message": "User with similar email already exists."
                }, status=400)

            # Create user object and save to database.
            custom_user = CustomUser(
                username=nw_user_body.get('username'),
                email=nw_user_body.get('email'),
                phone=nw_user_body.get('phone')
            )
            custom_user.set_password(nw_user_body.get('password'))
            custom_user.save()

            return JsonResponse({
                "success": True,
                "result": CustomUserSerializer(custom_user).data
            })

        except Exception as e:
            return JsonResponse({
                "success": False,
                "message": str(e)
            }, status=500)
