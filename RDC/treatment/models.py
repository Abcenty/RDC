from django.db import models
from user.models import Users, Patients, Services
from doctor_cabinet.models import Doctors, Report



# Create your models here.


# СМЕНИ FOREIGN KEY НА ONE TO MANY ЧТОБЫ РЕАЛИЗОВАТЬ ДОБАВЛЕНИЕ НЕСКОЛЬКИХ ФАЙЛОВ НА ОДИН ЗАПРОС
class Researches(models.Model):
    research_file = models.FileField(upload_to='researches/')
    user = models.ForeignKey(Users, on_delete=models.CASCADE, default=1)

    def research_(self):
        return '<a href="/media/{0}"><img src="/media/{0}"></a>'.format(self.research_file)
    research_.allow_tags = True
    

    def __str__(self):
        return f'{self.research_file}'
    


class Requests(models.Model):
    user = models.ForeignKey(Users, on_delete=models.CASCADE, default=1)

    # ОБЯЗАТЕЛЬНО СОЗДАВАЙ УСЛУГУ ПО УМОЛЧАНИЮ И УКАЗЫВАЙ ЕГО ID В default
    service = models.ForeignKey(Services, on_delete=models.CASCADE, default = 1)

    # ОБЯЗАТЕЛЬНО СОЗДАВАЙ ПАЦИЕНТА ПО УМОЛЧАНИЮ И УКАЗЫВАЙ ЕГО ID В default
    patient = models.ForeignKey(Patients, on_delete=models.CASCADE, default=1)

    # Может возникнуть ошибка, если один пользователь создаст два запроса, которые одновременно будут иметь один статус с 1 по 4
    
    # ИСПРАВЬ ОШИБКУ С НАЖАТИЕМ КНОПКИ "НАЗАД" (НУЖНО МЕНЯТЬ СТАТУС ОБРАТНО ПРИ ПЕРЕХОДЕ)

    # НА СТРАНИЦЕ АНАЛИЗА НУЖНО, ЧТОБЫ ЛЮБОЙ ПЕРЕХОД НА ДРУГУЮ СТРАНИЦУ МЕНЯЛ СТАТУС ЗАЯВКИ

    status = models.IntegerField(
        default=1)  # 0 - ошибка оплаты, 1 - новый запрос, 2 - выбран врач, 3 - выбран пациент, ожидает исследования
    # 4 - ожидает подтверждения пользователя 5 - ожидает оплаты, 6 - оплачено, ожидает подтверждение от врача,
    # 7 - в работе, 8 - в процессе анализа, 9 - выполнена, 10 - отклонена, 11 - просматривается пользователем

    # ОБЯЗАТЕЛЬНО СОЗДАВАЙ ДОКТОРА ПО УМОЛЧАНИЮ И УКАЗЫВАЙ ЕГО ID В default
    doctor = models.ForeignKey(Doctors, on_delete=models.CASCADE, default=2)
    request_data = models.DateField(auto_now_add=True)
    request_time = models.TimeField(auto_now_add=True)
    payment_data = models.DateField(default='2000-01-01')
    # ОБЯЗАТЕЛЬНО СОЗДАВАЙ ИССЛЕДОВАНИЕ ПО УМОЛЧАНИЮ И УКАЗЫВАЙ ЕГО ID В default
    research = models.ForeignKey(Researches, on_delete=models.CASCADE, default = 1)
    report = models.ForeignKey(Report, on_delete=models.CASCADE, default=1)

    def __str__(self):
        return f'Запрос №{self.id}'
    



    
