from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User, Group
from informationpage.models import hotel, museum, restaurant, shoppingmall, industrie, city_park, zoo, college, library


# Create your views here.



def homepage(request):
    if not request.user.is_authenticated:
        return redirect('/welcome/')
    if request.user.is_authenticated:
        if request.user.groups.filter(name='Tourist').exists():
            return redirect('/tourist/Home/')
        if request.user.groups.filter(name='Business').exists():
            return redirect('/business/Home/')
        if request.user.groups.filter(name='Student').exists():
            return redirect('/student/Home/')
        if request.user.is_staff:
            return redirect ('/admin/home')
    return None;

def homepagetourist(request):
    hotels = hotel.objects.all()
    museums = museum.objects.all()
    cityparks = city_park.objects.all()
    malls = shoppingmall.objects.all()
    rest = restaurant.objects.all()
    zoos = zoo.objects.all()
    print(museum)
    if request.user.is_authenticated:
        if request.user.groups.filter(name='tourist').exists() or request.user.is_superuser:
            return render(request, 'homepagetourist.html',  {'museums':museums, 'hotels':hotels, 'cityparks':cityparks, 'cityparks':cityparks, 'malls':malls, 'rest':rest,'zoos':zoos})
        else:
            return redirect('/')
    else:
        return redirect('/')

def homepageStudent(request):
    museums = museum.objects.all()
    librarys = library.objects.all()
    cityparks = city_park.objects.all()
    malls = shoppingmall.objects.all()
    restaurants = restaurant.objects.all()
    colleges = college.objects.all()
    if request.user.is_authenticated:
        if request.user.groups.filter(name='student').exists() or request.user.is_superuser:
            return render(request, 'homepageStudent.html', {'museums': museums, 'librarys':librarys, 'cityparks':cityparks, 'malls':malls, 'rest':restaurants,'colleges':colleges})
        else:
            return redirect('/')
    else:
        return redirect('/')

def homepageBusiness(request):
    hotels = hotel.objects.all()
    cityparks = city_park.objects.all()
    museums = museum.objects.all()
    malls = shoppingmall.objects.all()
    rest = restaurant.objects.all()
    indust = industrie.objects.all()
    if request.user.is_authenticated:
        if request.user.groups.filter(name='business').exists() or request.user.is_superuser:
            return render(request, 'homepageBusiness.html', {'museums':museums, 'hotels':hotels, 'cityparks':cityparks, 'malls':malls, 'rest':rest, 'indust':indust})
        else:
            return redirect('/')
    else:
        return redirect('/')
