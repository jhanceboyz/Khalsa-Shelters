from django.http import HttpResponse
from django.shortcuts import render
from .models import Tile

# Create your views here.


def index(request):
    if request.method == 'POST':
        print(request.POST['id'])
    return render(request, 'index.html', {"Tiles":Tile.objects.all()})

def tiledetails(request, tileID):
    print("----------------------------------")
    print( tileID)
    return render(request, 'tiledetails.html', {"Tiles":Tile.objects.all()})