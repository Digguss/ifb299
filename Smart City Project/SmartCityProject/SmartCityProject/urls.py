"""SmartCityProject URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import include, url
from django.contrib import admin
from django.conf.urls.static import static
from django.conf import settings


urlpatterns = [
    url(r'^adminportal/', admin.site.urls ),
    url(r'^admin/', include('admin.urls')),
    url(r'^register/', include('regpage.urls')),
    url(r'^', include('homepage.urls')),
    url(r'^login/', include('loginpage.urls')),
    url(r'^logout/', include('logoutpage.urls')),
    url(r'^welcome/', include('welcomepage.urls')),
    url(r'^account/', include('accountpage.urls')),
    url(r'^resetpassword/', include('resetpassword.urls')),
    url(r'^informationcreaton/', include('informationpage.urls')),
    url(r'^cityinfomation/', include('viewinfopages.urls')),
    url(r'^help/', include('helppage.urls')),
    url(r'^search/', include('search.urls')),
]  + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
