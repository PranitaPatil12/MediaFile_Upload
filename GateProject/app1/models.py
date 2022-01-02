from django.db import models
from phone_field import PhoneField


# Create your models here.
class Applicant(models.Model):
    Applicant_name = models.CharField(max_length=32)
    Mobile_No = PhoneField(blank=True, help_text='Contact phone number')
    Gender = models.CharField(max_length=32)
    Address= models.CharField(max_length=32)
    Aadhar_No = models.IntegerField()
    Picture = models.ImageField(default='')
    document = models.FileField(default='')
