from django.shortcuts import render
from informationpage.models import hotel

# Create your views here.


def viewpage(request):
    hotels = hotel.objects.get(id=2)
    return render(request, "informationpage.html", {'hotels': hotels})
