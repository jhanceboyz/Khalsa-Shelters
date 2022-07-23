from pyexpat import model
from django.db import models

# Create your models here.
class Tile(models.Model):
    title = models.CharField(max_length=64)
    category = models.CharField(max_length=64)
    description = models.CharField(max_length=1000)
