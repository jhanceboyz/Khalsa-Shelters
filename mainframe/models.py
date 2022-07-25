import email
from pyexpat import model
from django.db import models

# Create your models here.
class Tile(models.Model):
    title = models.CharField(max_length=64)
    description = models.CharField(max_length=1000)
    city = models.CharField(max_length=64, null=True)
    price = models.IntegerField( null=True)
    email = models.CharField(max_length=254, null=True)
    phone = models.CharField(max_length=50, null=True)
    numberofbedroom = models.IntegerField( null=True)
    numberofbathroom = models.IntegerField( null=True)
    occupants = models.IntegerField(null=True)