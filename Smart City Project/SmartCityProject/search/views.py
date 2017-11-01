from django.shortcuts import render, redirect
from search.forms import searchform
from informationpage.models import hotel, museum, restaurant, shoppingmall, industrie, city_park, zoo, college, library

# Create your views here.
def searchpage(request):
    if not request.user.is_authenticated():
        return redirect('/welcome/')
    if request.method == 'POST':
        form = searchform(request.POST, instance = request.user)
        if form.is_valid():
            query = form.cleaned_data['entry']
            searchresults = ""
            resultsList = ()
            if hotel.objects.filter(name__icontains = query).exists():
                resultsList = list(hotel.objects.filter(name__icontains = query))
            if museum.objects.filter(name__icontains = query).exists():
                resultsList.append(list(museum.objects.filter(name__icontains = query)))
            if restaurant.objects.filter(name__icontains = query).exists():
                resultsList.append(list(restaurant.objects.filter(name__icontains = query)))
            if shoppingmall.objects.filter(name__icontains = query).exists():
                resultsList.append(list(shoppingmall.objects.filter(name__icontains = query)))
            if industrie.objects.filter(name__icontains = query).exists():
                resultsList.append(list(industrie.objects.filter(name__icontains = query)))
            if city_park.objects.filter(name__icontains = query).exists():
                resultsList.append(list(city_park.objects.filter(name__icontains = query)))
            if zoo.objects.filter(name__icontains = query).exists():
                resultsList.append(list(zoo.objects.filter(name__icontains = query)))
            if college.objects.filter(name__icontains = query).exists():
                resultsList.append(list(college.objects.filter(name__icontains = query)))
            if library.objects.filter(name__icontains = query).exists():
                resultsList.append(list(library.objects.filter(name__icontains = query)))
            for result in resultsList:
                try:
                    searchresults += result.name
                except Exception as e:
                    searchresults += result[0].name
                searchresults += "\n"

            return render (request, 'searchresultpage.html', {'form' : form, 'searchresults' : searchresults, 'searchquery' : query})
    else:
        form = searchform(instance = request.user)
        return render (request, 'searchpage.html', {'form' : form})
