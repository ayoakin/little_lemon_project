from django.contrib.auth.models import User
from .models import Menu, Table
from rest_framework import serializers

class MenuSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Menu
        fields = ['id', 'Title', 'Price', 'Inventory']

class TableSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Table
        fields = ['id', 'Name', 'No_of_guests', 'BookingDate']