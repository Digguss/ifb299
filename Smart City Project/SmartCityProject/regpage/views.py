from django.shortcuts import render
from django.contrib.auth import login, authenticate
from django.shortcuts import render, redirect
from regpage.forms import regpage
from django.contrib.auth.models import Group, User
from django.contrib import messages
# Create your views here.


def registration(request):
    if request.user.is_authenticated():
        return redirect('/')
    if not Group.objects.filter(name='business').exists():
        Group.objects.create(name='business')
    if not Group.objects.filter(name='tourist').exists():
        Group.objects.create(name='tourist')
    if not Group.objects.filter(name='student').exists():
        Group.objects.create(name='student')
    if request.method == 'POST':
        form = regpage(request.POST)
        if form.is_valid():
            emailfield = form.cleaned_data['email']
            if User.objects.filter(email=emailfield).exists():
                messages.error(request,'Email Already in use')
            else:
                user = form.save()
                groupname = form.cleaned_data['groups']
                usergroup = Group.objects.get(name=groupname)
                usergroup.user_set.add(user)
                return redirect('/login/')
    else:
        form = regpage()
    return render(request, 'registerpage.html', {'form': form})
