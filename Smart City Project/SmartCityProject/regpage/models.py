from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class websiteUser(models.Model):
    user = models.OneToOneField(User)
    address = models.CharField(max_length= 30)
    phonenumber = models.CharField(max_length= 30)
