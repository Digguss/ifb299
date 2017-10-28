from django.conf.urls import url
from . import views

urlpatterns = [

    url(r'^$', views.loginadmin,name='adminlogin'),
    url(r'home/', views.adminhome, name='adminhomepage'),
    url(r'createstaff', views.createadmin, name='createadmin'),
    url(r'uploadmap', views.uploadImage, name='uploadcitymap'),
            ]
