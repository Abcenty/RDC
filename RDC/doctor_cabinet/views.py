from django.shortcuts import render
from treatment.models import Requests
from doctor_cabinet.models import Doctors, Report
from doctor_cabinet.forms import DoctorReportAddForm

# Create your views here.


def doctor_cabinet(request):
    doctor = Doctors.objects.get(user=request.user.id)
    # ВЫВОДИ ТОЛЬКО ЗАПРОСЫ С НУЖНЫМ СТАТУСОМ
    context={
        'requests': Requests.objects.filter(doctor=doctor, status = 6)
    }
    return render(request, 'doctor_cabinet/doctor_cabinet.html', context)


def doctors_request(request):
    doctor = Doctors.objects.get(user=request.user.id)
    # ВЫВОДИ ТОЛЬКО ЗАПРОСЫ С НУЖНЫМ СТАТУСОМ
    context={
        'requests': Requests.objects.filter(doctor=doctor, status = 7)
    }
    return render(request, 'doctor_cabinet/doctors_request.html', context)


# ЗАГРУЖЕННЫЙ ФАЙЛ ОБНОВЛЯЕТСЯ ПРИ ПРОСМОТРЕ, НУЖНО ЧТОБЫ ОСТАВАЛСЯ ПРЕЖНИЙ
def analysis_request(request):
    doctor = Doctors.objects.get(user=request.user.id)
    # !!!  ИСПРАВЬ ФИЛЬТРАЦИИ, ОНО МОЖЕТ ВЗЯТЬ ПОСЛЕДНИЙ ЗАГРУЖЕННЫЙ, НО НЕ ОБЯЗАТЕЛЬНО ТЕКУЩЕГО ПОЛЬЗОВАТЕЛЯ !!!
    # ИЛИ ВЗЯТЬ НЕСКОЛЬКО ЗАПРОСОВ
    file = Report.objects.latest('id').file
    comment = Report.objects.latest('id').comment
    context={
        'requests': Requests.objects.filter(doctor=doctor, status = 8),
        'form': DoctorReportAddForm(initial={'comment': comment, 'file': file}),
    }
    return render(request, 'doctor_cabinet/analysis_request.html', context)


def completed_request(request):
    doctor = Doctors.objects.get(user=request.user.id)
    context={
        'requests': Requests.objects.filter(doctor=doctor, status__gte = 9),
    }
    return render(request, 'doctor_cabinet/completed_request.html', context)
