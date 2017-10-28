from django.shortcuts import render
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib.auth.forms import AuthenticationForm
from django.contrib import messages
from .forms import regpage, regpageadmin
from django.contrib.auth.models import Group, User
from django.contrib import messages
from .forms import imgupload
# Create your views here.



def loginadmin(request):
    if request.user.is_authenticated:
        return redirect('/')
    username = request.POST.get('username')
    password = request.POST.get('password')
    if username and password != '':
            user = authenticate(username=username, password=password)
            if user is not None:
                if user.is_staff:
                    login(request, user)
                    return redirect('/admin/home/')
                else:
                    messages.error(request,'You are not authorized to login here, Please go to the login page under the sidebar')
            else:
                messages.error(request,'Invalid Username or password')
    return render(request, 'adminlogin.html')

def adminhome(request):
    if request.user.is_authenticated:
        if request.user.is_staff:
            return render(request, 'adminhomepage.html')
        if not request.user.is_staff:
            return redirect('/admin/')

def createuser(request):
    if request.user.is_authenticated:
        if request.user.is_staff:
            if not Group.objects.filter(name='Business').exists():
                Group.objects.create(name='Business')
            if not Group.objects.filter(name='Tourist').exists():
                Group.objects.create(name='Tourist')
            if not Group.objects.filter(name='Student').exists():
                Group.objects.create(name='Student')
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
                        user.refresh_from_db()
                        user.webuser.address = form.cleaned_data['address']
                        user.webuser.phonenumber = form.cleaned_data['phonenumber']
                        user.webuser.save()
                        return redirect('/admin/')
            else:
                form = regpage()

        else:
            return redirect('/')
    return render(request, 'adminuserreg.html', {'form': form})

def createadmin(request):
    if request.user.is_authenticated:
        if request.user.is_staff:
            if request.method == 'POST':
                form = regpageadmin(request.POST)
                if form.is_valid():
                    emailfield = form.cleaned_data['email']
                    if User.objects.filter(email=emailfield).exists():
                        messages.error(request,'Email Already in use')
                    else:
                        user = form.save()
                        user.refresh_from_db()
                        user.webuser.address = form.cleaned_data['address']
                        user.webuser.phonenumber = form.cleaned_data['phonenumber']
                        user.is_staff = True
                        user.is_admin = True
                        user.is_superuser = True
                        user.webuser.save()
                        user.save()
                        return redirect('/admin/')
            else:
                form = regpageadmin()

        else:
            return redirect('/')
    return render(request, 'regadmin.html', {'form': form})

def uploadImage(request):
    if request.user.is_authenticated:
        if request.user.is_staff:
            form = imgupload(request.POST,request.FILES or None)
            if form.is_valid():
                form.save()
                return redirect('admin/home')
        else:
            return ('/')
    return render(request, "uploadcitymap.html",{'form':form})
