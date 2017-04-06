from __future__ import unicode_literals

from django.db import models

class Contact(models.Model):
    first_name = models.CharField(max_length=100, unique=True, verbose_name="first_name")
    last_name = models.CharField(max_length=100, unique=True, verbose_name="last_name")
    email = models.EmailField(max_length=70,blank=True, null= True, unique= True, verbose_name="email")

class Wizard(models.Model):
    #step 1
    first_name = models.CharField(max_length=100, unique=True, verbose_name="first_name")
    last_name = models.CharField(max_length=100, unique=True, verbose_name="last_name")
    email = models.EmailField(max_length=70,blank=True, null= True, unique= True, verbose_name="email")
    avatar_image = models.ImageField(upload_to='avatar/%Y/%m/%d', verbose_name="avatar_image")
    #step 2
    child = models.BooleanField(default=False, verbose_name="child")
    minor = models.BooleanField(default=False, verbose_name="minor")
    adult = models.BooleanField(default=False, verbose_name="child")
    #step 3
    adresse = models.CharField(max_length=100, unique=True, verbose_name="adresse")
    #Choice field ???
    country = models.CharField(max_length=100, unique=True, verbose_name="country")

