from django.conf.urls import url
from . import views

urlpatterns = [

    url(r'hotelone', views.hotelpageone),
    url(r'hoteltwo', views.hotelpagetwo),
    url(r'museumone', views.musone),
    url(r'museumtwo', views.mustwo),
    url(r'parkone', views.parksone),
    url(r'parktwo', views.parkstwo),
    url(r'mallone', views.mallone),
    url(r'malltwo', views.malltwo),
    url(r'restaurantone', views.restone),
    url(r'restauranttwo', views.resttwo),
    url(r'industrieone', views.industone),
    url(r'industrietwo', views.industtwo),
    url(r'collegeone', views.collegeone),
    url(r'collegetwo', views.collegetwo),
    url(r'libone', views.libraryone),
    url(r'libtwo', views.librarytwo),
    url(r'zooone', views.zooone),
    url(r'zootwo', views.zootwo),
    url(r'citymap', views.citymapview),

        ]
