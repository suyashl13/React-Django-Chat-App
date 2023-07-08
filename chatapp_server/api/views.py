from django.core.handlers.asgi import ASGIRequest
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt

from api.users.models import CustomUser
from django.contrib.auth import authenticate, login


# Create your views here.
def home(req: ASGIRequest):
    try:
        custom_user = CustomUser()

        custom_user.email = 'suyash.lawand@gmail.com'
        custom_user.username = 'suyashl13'
        custom_user.is_staff = True
        custom_user.is_superuser = True
        custom_user.set_password('slaw1113')
        custom_user.phone = '919545731113'

        custom_user.save()

        print(len(CustomUser.objects.filter()))

        return JsonResponse({
            'success': True,
            'message': "This is home route: " + req.path,
            'data': custom_user.id
        }, status=200)

    except Exception as e:
        return JsonResponse({
            'success': False,
            'message': "Could not create super admin",
            'data': None
        }, status=200)


@csrf_exempt
def login_usr(request):
    username = request.POST['username']
    password = request.POST['password']

    try:
        user = authenticate(username=username, password=password)
        if user is not None:
            login(request, user)
            return JsonResponse({
                "message": "Logged in successfully!",
                "success": True
            }, status=200)
        else:
            return JsonResponse({
                "message": "Invalid auth credentials.",
                "success": False
            }, status=400)
    except Exception as e:
        return JsonResponse({
            "message": str(e),
            "success": False
        }, status=400)
