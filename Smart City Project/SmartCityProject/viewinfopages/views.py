from django.shortcuts import render, redirect
from informationpage.models import hotel
from informationpage.models import citymap
from informationpage.models import museum

# Create your views here.


def hotelpageone(request):
    hotels = hotel.objects.all()
    return render(request, "hotelone.html", {'hotels': hotels})

def hotelpagetwo(request):
    hotels = hotel.objects.all()
    return render(request, "hoteltwo.html", {'hotels': hotels})

def musone(request):
    museums = museum.objects.all()
    return render(request, "musone.html", {'museums': museums})

def mustwo(request):
    museums = museum.objects.all()
    return render(request, "hotelone.html", {'museums': museums})

def citymapview(request):
    if request.user.is_authenticated:
        mapofcity = citymap.objects.all()
        return render(request, "citymap.html", {'mapofcity':mapofcity})
    else:
        return redirect('/')
