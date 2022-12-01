from django.db import models
from django.contrib.auth.models import User
from . import namegen

# Create your models here.

class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    avatar = models.IntegerField(default=0)
    description = models.TextField(max_length=128,default="")
    isActive = models.BooleanField(default=False)
    _a = models.CharField(max_length=16,default=str(namegen.random_name_file(16)[0]))
