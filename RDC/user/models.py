from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.


class Services(models.Model):
    title = models.CharField(max_length=256)
    price = models.IntegerField(default=0)

    def __str__(self):
        return f'{self.title} | {self.price} руб.'


class Users(AbstractUser):
    username=models.CharField(unique=True)
    email = models.EmailField()
    last_name = models.CharField(max_length=32)
    first_name = models.CharField(max_length=32)
    patronymic = models.CharField(max_length=32)
    birth_date = models.DateField(default='2000-01-01')
    # phone = models.CharField(max_length=11, default='89000000000')
    SNILS = models.CharField(max_length=11, blank=True)
    Passport = models.CharField(max_length=10)

class Patients(models.Model):
    last_name = models.CharField(max_length=32, blank=True)
    first_name = models.CharField(max_length=32, blank=True)
    patronymic = models.CharField(max_length=32, blank=True)
    birth_date = models.DateField(default='2000-01-01', blank=True)
    SNILS = models.CharField(max_length=11, blank=True)
    Passport = models.CharField(max_length=10, blank=True)

    def __str__(self):
        return f'{self.last_name} {self.first_name} {self.patronymic}'



