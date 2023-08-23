from django.db import models
from user.models import Users, Patients, Services
import datetime



# Create your models here.


class Requests(models.Model):
    user = models.ForeignKey(Users, on_delete=models.CASCADE)
    service = models.ForeignKey(Services, on_delete=models.CASCADE)
    patient = models.ForeignKey(Patients, on_delete=models.CASCADE, blank=True, default=2)
    # ОБЯЗАТЕЛЬНО СОЗДАВАЙ ПАЦИЕНТА С ПОЛЯМИ DEFAULT И УКАЗЫВАЙ ЕГО ID В default - ОН ЗАКОСТЫЛЕН
    status = models.IntegerField(
        default=1)  # 0 - ошибка оплаты, 1 - новый запрос, 2 - оплачено, 3 - отправлено, 4 - ожидает подтверждения,
    # 5 - в работе, 6 - выполнена, 7 - отклонена
    request_data = models.DateTimeField(auto_now_add=True)
    payment_data = models.DateTimeField(default='2000-01-01')


class Researches(models.Model):
    research_file = models.FileField()
    request = models.ForeignKey(Requests, on_delete=models.CASCADE)
