from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.


class Services(models.Model):
    title = models.CharField(max_length=256)
    price = models.IntegerField(default=0)


class Users(AbstractUser):
    last_name = models.CharField(max_length=32)
    first_name = models.CharField(max_length=32)
    patronymic = models.CharField(max_length=32)
    birth_date = models.DateField()
    email = models.EmailField()
    SNILS = models.CharField(max_length=11, blank=True)
    Passport = models.CharField(max_length=10)


class Patients(models.Model):
    last_name = models.CharField(max_length=32)
    first_name = models.CharField(max_length=32)
    patronymic = models.CharField(max_length=32)
    birth_date = models.DateField()
    SNILS = models.CharField(max_length=11, blank=True)
    Passport = models.CharField(max_length=10)


class Doctors(models.Model):
    user = models.ForeignKey(Users, on_delete=models.CASCADE)
    services = models.ManyToManyField(Services)
