from django.db import models
from django.core.files.storage import FileSystemStorage
# Create your models here.

photostorage = FileSystemStorage(location='/SmartCityProject/storage')


class hotel(models.Model):
    name = models.CharField(max_length = 300)
    description = models.CharField(max_length= 256)
    phonenumber = models.CharField(max_length= 30)
    address = models.CharField(max_length = 300)
    email = models.CharField(max_length= 256,null=True)
    image = models.ImageField(null=True,blank=True,upload_to="storage")

    def __str__(self):
        return self.name

class museum(models.Model):
    name = models.CharField(max_length = 300)
    description = models.CharField(max_length= 256)
    phonenumber = models.CharField(max_length= 30)
    address = models.CharField(max_length = 100)
    email = models.CharField(max_length= 256,null=True)
    image = models.ImageField(null=True,blank=True,upload_to="storage")


    def __str__(self):
        return self.name

class restaurant(models.Model):
    name = models.CharField(max_length = 300)
    description = models.CharField(max_length= 256)
    phonenumber = models.CharField(max_length= 30)
    address = models.CharField(max_length = 100)
    email = models.CharField(max_length= 256,null=True)
    image = models.ImageField(null=True,blank=True,upload_to="storage")


    def __str__(self):
        return self.name

class shoppingmall(models.Model):
    name = models.CharField(max_length = 300)
    description = models.CharField(max_length= 256)
    phonenumber = models.CharField(max_length= 30)
    address = models.CharField(max_length = 100)
    email = models.CharField(max_length= 256,null=True)
    image = models.ImageField(null=True,blank=True,upload_to="storage")

    def __str__(self):
        return self.name

class industrie(models.Model):
    name = models.CharField(max_length = 300)
    description = models.CharField(max_length= 256)
    phonenumber = models.CharField(max_length= 30)
    address = models.CharField(max_length = 100)
    email = models.CharField(max_length= 256,null=True)
    image = models.ImageField(null=True,blank=True,upload_to="storage")

    def __str__(self):
        return self.name

class city_park(models.Model):
    name = models.CharField(max_length = 300)
    description = models.CharField(max_length= 256)
    phonenumber = models.CharField(max_length= 30)
    address = models.CharField(max_length = 100)
    email = models.CharField(max_length= 256,null=True)
    image = models.ImageField(null=True,blank=True,upload_to="storage")

    def __str__(self):
        return self.name

class zoo(models.Model):
    name = models.CharField(max_length = 300)
    description = models.CharField(max_length= 256)
    phonenumber = models.CharField(max_length= 30)
    address = models.CharField(max_length = 100)
    email = models.CharField(max_length= 256,null=True)
    image = models.ImageField(null=True,blank=True,upload_to="storage")

    def __str__(self):
        return self.name

class college(models.Model):
    name = models.CharField(max_length = 300)
    description = models.CharField(max_length= 256)
    phonenumber = models.CharField(max_length= 30)
    address = models.CharField(max_length = 100)
    email = models.CharField(max_length= 256,null=True)
    image = models.ImageField(null=True,blank=True,upload_to="storage")

    def __str__(self):
        return self.name

class libary(models.Model):
    name = models.CharField(max_length = 300)
    description = models.CharField(max_length= 256)
    phonenumber = models.CharField(max_length= 30)
    address = models.CharField(max_length = 100)
    email = models.CharField(max_length= 256,null=True)
    image = models.ImageField(null=True,blank=True,upload_to="storage")

    def __str__(self):
        return self.name

class citymap(models.Model):
    name = models.CharField(max_length=100)
    citymap = models.ImageField(null=True,blank=True,upload_to="storage/citymap")

    def __str__(self):
        return self.name
