from django.conf.urls import url
from informationpage import views


urlpatterns = [

        url(r'^$', views.enterhotelinfo),
]
