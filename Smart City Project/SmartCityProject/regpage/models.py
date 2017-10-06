from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver

# Create your models here.

class WebUser(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    phonenumber = models.CharField(max_length= 30)
    address = models.CharField(max_length = 30)

    def __str__(self):
        return self.user.username



@receiver(post_save, sender=User)
def saveuser(sender,instance, created, **kwargs):
    if created:
        WebUser.objects.create(user=instance)
