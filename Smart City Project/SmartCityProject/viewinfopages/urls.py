from django.conf.urls import url
from . import views

urlpatterns = [

    url(r'hotelone', views.hotelpageone),
    url(r'hoteltwo', views.hotelpagetwo),
    url(r'museumone', views.musone),
    url(r'citymap', views.citymapview),
            ]
