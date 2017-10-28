from django.shortcuts import render
from informationpage.forms import enterhotelinfo
from .models import citymap
# Create your views here.

def infopage(request):
    return render(request, 'informationpage.html')



def enterhotelinfo(request):
    form = enterinfo(request.POST)
    if request.method == 'POST':
        if form.is_valid():
            form.save()
    else:
        form = enterinfo()
        return render(request, 'createinfo.html', {'form': form})
