from django.db import models

# Create your models here.
class Menu (models.Model):
    Title = models.CharField(max_length=255)
    Price = models.DecimalField(max_digits=10,decimal_places=2)
    Inventory = models.IntegerField(max_length=5)
    


class Table (models.Model):
    Name = models.CharField(max_length=255)
    No_of_guests = models.IntegerField(max_length=6)
    BookingDate = models.DateTimeField()

