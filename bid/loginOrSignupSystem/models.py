# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.
class User(models.Model):
    userid = models.AutoField(primary_key=True)
    username = models.CharField(max_length=100)
    useraddress = models.CharField(max_length=3000)
    userpassword = models.CharField(max_length=100)
    userphonenumber = models.IntegerField(default=0)

    def __str__(self):
        return self.username
    