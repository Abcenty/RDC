from django.db import models
from user.models import Users, Patients, Services, Doctors
import datetime



# Create your models here.


# СМЕНИ FOREIGN KEY НА ONE TO MANY ЧТОБЫ РЕАЛИЗОВАТЬ ДОБАВЛЕНИЕ НЕСКОЛЬКИХ ФАЙЛОВ НА ОДИН ЗАПРОС
class Researches(models.Model):
    research_file = models.FileField(upload_to='media/')

    def __str__(self):
        return f'Документ №{self.id}'
    


class Requests(models.Model):
    user = models.ForeignKey(Users, on_delete=models.CASCADE)
    service = models.ForeignKey(Services, on_delete=models.CASCADE)

    # ОБЯЗАТЕЛЬНО СОЗДАВАЙ ПАЦИЕНТА С ПОЛЯМИ DEFAULT И УКАЗЫВАЙ ЕГО ID В default
    patient = models.ForeignKey(Patients, on_delete=models.CASCADE, default=1)

    # Может возникнуть ошибка, если один пользователь создаст два запроса, которые одновременно будут иметь один статус с 1 по 4
    
    # ИСПРАВЬ ОШИБКУ С НАЖАТИЕМ КНОПКИ "НАЗАД" (НУЖНО МЕНЯТЬ СТАТУС ОБРАТНО ПРИ ПЕРЕХОДЕ)

    status = models.IntegerField(
        default=1)  # 0 - ошибка оплаты, 1 - новый запрос, 2 - выбран врач, 3 - выбран пациент, ожидает исследования
    # 4 - ожидает подтверждения пользователя 5 - ожидает оплаты, 6 - оплачено, 7 - ожидает подтверждение от врача,
    # 8 - в работе, 9 - выполнена, 10 - отклонена

    # СТАТУСЫ 3 И 4 ПОД ВОПРОСОМ, ИХ ВОЗМОЖНО ПРИДЕТСЯ ИЗМЕНИТЬ, ОБРАТИ ВНИМАНИЕ ПРИ ПРОПИСЫВАНИИ ЛОГИКИ ДОБАВЛЕНИЯ ФАЙЛОВ

    # ОБЯЗАТЕЛЬНО СОЗДАВАЙ ДОКТОРА С ПОЛЯМИ DEFAULT И УКАЗЫВАЙ ЕГО ID В default
    doctor = models.ForeignKey(Doctors, on_delete=models.CASCADE, default=2)
    request_data = models.DateTimeField(auto_now_add=True)
    request_time = models.TimeField(auto_now_add=True)
    payment_data = models.DateTimeField(default='2000-01-01')
    # ОБЯЗАТЕЛЬНО СОЗДАВАЙ ИССЛЕДОВАНИЕ ПО УМОЛЧАНИЮ И УКАЗЫВАЙ ЕГО ID В default
    research = models.ForeignKey(Researches, on_delete=models.CASCADE, default = 12)
    



    
