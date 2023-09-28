from django.shortcuts import HttpResponseRedirect
from doctor_cabinet.models import Doctors, Report
from treatment.models import Requests
from django.urls import reverse
from doctor_cabinet.forms import DoctorReportAddForm


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
    if request.method == "POST":
        form = DoctorReportAddForm(data=request.POST, files=request.FILES)
        if form.is_valid():
            form.save()
            # !!!  ИСПРАВЬ ФИЛЬТРАЦИИ, ОНО МОЖЕТ ВЗЯТЬ ПОСЛЕДНИЙ ЗАГРУЖЕННЫЙ, НО НЕ ОБЯЗАТЕЛЬНО ТЕКУЩЕГО ПОЛЬЗОВАТЕЛЯ !!!
            # ИЛИ ВЗЯТЬ НЕСКОЛЬКО ЗАПРОСОВ
            report_file = Report.objects.latest('id')
            # ТУТ БЕРУТСЯ ВСЕ ЗАПРОСЫ СО СТАТУСОМ 8, А НУЖНО ТОЛЬКО ЗАПРОСЫ ПОЛЬЗОВАТЕЛЯ
            Requests.objects.filter(id=request_id, doctor=doctor, status = 8).update(status=9, report=report_file)
    return HttpResponseRedirect(reverse('completed_request'))


# только для завершенных запросов (отмененные нельзя пересмотреть)
# ДОКТОР И ПОЛЬЗОВАТЕЛЬ НЕ МОГУТ ПРОСМОТРЕТЬ ЗАЯВКУ ОДНОВРЕМЕННО
def review_analysis(request, request_id):
    doctor = Doctors.objects.get(user=request.user.id)
    Requests.objects.filter(id=request_id, doctor=doctor, status = 9).update(status=8)
    return HttpResponseRedirect(reverse('analysis_request'))


# def report_add(request):
#     if request.method == "POST":
#         form = DoctorReportAddForm(data=request.POST, files=request.FILES)
#         if form.is_valid():
#             form.save()
#             # !!!  ИСПРАВЬ ФИЛЬТРАЦИИ, ОНО МОЖЕТ ВЗЯТЬ ПОСЛЕДНИЙ ЗАГРУЖЕННЫЙ, НО НЕ ОБЯЗАТЕЛЬНО ТЕКУЩЕГО ПОЛЬЗОВАТЕЛЯ !!!
#             # ИЛИ ВЗЯТЬ НЕСКОЛЬКО ЗАПРОСОВ
#             file = Report.objects.latest('id')
#             Requests.objects.get(user=request.user, status=8).report.update(file=file)
#     return HttpResponseRedirect(request.META.get('HTTP_REFERER'))
