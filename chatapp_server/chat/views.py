from django.http import HttpRequest, JsonResponse
from rest_framework.decorators import api_view, permission_classes
from rest_framework.pagination import PageNumberPagination
from rest_framework.permissions import IsAuthenticated

from chat.models import Chat, Room
from chat.serializers import ChatSerializer, RoomSerializer
from users.models import CustomUser


# Create your views here.
@api_view(['GET', 'POST'])
@permission_classes([IsAuthenticated])
def room_router(request: HttpRequest):
    if request.method == 'GET':
        rooms_qs = Room.objects.filter(
            created_user__id=request.user.id
        ) | Room.objects.filter(
            added_user__id=request.user.id
        )

        paginator = PageNumberPagination()
        paginator.page_size = 5

        paged_qs = paginator.paginate_queryset(rooms_qs, request=request)
        response = RoomSerializer(paged_qs, many=True).data

        for room in response:
            room['created_user'] = (CustomUser.objects.get(id=room['created_user'])).username
            room['added_user'] = (CustomUser.objects.get(id=room['added_user'])).username

        return paginator.get_paginated_response(response)

    if request.method == 'POST':

        try:
            assert 'added_username' in request.POST.keys(), "Please provide a user to add."
        except Exception as e:
            return JsonResponse({
                "success": False,
                "message": str(e)
            }, status=400)

        try:
            added_user = CustomUser.objects.filter(username=request.POST.get('added_username'))
            assert len(added_user) != 0, "User not found!"

            existance = len(Room.objects.filter(created_user=request.user, added_user=added_user[0])) > 0
            assert existance, "Room already exists."

            nw_room = Room(created_user=request.user, added_user=added_user[0])
            nw_room.save()

            return JsonResponse({
                "success": True,
                "data": RoomSerializer(nw_room).data
            })

        except Exception as e:
            return JsonResponse({
                "success": False,
                "message": str(e)
            }, status=400)

@api_view(['GET', 'POST'])
@permission_classes([IsAuthenticated])
def chat_router(requset: HttpRequest):
    pass