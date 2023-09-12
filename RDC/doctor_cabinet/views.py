from django.shortcuts import render
from treatment.models import Requests
from doctor_cabinet.models import Doctors

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


def analysis_request(request):
    return render(request, 'doctor_cabinet/analysis_request.html')


def completed_request(request):
    return render(request, 'doctor_cabinet/completed_request.html')
