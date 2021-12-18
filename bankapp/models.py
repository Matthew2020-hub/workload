from django.db import models
from django_countries.fields import CountryField

# Create your models here.

class CustomUser(models.Model):
    First_Name = models.CharField(max_length=20, null=True)
    Last_Name = models.CharField(max_length=20, null=True)
    Email = models.EmailField(max_length=50, primary_key=True, error_messages= {"error": "This field already exist"})
    Phone_Number = models.CharField(max_length=11, null=True)
    Country = CountryField(null=True)
    Password1 = models.CharField(max_length=20, null=True)
    Confirm_Password = models.CharField(max_length=20, null=True)

    def __repr__(self):
        return self.First_Name

class Helpline(models.Model):
    Phone_number = models.CharField(max_length=11)
    Branch_name = models.CharField(max_length=50)
    Country = CountryField()

    def __repr__(self):
        return self.Branch_name



