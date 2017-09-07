from django.conf.urls import url
from . import views as core_views

from . import views

urlpatterns = [
     url(r'^signup/$', signup, name='signup'),
]
