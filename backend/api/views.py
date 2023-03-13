from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from .serializers import *
from .models import *

@api_view(['GET', 'POST', 'PUT', 'DELETE'])
def userViewByKey(request, pk):
    if request.method == 'GET':
        user = Users.objects.get(userKey = pk)
        serializers = UserSerializer(instance=user, many=False)
        return Response(serializers.data)

    if request.method == 'POST':
        user = Users.objects.get(ProductKey = pk)
        serializers = UserSerializer(instance=user, data = request.data)
        if serializers.is_valid():
            serializers.save()
            return Response(serializers.data)
        return Response(serializers.errors)

@api_view(['GET'])
@permission_classes((IsAuthenticated, ))
def usersView(request):
    content = {
        'user': str(request.user),  # `django.contrib.auth.User` instance.
        'auth': str(request.auth),  # None
    }
    if request.method == 'GET':
        users = Users.objects.all()
        serializers = UserSerializer(instance=users, many=False)
        return Response(serializers.data)