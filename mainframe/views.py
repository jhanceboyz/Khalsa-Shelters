from django.http import HttpResponse
from django.shortcuts import render
from .models import Tile

# Create your views here.


def index(request):
    return render(request, 'index.html', {"Tiles":Tile.objects.all()})