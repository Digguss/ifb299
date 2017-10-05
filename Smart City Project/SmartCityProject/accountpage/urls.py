from django.conf.urls import url
from . import views


urlpatterns = [

    url(r'^$', views.accountpage, name='account'),
    url(r'edit/', views.accounteditpage, name='accountedit'),
    url(r'changepassword/', views.accountchangepasswordpage, name='accountchangepassword'),

]
