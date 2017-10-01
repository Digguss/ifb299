from django.conf.urls import url
from . import views


urlpatterns = [

    url(r'^$', views.homepage, name='default'),
    url(r'tourist/Home/', views.homepagetourist, name='tourist'),
    url(r'business/Home/', views.homepageBusiness, name='business'),
    url(r'student/Home/', views.homepageStudent, name='student'),
]
