from django.db import models

# Create your models here.
class Prof(models.Model):
    profile_photo=models.ImageField(upload_to='photos/')
    username=models.CharField(max_length=30)
    phone_number=models.CharField(max_length=20)
    address=models.CharField(max_length=600)
    postal_code=models.CharField(max_length=20)
class Contact(models.Model):
    username=models.CharField(max_length=30)
    email=models.CharField(max_length=30)
    contactnumber=models.CharField(max_length=20)
    message=models.CharField(max_length=500)
