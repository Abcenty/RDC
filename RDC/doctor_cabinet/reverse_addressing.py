from django.shortcuts import HttpResponseRedirect
from treatment.models import Requests
from doctor_cabinet.models import Doctors
from django.urls import reverse


# !!! При использовании 
def to_doctors_requests(request):
    doctor = Doctors.objects.get(user=request.user.id)
    Requests.objects.filter(doctor=doctor, status=8).update(status=7)
    return HttpResponseRedirect(reverse('doctors_request'))

