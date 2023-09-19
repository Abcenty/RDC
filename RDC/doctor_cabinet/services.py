from django.shortcuts import HttpResponseRedirect
from doctor_cabinet.models import Doctors
from treatment.models import Requests
from django.urls import reverse


def request_accept(request, request_id):
    doctor = Doctors.objects.get(user=request.user.id)
    Requests.objects.filter(id=request_id, doctor=doctor, status = 6).update(status=7)
    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))


def continue_analysis(request, request_id):
    doctor = Doctors.objects.get(user=request.user.id)
    Requests.objects.filter(id=request_id, doctor=doctor, status = 7).update(status=8)
    return HttpResponseRedirect(reverse('analysis_request'))


def complete_analysis(request, request_id):
    doctor = Doctors.objects.get(user=request.user.id)
    Requests.objects.filter(id=request_id, doctor=doctor, status = 8).update(status=9)
    return HttpResponseRedirect(reverse('completed_request'))


# только для завершенных запросов (отмененные нельзя пересмотреть)
def review_analysis(request, request_id):
    doctor = Doctors.objects.get(user=request.user.id)
    Requests.objects.filter(id=request_id, doctor=doctor, status = 9).update(status=8)
    return HttpResponseRedirect(reverse('analysis_request'))
