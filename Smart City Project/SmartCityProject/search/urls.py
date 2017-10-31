from django.conf.urls import url
from . import views


urlpatterns = [

    url(r'^$', views.searchpage, name='search'),
    url(r'results/', views.searchresultpage, name='searchresults'),

]
