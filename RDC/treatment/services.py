from django.shortcuts import HttpResponseRedirect, get_object_or_404, render
from treatment.models import Requests
from user.models import Services, Patients
from django.urls import reverse
from user.forms import PatientChoosingForm


def request_add(request):
    if request.method == "POST":
       service_pk = request.POST.get('service', None)
       service = Services.objects.get(pk__in=service_pk)
       Requests.objects.create(status=1, user=request.user, service=service)
    return HttpResponseRedirect(reverse('doctor'))


def doctor_add(request):
    if request.method == "POST":
       doctor_pk = request.POST.get('doctor', None)
       doctor = Services.objects.get(pk__in=doctor_pk)
       Requests.objects.filter(user=request.user, status=1).update(doctor=doctor, status=2)
    return HttpResponseRedirect(reverse('whomToServe'))


"""def patient_add(request):
    user = request.user
    user_patient = request.POST.get('serviceForMe', None)
    another_patient = request.POST.get('serviceForAnother', None)
    default_patient = request.POST.get('serviceForNobody', None)
    if request.method == "POST" and user_patient:
        patient = Patients.objects.create(first_name=user.first_name, last_name=user.last_name, patronymic=user.patronymic,
                                          SNILS=user.SNILS, Passport=user.Passport, birthDate=user.birthDate)
        Requests.objects.filter(user=request.user, status=2).update(patient=patient, status=3)
        return HttpResponseRedirect(reverse('uploadedfiles'))
    # another_patient - словарь "ключ-значение". Если по ключу serviceForAnother будет записано какое-то значение (то есть
    # радио-кнопка нажата) то при проверке на следующей строчке код пойдет дальше на заполнение формы, если по ключу ничего
    # не придет, то по нему будет записано None и заполнение формы не последует. Такая же логика во всем контроллере
    elif request.method == "POST" and another_patient:
        form = PatientChoosingForm(data=request.POST)
        if form.is_valid():
            first_name = request.POST['first_name']
            last_name = request.POST['last_name']
            patronymic = request.POST['patronymic']
            SNILS = request.POST['SNILS']
            Passport = request.POST['Passport']
            birthDate = request.POST['birthDate']
            patient = Patients.objects.create(first_name=first_name, last_name=last_name, patronymic=patronymic, SNILS=SNILS,
                                      Passport=Passport, birthDate=birthDate)
            Requests.objects.filter(user=request.user, status=2).update(patient=patient, status=3)
            return HttpResponseRedirect(reverse('uploadedfiles'))
    else:
        if request.method == "POST" and default_patient:
            Requests.objects.filter(user=request.user, status=2).update(status=3)
            return HttpResponseRedirect(reverse('uploadedfiles'))
    return HttpResponseRedirect(reverse('whomToServe'))"""
        

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
            form = PatientChoosingForm(data=request.POST)
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




"""def request_add(request):
    services = Services.objects.all()
    if request.method == "POST":
       service_pk = request.POST.get('service', None)
       service = Services.objects.get(pk__in=service_pk)
       Requests.objects.create(status=1, user=request.user, service=service)
    context = {
        'services': services,
    }
    return render(request, 'treatment/Applications/Service.html', context)"""


"""def form_view(request):
    context = {
        'all_cities': City.objects.all()
    }

    if request.POST:
        city_pk_list = request.POST.getlist('city', None)
        print(request.POST.getlist('city', None))

        selected_city_obj_list = City.objects.filter(pk__in=city_pk_list)
        print(selected_city_obj_list)


    return render(request, 'index.html', context=context)"""


"""def selectview(request):
   item  = Item.objects.all() # use filter() when you have sth to filter ;)
   form = request.POST # you seem to misinterpret the use of form from django and POST data. you should take a look at [Django with forms][1]
   # you can remove the preview assignment (form =request.POST)
   if request.method == 'POST':
      selected_item = get_object_or_404(Item, pk=request.POST.get('item_id'))
      # get the user you want (connect for example) in the var "user"
      user.item = selected_item
      user.save()

      # Then, do a redirect for example

   return render_to_response ('select/item.html', {'items':item}, context_instance =  RequestContext(request),)"""

"""def get_name(request):
    # if this is a POST request we need to process the form data
    if request.method == "POST":
        # create a form instance and populate it with data from the request:
        form = NameForm(request.POST)
        # check whether it's valid:
        if form.is_valid():
            # process the data in form.cleaned_data as required
            # ...
            # redirect to a new URL:
            return HttpResponseRedirect("/thanks/")

    # if a GET (or any other method) we'll create a blank form
    else:
        form = NameForm()

    return render(request, "name.html", {"form": form})"""