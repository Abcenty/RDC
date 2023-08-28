from django.shortcuts import render, HttpResponseRedirect
from user.models import Services, Doctors, Patients
from treatment.models import Requests
from django.urls import reverse
from user.forms import UserConfirmationForm


# Create your views here.
# MyModel.objects.exclude(category= u'mycategory')

def service(request):
    context = {
        'services': Services.objects.exclude(title='Default'),
    }
    return render(request, 'treatment/Applications/Service.html', context)


def doctor(request):
    current_request = Requests.objects.get(user=request.user, status=1)
    context = {
        'doctors': Doctors.objects.filter(services=current_request.service),
    }
    return render(request, 'treatment/Applications/Doctor.html', context)


""""""

"""def service(request):
    services = Services.objects.all()
    if request.method == "POST":
       selected_service = get_object_or_404(Services, pk=request.POST.get('service_id'))
       Requests.objects.create(user=request.user, service=selected_service, status=1)
    context = {
        'services': services,
    }
    return render(request, 'treatment/Applications/Service.html', context)"""


def whomToServe(request):
    return render(request, 'treatment/Applications/WhomToServe.html')


def uploadFiles(request):
    return render(request, 'treatment/Applications/UploadFiles.html')


def confirmation(request):
    context = {
        'request': Requests.objects.filter(user=request.user, status=3),
        # 'form': UserConfirmationForm(instance=request.user),
    }
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



