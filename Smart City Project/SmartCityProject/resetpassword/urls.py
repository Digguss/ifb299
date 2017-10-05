from django.conf.urls import url
from . import views


urlpatterns = [
    url(r'^$', views.resetpasswordpage, name='resetpassword'),
    url(r'success', views.resetsuccesspage, name='resetsuccess'),
]
