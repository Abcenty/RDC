from django.shortcuts import HttpResponseRedirect
from treatment.models import Requests, Researches
from user.models import Services, Patients
from django.urls import reverse
from treatment.forms import PatientChoosingForm, UserResearchAddForm
from datetime import date


# def to_services(request):
#     if request.method == "POST":
#        service_pk = request.POST.get('service', None)
#        # service = Services.objects.get(pk__in=service_pk)
#        service = Services.objects.filter(pk__in=service_pk).latest('id')
#        Requests.objects.create(status=1, user=request.user, service=service)
#     return HttpResponseRedirect(reverse('doctor'))


def to_services(request):
    Requests.objects.filter(status=1, user=request.user).delete()
    return HttpResponseRedirect(reverse('service'))


def to_doctors(request):
    Requests.objects.filter(user=request.user, status=2).update(status=1)
    return HttpResponseRedirect(reverse('doctor'))

def to_patients(request):
    Requests.objects.filter(user=request.user, status=3).update(status=2, patient=1)
    return HttpResponseRedirect(reverse('whomToServe'))


def to_researches(request):
    Requests.objects.filter(user=request.user, status=4).update(status=3)
    return HttpResponseRedirect(reverse('uploadfiles'))


def to_confirming(request):
    Requests.objects.filter(user=request.user, status=5).update(status=4)
    return HttpResponseRedirect(reverse('confirmation'))