from django.shortcuts import HttpResponseRedirect
from doctor_cabinet.models import Doctors
from treatment.models import Requests


def request_accept(request, request_id):
    doctor = Doctors.objects.get(user=request.user.id)
    Requests.objects.filter(id=request_id, doctor=doctor, status = 6).update(status=7)
    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))