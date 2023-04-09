from django.contrib.auth.models import User
from . import models
from rest_framework import serializers

class MenuSerializer(serializers.ModelSerializer):
    class Meta:
        model = Menu
        fields = ['url', 'username', 'email', 'groups']