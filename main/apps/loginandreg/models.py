from __future__ import unicode_literals

from django.db import models
class UsersManager(models.Manager):
    # def login(self, postData):

    def register(self, postData):
        if len(postData['first_name'])<3:
            error_msgs.append("too short")
        if len(postData['last_name'])<3:
            error_msgs.append("too short")
# Create your models here.
class Users(models.Model):
    first_name = models.CharField(max_length=45)
    last_name= models.CharField(max_length=45)
    email = models.CharField(max_length=45)
    password =models.CharField(max_length=45)
    pw_confirm = models.CharField(max_length=45)
    objects=UsersManager()
