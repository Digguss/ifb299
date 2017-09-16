from django.shortcuts import render
from django.contrib.auth import login, authenticate
from django.shortcuts import render, redirect
from regpage.forms import regpage
from django.contrib.auth.models import Group
# Create your views here.


def registration(request):
    if request.user.is_authenticated():
        return redirect('/')
    if request.method == 'POST':
        form = regpage(request.POST)
        if form.is_valid():
            user = form.save()
            groupname = form.cleaned_data['groups']
            usergroup = Group.objects.get(name=groupname)
            usergroup.user_set.add(user)
            return redirect('/login/')
    else:
        form = regpage()
    return render(request, 'registerpage.html', {'form': form})
