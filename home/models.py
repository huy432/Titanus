from django.db import models

# Create your models here.
class Movie(models.Model):
    mid = models.CharField(max_length=12)
    thumbnail = models.CharField(max_length=64)
    title = models.TextField()
    description = models.TextField(default="")