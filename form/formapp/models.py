from django.db import models
from django import forms
# Create your models here.
class student(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(max_length=100,unique=True)
    mobile = models.CharField(max_length=100,default = "")
    photo = models.ImageField(upload_to = 'photo/', default = True)
    STREAM_CHOICES = (
        ('1', 'CSE'),
        ('2', 'ECE'),
        ('3', 'MINING')


    )
    stream = models.CharField(max_length=1, choices=STREAM_CHOICES,default=True)
    video_file = models.FileField(upload_to = 'video/', max_length=200,default=True)
    phone = forms.CharField(max_length=100)
