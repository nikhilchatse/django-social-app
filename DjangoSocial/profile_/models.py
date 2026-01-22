from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Profile(models.Model):
    user=models.OneToOneField(User,on_delete=models.CASCADE,null=True,blank=True)
    profile_img=models.ImageField(upload_to='profile_img',null=True,blank=True)
    name=models.CharField(max_length=50,null=True,blank=True)
    contact=models.CharField(max_length=15,null=True,blank=True)
    email=models.CharField(max_length=50,null=True,blank=True)
    bio=models.TextField(max_length=200,null=True,blank=True)

