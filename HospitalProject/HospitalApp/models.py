from django.db import models
from django.contrib.auth.models import User

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    # Add your additional fields here
    bio = models.TextField(blank=True)
    # Add more fields as needed


class Doctor(models.Model):
    name=models.TextField(max_length=30)
    qualification=models.TextField(max_length=50)
    specialist=models.TextField(max_length=30)
    experience=models.CharField(max_length=15)
    rating=models.CharField(max_length=10,null=True)

class Appointment(models.Model):
    username=models.CharField(max_length=30)
    ref_no=models.CharField(max_length=10,null=False,primary_key=True,default='unknown')  #initially we didnt define this field as primary key but now we wannt to make it as primary key so we have to give null as false and also we have to give a default value
    patient_name=models.CharField(max_length=40)
    age=models.IntegerField()
    gender=models.CharField(max_length=10)
    mobile=models.CharField(max_length=11)
    city=models.CharField(max_length=100)
    problem=models.TextField(max_length=500)
    status=models.TextField(max_length=15,null=True)




    




# Create your models here.
