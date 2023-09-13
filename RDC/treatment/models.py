from django.db import models
from user.models import Users, Patients, Services
from doctor_cabinet.models import Doctors



# Create your models here.


# СМЕНИ FOREIGN KEY НА ONE TO MANY ЧТОБЫ РЕАЛИЗОВАТЬ ДОБАВЛЕНИЕ НЕСКОЛЬКИХ ФАЙЛОВ НА ОДИН ЗАПРОС
class Researches(models.Model):
    research_file = models.FileField(upload_to='media/')
    

    def __str__(self):
        return f'Документ №{self.id}'
    


class Requests(models.Model):
    user = models.ForeignKey(Users, on_delete=models.CASCADE)
    service = models.ForeignKey(Services, on_delete=models.CASCADE)

    # ОБЯЗАТЕЛЬНО СОЗДАВАЙ ПАЦИЕНТА ПО УМОЛЧАНИЮ И УКАЗЫВАЙ ЕГО ID В default
    patient = models.ForeignKey(Patients, on_delete=models.CASCADE, default=1)

    # Может возникнуть ошибка, если один пользователь создаст два запроса, которые одновременно будут иметь один статус с 1 по 4
    
    # ИСПРАВЬ ОШИБКУ С НАЖАТИЕМ КНОПКИ "НАЗАД" (НУЖНО МЕНЯТЬ СТАТУС ОБРАТНО ПРИ ПЕРЕХОДЕ)

    # НА СТРАНИЦЕ АНАЛИЗА НУЖНО, ЧТОБЫ ЛЮБОЙ ПЕРЕХОД НА ДРУГУЮ СТРАНИЦУ МЕНЯЛ СТАТУС ЗАЯВКИ

    status = models.IntegerField(
        default=1)  # 0 - ошибка оплаты, 1 - новый запрос, 2 - выбран врач, 3 - выбран пациент, ожидает исследования
    # 4 - ожидает подтверждения пользователя 5 - ожидает оплаты, 6 - оплачено, ожидает подтверждение от врача,
    # 7 - в работе, 8 - в процессе анализа, 9 - выполнена, 10 - отклонена

    # ОБЯЗАТЕЛЬНО СОЗДАВАЙ ДОКТОРА ПО УМОЛЧАНИЮ И УКАЗЫВАЙ ЕГО ID В default
    doctor = models.ForeignKey(Doctors, on_delete=models.CASCADE, default=2)
    request_data = models.DateField(auto_now_add=True)
    request_time = models.TimeField(auto_now_add=True)
    payment_data = models.DateField(default='2000-01-01')
    # ОБЯЗАТЕЛЬНО СОЗДАВАЙ ИССЛЕДОВАНИЕ ПО УМОЛЧАНИЮ И УКАЗЫВАЙ ЕГО ID В default
    research = models.ForeignKey(Researches, on_delete=models.CASCADE, default = 12)
    doctors_comment = models.TextField(blank=True)
    



    
