from django.shortcuts import render, redirect
from informationpage.models import hotel
from informationpage.models import citymap
from informationpage.models import museum,restaurant,shoppingmall,industrie,city_park,zoo,college, libary

# Create your views here.


def hotelpageone(request):
    hotels = hotel.objects.all()
    return render(request, "hotelone.html", {'hotels': hotels})
def hotelpagetwo(request):
    hotels = hotel.objects.all()
    return render(request, "hoteltwo.html", {'hotels': hotels})

def mustwo(request):
    museums = museum.objects.all()
    return render(request, "mustwo.html", {'museums': museums})
def musone(request):
    museums = museum.objects.all()
    return render(request, "musone.html", {'museums': museums})

def parksone(request):
    parks = city_park.objects.all()
    return render(request, "parksone.html", {'parks':parks})
def parkstwo(request):
    parks = city_park.objects.all()
    return render(request, "parkstwo.html", {'parks':parks})

def mallone(request):
    malls = shoppingmall.objects.all()
    return render(request, "mallone.html" ,{'malls':malls})
def malltwo(request):
    malls = shoppingmall.objects.all()
    return render(request, "malltwo.html", {'malls':malls})

def restone(request):
    rest = restaurant.objects.all()
    return render(request, "restone.html" ,{'rest':rest})
def resttwo(request):
    rest = restaurant.objects.all()
    return render(request, "resttwo.html" ,{'rest':rest})

def industone(request):
    indust = industrie.objects.all()
    return render(request, "industone.html" ,{'indust':indust})
def industtwo(request):
    indust = industrie.objects.all()
    return render(request, "industtwo.html" ,{'indust':indust})

def collegeone(request):
    colleges = college.objects.all()
    return render(request, "collegeone.html" ,{'colleges':colleges})
def collegetwo(request):
    colleges = college.objects.all()
    return render(request, "collegetwo.html" ,{'colleges':colleges})

def libraryone(request):
    librarys = libary.objects.all()
    return render(request, "libone.html" ,{'librarys':librarys})
def librarytwo(request):
    librarys = libary.objects.all()
    return render(request, "libtwo.html" ,{'librarys':librarys})

def zooone(request):
    zoos = zoo.objects.all()
    return render(request, "zooone.html" ,{'zoos':zoos})
def zootwo(request):
    zoos = zoo.objects.all()
    return render(request, "zootwo.html" ,{'zoos':zoos})

def citymapview(request):
    if request.user.is_authenticated:
        mapofcity = citymap.objects.all()
        return render(request, "citymap.html", {'mapofcity':mapofcity})
    else:
        return redirect('/')
