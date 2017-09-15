from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required

# Create your views here.



def homepage(request):
    if not request.user.is_authenticated:
        return redirect('/welcome/')
    return render (request, 'homepage.html')
