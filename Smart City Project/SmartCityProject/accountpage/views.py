from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.db import models
from accountpage.forms import editform
from django.contrib.auth.models import User, Group
from django.contrib import messages
# Create your views here.



def accountpage(request):
    if not request.user.is_authenticated:
        return redirect('/welcome/')
    usergroup = ""
    if request.user.groups.filter(name = 'Business').exists():
        usergroup = "Business"
    if request.user.groups.filter(name = 'Student').exists():
        usergroup = "Student"
    if request.user.groups.filter(name = 'Tourist').exists():
        usergroup = "Tourist"
    return render (request, 'accountpage.html', {'usergroup':usergroup})

def accounteditpage(request):
    if not request.user.is_authenticated():
        return redirect('/welcome/')
    if request.method == 'POST':
        form = editform(request.POST, instance = request.user)
        if form.is_valid():
            emailfield = form.cleaned_data['email']
            if (User.objects.filter(email=emailfield).exists() & (request.user.email != emailfield)):
                messages.error(request,'Email Already in use')
            else:
                user = form.save(commit = False)
                user.save()
                return redirect('/account/')
    else:
        form = editform(instance = request.user)
    return render (request, 'accounteditpage.html', {'form' : form})
