from django.db import models
from user.models import Users, Patients, Services, Doctors
import datetime



# Create your models here.


class Requests(models.Model):
    user = models.ForeignKey(Users, on_delete=models.CASCADE)
    service = models.ForeignKey(Services, on_delete=models.CASCADE)

    # ОБЯЗАТЕЛЬНО СОЗДАВАЙ ПАЦИЕНТА С ПОЛЯМИ DEFAULT И УКАЗЫВАЙ ЕГО ID В default
    patient = models.ForeignKey(Patients, on_delete=models.CASCADE, blank=True, default=1)

    # Может возникнуть ошибка, если один пользователь создаст два запроса, которые одновременно будут иметь один статус с 1 по 4
    status = models.IntegerField(
        default=1)  # 0 - ошибка оплаты, 1 - новый запрос, 2 - выбран врач, 3 - выбран пациент,
    # 4 - ожидает подтверждения пользователя, 5 - ожидает оплаты, 6 - оплачено, 7 - ожидает подтверждение от врача,
    # 8 - в работе, 9 - выполнена, 10 - отклонена

    # ОБЯЗАТЕЛЬНО СОЗДАВАЙ ДОКТОРА С ПОЛЯМИ DEFAULT И УКАЗЫВАЙ ЕГО ID В default
    doctor = models.ForeignKey(Doctors, on_delete=models.CASCADE, default=2)
    request_data = models.DateTimeField(auto_now_add=True)
    payment_data = models.DateTimeField(default='2000-01-01')


class Researches(models.Model):
    research_file = models.FileField()
    request = models.ForeignKey(Requests, on_delete=models.CASCADE)
