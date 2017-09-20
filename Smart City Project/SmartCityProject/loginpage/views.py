from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib.auth.forms import AuthenticationForm
from django.http import HttpResponse

# Create your views here.



def loginuser(request):
    form = AuthenticationForm(request.POST)
    if request.user.is_authenticated:
        return redirect ('/')
    if form.is_valid:
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username=username,password=password)
        if user is not None:
            login(request,user)
            return redirect('/')
    else:
        form = AuthenticationForm()
    return render(request, 'loginpage.html', {'form': form })
