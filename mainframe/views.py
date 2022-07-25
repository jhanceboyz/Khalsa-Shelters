from cgi import print_exception
from turtle import title
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

def postad(request):
    if request.method == 'POST':
        print(request.POST)
        number_of_occupants = int(request.POST.get('numberofoccupantspp',False))
        number_of_bedroom = int(request.POST.get('numberofbedroompp',False))
        number_of_bathroom = int(request.POST.get('numberofbathroompp',False))
        print(type(450 * number_of_occupants))
        i = Tile(title= request.POST.get('titlepp',False),
                    description= request.POST.get('descriptionpp',False),
                    city= request.POST.get('citypp',False),
                    price = 450 * number_of_occupants,
                    email= request.POST.get('emailpp',False),
                    phone= request.POST.get('phonepp',False),
                    numberofbedroom= number_of_bedroom,
                    numberofbathroom= number_of_bathroom,
                    occupants= number_of_occupants,
                    )
        i.save()
    return render(request, 'postad.html', {})

def contact(request):
    return render(request, 'contact.html', {})