from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from django.http import JsonResponse
from hashlib import sha256
from datetime import datetime
import pytz
from .serializers import *
from .models import *

test_value = [{
            "userKey": 2,
            "Username": "sundui",
            "Password": "testpwd"
            },
            {
            "Username": "sundui",
            "Password": "testpwd"
            }
            ]

timezoneDateTime = str(datetime.now(pytz.timezone('Asia/Ulaanbaatar')))

def content(request):
    content = {
        'user': str(request.user),  # `django.contrib.auth.User` instance.
        'auth': str(request.auth),  # None
    }
    return content

@api_view(['GET', 'PUT', 'DELETE'])
def userViewByKey(request, pk):
    if request.method == 'GET':
        user = Users.objects.get(userKey = pk)
        serializers = UserSerializer(instance=user, many=False)
        return Response(serializers.data)

    if request.method == 'PUT':
        user = Users.objects.get(userKey = pk)
        serializers = UserSerializer(instance=user, data = request.data)
        if serializers.is_valid():
            serializers.save()
            return Response(serializers.data)
        return Response(serializers.errors)

@api_view(['GET', 'POST'])
@permission_classes((IsAuthenticated, ))
def usersView(request):
    if request.method == 'GET':
        users = Users.objects.all()
        serializers = UserSerializer(users, many=True)
        return Response(serializers.data)

    if request.method == 'POST':
        data = request.data
        serializers = UserSerializer(data = data)

        if serializers.is_valid():
            serializers.save(CreatedAt='2023-03-14T11:49:14.3023159+08:00', 
                             ModifiedAt=timezoneDateTime)
            return Response(serializers.data)
        return Response(serializers.errors)
    

@api_view(['POST'])
@permission_classes((IsAuthenticated, ))
def authentication(request):
    if request.method == 'POST':
        data = request.data
        h = sha256()
        h.update(f"{data['Username']}{data['Password']}".encode('utf-8'))
        hash = h.hexdigest()
        return JsonResponse({"hash": hash})