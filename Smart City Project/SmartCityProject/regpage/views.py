from django.shortcuts import render
from django.contrib.auth import login, authenticate
from django.shortcuts import render, redirect
from regpage.forms import regpage
# Create your views here.


def registration(request):
    if request.method == 'POST':
        form = regpage(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            email = form.cleaned_data.get('email')
            user = authenticate(username=username, password=password,email=email)
            login(request, user)
    else:
        form = regpage()
    return render(request, 'registerpage.html', {'form': form})
