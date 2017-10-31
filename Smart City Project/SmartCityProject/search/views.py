from django.shortcuts import render, redirect
from search.forms import searchform
from search.models import Place

searchresults = ""
# Create your views here.
def searchpage(request):
    if not request.user.is_authenticated():
        return redirect('/welcome/')
    if request.method == 'POST':
        form = searchform(request.GET, instance = request.user)
        #if form.is_valid():
        query = request.GET['query']
        searchresults = ""
        searchComplete = False
        results = Place.objects.filter(name__icontains = query)
        for result in results:
            searchresults += result.name

        return redirect('/search/results/')
    else:
        form = searchform(instance = request.user)
        return render (request, 'searchpage.html', {'form' : form})

def searchresultpage(request):
    form = searchform(instance = request.user)
    searchresults = "HELLOWORLD"
    return render (request, 'searchresultpage.html', {'form' : form, 'searchresults' : searchresults, 'searchquery' : searchquery})
