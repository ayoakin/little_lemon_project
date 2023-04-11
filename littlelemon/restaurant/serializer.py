from django.contrib.auth.models import User
from .models import Menu
from rest_framework import serializers

class MenuSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Menu
        fields = ['id', 'Title', 'Price', 'Inventory']