from __future__ import unicode_literals
from django.contrib.auth.models import User
from django.db import models

# Create your models here.
#models fro user base
class userDataBase(models.Model):
    user=models.OneToOneField(User)
    dob=models.DateField(blank=True)


    def __unicode__(self):
        return self.user.username

    def __str__(self):
        return '%s'%(self.user.username)


#this is for comic database

class comicDataBase(models.Model):
    title=models.CharField(max_length=50)
    #uploade=time
    author=models.CharField(max_length=30)
    fileup=models.FileField(upload_to='files',null=True)
    userdatabse=models.ForeignKey(userDataBase,on_delete=models.CASCADE)

    def __unicode__(self):
        return self.title



