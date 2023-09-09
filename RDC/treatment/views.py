from django.shortcuts import render, HttpResponseRedirect
from user.models import Services, Doctors, Patients
from treatment.models import Requests
from django.urls import reverse
from user.forms import UserConfirmationForm, PatientChoosingForm, UserResearchAddForm


# Create your views here.
# MyModel.objects.exclude(category= u'mycategory')

def service(request):
    context = {
        'services': Services.objects.exclude(title='Default'),
    }
    return render(request, 'treatment/Applications/Service.html', context)


def doctor(request):
    # current_request = Requests.objects.get(user=request.user, status=1)
    # МОГУТ ВОЗНИКНУТЬ ПРОБЛЕМЫ ИЗ-ЗА ЛОГИКИ ФИЛЬТРАЦИИ. ПРОВЕРЬ ЕЕ В СЛУЧАЕ ОШИБОК С ДОБАВЛЕНИЕМ ДОКТОРА В БД
    # current_request = Requests.objects.filter(user=request.user, status=1).latest('request_data')
    # current_request = Requests.objects.filter(user=request.user, status=1).order_by('request_time').reverse[0]
    
    current_request = Requests.objects.filter(user=request.user, status=1).latest('request_time')
    context = {
        'doctors': Doctors.objects.filter(services=current_request.service),
    }
    return render(request, 'treatment/Applications/Doctor.html', context)


def whomToServe(request):
    context = {
        'form': PatientChoosingForm(),
    }
    return render(request, 'treatment/Applications/WhomToServe.html', context)


def uploadFiles(request):
    context = {
        'form': UserResearchAddForm()
    }
    return render(request, 'treatment/Applications/UploadFiles.html', context)


def confirmation(request):
    """service = Requests.objects.get(user=request.user, status=3).service
    patient = Requests.objects.get(user=request.user, status=3).patient
    doctor = Requests.objects.get(user=request.user, status=3).doctor"""
    service = Requests.objects.filter(user=request.user, status=4).latest('request_time').service
    patient = Requests.objects.filter(user=request.user, status=4).latest('request_time').patient
    doctor = Requests.objects.filter(user=request.user, status=4).latest('request_time').doctor
    research = Requests.objects.filter(user=request.user, status=4).latest('request_time').research
    context = {
        'request': Requests.objects.filter(user=request.user, status=3),
        'form': UserConfirmationForm(initial={'service': service, 'patient': patient, 'doctor': doctor, 'research': research}),
    }
    Requests.objects.filter(user=request.user, status=4).update(status=5)
    return render(request, 'treatment/Applications/Confirmation.html', context)


def payment(request):
    return render(request, 'treatment/Applications/Payment.html')


def services(request):
    context = {
        'services': Requests.objects.filter(user=request.user),
    }
    return render(request, 'treatment/Services/services.html', context)


def uploadedfiles(request):
    return render(request, 'treatment/UploadedFiles/uploadedfiles.html')



