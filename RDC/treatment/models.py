from django.db import models
from user.models import Users, Patients, Services, Doctors
import datetime



# Create your models here.


class Requests(models.Model):
    user = models.ForeignKey(Users, on_delete=models.CASCADE)
    service = models.ForeignKey(Services, on_delete=models.CASCADE)

    # ОБЯЗАТЕЛЬНО СОЗДАВАЙ ПАЦИЕНТА С ПОЛЯМИ DEFAULT И УКАЗЫВАЙ ЕГО ID В default
    patient = models.ForeignKey(Patients, on_delete=models.CASCADE, default=1)

    # Может возникнуть ошибка, если один пользователь создаст два запроса, которые одновременно будут иметь один статус с 1 по 4
    status = models.IntegerField(
        default=1)  # 0 - ошибка оплаты, 1 - новый запрос, 2 - выбран врач, 3 - выбран пациент, ожидает подтверждения пользователя
    # 4 - ожидает оплаты, 5 - оплачено, 6 - ожидает подтверждение от врача,
    # 7 - в работе, 8 - выполнена, 9 - отклонена

    # СТАТУСЫ 3 И 4 ПОД ВОПРОСОМ, ИХ ВОЗМОЖНО ПРИДЕТСЯ ИЗМЕНИТЬ, ОБРАТИ ВНИМАНИЕ ПРИ ПРОПИСЫВАНИИ ЛОГИКИ ДОБАВЛЕНИЯ ФАЙЛОВ

    # ОБЯЗАТЕЛЬНО СОЗДАВАЙ ДОКТОРА С ПОЛЯМИ DEFAULT И УКАЗЫВАЙ ЕГО ID В default
    doctor = models.ForeignKey(Doctors, on_delete=models.CASCADE, default=2)
    request_data = models.DateTimeField(auto_now_add=True)
    request_time = models.TimeField(auto_now_add=True)
    payment_data = models.DateTimeField(default='2000-01-01')


class Researches(models.Model):
    research_file = models.FileField()
    request = models.ForeignKey(Requests, on_delete=models.CASCADE)
