from rest_framework import serializers
from rest_framework.serializers import ModelSerializer
from .models import *

class UserSerializer(ModelSerializer):
    class Meta:
        model =  Users
        field = '__all__'