from django.shortcuts import render, redirect
from informationpage.models import hotel
from informationpage.models import citymap
from informationpage.models import museum,restaurant,shoppingmall,industrie,city_park,zoo,college, library

# Create your views here.


def hotelpageone(request):
    if request.user.is_authenticated:
        hotels = hotel.objects.all()
        return render(request, "hotelone.html", {'hotels': hotels})
    else:
        return redirect('/')
def hotelpagetwo(request):
    if request.user.is_authenticated:
        hotels = hotel.objects.all()
        return render(request, "hoteltwo.html", {'hotels': hotels})
    else:
        return redirect('/')

def mustwo(request):
    if request.user.is_authenticated:
        museums = museum.objects.all()
        return render(request, "mustwo.html", {'museums': museums})
    else:
        return redirect('/')
def musone(request):
    if request.user.is_authenticated:
        museums = museum.objects.all()
        return render(request, "musone.html", {'museums': museums})
    else:
        return redirect('/')

def parksone(request):
    if request.user.is_authenticated:
        parks = city_park.objects.all()
        return render(request, "parksone.html", {'parks':parks})
    else:
        return redirect('/')
def parkstwo(request):
    if request.user.is_authenticated:
        parks = city_park.objects.all()
        return render(request, "parkstwo.html", {'parks':parks})
    else:
        return redirect('/')

def mallone(request):
    if request.user.is_authenticated:
        malls = shoppingmall.objects.all()
        return render(request, "mallone.html" ,{'malls':malls})
    else:
        return redirect('/')
def malltwo(request):
    if request.user.is_authenticated:
        malls = shoppingmall.objects.all()
        return render(request, "malltwo.html", {'malls':malls})
    else:
        return redirect('/')

def restone(request):
    if request.user.is_authenticated:
        rest = restaurant.objects.all()
        return render(request, "restone.html" ,{'rest':rest})
    else:
        return redirect('/')
def resttwo(request):
    if request.user.is_authenticated:
        rest = restaurant.objects.all()
        return render(request, "resttwo.html" ,{'rest':rest})
    else:
        return redirect('/')

def industone(request):
    if request.user.is_authenticated:
        if request.user.groups.filter(name='business').exists():
            indust = industrie.objects.all()
            return render(request, "industone.html" ,{'indust':indust})
        else:
            return redirect('/')
    else:
        return redirect('/')
def industtwo(request):
    if request.user.is_authenticated:
        if request.user.groups.filter(name='business').exists():
            indust = industrie.objects.all()
            return render(request, "industtwo.html" ,{'indust':indust})
        else:
            return redirect('/')
    else:
        return redirect('/')

def collegeone(request):
    if request.user.is_authenticated:
        if request.user.groups.filter(name='student').exists():
            colleges = college.objects.all()
            return render(request, "collegeone.html" ,{'colleges':colleges})
        else:
            return redirect('/')
    else:
        return redirect('/')
def collegetwo(request):
    if request.user.is_authenticated:
        if request.user.groups.filter(name='student').exists():
            colleges = college.objects.all()
            return render(request, "collegetwo.html" ,{'colleges':colleges})
        else:
            return redirect('/')
    else:
        return redirect('/')

def libraryone(request):
    if request.user.is_authenticated:
            if request.user.groups.filter(name='student').exists():
                librarys = library.objects.all()
                return render(request, "libone.html" ,{'librarys':librarys})
            else:
                return redirect('/')
    else:
        return redirect('/')
def librarytwo(request):
    if request.user.is_authenticated:
        if request.user.groups.filter(name='student').exists():
            librarys = library.objects.all()
            return render(request, "libtwo.html" ,{'librarys':librarys})
        else:
            return redirect('/')
    else:
        return redirect('/')

def zooone(request):
    if request.user.is_authenticated:
        if request.user.groups.filter(name='tourist').exists():
            zoos = zoo.objects.all()
            return render(request, "zooone.html" ,{'zoos':zoos})
        else:
            return redirect('/')
    else:
        return redirect('/')
def zootwo(request):
    if request.user.is_authenticated:
        if request.user.groups.filter(name='tourist').exists():
            zoos = zoo.objects.all()
            return render(request, "zootwo.html" ,{'zoos':zoos})
        else:
            return redirect('/')
    else:
        return redirect('/')

def citymapview(request):
    if request.user.is_authenticated:
        mapofcity = citymap.objects.all()
        return render(request, "citymap.html", {'mapofcity':mapofcity})
    else:
        return redirect('/')
