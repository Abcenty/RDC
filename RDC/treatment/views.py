from django.shortcuts import render
from user.models import Services
from treatment.models import Requests, Researches
from treatment.forms import PatientChoosingForm, UserResearchAddForm, UserConfirmationForm, UserReportViewForm
from doctor_cabinet.models import Doctors, Report


# Корректно
def service(request):
    context = {
        'services': Services.objects.exclude(title='Default'),
    }
    return render(request, 'treatment/Applications/Service.html', context)


# Корректно
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

    # research = Requests.objects.filter(user=request.user, status=4).latest('request_time').research

    # Строчка перенесена в контроллер добавления исследования
    # Requests.objects.filter(user=request.user, status=3).update(status=4)
    service = Requests.objects.filter(user=request.user, status=4).latest('id').service
    patient = Requests.objects.filter(user=request.user, status=4).latest('id').patient
    doctor = Requests.objects.filter(user=request.user, status=4).latest('id').doctor
    research = Requests.objects.filter(user=request.user, status=4).latest('id').research
    context = {
        'request': Requests.objects.filter(user=request.user, status=3),
        'form': UserConfirmationForm(initial={'service': service, 'patient': patient, 'doctor': doctor, 'research': research}),
    }
    return render(request, 'treatment/Applications/Confirmation.html', context)


def payment(request):
    Requests.objects.filter(user=request.user, status=4).update(status=5)
    return render(request, 'treatment/Applications/Payment.html')


def services(request):
    context = {
        'services': Requests.objects.filter(user=request.user),
    }
    return render(request, 'treatment/Services/services.html', context)


def uploadedfiles(request):
    context = {
        'requests': Requests.objects.filter(user=request.user),
        'researches': Researches.objects.all(),
    }
    return render(request, 'treatment/UploadedFiles/uploadedfiles.html', context)


def protocols(request):
    context={
        'requests': Requests.objects.filter(user=request.user, status = 9),
    }
    return render(request, 'treatment/Protocols/protocols.html', context)


def detailed_view(request):
    comment = Report.objects.latest('id').comment
    context={
        'requests': Requests.objects.filter(user=request.user, status = 11),
        'form': UserReportViewForm(initial={'comment': comment}),
    }
    return render(request, 'treatment/Protocols/detailed_view.html', context)



