from django.shortcuts import render
from django.contrib.auth import login, authenticate
from django.shortcuts import render, redirect
from regpage.forms import regpage
# Create your views here.


def registration(request):
    if request.method == 'POST':
        form = regpage(request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            form.save()
            user = authenticate(username=username, password=password)
            login(request, user)
    else:
        form = regpage()
    return render(request, 'registerpage.html', {'form': form})
