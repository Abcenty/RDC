from django.db import models
from user.models import Users, Services

# Create your models here.


class Doctors(models.Model):
    user = models.ForeignKey(Users, on_delete=models.CASCADE)
    services = models.ManyToManyField(Services)

    def __str__(self):
        return f'{self.user.last_name} {self.user.first_name} {self.user.patronymic} {self.id}'
    

class Report(models.Model):
    file = models.FileField(upload_to='reports/', blank=True)
    comment = models.TextField(blank=True)

    def __str__(self):
        return f'Заключение №{self.id}'