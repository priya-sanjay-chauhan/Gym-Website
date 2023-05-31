from django.db import models

# Create your models here.

class data(models.Model):
    Name=models.CharField(max_length=50)
    Email=models.CharField(max_length=60)
    Phone=models.CharField(max_length=10)
    gender_choices=(('M','Male'),('F','Female'),('O','Others'))
    Gender=models.CharField(choices=gender_choices,max_length=128)
    DOB=models.DateField(max_length=8)
    Address = models.CharField(max_length=1024)



class contact_detail(models.Model):
    Username=models.CharField(max_length=60)
    Email=models.CharField(max_length=70)
    Message=models.CharField(max_length=1000)
