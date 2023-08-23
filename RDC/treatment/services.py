from django.shortcuts import HttpResponseRedirect, get_object_or_404, render
from treatment.models import Requests
from user.models import Services
from django.urls import reverse


def request_add(request):
    services = Services.objects.all()
    if request.method == "POST":
       service_pk = request.POST.get('service', None)
       service = Services.objects.get(pk__in=service_pk)
       Requests.objects.create(status=1, user=request.user, service=service)
    context = {
        'services': services,
    }
    return render(request, 'treatment/Applications/Doctor.html', context)


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