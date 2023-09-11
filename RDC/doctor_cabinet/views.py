from django.shortcuts import render

# Create your views here.


def doctor_cabinet(request):
    return render(request, 'doctor_cabinet/templates/doctor_cabinet/doctor_cabinet.html')


def doctors_request(request):
    return render(request, 'doctor_cabinet/templates/doctor_cabinet/doctors_request.html')


def analysis_request(request):
    return render(request, 'doctor_cabinet/templates/doctor_cabinet/analysis_request.html')


def completed_request(request):
    return render(request, 'doctor_cabinet/templates/doctor_cabinet/completed_request')
