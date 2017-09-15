from django.shortcuts import render, redirect

# Create your views here.


def welcomepage(request):
    if request.user.is_authenticated:
        return redirect('/')
    return render(request, 'welcomepage.html')
