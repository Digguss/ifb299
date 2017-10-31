from __future__ import unicode_literals

from django.db import models

# Create your models here.

class Place(models.Model):
    id = models.IntegerField(primary_key = True)
    name = models.CharField(max_length = 300)
    description = models.CharField(max_length = 256)
    phonenumber = models.CharField(max_length = 30)
    address = models.CharField(max_length = 30)
    email = models.CharField(max_length = 254)
    image = models.CharField(max_length = 300)
