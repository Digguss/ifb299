from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User, Group

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
            return redirect ('/admin/')
    return None;

def homepagetourist(request):
    if request.user.is_authenticated:
        return render(request, 'homepagetourist.html')

def homepageBusiness(request):
    if request.user.is_authenticated:
        return render(request, 'homepageBusiness.html')

def homepageStudent(request):
    if request.user.is_authenticated:
        return render(request, 'homepageStudent.html')
