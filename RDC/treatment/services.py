from django.shortcuts import HttpResponseRedirect
from treatment.models import Requests, Researches
from user.models import Services, Patients
from django.urls import reverse
from user.forms import PatientChoosingForm, UserResearchAddForm


def request_add(request):
    if request.method == "POST":
       service_pk = request.POST.get('service', None)
       # service = Services.objects.get(pk__in=service_pk)
       service = Services.objects.filter(pk__in=service_pk).latest('id')
       Requests.objects.create(status=1, user=request.user, service=service)
    return HttpResponseRedirect(reverse('doctor'))


def doctor_add(request):
    if request.method == "POST":
       doctor_pk = request.POST.get('doctor', None)
       # doctor = Services.objects.get(pk__in=doctor_pk)
       doctor = Services.objects.filter(pk__in=doctor_pk).latest('id')
       Requests.objects.filter(user=request.user, status=1).update(doctor=doctor, status=2)
       return HttpResponseRedirect(reverse('whomToServe'))
        

def patient_add(request):
    user = request.user
    user_choice = request.POST.get('service_choice')
    if user_choice == "me":
        patient = Patients.objects.create(first_name=user.first_name, last_name=user.last_name, patronymic=user.patronymic,
                                          SNILS=user.SNILS, Passport=user.Passport, birth_date=user.birth_date)
        Requests.objects.filter(user=request.user, status=2).update(patient=patient, status=3)
        return HttpResponseRedirect(reverse('uploadfiles'))
    # another_patient - словарь "ключ-значение". Если по ключу serviceForAnother будет записано какое-то значение (то есть
    # радио-кнопка нажата) то при проверке на следующей строчке код пойдет дальше на заполнение формы, если по ключу ничего
    # не прuser_choiceкая же логика во всем контроллере
    elif user_choice == "other":
        if request.method == "POST":
            form = PatientChoosingForm(data=request.POST, instance=request.POST)
            if form.is_valid():
                first_name = request.POST.get('first_name', None)
                last_name = request.POST.get('last_name', None)
                patronymic = request.POST.get('patronymic', None)
                SNILS = request.POST.get('SNILS', None)
                Passport = request.POST.get('Passport', None)
                birth_date = request.POST.get('birth_date', None)
                patient = Patients.objects.create(first_name=first_name, last_name=last_name, patronymic=patronymic, SNILS=SNILS,
                                      Passport=Passport, birth_date=birth_date)
                Requests.objects.filter(user=request.user, status=2).update(patient=patient, status=3)
            return HttpResponseRedirect(reverse('uploadfiles'))
    else:
        if user_choice == "none":
            Requests.objects.filter(user=request.user, status=2).update(status=3)
            return HttpResponseRedirect(reverse('uploadfiles'))
    return HttpResponseRedirect(reverse('whomToServe'))


def research_add(request):
    if request.method == "POST":
        form = UserResearchAddForm(data=request.POST, files=request.FILES)
        if form.is_valid():
            form.save()
            # !!!  ИСПРАВЬ ФИЛЬТРАЦИИ, ОНО МОЖЕТ ВЗЯТЬ ПОСЛЕДНИЙ ЗАГРУЖЕННЫЙ, НО НЕ ОБЯЗАТЕЛЬНО ТЕКУЩЕГО ПОЛЬЗОВАТЕЛЯ !!!
            # ИЛИ ВЗЯТЬ НЕСКОЛЬКО ЗАПРОСОВ
            research_file = Researches.objects.latest('id')
            Requests.objects.filter(user=request.user, status=3).update(research=research_file)
    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))
