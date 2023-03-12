from rest_framework.response import Response
from rest_framework.decorators import api_view
from .serializers import *
from .models import *

@api_view(['GET', 'POST', 'PUT', 'DELETE'])
def usersViewByKey(request, pk):
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
    