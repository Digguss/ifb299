from django.shortcuts import render
from django.contrib.auth import login, authenticate
from django.shortcuts import render, redirect
from regpage.forms import regpage
# Create your views here.


def registration(request):
    if request.user.is_authenticated():
        return redirect('/')
    if request.method == 'POST':
        form = regpage(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            return redirect('/login/')
    else:
        form = regpage()
    return render(request, 'registerpage.html', {'form': form})
