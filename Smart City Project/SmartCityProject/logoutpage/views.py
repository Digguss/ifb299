from django.shortcuts import render, redirect
from django.contrib.auth import logout

# Create your views here.

def logoutuser(request):
    logout(request)
    return redirect('/')
