from django.db import models

# Create your models here.
class AppUser(models.Model):
    Username = models.CharField(max_length=70, blank=False, default='')
    email = models.CharField(max_length=200,blank=False, default='')
    mobile = models.CharField(max_length=10,default=False)